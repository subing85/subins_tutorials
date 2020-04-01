import math

from maya import OpenMaya

from studio_usd_pipe.api import studioMaya
from __builtin__ import True, False

reload(studioMaya)


class Model(studioMaya.Maya):
    
    def __init__(self):
        # studioMaya.Maya.__init__(self)
        super(Model, self).__init__()

         
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
        ds_mplug = mfn_mesh.findPlug('doubleSided')
        bounding_box = mfn_mesh.boundingBox()
        min_mpoint = bounding_box.min()
        max_mpoint = bounding_box.max()
        bounding_value = {
            'min': [min_mpoint.x, min_mpoint.y, min_mpoint.z],
            'max': [max_mpoint.x, max_mpoint.y, max_mpoint.z]
            }
        mesh_smooth = OpenMaya.MMeshSmoothOptions()
        mfn_mesh.getSmoothMeshDisplayOptions(mesh_smooth)
        
        num_polygons, polygon_vertices = self.get_kfacesvertices(mfn_mesh)
        data = {
            'vertices': vertice_list,
            'vertex_count': list(vertex_count),
            'vertex_list': list(vertex_array),
            'num_vertices': mfn_mesh.numVertices(),
            'num_polygons': num_polygons,
            'polygon_vertices': polygon_vertices,
            'double_sided': ds_mplug.asInt(),
            'bounding': bounding_value,
            'shape':  mfn_mesh.name(),
            'subdmesh': mesh_smooth.divisions()
            }
        return data
    
    def get_kfacesvertices(self, mfn_mesh):
        num_polygons = mfn_mesh.numPolygons()
        polygon_vertices = []
        for index in range(num_polygons):
            mint_array = OpenMaya.MIntArray()
            mfn_mesh.getPolygonVertices(index, mint_array)
            polygon_vertices.append(list(mint_array))
        return num_polygons, polygon_vertices   
    
    def validate_mesh(self, mfn_mesh, num_polygons, polygon_vertices):
        m_num_polygons, m_polygon_vertices = self.get_kfacesvertices(mfn_mesh)
        if num_polygons != m_num_polygons:
            return False
        if polygon_vertices != m_polygon_vertices:
            return False
        return True
            
    def create_model(self, name, data, replace=False):
        if replace:
            mfn_mesh = self.update_kmodel(name, data)
            if not mfn_mesh:
                if self.object_exists(name):
                    children = self.get_children(name)
                    for x in range(children.length()):
                        self.unparent(children[x])
                    self.remove_node(name)                
                mfn_mesh = self.create_kmodel(name, data)       
        else:
            mfn_mesh = self.create_kmodel(name, data)

    def create_kmodel(self, name, data):
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
        mfn_dag_node = OpenMaya.MFnDagNode(mfn_mesh.parent(0))
        mfn_dag_node.setName(name)        
        mfn_mesh.updateSurface()
        return mfn_mesh

    def update_kmodel(self, name, data):
        num_polygons = data['num_polygons']
        polygon_vertices = data['polygon_vertices']
        vertex_array = self.create_floatpoint_array(data['vertices'])
        if not self.object_exists(name):
            return None
        dag_path = self.get_dagpath(name)         
        shape_dag_path = self.get_shape_node(dag_path)
        mfn_mesh = OpenMaya.MFnMesh(shape_dag_path)
        if not self.validate_mesh(mfn_mesh, num_polygons, polygon_vertices):
            return None
        mfn_mesh.setPoints(vertex_array, OpenMaya.MSpace.kObject)
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
                                  
    def get_model_data(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, root_mobject=mobject)
        data = {}
        for x in range(transform_mesh.length()):
            model_data = self.get_kmodel(transform_mesh[x])
            model_data['order'] = x
            data.setdefault(transform_mesh[x].fullPathName(), model_data)            
        return data
    
    def get_uv_data(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, root_mobject=mobject)
        data = {}
        for x in range(transform_mesh.length()):
            model_data = self.get_kuv(transform_mesh[x])
            model_data['order'] = x
            data.setdefault(transform_mesh[x].fullPathName(), model_data)            
        return data
    



        
        
        
        
          