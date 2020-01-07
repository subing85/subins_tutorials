import json

import os

from pxr import Vt
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
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
        if data>0:
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
        
        
    
    def create_model_usd(self, root, data, show=False):
        
       
        
        stage = self.create_geometry(data['mesh'], stage=None)
        
        stage = self.create_uv(data['curve'], stage=stage)
        
        if show:
            print stage.GetRootLayer().ExportToString()
                    
        stage.Save()
        
        #=======================================================================
        # root_location = Sdf.Path('/{}'.format(root))       #   
        # self.make_defalt_prim(stage, root_location)
        # 
        # stage.Save()
        # os.utime(self.usd_path, (time_stamp, time_stamp))
        # print '// Result:', self.usd_path 
        # OpenMaya.MGlobal.displayInfo('create usd geometry success!...')
        #=======================================================================
        
    
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
            curev_define = UsdGeom.NurbsCurves.Define(stage, sdf_path.GetPrefixes()[-1])

            self.make_c_vertex_counts(curev_define, [11])
            self.make_c_extent(curev_define, current_data['bounding'])
            self.make_c_knots(curev_define, current_data['knots'])
            self.make_c_order(curev_define, [4])
            self.make_c_points(curev_define, current_data['points'])
            self.make_c_ranges(curev_define, (0, 8))
            self.make_c_widths(curev_define, [1])
            
        return stage
        
        
            
                        
                            
    def create_geometry(self, data, stage=None):
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

        return  stage
            


    
    def create_preview_surface(self, data, output_path, time_stamp):
        pass
    
    
    def create_surface(self, data, output_path, time_stamp):
        pass
    

    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order        