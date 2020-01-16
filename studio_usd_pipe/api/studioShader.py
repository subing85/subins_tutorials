from maya import OpenMaya

from studio_usd_pipe.api import studioMaya

reload(studioMaya)


class Shader(studioMaya.Maya):
    
    def __init__(self):
        # studioMaya.Maya.__init__(self) 
        super(Shader, self).__init__()
         

    def assign_shading_engine(self, mobject, shading_group=None):
        if not shading_group:            
            shading_group = 'initialShadingGroup'
        if isinstance(shading_group, str):
            shading_group = self.get_mobject(shading_group)
        mfn_set = OpenMaya.MFnSet(shading_group)
        mfn_set.addMember(mobject)
    
    def get_shading_engines(self, mobject):
        dependency_graph = OpenMaya.MItDependencyGraph(
            mobject,
            OpenMaya.MFn.kShadingEngine,
            OpenMaya.MItDependencyGraph.kDownstream,
            OpenMaya.MItDependencyGraph.kDepthFirst,
            OpenMaya.MItDependencyGraph.kNodeLevel
            )
        shading_engines = OpenMaya.MObjectArray()
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            shading_engines.append(current_item)
            dependency_graph.next()
        return shading_engines    
    
    def get_assigned_components(self, mobject):
        mfn_set = OpenMaya.MFnSet(mobject)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        components = []
        selection_list.getSelectionStrings(components)
        return components

    def get_assigned_objects(self, mobject):
        mfn_set = OpenMaya.MFnSet(mobject)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        components = []
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            selection_list.getDagPath(index, m_dag_path)
            node = m_dag_path.partialPathName()
            if node in components:
                continue
            components.append(node)
        return components    
    
    def get_kmaterial_nodes(self, mobject):        
        mit_dependency_graph = OpenMaya.MItDependencyGraph(
            mobject,
            OpenMaya.MItDependencyGraph.kUpstream,
            OpenMaya.MItDependencyGraph.kPlugLevel
            )
        default_nodes = self.get_default_nodes()
        unknown_types = self.get_unknown_types()
        components = self.get_assigned_objects(mobject)
        mobject_array = OpenMaya.MObjectArray()
        while not mit_dependency_graph.isDone():       
            current_item = mit_dependency_graph.currentItem()
            mfn_dependency_node = OpenMaya.MFnDependencyNode(current_item)
            if mfn_dependency_node.object() in default_nodes:
                mit_dependency_graph.next()
                continue                   
            if mfn_dependency_node.typeName() in unknown_types:
                mit_dependency_graph.next()
                continue 
            if mfn_dependency_node.name() in components:
                mit_dependency_graph.next()
                continue     
            mobject_array.append(current_item)
            mit_dependency_graph.next()
        return mobject_array
    
    def get_kpreviewmaterial(self, mobject):
        '''
            :param mobject <OpenMaya.MObject> shading engine
        '''
        shader, attribute = self.get_shader(mobject)
        mobject = self.get_mobject(shader)
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        attributes = {
            'color': 'fileTextureName'
            }        
        for k, v  in attributes.items():
            if not mfn_dependency_node.hasAttribute(k):
                continue        
            k_mplug = mfn_dependency_node.findPlug(k)    
            if k_mplug.isConnected():
                mplug_array = OpenMaya.MPlugArray()
                k_mplug.connectedTo(mplug_array, True, False)
                file_dependency_node = OpenMaya.MFnDependencyNode(mplug_array[0].node())
                if file_dependency_node.hasAttribute(v):
                    v_mplug = file_dependency_node.findPlug(v)
                    value = v_mplug.asString()
                    return 'image', value  
            else:
                value = []
                for x in range(k_mplug.numChildren()):
                    child = k_mplug.child(x)
                    value.append(child.asFloat())
                return 'rgb', value 
        return None, None 

    def get_kshader(self, mobject):
        '''
            :param mobject <OpenMaya.MObject> shading engine
        '''
        mobject_array = self.get_kmaterial_nodes(mobject)        
        node_data = {} 
        for x in range (mobject_array.length()):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject_array[x])
            attribute_data = self.get_attributes(mfn_dependency_node.name())
            connection_data = self.get_connections(mfn_dependency_node.name())
            contents = {}
            if attribute_data:
                contents['parameters'] = attribute_data
            if connection_data:
                contents['connections'] = connection_data
            contents['type'] = mfn_dependency_node.typeName()
            contents['name'] = mfn_dependency_node.name()
            node_data.setdefault(mfn_dependency_node.name(), contents)
        shader, attribute = self.get_shader(mobject)
        data = {
            'nodes': node_data,
            'surface': {
                'shader': shader,
                'attribute': attribute
                }            
            }
        return data
    
    def get_shader(self, mobject):
        '''
            :param mobject <OpenMaya.MObject> shading engine
        '''        
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        surface_mplug = mfn_dependency_node.findPlug('surfaceShader')        
        if not surface_mplug.isConnected():
            return None        
        mplug_array = OpenMaya.MPlugArray()        
        surface_mplug.connectedTo(mplug_array, True, False)
        if not mplug_array.length():
            return None        
        shader, attribute = mplug_array[0].name().split('.')
        return shader, attribute
    
    def get_surface_data(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, root_mobject=mobject)
        data = {}
        for x in range(transform_mesh.length()):
            child = self.get_shape_node(transform_mesh[x])
            shader_engines = self.get_shading_engines(child.node())            
            if not shader_engines.length():
                continue            
            mfn_dependency_node = OpenMaya.MFnDependencyNode(shader_engines[0])
            mfn_dependency_node.name()
            if mfn_dependency_node.name() in data:
                data[mfn_dependency_node.name()].setdefault(
                    'geometries', []).append(transform_mesh[x].fullPathName())
                continue
            model_data = self.get_kshader(shader_engines[0])
            model_data['order'] = x
            model_data['geometries'] = [transform_mesh[x].fullPathName()]
            data.setdefault(mfn_dependency_node.name(), model_data)
        return data          
