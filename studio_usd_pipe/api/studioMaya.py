from pymel import core
from maya import OpenMaya


from studio_usd_pipe import resource
from studio_usd_pipe.core import common


class Maya(object):

    def __init__(self):
        self.valid_shapes = [
            OpenMaya.MFn.kMesh
            ]
        
    def is_dagpath(self, mobject):           
        mobject = self.get_mobject(mobject)
        result = None
        try:
            OpenMaya.MFnDagNode(mobject)
            result = True        
        except:
            result = False        
        return result 
    
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
        
    def create_mpoint_array(self, array):
        m_point_array = OpenMaya.MPointArray()
        for x, y, z, w in array:
            m_point_array.append(x, y, z, w)
        return m_point_array
    
    def create_mdouble_array(self, array):
        mdouble_array = OpenMaya.MDoubleArray()
        for x in array:
            mdouble_array.append(x)
        return mdouble_array
        
    def get_default_nodes(self, type=True):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'ls -defaultNodes', mcommand_result, True, True)
        nodes = []
        mcommand_result.getResult(nodes)
        cameras = [
            'persp',
            'top',
            'front',
            'side',
            'perspShape',
            'topShape',
            'frontShape',
            'sideShape',
            'lightLinker1',
            'shapeEditorManager',
            'poseInterpolatorManager',
            'layerManager',
            'defaultLayer',
            'renderLayerManager',
            'defaultRenderLayer',
            'ikSCsolver',
            'ikRPsolver',
            'ikSplineSolver',
            'hikSolver'            
            ]          
        nodes.extend(cameras) 
        nodes = list(set(nodes))       
        mobjects = []
        if type:      
            mobjects = OpenMaya.MObjectArray()     
        for node in nodes:
            if not self.object_exists(node):
                continue
            mobject = self.get_mobject(node)
            mobjects.append(mobject)
        return mobjects        
        
    def object_exists(self, mobject):
        if isinstance(mobject, unicode) :
            mobject = mobject.encode()        
        if not isinstance(mobject, str) :
            mobject = self.get_name(mobject)
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'objExists \"%s\"' % mobject
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, True, True)
        script_util = OpenMaya.MScriptUtil()
        index_ptr = script_util.asIntPtr()        
        mcommand_result.getResult(index_ptr)
        value = script_util.getInt(index_ptr)
        data = {0: False, 1: True}
        return data[value]  
          
    def remove_node(self, mobject):
        #=======================================================================
        # if not self.object_exists(mobject):
        #     return
        # try:
        #     OpenMaya.MGlobal.deleteNode(mobject)            
        # except:
        #     pass
        #=======================================================================
        if isinstance(mobject, unicode) :
            mobject = mobject.encode()        
        if not isinstance(mobject, str):
            mobject = self.get_name(mobject)
        if not self.object_exists(mobject):
            return
        mcommand_result = OpenMaya.MCommandResult()       
        mel_command = 'delete \"%s\"' % mobject 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
          
    def extract_depend_nodes(self, default=False):        
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes(type=False)            
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():            
            mobject = mit_dependency_nodes.item()
            if mobject.hasFn(OpenMaya.MFn.kWorld):
                mit_dependency_nodes.next()
                continue       
            if mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()
                continue            
            if self.is_dagpath(mobject):                
                mit_dependency_nodes.next()                           
                continue                   
            if mobject in default_nodes:
                mit_dependency_nodes.next()                           
                continue                                                      
            mobjects.append(mobject)   
            mit_dependency_nodes.next()
        return mobjects           
        
    def extract_transform_geometries(self):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = []
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            if not mobject.hasFn(OpenMaya.MFn.kMesh):
                mit_dependency_nodes.next()    
                continue                                    
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            p_mobject = mfn_dag_node.parent(0)
            if p_mobject in mobjects:
                mit_dependency_nodes.next()    
                continue        
            mobjects.append(p_mobject)   
            mit_dependency_nodes.next()            
        mobject_array = OpenMaya.MObjectArray()    
        for mobject in mobjects:
            mobject_array.append(mobject)
        return mobject_array        
        
    def extract_top_transforms(self, default=False):
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes(type=False)    
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        transform_mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            if not mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()    
                continue             
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            p_mobject = mfn_dag_node.parent(0)
            if not p_mobject.hasFn(OpenMaya.MFn.kWorld):
                mit_dependency_nodes.next()    
                continue             
            if mobject in default_nodes:
                mit_dependency_nodes.next()                           
                continue                                             
            transform_mobjects.append(mobject)   
            mit_dependency_nodes.next()            
        return transform_mobjects        
        
    def assign_shading_group(self, mobject, shading_group=None):
        if not shading_group:
            shading_group = self.get_mobject('initialShadingGroup')
        mfn_set = OpenMaya.MFnSet(shading_group)
        mfn_set.addMember(mobject)
        
    def create_maya_id(self, mobject, inputs):
        attributes = common.sorted_order(inputs)
        self.remove_maya_id(mobject, inputs)
        hidden = {True: False, False: True} 
        for attribute in attributes:
            short = inputs[attribute]['short']
            type_attribute = OpenMaya.MFnTypedAttribute()
            sample_mobject = OpenMaya.MObject()
            sample_mobject = type_attribute.create(attribute, short, OpenMaya.MFnData.kString)
            type_attribute.setKeyable(False)
            type_attribute.setReadable(True)
            type_attribute.setChannelBox(False)
            type_attribute.setWritable(inputs[attribute]['locked'])
            type_attribute.setHidden(hidden[inputs[attribute]['show']])
            mfn_dependency_node = OpenMaya.MFnDependencyNode()  
            mfn_dependency_node.setObject(mobject)
            mfn_dependency_node.addAttribute(sample_mobject)
            mplug = mfn_dependency_node.findPlug(type_attribute.name())
            mplug.setString(inputs[attribute]['value'])     
                        
    def remove_maya_id(self, mobject, inputs):
        mfn_dependency = OpenMaya.MFnDependencyNode(mobject)
        for attribute in inputs:
            if not mfn_dependency.hasAttribute(attribute):
                continue
            attribute_mobject = mfn_dependency.attribute(attribute)
            mfn_dependency.removeAttribute(
                attribute_mobject,
                OpenMaya.MFnDependencyNode.kLocalDynamicAttr
                )        
         
    def create_group(self, name):        
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('transform')
        mfn_dag_node.setName(name)
        return mfn_dag_node
    
    def create_world(self, mfn_dag_node, parent=False):
        parent_node = OpenMaya.MFnDependencyNode(mfn_dag_node.object())
        mplug_x = parent_node.findPlug('boundingBoxMaxX')
        mplug_z = parent_node.findPlug('boundingBoxMaxZ')        
        radius = max([mplug_x.asFloat(), mplug_z.asFloat()])
        world_data = resource.getWroldData()
        world_node = self.set_curve(world_data, radius=radius+0.5, name='world') 
        if parent:
            children = OpenMaya.MObjectArray()
            for x in range (mfn_dag_node.childCount()): 
                children.append(mfn_dag_node.child(x))                
            for x in range(children.length()):                
                self.set_parent(children[x], world_node.object())   
            self.set_parent(world_node.object(), mfn_dag_node.object())
        return world_node
        
    def set_curve(self, data, radius=1, name=None):
        cv_array = self.create_mpoint_array(data['control_vertices'])
        knots_array = self.create_mdouble_array(data['knots'])
        mfn_curve = OpenMaya.MFnNurbsCurve()
        mfn_curve.create(
            cv_array,
            knots_array,
            data['degree'],
            data['form'],
            False,
            True,          
            )
        mfn_curve.updateCurve() 
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mfn_curve.parent(0))
        mfn_dependency_node.setName(name)        
        mplug_x = mfn_dependency_node.findPlug('scaleX')
        mplug_y = mfn_dependency_node.findPlug('scaleY')  
        mplug_z = mfn_dependency_node.findPlug('scaleZ')  
        mplug_x.setFloat(radius)
        mplug_y.setFloat(radius)
        mplug_z.setFloat(radius)
        self.freeze_transformations(mfn_dependency_node.object())
        return mfn_dependency_node
    
    
    


    
    def get_curve(self, mobject):        
        mfn_curve = OpenMaya.MFnNurbsCurve(mobject)                
        cvs_array = OpenMaya.MPointArray()        
        mfn_curve.getCVs(cvs_array, OpenMaya.MSpace.kObject)
        knots_array = OpenMaya.MDoubleArray()
        mfn_curve.getKnots(knots_array)
        vertices = []
        for x in range(cvs_array.length()):
            array = [
                cvs_array[x].x,
                cvs_array[x].y,
                cvs_array[x].z,
                cvs_array[x].w
            ]            
            vertices.append(array)
        data = {
            'control_vertices': vertices,
            'knots': list(knots_array),
            'degree': mfn_curve.degree(),
            'form': mfn_curve.form(),
            'name': mfn_curve.name()  
            }        
        return data

         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
            
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
        
    def get_dependences(self, mobject, node_type, upstream=False, downstream=False):
        if isinstance(mobject, str):
            mobject = self.getMObject(mobject)
        if isinstance(mobject, OpenMaya.MDagPath):
            mobject = mobject.node()
        if not upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(
                mobject, node_type)
        if upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(
                mobject,
                node_type,
                OpenMaya.MItDependencyGraph.kUpstream,
                OpenMaya.MItDependencyGraph.kDepthFirst,
                OpenMaya.MItDependencyGraph.kNodeLevel
                )
        if not upstream and downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(
                mobject,
                node_type,
                OpenMaya.MItDependencyGraph.kDownstream,
                OpenMaya.MItDependencyGraph.kDepthFirst,
                OpenMaya.MItDependencyGraph.kNodeLevel
                )
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
    

    
    def set_locked(self, mobject, attributes=None, locked=True):
        if not attributes:
            attributes = [
                'translateX', 'translateY', 'translateZ',
                'rotateX', 'rotateY', 'rotateZ',
                'scaleX', 'scaleY', 'scaleZ',
                'visibility',
                ]
        for attribute in attributes:    
            dependency_node = OpenMaya.MFnDependencyNode(mobject)
            attr_mobject = dependency_node.attribute(attribute)
            mplug = dependency_node.findPlug(attr_mobject)
            mplug.setLocked(locked)
            
    def disconnect_chanelbox(self, mobject):        
        dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        attributes = [
            'translateX', 'translateY', 'translateZ',
            'rotateX', 'rotateY', 'rotateZ',
            'scaleX', 'scaleY', 'scaleZ',
            'visibility',
            'translate', 'rotate', 'scale'     
            ]            
        for attribute in attributes:    
            attr_mobject = dependency_node.attribute(attribute)
            output_plug = dependency_node.findPlug(attr_mobject)
            if not output_plug.isConnected():
                continue
            input_plugs = OpenMaya.MPlugArray()
            output_plug.connectedTo(input_plugs, 1, 0)
            dg_modifier = OpenMaya.MDGModifier()
            dg_modifier.disconnect(input_plugs[0], output_plug)
            dg_modifier.doIt() 
            
    def set_parent(self, child, parent):    
        if not isinstance(child, str):
            mfn_dagpath = OpenMaya.MFnDagNode(child)
            child = mfn_dagpath.fullPathName()            
        if not isinstance(parent, str):
            mfn_dagpath = OpenMaya.MFnDagNode(parent)
            parent = mfn_dagpath.fullPathName()                             
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'parent \"%s\" \"%s\" ' % (child, parent)
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        mobject = self.get_mobject(results[0])   
        return mobject
    
    def assigin_lambert(self, mobjects):        
        for x in range(mobjects.length()):
            pass
            
    def delete_history(self, node): 
        if not isinstance(node, str):
            dep = OpenMaya.MFnDagNode(node)
            node = dep.fullPathName()            
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'bakePartialHistory -preCache \"%s\"' % node 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        return results
                
    def set_default_position(self, mobject):
        self.freeze_transformations(mobject)
        attributes = [       
            'scalePivotZ', 'rotatePivotX', 'rotatePivotY',
            'rotatePivotZ', 'scalePivotX', 'scalePivotY'
            ]
        for attribute in attributes:    
            dependency_node = OpenMaya.MFnDependencyNode(mobject)
            attr_mobject = dependency_node.attribute(attribute)
            mplug = dependency_node.findPlug(attr_mobject)
            mplug.setFloat(0.0)    
    
    def freeze_transformations(self, node): 
        if not isinstance(node, str):
            node = self.get_name(node)      
        mcommand_result = OpenMaya.MCommandResult()        
        mel_command = 'makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 \"%s\"' % node
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        return results
    
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
            if child.type() != 'mesh':
                continue
            return [child]
        return chidren
    
    def _extract_mobjects(self):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = OpenMaya.MObjectArray()        
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            mobjects.append(mobject)   
            mit_dependency_nodes.next()
        return mobjects
    
    def _extract_transforms(self):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            if not mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()    
                continue                                   
            mobjects.append(mobject)   
            mit_dependency_nodes.next()            
        return mobjects
            
    def _extract_dependency_nodes(self):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item() 
            if mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()    
                continue
            if mobject.hasFn(OpenMaya.MFn.kMesh):
                mit_dependency_nodes.next()    
                continue 
            mobjects.append(mobject)   
            mit_dependency_nodes.next()            
        return mobjects

