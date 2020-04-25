import json

import os

import sys

sys.path.append('/usr/local/usd/maya2018/pixar/19.05/lib/python')

from pxr import Vt
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import Kind
from pxr import UsdGeom
from pxr import UsdShade
from maya import OpenMaya


class Susd(object):
    
    def __init__(self, path=None):
        if path:
            path = '{}.usd'.format(os.path.splitext(path)[0])
        self.usd_path = path
        self.up_axis = UsdGeom.Tokens.y
        
    def make_defalt_prim(self, stage, location):
        stage.SetDefaultPrim(stage.GetPrimAtPath(location))
        UsdGeom.SetStageUpAxis(stage, self.up_axis)
        
    def make_m_subdivision(self, define, data):
        subdivision = define.CreateSubdivisionSchemeAttr()        
        subdmesh = 'none'    
        if data > 0:
            subdmesh = 'catmullClark'   
        subdivision.Set(subdmesh)
        
    def make_m_doublesided(self, define, data):        
        doublesided = define.CreateDoubleSidedAttr()
        doublesided_value = Vt.Bool(data)
        doublesided.Set(doublesided_value)
        
    def make_m_extent(self, define, data):
        extent = define.CreateExtentAttr()
        extent_value = Vt.Vec3fArray(
            2, (Gf.Vec3f(data['min']), Gf.Vec3f(data['max'])))    
        extent.Set(extent_value)
        
    def make_m_face_vertex_counts(self, define, data):
        vertex_counts = define.CreateFaceVertexCountsAttr()
        vertex_count_value = Vt.IntArray(data)
        vertex_counts.Set(vertex_count_value)   
         
    def make_m_face_vertex_indices(self, define, data):    
        vertex_indices = define.CreateFaceVertexIndicesAttr()
        vertex_indices_value = Vt.IntArray(data)
        vertex_indices.Set(vertex_indices_value)
        
    def make_m_points(self, define, data):    
        points = define.CreatePointsAttr()
        xyz = [(x, y, z) for x, y, z, w in data]
        point_value = Vt.Vec3fArray(len(xyz), (xyz))
        points.Set(point_value)
        
    def make_uv_points_ids(self, define, set, data):
        uv_primvar = define.CreatePrimvar(
            set,
            Sdf.ValueTypeNames.Float2Array,
            UsdGeom.Tokens.faceVarying
            )
        value = Vt.Vec2fArray(len(data), data[0])
        uv_primvar.Set(value)
        value = Vt.IntArray(data[1])
        uv_primvar.SetIndices(value)                
        
    def make_uv_ids(self, define, set, data):
        uv_indices = define.CreatePrimvar(
            set,
            Sdf.ValueTypeNames.IntArray
            )
        value = Vt.IntArray(data)
        uv_indices.SetIndices(value)
        
    def make_c_vertex_counts(self, define, data):        
        vertex_counts = define.CreateCurveVertexCountsAttr()
        vertex_count_value = Vt.IntArray(data)
        vertex_counts.Set(vertex_count_value)
        
    def make_c_extent(self, define, data):
        extent = define.CreateExtentAttr()
        extent_value = Vt.Vec3fArray(
            2, (Gf.Vec3f(data['min']), Gf.Vec3f(data['max'])))                                                  
        extent.Set(extent_value)
        
    def make_c_knots(self, define, data):
        knots = define.CreateKnotsAttr()
        knots_value = Vt.DoubleArray(data)
        knots.Set(knots_value)
        
    def make_c_order(self, define, data):
        order = define.CreateOrderAttr()
        order_value = Vt.IntArray(data)
        order.Set(order_value)
        
    def make_c_points(self, define, data):
        points = define.CreatePointsAttr()
        xyz = [(x, y, z) for x, y, z, w in data]
        point_value = Vt.Vec3fArray(len(xyz), (xyz))
        points.Set(point_value)
        
    def make_c_ranges(self, define, data):
        ranges = define.CreateRangesAttr()
        ranges_value = Vt.Vec2dArray(1, (data))
        ranges.Set(ranges_value)
        
    def make_c_widths(self, define, data):
        widths = define.CreateWidthsAttr()
        widths_value = Vt.FloatArray(data)
        widths.Set(widths_value)        
        
    def create_asset_ids(self, stage, root, data):
        define = UsdGeom.Xform.Define(stage, '/{}'.format(root))
        ids = self.sort_dictionary(data)
        for id in ids:
            primvar = define.CreatePrimvar(id, Sdf.ValueTypeNames.String)
            primvar.Set(data[id]['value'])
            primvar.SetInterpolation('constant')
        return stage

    def create_curve(self, data, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        geometries = self.sort_dictionary(data)
        for geometry in geometries:
            location = geometry.replace(':', '_')  
            sdf_path = Sdf.Path(location.replace('|', '/'))        
            current_data = data[geometry]
            for path in sdf_path.GetPrefixes():
                UsdGeom.Xform.Define(stage, path)
            curev_define = UsdGeom.NurbsCurves.Define(stage, sdf_path.GetPrefixes()[-1])
            self.make_c_vertex_counts(curev_define, [11])
            self.make_c_extent(curev_define, current_data['bounding'])
            self.make_c_knots(curev_define, current_data['knots'])
            self.make_c_order(curev_define, [4])
            self.make_c_points(curev_define, current_data['points'])
            self.make_c_ranges(curev_define, (0, 8))
            self.make_c_widths(curev_define, [1])
            
        return stage
          
    def create_model(self, data, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        geometries = self.sort_dictionary(data)
        for geometry in geometries:
            location = geometry.replace(':', '_')  
            sdf_path = Sdf.Path(location.replace('|', '/'))
            current_data = data[geometry]
            for path in sdf_path.GetPrefixes():
                UsdGeom.Xform.Define(stage, path)
            mesh_define = UsdGeom.Mesh.Define(stage, sdf_path.GetPrefixes()[-1])
            self.make_m_subdivision(mesh_define, current_data['subdmesh'])
            self.make_m_doublesided(mesh_define, current_data['double_sided'])            
            self.make_m_extent(mesh_define, current_data['bounding'])
            self.make_m_face_vertex_counts(mesh_define, current_data['vertex_count'])
            self.make_m_face_vertex_indices(mesh_define, current_data['vertex_list'])
            self.make_m_points(mesh_define, current_data['vertices'])
        return stage

    def create_uv(self, data, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        geometries = self.sort_dictionary(data)
        for geometry in geometries:
            location = geometry.replace(':', '_')  
            sdf_path = Sdf.Path(location.replace('|', '/'))
            current_data = data[geometry]
            for path in sdf_path.GetPrefixes():
                UsdGeom.Xform.Define(stage, path)
            mesh_define = UsdGeom.Mesh.Define(stage, sdf_path.GetPrefixes()[-1])
            uv_sets = self.sort_dictionary(current_data)
            for index, uv_set in enumerate(uv_sets):
                uv_d = current_data[uv_set]
                uv_points = []
                for x in range(len(uv_d['u_array'])):
                    uv_points.append((uv_d['u_array'][x], uv_d['u_array'][x]))
                current_set = 'st'
                if index>0:
                    current_set = uv_set
                uv_data = [uv_points, uv_d['uv_ids']]
                self.make_uv_points_ids(mesh_define, current_set, uv_data)
        return stage
    
    def create_preview_surface(self, data, stage=None):
        pass
    
           
    def create_surface(self, root, data, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        # make geomery hierarchy
        for material in data:            
            for geometry in data[material]['geometries']:
                location = geometry.replace(':', '_')  
                sdf_path = Sdf.Path(location.replace('|', '/'))                
                for path in sdf_path.GetPrefixes():
                    UsdGeom.Xform.Define(stage, path)
                mesh_define = UsdGeom.Mesh.Define(stage, sdf_path.GetPrefixes()[-1])
                
        look_path = Sdf.Path('/{}/Looks'.format(root))                     
        UsdGeom.Scope.Define(stage, look_path)
        materials = self.sort_dictionary(data)        
        for material in materials: # make materials
            contents = data[material]
            material_path = look_path.AppendPath(material)    
            UsdShade.Material.Define(stage, material_path)
            # make shader and attributes
            for node, node_contents in contents['nodes'].items():
                shader_path = material_path.AppendPath(node)
                shader_define = UsdShade.Shader.Define(stage, shader_path)
                shader_define.CreateIdAttr(node_contents['type'])               
                if 'parameters' not in node_contents:
                    continue            
                for parameter, parameter_contents in node_contents['parameters'].items():
                    current_type, current_value = self.get_prameter_values(
                        parameter_contents['type'],
                        parameter_contents['value']
                        )
                    if not current_type or current_value=='null':
                        print '#need to update attribute configure'
                        print '\tmaterial', material, node, parameter
                        print '\t', parameter, parameter_contents['type'], parameter_contents['value']
                        print '\t', current_type, current_value
                        print '\t', type(current_type)                
                        raise Exception('function get_prameter_values need to update')
                    print '\t\t>>>>>', current_type, parameter_contents['value']
                    shader_define.CreateInput(parameter, current_type).Set(current_value)
        # shader connections
        for material, contents in data.items():
            for node, node_contents in contents['nodes'].items(): 
                if 'connections' not in node_contents:
                    continue               
                for parameter, connection_contents in node_contents['connections'].items():
                    source_attribute, source_node = connection_contents['value'].split('@')
                    shader_path = look_path.AppendPath('%s/%s'%(material, node))
                    source_path = look_path.AppendPath('%s/%s'%(material, source_node))
                    shader_define = UsdShade.Shader.Define(stage, shader_path)
                    source_define = UsdShade.Shader.Define(stage, source_path)
                    current_type, current_value = self.get_prameter_values(
                        connection_contents['type'],
                        None
                        )
                    shader_input = shader_define.CreateInput(parameter, current_type)
                    shader_input.ConnectToSource(source_define, source_attribute)
        for material in data:
            # material assignments
            material_path = look_path.AppendPath(material)    
            material_define = UsdShade.Material.Define(stage, material_path)
            for geometry in data[material]['geometries']:
                location = geometry.replace(':', '_') 
                sdf_path = Sdf.Path(location.replace('|', '/'))
                mesh_define = UsdGeom.Mesh.Define(stage, sdf_path) 
                UsdShade.MaterialBindingAPI(mesh_define).Bind(material_define)           
            # material to shader connection                        
            shader = data[material]['surface']['shader']
            attribute = data[material]['surface']['attribute']    
            shader_path = look_path.AppendPath('%s/%s'%(material, shader))     
            material_define = UsdShade.Material.Define(stage, material_path)
            shader_define = UsdShade.Shader.Define(stage, shader_path)
            shader_output = material_define.CreateOutput('ri:surface', Sdf.ValueTypeNames.Token)
            shader_output.ConnectToSource(shader_define, attribute)
        return stage   
   
    def create_model_usd(self, root, data, show=False):
        stage = self.create_model(data['mesh'], stage=None)
        stage = self.create_curve(data['curve'], stage=stage)
        stage = self.create_asset_ids(stage, root, data['asset_id'])
        self.add_default_prim(root, stage, Kind.Tokens.component)
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
          
    def create_uv_usd(self, root, data, show=False):
        stage = self.create_uv(data['mesh'], stage=None)
        stage = self.create_asset_ids(stage, root, data['asset_id'])
        self.add_default_prim(root, stage, Kind.Tokens.subcomponent)
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
        
    def create_surface_usd(self, root, data, show=False):
        '''
            from studio_usd_pipe.api import studioMaya
            from studio_usd_pipe.api import studioShader
            from studio_usd_pipe.core import mayapack
            from studio_usd_pipe.api import studioUsd
            
            sm = studioMaya.Maya()
            ss = studioShader.Shader()
            mp = mayapack.Pack()
            sud = studioUsd.Susd()
            
            asset_ids = [
                'sentity',
                'scaption',
                'stype',
                'stag',
                'sversion',
                'smodified',
                'spath',
                'sdescription'
                ]
            
            mobject = sm.get_mobject('model')
            surface_data = ss.get_surface_data(mobject)
            asset_ids = mp.get_asset_id_data('model', asset_ids)
            final_data = {
                'surface': surface_data,
                'asset_id': asset_ids            
                }  
                
            output_path = '/venture/shows/my_hero/assets/batman/surface/0.0.0/hello.usd'         
            susd = studioUsd.Susd(path=output_path)                
            susd.create_surface_usd('model', final_data)        
        '''
        stage = self.create_surface(root, data['surface'], stage=None)
        stage = self.create_asset_ids(stage, root, data['asset_id'])
        self.add_default_prim(root, stage, Kind.Tokens.subcomponent)
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
        
    def add_default_prim(self, header, stage, kind):    
        define_path = Sdf.Path('/{}'.format(header))
        default_prim = stage.DefinePrim(define_path)
        UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
        Usd.ModelAPI(default_prim).SetKind(kind)
    
    def get_prameter_values(self, attribute_type, attribute_value):
        current_type = None
        current_value = 'null'           
        if attribute_type=='StringAttr':
            current_type = Sdf.ValueTypeNames.String
            if attribute_value:
                if os.path.isabs(attribute_value):
                    current_type = Sdf.ValueTypeNames.Asset
                current_value = attribute_value 
        if  attribute_type=='IntAttr':
            current_type = Sdf.ValueTypeNames.Int            
            if isinstance(attribute_value, bool):
                current_value = int(attribute_value)
            if isinstance(attribute_value, int):
                current_value = int(attribute_value)
                         
        if  attribute_type=='FloatAttr':
            current_type = Sdf.ValueTypeNames.Float
            if attribute_value:
                current_value = attribute_value
        if attribute_type=='2FloatAttr':
            current_type = Sdf.ValueTypeNames.Float2
            if attribute_value:
                current_value =  Gf.Vec2f(attribute_value)     
        if attribute_type=='3FloatAttr':
            current_type = Sdf.ValueTypeNames.Color3f
            if attribute_value:
                current_value = Gf.Vec3f(attribute_value)
        return current_type, current_value

    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            if not isinstance(dictionary[contents], dict):
                continue
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order 
    
    
    
    def create_sublayer(self, components, stage=None):        
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        root_layer = stage.GetRootLayer()
        for component in components:
            root_layer.subLayerPaths.append(component)
        root_layer.Save()  
        return stage  
    
    def create_reference(self, name, components, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        # location = '/{}'.format(name)
        location = Sdf.Path('/{}'.format('subin'))
        prim = stage.DefinePrim(location, 'Xform')
        for component in components:
            prim.GetReferences().AddReference(component)
        stage.GetRootLayer().Save()  
    
    def create_payload(self, components, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
        for component in components:
            prim = stage.DefinePrim(component, 'Xform')
            path = component
            abc = Sdf.Payload(path, '/box_model')
            prim.SetPayload(abc)
        stage.GetRootLayer().Save()  
    
    
    def create_variant_reference(self, components, stage=None):
        if not stage:
            layer = Sdf.Layer.CreateNew(self.usd_path, args={'format': 'usda'})
            stage = Usd.Stage.Open(layer)
            
        
        components = ["/venture/shows/batman/assets/batman/model/0.0.0/batman.usd",
                        "/venture/shows/batman/assets/batman/model/1.0.0/batman.usd"]
                        
        usd_path = '/venture/shows/batman/tmp/variant_3.usd'                
                        
        layer = Sdf.Layer.CreateNew(usd_path, args={'format': 'usda'})
        stage = Usd.Stage.Open(layer)
        UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
        
        location = '/model'
        define = stage.DefinePrim(location, 'Xform')
        
        variant_prim = define.GetPrim()
        variant_path = define.GetPath()
        variant_set = variant_prim.GetVariantSet('versions')
        
        variant_set.AddVariant('0-0-0')
        variant_set.SetVariantSelection('0-0-0')
        
        with variant_set.GetVariantEditContext():
            referencs = variant_prim.GetReferences()
            referencs.AddReference(assetPath=components[0], primPath=variant_path)
        
        variant_set.AddVariant('1-0-0')
        variant_set.SetVariantSelection('1-0-0')
        
        with variant_set.GetVariantEditContext():
            referencs = variant_prim.GetReferences()
            referencs.AddReference(assetPath=components[1], primPath=variant_path)
        
        
        
        
        
        stage.GetRootLayer().Save()  
        
        
        
        
        
        # print stage.GetRootLayer().ExportToString()




    
    
    def create_inherits(self):
        pass
    
    def create_spe(self):
        pass    
    
    
    def example(self):
    
        {
        "model": {
            "2.0.1": {
                "usd": [
                    "/venture/shows/batman/assets/batman/model/2.0.1/batman.usd"
                ], 
                "location": "/venture/shows/batman/assets/batman/model/2.0.1"
            }
        }, 
        "uv": {
            "0.0.0": {
                "usd": [
                    "/venture/shows/batman/assets/batman/uv/0.0.0/batman.usd"
                ], 
                "location": "/venture/shows/batman/assets/batman/uv/0.0.0"
            }
        }, 
        "surface": {
            "2.0.1": {
                "usd": [
                    "/venture/shows/batman/assets/batman/surface/2.0.1/batman.usd"
                ], 
                "location": "/venture/shows/batman/assets/batman/surface/2.0.1"
            }
        }
        }           
