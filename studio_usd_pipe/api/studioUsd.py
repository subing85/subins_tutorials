import json

import os

from pxr import Vt
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
from maya import OpenMaya        
from __builtin__ import None
from dns.rdataclass import NONE


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
        materials = self.sort_dictionary(data)
        # make geomery hierarchy
        for material in materials:
            for geometry in data[material]['geometries']:
                sdf_path = Sdf.Path(geometry.replace('|', '/'))                
                for path in sdf_path.GetPrefixes():
                    UsdGeom.Xform.Define(stage, path)
                mesh_define = UsdGeom.Mesh.Define(stage, sdf_path.GetPrefixes()[-1])
                
        # make materials
        look_path = Sdf.Path('/{}/Looks'.format(root))                     
        UsdGeom.Scope.Define(stage, look_path)
        for material in materials:
            contents = data[material]
            material_path = look_path.AppendPath(material)    
            UsdShade.Material.Define(stage, material_path)
            for node, node_contents in contents['nodes'].items():
                shader_path = material_path.AppendPath(node)
                shader_define = UsdShade.Shader.Define(stage, shader_path)
                shader_define.CreateIdAttr(node_contents['type'])               
                                     
                if 'parameters' not in node_contents:
                    continue            
                print  '\n', node          
                for parameter, parameter_contents in node_contents['parameters'].items():            
                    current_type, current_value = self.get_prameter_values(
                        parameter_contents['type'],
                        parameter_contents['value']
                        )
                    if not current_type:
                        print '\t', parameter, parameter_contents['type']
                        print '\t', current_type, current_value
                        print '\t', type(current_type)                
                        raise Exception('function get_prameter_values need to update')
            

            
            shader_define.CreateInput(parameter, current_type).Set(current_value)
                  
        
                                             
                                     
                                     
        print stage.GetRootLayer().ExportToString()

    
    def create_model_usd(self, root, data, show=False):
        stage = self.create_model(data['mesh'], stage=None)
        stage = self.create_curve(data['curve'], stage=stage)
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
          
    def create_uv_usd(self, root, data, show=False):
        stage = self.create_uv(data['mesh'], stage=None)
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
        
    def create_surface_usd(self, root, data, show=False):
        
        return
        stage = self.create_surface(root, data['surface'], stage=None)
        
        return
        if show:
            print stage.GetRootLayer().ExportToString()
        stage.Save()
        
    
    def get_prameter_values(self, type, value):
        current_type = None
        current_value = None   
        
        
        if type=='StringAttr':
            current_type = Sdf.ValueTypeNames.String
            if os.path.isabs(value):
                current_type = Sdf.ValueTypeNames.Asset
            current_value = value 
            
        if  type=='IntAttr':
            current_type = Sdf.ValueTypeNames.Int
            current_value = value
            
        if  type=='FloatAttr':
            current_type = Sdf.ValueTypeNames.Float
            current_value = value
               
        if type=='2FloatAttr':
            current_type = Sdf.ValueTypeNames.Float2
            current_value =  Gf.Vec2f(value)     
                       
        if type=='3FloatAttr':
            current_type = Sdf.ValueTypeNames.Color3f
            current_value = Gf.Vec3f(value)
        
            
        
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
