import os

from pxr import Gf
from pxr import Vt

from pxr import Sdf
from pxr import Usd
from pxr import Kind
from pxr import UsdGeom
from pxr import UsdShade

from core import shader
from core import scenegraph

DEFAULT_PATH = '/root'
SCOPE_PATH = '/root/materials'


def create(knode, usd_path):
    '''
    :example
        from core import kusd
        knode = NodegraphAPI.GetNode('studio_lookdev_render')
        usd_path = '/venture/shows/katana_tutorials/dumps/shader/katana_lookdev_6.usda'
        stage, usd_path = kusd.create(knode, usd_path)    
    '''
    producer = scenegraph.get_producer(knode, location=None)
    shader_networks = shader.get_scene_shader_networks(producer, polymesh=False)
    stage = None
    stage = make_usd(usd_path, shader_networks)
    return stage, usd_path


def make_usd(usd_path, input_data):
    stage = None    
    stage = make_stage(usd_path)
    default_prim = make_default_prim(stage)
    scope_define = make_scope_define(stage)
    make_geometry_hierarchy(stage, input_data)
    stage = make_shader_networks(stage, input_data)
    make_material_binding(stage, input_data)
    stage.GetRootLayer().Save()
    # print stage.GetRootLayer().ExportToString()
    return stage


def make_stage(usd_path):
    usd_path = '%s.usd' % os.path.splitext(usd_path)[0]
    # stage = Usd.Stage.CreateNew(usd_path)
    layer = None
    stage = None
    layer = Sdf.Layer.CreateNew(usd_path, args={'format': 'usda'})
    stage = Usd.Stage.Open(layer)
    return stage


def make_default_prim(stage):
    default_path = Sdf.Path(DEFAULT_PATH)    
    default_prim = stage.DefinePrim(default_path)
    stage.SetDefaultPrim(default_prim)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
    UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.centimeters)
    Usd.ModelAPI(default_prim).SetKind(Kind.Tokens.component)
    return default_prim


def make_scope_define(stage):    
    scope_path = Sdf.Path(SCOPE_PATH)    
    scope_define = UsdGeom.Scope.Define(stage, scope_path)
    return scope_define


def make_geometry_hierarchy(stage, shader_networks):
    for material in shader_networks:
        if 'assigned_locations' not in shader_networks[material]:
            continue
        if not shader_networks[material]['assigned_locations']:
            continue
        for location, typed, in shader_networks[material]['assigned_locations'].items():
            object_path = Sdf.Path(location)            
            for level in object_path.GetPrefixes():
                UsdGeom.Xform.Define(stage, level)
            if typed == 'polymesh':                
                UsdGeom.Mesh.Define(stage, object_path)


def make_material_binding(stage, shader_networks):
    for material in shader_networks:
        if 'assigned_locations' not in shader_networks[material]:
            continue
        if not shader_networks[material]['assigned_locations']:
            continue        
        material_path = Sdf.Path(material)
        material_define = UsdShade.Material.Get(stage, material_path)     
        for location, typed, in shader_networks[material]['assigned_locations'].items():
            object_path = Sdf.Path(location) 
            if typed == 'group':
                define = UsdGeom.Xform.Get(stage, object_path)            
            else:
                define = UsdGeom.Mesh.Get(stage, object_path)                
            material_binding = UsdShade.MaterialBindingAPI(define)
            material_binding.Bind(material_define)


def make_shader_networks(stage, shader_networks):
    for material, contents in shader_networks.items():
        path = os.path.join(SCOPE_PATH, os.path.basename(material))
        material_path = Sdf.Path(path)
        material_define = UsdShade.Material.Define(stage, material_path)
        make_shader_node(stage, material_path, contents['nodes']) 
        set_material_shader_connection(stage, material_define, contents['terminals'])
    return stage
   

def make_shader_node(stage, material_path, nodes):    
    for node, contents in nodes.items():
        node_path = material_path.AppendPath(node)
        shader_define = UsdShade.Shader.Define(stage, node_path)
        shader_define.CreateIdAttr(contents['primary']['type']['value'])
        if contents['parameters']:
            set_parameter_values(shader_define, contents['parameters'])
    # set connections        
    for node, contents in nodes.items():        
        if not contents['connections']:
            continue
        set_connections(stage, material_path, node, contents['connections'])


