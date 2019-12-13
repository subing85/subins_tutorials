import math
import json

from pymel import core
from maya import OpenMaya


class Maya(object):
    
    def __init__(self):        
        self.valid_objects = [OpenMaya.MFn.kTransform, OpenMaya.MFn.kMesh]        
        self.default_nodes = self.get_default_nodes()
        self.default_node_types = self.get_default_node_types()
        self.valid_attribute = self.get_valid_attribute()           
        self.nested_bundle = {}
        self.flatted_bundle = {}

    def get_dagpath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path
    
    def get_mobject(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject
  
    def get_name(self, maya_object):
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependency_node.name().encode()
            
    def get_scene_dag_nodes(self):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobject_array = OpenMaya.MObjectArray()
        assemblies = OpenMaya.MDagPathArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()
            if mobject.apiType() not in self.valid_objects:
                mit_dependency_nodes.next()    
                continue                    
            if mobject.hasFn(OpenMaya.MFn.kTransform):    
                mfn_dag_node = OpenMaya.MFnDagNode(mobject)
                valid = self.has_node(mfn_dag_node, OpenMaya.MFn.kCamera)
                if valid:
                    mit_dependency_nodes.next()    
                    continue                
            mobject_array.append(mobject)    
            mit_dependency_nodes.next()
        return mobject_array
    
    def get_top_dag_nodes(self):
        '''
        # List top level transform Dag objects
        from studio_usd_pipe.api import studioMaya
        reload(studioMaya)
        maya = studioMaya.Maya()
        nodes = maya.get_scene_dag_nodes()
        for x in range(nodes.length()):
            print maya.getName(nodes[x])        
        '''     
        mobjects = self.get_scene_dag_nodes()
        mobject_array = OpenMaya.MObjectArray()
        for x in range(mobjects.length()):
            if not mobjects[x].hasFn(OpenMaya.MFn.kTransform):
                continue
            mfn_dag_node = OpenMaya.MFnDagNode(mobjects[x])
            parent_mobject = mfn_dag_node.parent(0)
            if not parent_mobject.hasFn(OpenMaya.MFn.kWorld):
                continue
            mobject_array.append(mobjects[x])
        return mobject_array                    
            
    def get(self, entity):
        mobjects = self.get_top_dag_nodes()
        
        for x in range(mobjects.length()):
            pynode = core.PyNode(mobjects[x])
            
            if entity=='kshader':
                self.flatted_bundle = {}               
                self.flatted_travel(pynode)
            else:
                self.nested_bundle = {}
                self.nested_travel(pynode)
                
            print json.dumps(self.bundle, indent=4)
            
    
    def flatted_travel(self):
        pass

       
    def nested_travel(self, node, entity, locations=None):    
        if not locations:
            locations = []        
        chidren = node.getChildren()       
        if chidren:             
            # avoid the multiple shape in the transform node, take fist shape node
            chidren = self.get_shape_node(chidren)                       
            for child in chidren:
                temp_parent = locations + [child] 
                self.nested_travel(child, entity, locations=temp_parent) 
        else:
            bundle = self.nested_bundle 
            for location in locations: 
                mobject = self.get_mobject(location.name())
                entity_data = {}                        
                if location.type()=='transform':
                    entity_data = self.get_ktransform(mobject)                
                if location.type()=='mesh' and entity=='kmesh':
                    entity_data = self.get_kmesh(mobject)   
                if location.type()=='mesh' and entity=='kuv':
                    entity_data = self.get_kuv(mobject)
                data = {
                    'data': entity_data,
                    } 
                bundle = bundle.setdefault(location.name(), data)

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
    
    def get_dependences(self, mobject, node_type, upstream=False, downstream=False):
        if isinstance(mobject, str):
            mobject = self.getMObject(mobject)
        if isinstance(mobject, OpenMaya.MDagPath):
            mobject = mobject.node()
        if not upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type)
        if upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(
                mobject,
                node_type,
                OpenMaya.MItDependencyGraph.kUpstream,
                OpenMaya.MItDependencyGraph.kDepthFirst,
                OpenMaya.MItDependencyGraph.kNodeLevel)
        if not upstream and downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(
                mobject,
                node_type,
                OpenMaya.MItDependencyGraph.kDownstream,
                OpenMaya.MItDependencyGraph.kDepthFirst,
                OpenMaya.MItDependencyGraph.kNodeLevel)
        result = OpenMaya.MObjectArray()
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            result.append(current_item)
            dependency_graph.next()
        return result

    def get_shadingengine(self, mobject):
        shading_engine_array = self.get_dependences(
            mobject, OpenMaya.MFn.kShadingEngine)
        return shading_engine_array    
    
    def get_networks(self, mshader_engine):
        if not object:
            return
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mshader_engine)
        shader_engine = mfn_dependency_node.name().encode()
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'listHistory %s' % shader_engine, mcommand_result, True, True)
        nodes = []
        mcommand_result.getResult(nodes)
        
        assign_objects = self.get_assign_objects(mshader_engine)
        networks = []
        for node in nodes:
            py_node = core.PyNode(node)
            if py_node.type() in self.default_node_types:
                continue
            if node in self.default_nodes:
                continue                        
            if node in networks:
                continue
            if node in assign_objects:
                continue
            networks.append(node.encode())
        return networks, assign_objects   
    
    def get_assign_objects(self, mshading_engine):
        mfn_set = OpenMaya.MFnSet(mshading_engine)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        objects = []
        if not selection_list.length():
            return objects
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            selection_list.getDagPath(index, m_dag_path)
            objects.append(m_dag_path.partialPathName())
        return objects
    
    def get_assign_components(self, mshading_engine):
        mfn_set = OpenMaya.MFnSet(mshading_engine)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        component_data = {}
        if not selection_list.length():
            return mfn_set.name(), component_data
        for index in range(selection_list.length()):
            components = []
            selection_list.getSelectionStrings(components)
            if components in component_data.values():
                continue
            component_data.setdefault(index, components)
        return mfn_set.name(), component_data
        
    def get_default_nodes(self):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'ls -defaultNodes', mcommand_result, True, True)
        nodes = []
        mcommand_result.getResult(nodes)      
        return nodes
    
    def get_default_node_types(self):    
        node_types = [
            'lightLinker',
            'materialInfo',
            'nodeGraphEditorInfo',
            'partition',
            'groupId',
            'hyperShadePrimaryNodeEditorSavedTabsInfo',
            'renderPartition',
            'timeToUnitConversion'
            ]
        return node_types
    
    def get_valid_attribute(self):
        attr_types = [
            'bool',
            'byte',
            'enum',
            'string',
            'long',
            'short',
            'typed',
            'float3',
            'float',
            'TdataCompound',
            'time',
            'float2',
            'double',
            'doubleAngle',
            'char'
        ]
        return attr_types    
    
    def has_node(self, mfn_dag_node, node_type):        
        for x in range (mfn_dag_node.childCount()): 
            child_object = mfn_dag_node.child(x)
            if child_object.hasFn(node_type):          
                return True
        return False                
                
    def get_shape_node(self, chidren):
        for child in chidren:
            if child.type()!='mesh':
                continue
            return [child]
        return chidren           
