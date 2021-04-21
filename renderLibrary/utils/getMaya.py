import os
import math

from maya import OpenMaya

from renderLibrary.api import mayaRender

MR = mayaRender.Connect()



def layer(render_layer):
    
    # engine = MR.currentRenderEngine
    
    
    
    
    
    pass





def rootNode(node):
    mn = mayaNode.Connect()
    root_node = mn.getRootNode(node)
    return root_node

    
def geometries(layer, root_node):
    selectLayer(layer)
    mn = mayaNode.Connect()    
    mesh_hierarchy = mn.getMeshHierarchy(root_node)
    
    _geometries = {}
    
    for index in range (mesh_hierarchy.length()):
        node = mesh_hierarchy[index].fullPathName()
        _node = mesh_hierarchy[index].partialPathName()
        
        _geometries[node] = {}
        
        mesh_hierarchy[index].extendToShape()
        shape = mesh_hierarchy[index].partialPathName()
        
        _geometries[node]['shape'] = shape
        
        shading_engines = mn.getShadingEngines(mesh_hierarchy[index])
        
        shading = {}
             
        for x in range(shading_engines.length()):
            
            shader = mn.getShader(shading_engines[x])
            materials = mn.getMaterialNodes(shader)            
            members = mn.getAssignComponents(shading_engines[x])
            members = set(sum(members.values(), []))
            
            _members = []
            for member in members:                
                if not member.startswith(_node):
                    continue
                _members.append(member)
           
            sg_mfnnode = OpenMaya.MFnDependencyNode(shading_engines[x])
            sh_mfn_node = OpenMaya.MFnDependencyNode(shader)
            
            _materials = []            
            for m in range(materials.length()):
                ma_mfnnode = OpenMaya.MFnDependencyNode(materials[m])
                _materials.append(ma_mfnnode.name())
            
            contents = {
                'shading_engines': sg_mfnnode.name(),
                'shader': sh_mfn_node.name(),
                'materials': _materials,
                'members': _members
                }
            
            shading.setdefault(x, contents)

        _geometries[node]['shading'] = shading

    return _geometries


def shaders(layer, root_node):
    selectLayer(layer)
    mn = mayaNode.Connect()    
    mesh_hierarchy = mn.getMeshHierarchy(root_node)
    
    _shaders, _nodes = {}, []
    
    for index in range (mesh_hierarchy.length()):
        node = mesh_hierarchy[index].fullPathName()
        _node = mesh_hierarchy[index].partialPathName()
        mesh_hierarchy[index].extendToShape()
        shape = mesh_hierarchy[index].partialPathName()

        shading_engines = mn.getShadingEngines(mesh_hierarchy[index])
             
        for x in range(shading_engines.length()):

            sg_mfnnode = OpenMaya.MFnDependencyNode(shading_engines[x])
            if sg_mfnnode.name() in _shaders:
                _shaders[sg_mfnnode.name()].setdefault('nodes', []).append(node)
                _shaders[sg_mfnnode.name()].setdefault('shapes', []).append(shape)
                continue
  
            shader = mn.getShader(shading_engines[x])
            materials = mn.getMaterialNodes(shader)            
            members = mn.getAssignComponents(shading_engines[x])
            members = set(sum(members.values(), []))
            
            _members = []
            for member in members:                
                if not member.startswith(_node):
                    continue
                _members.append(member)
           
            sh_mfn_node = OpenMaya.MFnDependencyNode(shader)
            
            _materials = []            
            for m in range(materials.length()):
                ma_mfnnode = OpenMaya.MFnDependencyNode(materials[m])
                _materials.append(ma_mfnnode.name())
            
            contents = {
                'shader': sh_mfn_node.name(),
                'materials': _materials,
                'members': _members,
                'nodes': [node],
                'shapes': [shape]
                }
            _shaders.setdefault(sg_mfnnode.name(), contents)
            _nodes.append(sg_mfnnode.name())
            _nodes.append(sh_mfn_node.name())
            _nodes.extend(_materials)

    return _shaders, _nodes


def lights(layer):
    selectLayer(layer)
    
    mn = mayaNode.Connect()    
    members = mn.getRenderMembers(layer)
    node_types = mn.nodeTypes('light')
    
    _lights = {}
    
    for member in members:

        dagpath = mn.getDagPath(member)
        
        if dagpath.childCount():
            dagpath.extendToShape()  
                  
        node_type = mn.nodeType(dagpath.fullPathName())
        
        if node_type not in node_types:
            continue
        
        shape = dagpath.fullPathName()
        
        dagnode = OpenMaya.MFnDagNode(dagpath)
        mobject = dagnode.parent(0)
        _dagpath = OpenMaya.MDagPath()
        _dagpath.getAPathTo(mobject, _dagpath)
    
        contents = {
            'shape': shape
        }
        _lights.setdefault(_dagpath.fullPathName(), contents)
                
    return  _lights       
    
  
