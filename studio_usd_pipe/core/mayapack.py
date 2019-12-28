import math
import json

from datetime import datetime

from maya import OpenMaya


from studio_usd_pipe import resource

from studio_usd_pipe.api import studioMaya


class Pack(studioMaya.Maya):
    
    def __init__(self):
        studioMaya.Maya.__init__(self)
        
       
        self.valid_objects = [OpenMaya.MFn.kTransform, OpenMaya.MFn.kMesh]        
        #=======================================================================
        # self.default_mobjects = self.get_default_nodes()
        # self.default_node_types = self.get_default_node_types()
        # self.valid_attribute = self.get_valid_attribute()           
        #=======================================================================
        self.nested_bundle = {}
        self.flatted_bundle = {}
        
    def make_packing_arguments(self, arguments):
        input_data = resource.getAssetIDData()        
        for k, v in input_data.items():            
            if k not in arguments:
                continue            
            if k == 'smodified':
                continue
            input_data[k]['value'] = arguments[k]         
        dt_object = datetime.fromtimestamp(arguments['smodified'])
        input_data['smodified']['value'] = dt_object.strftime('%Y:%d:%B-%I:%M:%S:%p')          
        return input_data
        
    def create_model(self, inputs):        
        '''
        :example
            import time
            from studio_usd_pipe.core import mayapack
            mpack = mayapack.Pack()        
            model_id_data = {
                'sentity': 'asset',
                'scaption': 'batman',
                'stype': 'intractive',
                'stag': 'character',
                'sversion': '0.0.0',
                'smodified': time.time(),
                'spath': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'sdescription': 'test publish'
                }                       
            mpack.create_model(model_id_data)      
        '''     
        # remove depend nodes
        depend_nodes = self.extract_depend_nodes(default=False)
        for x in range(depend_nodes.length()):
            self.remove_node(depend_nodes[x])  
                      
        # make model group             
        mesh_mobjects = self.extract_transform_primitive(OpenMaya.MFn.kMesh)
        model_dag_node = self.create_group('model')        
          
        # make geometry hierarchy  
        for x in range (mesh_mobjects.length()):
            self.set_locked(mesh_mobjects[x], attributes=None, locked=False)
            self.disconnect_chanelbox(mesh_mobjects[x])
            self.set_parent(mesh_mobjects[x], model_dag_node.object())
            # assigin default shader
            self.assign_shading_group(mesh_mobjects[x], shading_group=None)    
                    
        # remove unwanted dag nodes    
        transform_mobjects = self.extract_top_transforms(default=False)
        for x in range (transform_mobjects.length()):
            if transform_mobjects[x]==model_dag_node.object():
                continue                       
            self.remove_node(transform_mobjects[x])
            
        # reset transforms
        for x in range (mesh_mobjects.length()):
            self.delete_history(mesh_mobjects[x])
            self.freeze_transformations(mesh_mobjects[x])
            self.set_default_position(mesh_mobjects[x])        
        
        # create world control   
        world_dependency_node = self.create_world(model_dag_node, parent=True) 

        # set the name
        model_dag_node.setName('model')
        world_dependency_node.setName('world')
            
        # make asset id
        input_data = self.make_packing_arguments(inputs)
        self.create_maya_id(model_dag_node.object(), input_data)
        OpenMaya.MGlobal.clearSelectionList()
        
    def create_studio_model(self, output_path):
        mobject = self.get_mobject('world')
        hierarchy = self.extract_transform(mobject)
        
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, root_mobject=mobject)
        transform_curve = self.extract_transform_primitive(
            OpenMaya.MFn.kCurve, root_mobject=mobject)
        

        





















            
                          
            
    def get(self, entity, show=False):
        my_data = {}        
        if entity=='kmesh' or entity=='kuv':
            mobjects = self.get_top_dag_nodes()
            for x in range(mobjects.length()):
                self.nested_bundle = {}
                pynode = core.PyNode(mobjects[x])            
                self.nested_travel(pynode, entity)
                my_data.update(self.nested_bundle)            
        if entity=='kshader':
            mobjects = self.get_scene_dag_nodes()
            self.flatted_bundle = {}               
            self.flatted_travel(mobjects, entity)  
            my_data = self.flatted_bundle
        if show:
            print json.dumps(my_data, indent=4)        
        return my_data                 
    
    def flatted_travel(self, mobjects, entity):
        index = 0
        for x in range(mobjects.length()):
            if entity=='kshader':                
                if not mobjects[x].hasFn(OpenMaya.MFn.kMesh):
                    continue        
                data = self.get_kshader(mobjects[x])
                self.flatted_bundle.setdefault(index, data)
                index+=1                                
       


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
    
    def get_kmesh(self, mobject):
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
        data = {}
        data['vertices'] = vertice_list
        data['vertex_count'] = list(vertex_count)
        data['vertex_list'] = list(vertex_array)
        data['num_edges'] = mfn_mesh.numEdges()
        data['num_face_vertices'] = mfn_mesh.numFaceVertices()
        data['num_polygons'] = mfn_mesh.numPolygons()
        data['num_normals'] = mfn_mesh.numNormals()
        data['num_vertices'] = mfn_mesh.numVertices()
        return data
    
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
            current_set_data = {
                'set_name': set_name.encode(),
                'u_array': list(u_array),
                'v_array': list(v_array),
                'uv_counts': list(uv_counts),
                'uv_ids': list(uv_ids)
                }
            data.setdefault(index, current_set_data)
        return data
    
    def get_kshader(self, mobject):        
        shader_engines = self.get_shadingengine(mobject)        
        if not shader_engines.length():            
            return        
        node_data, attribute_data, connection_data = {}, {}, {}
        geometry_data = []      
        mshader_engine = shader_engines[0]        
        nodes, assign_objects = self.get_networks(mshader_engine)
        
        # get attribute values
        for each_node in nodes:
            py_node = core.PyNode(each_node)
            node_data.setdefault(py_node.name(), py_node.type())
            attributes = py_node.listAttr(r=True, w=True, u=True, m=True, hd=True)
            if not attributes:
                continue
                      
            # attribute data
            current_attribute_data = {}
            for attribute in attributes:
                if attribute.nodeName() in assign_objects:
                    continue
                if attribute.type() not in self.valid_attribute:
                    continue
                try:
                    current_value = attribute.get()
                except:
                    current_value = '___unknown___'              
                if each_node not in attribute_data:
                    attribute_data.setdefault(each_node, {})
                attribute_data[each_node].setdefault(attribute.longName(), current_value)                
            # get connections
            connections = py_node.listConnections(s=False, d=True, p=True)
            for connection in connections:
                if connection.nodeName() in assign_objects:
                    continue
                if connection.nodeName() in self.default_nodes:
                    continue
                if connection.nodeType() in self.default_node_types:
                    continue
                source_attribute = connection.listConnections(s=True, d=False, p=True)
                if not source_attribute:
                    continue
                if py_node.name() not in connection_data:                
                    connection_data.setdefault(py_node.name(), {})                
                connection_data[py_node.name()].setdefault(
                    source_attribute[0].longName(), []).append(connection.name())
        
        # get shader assign geometries
        set_name, component_data = self.get_assign_components(mshader_engine)
        shader_data = {}        
        shader_data['nodes'] = node_data
        shader_data['attributes'] = attribute_data
        shader_data['connections'] = connection_data
        shader_data['geometries'] = component_data
        shader_data['shading_engine'] = set_name
        return shader_data           
    

    
  

    def maya_model(self):       
        pass         
