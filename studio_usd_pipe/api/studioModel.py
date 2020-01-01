import math

from maya import OpenMaya

from studio_usd_pipe.api import studioMaya

reload(studioMaya)


class Model(studioMaya.Maya):
    
    def __init__(self):
        studioMaya.Maya.__init__(self)
         
    def get_ktransform(self, mobject):
        mfn_transform = OpenMaya.MFnTransform(mobject)        
        m_matrix = mfn_transform.transformation()
        # get translate      
        mvector = m_matrix.translation(OpenMaya.MSpace.kWorld)        
        translation = [mvector.x, mvector.y, mvector.z]
        # get rotation   
        m_euler = m_matrix.eulerRotation()
        angles = [m_euler.x, m_euler.y, m_euler.z]
        rotation = [math.degrees(angle) for angle in angles]
        # get scale     
        scale_util = OpenMaya.MScriptUtil()
        scale_util.createFromList([0, 0, 0], 3)
        double = scale_util.asDoublePtr()
        m_matrix.getScale(double, OpenMaya.MSpace.kWorld)
        scale = [OpenMaya.MScriptUtil.getDoubleArrayItem(double, x) for x in range(3)]
        data = {
            'translate': translation,
            'rotate': rotation,
            'scale': scale
            }                 
        return data 
        
    def get_kmodel(self, mobject):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        point_array = OpenMaya.MFloatPointArray()
        mfn_mesh.getPoints(point_array, OpenMaya.MSpace.kObject)
        vertex_count = OpenMaya.MIntArray()
        vertex_array = OpenMaya.MIntArray()
        mfn_mesh.getVertices(vertex_count, vertex_array)        
        vertice_list = []
        for index in range(point_array.length()):
            points = point_array[index]
            vertice_list.append((points.x, points.y, points.z, points.w))
        data = {
            'vertices': vertice_list,
            'vertex_count': list(vertex_count),
            'vertex_list': list(vertex_array),
            'num_vertices': mfn_mesh.numVertices(),
            'num_polygons': mfn_mesh.numPolygons(),
            'shape':  mfn_mesh.name(),
            }
        return data    
    
    def create_kmodel(self, data):
        num_vertices = data['num_vertices']
        num_polygons = data['num_polygons']
        vertex_array = self.create_floatpoint_array(data['vertices'])
        vertex_count = self.create_int_array(data['vertex_count'])
        vertex_list = self.create_int_array(data['vertex_list'])        
        mfn_mesh = OpenMaya.MFnMesh()
        mfn_mesh.create(
            num_vertices,
            num_polygons,
            vertex_array,
            vertex_count,
            vertex_list
            )        
        mfn_mesh.setName(data['shape'])        
        parent_mobject = mfn_mesh.parent(0)
        mfn_mesh.updateSurface()
        return mfn_mesh
    
    def get_kuv(self, mobject):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        data = {}
        for index, set_name in enumerate(set_names):
            u_array = OpenMaya.MFloatArray()
            v_array = OpenMaya.MFloatArray()
            mfn_mesh.getUVs(u_array, v_array, set_name)
            uv_counts = OpenMaya.MIntArray()
            uv_ids = OpenMaya.MIntArray()
            mfn_mesh.getAssignedUVs(uv_counts, uv_ids, set_name)
            uvset_data = {
                'u_array': list(u_array),
                'v_array': list(v_array),
                'uv_counts': list(uv_counts),
                'uv_ids': list(uv_ids),
                'order': index
                }
            data.setdefault(set_name, uvset_data)
        return data        

    def create_kuv(self, mobject, data):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)                
        self.delete_uv_sets(mfn_mesh, set_names)        
        sorted_data = self.sort_dictionary(data)        
        for index, set_name in enumerate(sorted_data):
            contents = data[set_name]
            u_array = self.create_float_array(contents['u_array'])
            v_array = self.create_float_array(contents['v_array'])
            uv_counts = self.create_int_array(contents['uv_counts'])
            uv_ids = self.create_int_array(contents['uv_ids'])            
            if index == 0:
                mfn_mesh.clearUVs(set_name)
                mfn_mesh.renameUVSet(set_names[0], set_name)
            else:
                set_name = mfn_mesh.createUVSetWithName(set_name)                
            mfn_mesh.setUVs(u_array, v_array, set_name)
            mfn_mesh.assignUVs(uv_counts, uv_ids, set_name)
        mfn_mesh.updateSurface()
        return mfn_mesh              
              
    def delete_uv_sets(self, mfn_mesh, set_names):
        for set_name in set_names:
            try:
                mfn_mesh.deleteUVSet(set_name)
            except Exception as error:
                print '\nDeleteError', error
                                  