def set_connections(stage, material_path, node, contents):
    for parameter, connections in contents.items():
        attribute, connected_node = connections['value'].split('@')
        node_path = material_path.AppendPath(node)        
        source_node_path = material_path.AppendPath(connected_node)
        node_define = UsdShade.Shader.Get(stage, node_path)
        source_node_define = UsdShade.Shader.Get(stage, source_node_path)
        typed, value = get_parameter_type(connections['type'], attribute)
        if not typed and not value:
            continue        
        node_define_input = node_define.CreateInput(parameter, typed)
        node_define_input.ConnectToSource(source_node_define, attribute)


def set_material_shader_connection(stage, material_define, contents):
    shader = contents['prmanBxdf']['value']  
    attribute = contents['prmanBxdfPort']['value']  
    material_path = material_define.GetPath()
    shader_path = material_path.AppendPath(shader)
    shader_define = UsdShade.Shader.Get(stage, shader_path)
    material_define_output = material_define.CreateOutput('ri:surface', Sdf.ValueTypeNames.Token)
    material_define_output.ConnectToSource(shader_define, attribute)


def set_parameter_values(define, parameters):
    for parameter, contents in parameters.items():
        # print '\t', parameter, contents['type']
        # contents['value']
        typed, value = get_parameter_type(contents['type'], contents['value'])
        if not typed and not value:
            continue
        define_input = define.CreateInput(parameter, typed)
        define_input.Set(value)


def get_parameter_type(typed, value):
    current_type = None
    current_value = None
    # FloatAttr2 == Float2
    # FloatAttr3 == Color3f
    # FloatAttr6 == Double3Array
    # DoubleAttr3 == 3DDouble3Arry
    # DoubleAttr6 == Double3Arry
    if typed == 'StringAttr1':
        current_type = Sdf.ValueTypeNames.String
        if os.path.isabs(value):
            current_type = Sdf.ValueTypeNames.Asset
        current_value = value
    if typed == 'IntAttr1':
        current_type = Sdf.ValueTypeNames.Int
        current_value = int(value)
    if typed == 'FloatAttr1':
        current_type = Sdf.ValueTypeNames.Float
        current_value = value
    if typed == 'FloatAttr2':  # Float2
        current_type = Sdf.ValueTypeNames.Float2
        current_value = Gf.Vec2f(value)
    if typed == 'FloatAttr3':  # Color3f
        current_type = Sdf.ValueTypeNames.Color3f
        current_value = Gf.Vec3f(value)          
    if typed == 'FloatAttr6':  # Double3Array
        current_type = Sdf.ValueTypeNames.Double3Array
        current_value = Vt.Vec3fArray(
            2,
            (
                Gf.Vec3f(
                    value[0],
                    value[1],
                    value[2]
                    ),
                Gf.Vec3f(
                    value[3],
                    value[4],
                    value[5]
                    )                    
                )
            )
    if typed == 'FloatArray2':
        current_type = Sdf.ValueTypeNames.Float23Array
        array_size = len(value)
        current_value = Vt.Vec2fArray(array_size, value)
    if typed == 'IntArrayAttr':
        current_type = Sdf.ValueTypeNames.IntArray
        current_value = Vt.IntArray(value)
    if typed == 'DoubleAttr3':  # 3DDouble3Arry
        current_type = Sdf.ValueTypeNames.Double3Array
        current_value = Gf.Vec3f(value)
    if typed == 'DoubleAttr6' and len(current_value) == 3:  # Double3Arry
        current_type = Sdf.ValueTypeNames.Double3Array
        current_value = Vt.Vec3dArray(
            2,
            (
                Gf.Vec3d(
                    value[0],
                    value[1],
                    value[2]
                    ),
                Gf.Vec3d(
                    value[3],
                    value[4],
                    value[5]
                    )                    
                )
            )
    return current_type, current_value

