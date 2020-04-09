import os
import shutil

import warnings

from maya import OpenMaya

from studio_usd_pipe.core import image
from studio_usd_pipe.api import studioMaya


reload(image)
reload(studioMaya)


class Shader(studioMaya.Maya):
    
    def __init__(self):
        # studioMaya.Maya.__init__(self) 
        super(Shader, self).__init__()    
        
        self.shader_node_bundles = {
            'shader': 'asShader',
            'texture': 'asTexture',
            'texture/3D': 'asTexture',
            'texture/Environment': 'asTexture',          
            'utility': 'asUtility',
            'light': 'asLight',
            'rendering': 'asRendering',
            'postProcess': 'asPostProcess',
            'shadingEngine': 'shadingEngine'         
            }             

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
    
    def get_scene_shading_engines(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, shape=True, parent_mobject=mobject)
        data = []
        for x in range(transform_mesh.length()):
            shader_engines = self.get_shading_engines(transform_mesh[x].node())
            if not shader_engines.length():
                continue
            for x in range(shader_engines.length()):         
                mfn_dependency_node = OpenMaya.MFnDependencyNode(shader_engines[x])
                if mfn_dependency_node.name() in data:
                    continue
                data.append(mfn_dependency_node.name())
        return data                               
    
    def get_surface_data(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, shape=True, parent_mobject=mobject)
        data = {}
        for x in range(transform_mesh.length()):
            shader_engines = self.get_shading_engines(transform_mesh[x].node())            
            if not shader_engines.length():
                continue            
            mfn_dependency_node = OpenMaya.MFnDependencyNode(shader_engines[0])
            if mfn_dependency_node.name() in data:
                data[mfn_dependency_node.name()].setdefault(
                    'geometries', []).append(transform_mesh[x].fullPathName())
                continue
            shader_data = self.get_kshader(shader_engines[0])
            shader_data['order'] = x
            shader_data['geometries'] = [transform_mesh[x].fullPathName()]
            data.setdefault(mfn_dependency_node.name(), shader_data)
        return data
    
    def get_source_image_data(self, mobject):
        transform_mesh = self.extract_transform_primitive(
            OpenMaya.MFn.kMesh, shape=True, parent_mobject=mobject)
        data = {}
        for x in range(transform_mesh.length()):
            shader_engines = self.get_shading_engines(transform_mesh[x].node())
            if not shader_engines.length():
                continue            
            material_nodes = self.get_kmaterial_nodes(shader_engines[0])
            for x in range (material_nodes.length()): 
                mfn_dependency_node = OpenMaya.MFnDependencyNode(material_nodes[x])
                attribute_data = self.get_source_images(mfn_dependency_node.name())
                if not attribute_data:
                    continue
                data.setdefault(mfn_dependency_node.name(), attribute_data)
        return data

    def get_source_images(self, object):
        attribute_data = {}        
        mplug_array = self.get_mplug_attributes(object)  
        for x in range(mplug_array.length()):
            attribute = mplug_array[x].attribute()
            if attribute.apiType()!=OpenMaya.MFn.kTypedAttribute:
                continue
            value, type = self.get_attribute_type(mplug_array[x])
            if not os.path.isabs(value):
                continue
            attribute_name = '.'.join(mplug_array[x].name().split('.')[1:])
            attribute_data[attribute_name] = {
                'value': value,
                'type': type
                }                
        return attribute_data    
    
    def set_source_images(self, input_data, temp_output_path, output_path):
        data = {}
        for node, node_contents in input_data.items():
            for attribute, attribute_contents in node_contents.items():
                source_image = os.path.basename(attribute_contents['value'])
                target_path = os.path.join(output_path, source_image)
                temp_target_path = os.path.join(temp_output_path, source_image)
                if not os.path.isdir(os.path.dirname(temp_target_path)):
                    os.makedirs(os.path.dirname(temp_target_path))
                if os.path.isfile(attribute_contents['value']):
                    shutil.copy2(attribute_contents['value'], temp_target_path)
                mplug = self.get_mplug('{}.{}'.format(node, attribute))
                mplug.setString(target_path)
                if node not in data:
                    data.setdefault(node, {})
                data[node][attribute] = {
                    'value': target_path,
                    'temp_value': temp_target_path,                    
                    'type': attribute_contents['type']
                    }
        return data
    
    
    def create_lowres_source_images(self, input_data, output_path):
        data = {}        
        for node, node_contents in input_data.items():
            for attribute, attribute_contents in node_contents.items():                
                if not os.path.isfile(attribute_contents['value']):
                    raise IOError('Cannot found, <%s>'%attribute_contents['value'])
                source_image = '{}_lores.png'.format(
                    os.path.splitext(os.path.basename(attribute_contents['value']))[0])
                target_path = os.path.join(output_path, source_image)
                target_path = image.image_resize(
                    attribute_contents['value'],
                    target_path,
                    512,
                    512,
                    )          
                if node not in data:
                    data.setdefault(node, {})
                data[node][attribute] = {
                    'value': target_path,
                    'type': attribute_contents['type']
                    }
        return data
    
    
    
    
    def create_shadernet(self, name, data, replace=False):
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
            mfn_mesh = self.create_kshadernet(name, data)
        return mfn_mesh
    

    def create_kshadernet(self, name, data):        
        nodes = data['nodes']
        
        # create node        
        for node, contents in nodes.items():
            node_mobject = self.create_knode(contents['type'], node)
            
            print '\n', node
            # set parameters(attributes) values
            for parameter in contents['parameters']:
                
                
                print '\t', parameter
            
            # print node, contents['parameters']
            
            # place2dTexture1 {u'repeatUV': {u'type': u'2FloatAttr', u'value': [10.0, 10.0]}}

            
        # set node connections
        
        #===================================================================
        # [u'connections', u'type', u'name', u'parameters']
        # [u'connections', u'type', u'name', u'parameters']
        #===================================================================

        
        
        
        
        pass
    
    def create_knode(self, node_type, name):        
        node_types = self.get_shading_node_types()
        if node_type not in node_types:
            warnings.warn('node type <%s> not found in the hyper shade  library'%node_type)
            return
        current_dg_type = self.shader_node_bundles[node_types[node_type]]
        mcommand_result = OpenMaya.MCommandResult()        
        mel_command = 'shadingNode -%s \"%s\" -n \"%s\"' % (current_dg_type, node_type, name)
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
        mobject = self.get_mobject(results[0])
        return mobject
    

    def get_shading_node_types(self):
        data = {}
        for node_type in self.shader_node_bundles:
            nodes = self.list_knode_types(node_type)
            for node in nodes:
                data.setdefault(node, node_type)
        return data    
    
    
    
    
    
    
    
    
    
