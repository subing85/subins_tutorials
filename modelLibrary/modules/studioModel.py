
from maya import OpenMaya


from modelLibrary.modules import studioMaya

import studioMaya

reload(studioMaya)


class Model(studioMaya.Maya):
    
    def __init__(self, maya_object=None, object_data=None):
        
        self.object = maya_object
        self.data = object_data    
    
    def create(self):
        pass
    
    def save(self):
        passs   
    
    def read(self):        
        data = self.get_polygon_mesh(self.object)
        return data
    
    def write(self):
        pass
        

    def get_polygon_mesh (self, mesh_shape):       
        mesh_dag_path = self.getDagPath(mesh_shape)    
        mfn_mesh = OpenMaya.MFnMesh (mesh_dag_path)
           
        point_array = OpenMaya.MFloatPointArray()
        mfn_mesh.getPoints (point_array, OpenMaya.MSpace.kObject)
        
        vertex_count = OpenMaya.MIntArray ()
        vertex_array = OpenMaya.MIntArray ()
        mfn_mesh.getVertices (vertex_count, vertex_array)
        
        set_names = []        
        mfn_mesh.getUVSetNames(set_names)                
        uvs_data = {}           
        for index in range (len(set_names)):        
            u_array = OpenMaya.MFloatArray ()
            v_array = OpenMaya.MFloatArray ()
            mfn_mesh.getUVs (u_array, v_array, set_names[index])
        
            uv_counts = OpenMaya.MIntArray ()
            uv_ids = OpenMaya.MIntArray ()
            mfn_mesh.getAssignedUVs (uv_counts, uv_ids, set_names[index]) 
                            
            current_set = {}            
            current_set['set_name'] = set_names[index]
            current_set['u_array'] = list(u_array)
            current_set['v_array'] = list(v_array)
            current_set['uv_counts'] = list(uv_counts)
            current_set['uv_ids'] = list(uv_ids)
            
            uvs_data.setdefault (index, current_set)           
    
        vertice_list = []        
        for index in range (point_array.length()) :
            print           point_array[index]
            vertice_list.append ((point_array[index].x, point_array[index].y, point_array[index].z, point_array[index].w)) 
            
        m_dag_path = self.getParentNode(mesh_shape)   
          
        polyData = {}  
        
        polyData['name'] = {
            'transform': m_dag_path.fullPathName().encode(), 
            'shape': mesh_shape.encode()
            }
        polyData['vertices'] = vertice_list    
        polyData['vertex_count'] = list(vertex_count)
        polyData['vertex_list'] = list(vertex_array)
        polyData['uvs'] = uvs_data
        
        polyData['num_edges'] = mfn_mesh.numEdges()
        polyData['num_fFace_vertices'] = mfn_mesh.numFaceVertices()
        polyData['num_polygons'] = mfn_mesh.numPolygons()
        polyData['num_normals'] = mfn_mesh.numNormals()
        polyData['num_uv_sets'] = mfn_mesh.numUVSets()
        polyData['num_uvs'] = mfn_mesh.numUVs()
        polyData['num_ertices'] = mfn_mesh.numVertices()   
    
        return polyData
        
        
    
    