def overrides(layer, includes):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getOverrides('batman')
    '''
    selectLayer(layer)
    
    if isinstance(includes, dict):       
        nodes = []
        for k, v in includes.items():
            nodes.append(k)
            if not v.get('shape'):
                continue
            nodes.append(v['shape'])
    else:
        nodes = includes
        
    mn = mayaNode.Connect()
    _overrides = {}
    for node in nodes:        
        overrides = mn.getOverrides(node, layer)
        if not overrides:
            continue
        _overrides.setdefault(node, overrides)
    return _overrides


def renderMembers(layer, includes):
    '''
    :example
        from renderLibrary.utils import studioMaya
        studioMaya.getRenderMembers('batman', typed=OpenMaya.MFn.kMesh)
    '''  
    
    selectLayer(layer)
    
    if isinstance(includes, dict):       
        nodes = []
        for k, v in includes.items():
            nodes.append(k)
            if not v.get('shape'):
                continue
            nodes.append(v['shape'])
    else:
        nodes = includes
    
    mn = mayaNode.Connect()    
    members = mn.getRenderMembers(layer)
    _members = []
    for member in members:
        if member not in nodes:
            continue
        _members.append(member)
    return _members


def nodesTransform(nodes):
    _transform = {}
    for node in nodes:
        _values = transformValues(node)
        _transform.setdefault(node, _values)
    return _transform
        

def transformValues(node):
    mn = mayaNode.Connect()
    dagpath = mn.getDagPath(node)
    # get world sapce translate value
    transform_matrix = OpenMaya.MTransformationMatrix(dagpath.inclusiveMatrix())
    mvector = transform_matrix.getTranslation(OpenMaya.MSpace.kWorld)       
    
    # get world sapce rotate pivot value
    mfn_transform = OpenMaya.MFnTransform(dagpath)
    _transform_matrix = mfn_transform.transformation()
    mpoints = _transform_matrix.rotatePivot(OpenMaya.MSpace.kWorld)
    
    translate = [
        mvector.x + mpoints.x,
        mvector.y + mpoints.y,
        mvector.z + mpoints.z
        ]
    
    # get rotation value
    m_euler = transform_matrix.eulerRotation()
    angles = [m_euler.x, m_euler.y, m_euler.z]
    rotate = [math.degrees(angle) for angle in angles] 
    
    # get scale value
    scale_util = OpenMaya.MScriptUtil()
    scale_util.createFromList([0, 0, 0], 3)
    double = scale_util.asDoublePtr()
    transform_matrix.getScale(double, OpenMaya.MSpace.kWorld)
    scale = [OpenMaya.MScriptUtil.getDoubleArrayItem(double, x) for x in range(3)]       
       
    _transform = {
        'translate': translate,
        'rotate': rotate,
        'scale': scale
        }
    
    return _transform


def renderLayer(layer):
    selectLayer(layer)    
    mr = mayaRender.Connect()    
    layer_attributes = mr.getLayerAttributes(layer)
    return layer_attributes    


def aovs(layer):
    selectLayer(layer)    
    mr = mayaRender.Connect()
    aovs = mr.getAovs(overrides=True, layer=layer)
    return aovs


def renderGlobals(layer):
    selectLayer(layer)    
    mr = mayaRender.Connect()
    render_globals = mr.getRenderGlobals()
    return render_globals    


def nodesAttributes(nodes):
    
    if isinstance(nodes, dict):       
        _nodes = []
        for k, v in nodes.items():
            _nodes.append(k)
            if not v.get('shape'):
                continue
            _nodes.append(v['shape'])
    else:
        nodes = nodes
 
    node_attributes = {}
    
    for node in _nodes:
        attributes = attributeValue(node)
        node_attributes.setdefault(node, attributes)
    return node_attributes


def attributeValue(node):    
    mn = mayaNode.Connect()
    attributes = mn.getAttributes(node)
    return attributes


def addStudioAttribute(node, values):
    mn = mayaNode.Connect()
        
    mn.addStringATtributes(node, 'studioSceneDescription', 'ssd', value=str(values))


def exportSelection(nodes, path, **kwargs):
    format = kwargs.get('format') or 'mayaAscii'    
    preserved = kwargs.get('preserved') or False
    
    if os.path.isfile(path):
        try:
            os.chmod(path, 0777)
            os.remove(path)
        except Exception as error:
            print '#remove error', error
    
    mselection_list = OpenMaya.MSelectionList()
    for node in nodes:
        mselection_list.add(node)  
    OpenMaya.MGlobal.setActiveSelectionList(mselection_list)
    OpenMaya.MFileIO.exportSelected(path, format, preserved) 
    OpenMaya.MGlobal.clearSelectionList()
    
    

             
