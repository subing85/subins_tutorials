

from maya import OpenMaya
from maya import OpenMayaRender

# from renderLibrary import resources


class Connect(object):

    def __init__(self, **kwargs):        
        pass
    
    def objectExists(self, name):
        mit_dependency = OpenMaya.MItDependencyNodes()
        while not mit_dependency.isDone():
            _object = mit_dependency.item()
            mfn_dependency = OpenMaya.MFnDependencyNode(_object)
            if mfn_dependency.name() == name:
                return True
            mit_dependency.next()
        return False
    
    @property
    def selectedNodes(self):
        selected = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selected)
        nodes = []
        selected.getSelectionStrings(nodes)
        return nodes
            
    def getDagPath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getMObject(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject
    
    def getRootNode(self, node):
        dagpath = self.getDagPath(node)        
        root = dagpath.fullPathName().split('|')[1]
        mdag_path = self.getDagPath(root)
        return mdag_path
    
    def getMPlug(self, node, attribute):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add('%s.%s' % (node, attribute))
        mselection.getPlug(0, mplug)    
        return mplug
    
    def _getMPlug(self, attribute):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add(attribute)
        mselection.getPlug(0, mplug)    
        return mplug       
    
    def findDagPaths(self, dagpath, typed):
        '''
        :dagpath <MDagPath>
        :typed <MFn object type> OpenMaya.MFn.kMesh
        '''
        dag_array = OpenMaya.MDagPathArray()
        stack = [dagpath]
        while stack:
            current = stack.pop()    
            mobject = current.node()
            if mobject.hasFn(typed):
                dag_array.append(current)      
            for x in range (current.childCount()):
                child_dagpath = OpenMaya.MDagPath()
                child_dagpath.getAPathTo(current.child(x), child_dagpath)
                stack.append(child_dagpath)
        return dag_array
    
    def getGeometryHierarchy(self, dagpath): 
        dag_array = OpenMaya.MDagPathArray()
        dagpaths = self.findDagPaths(dagpath, OpenMaya.MFn.kMesh)
        for x in range(dagpaths.length()):
            mfndag_node = OpenMaya.MFnDagNode(dagpaths[x])
            _parent = mfndag_node.parent(0)
            child_dagpath = OpenMaya.MDagPath()
            child_dagpath.getAPathTo(_parent, child_dagpath)
            dag_array.append(child_dagpath)
        return dag_array
    
    def getSelectedDagPaths(self):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        dagpaths = OpenMaya.MDagPathArray()
        for x in range(mselection.length()):
            dag_path = OpenMaya.MDagPath()
            mselection.getDagPath(x, dag_path)
            dagpaths.append(dag_path)
        return dagpaths
    
    def getShadingEngines(self, node):
        mobject = self.getMObject(node)
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
    
    def getShader(self, shading_engine_mobject):
        '''
            :param mobject <OpenMaya.MObject> shading engine
        '''        
        mfn_dependency_node = OpenMaya.MFnDependencyNode(shading_engine_mobject)
        surface_mplug = mfn_dependency_node.findPlug('surfaceShader')        
        if not surface_mplug.isConnected():
            return None        
        mplug_array = OpenMaya.MPlugArray()        
        surface_mplug.connectedTo(mplug_array, True, False)
        if not mplug_array.length():
            return None        
        return mplug_array[0].node()
    
    def getMaterialNodes(self, shader_mobject):
        mit_dependency_graph = OpenMaya.MItDependencyGraph(
            shader_mobject,
            OpenMaya.MItDependencyGraph.kUpstream,
            OpenMaya.MItDependencyGraph.kPlugLevel
            )
        mobject_array = OpenMaya.MObjectArray()
        while not mit_dependency_graph.isDone():       
            current_item = mit_dependency_graph.currentItem()
            mobject_array.append(current_item)
            mit_dependency_graph.next()
        return mobject_array
                
    def getAssignComponents(self, shading_group):
        mfn_set = OpenMaya.MFnSet(shading_group)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        component_data = {}
        if not selection_list.length():
            return component_data
        for index in range(selection_list.length()):
            components = []
            selection_list.getSelectionStrings(components)
            if components in component_data.values():
                continue
            component_data.setdefault(index, components)
        return component_data

    def getAssignObjects(self, shading_group):
        mfn_set = OpenMaya.MFnSet(shading_group)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        objects = []
        if not selection_list.length():
            return objects
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            m_object = OpenMaya.MObject()
            selection_list.getDagPath(index, m_dag_path, m_object)
            objects.append(m_dag_path.partialPathName())
        return objects
    
    def addStringATtributes(self, node, attribute, shortname, value=None):
        mobject = self.getMObject(node)
        mfndependency_node = OpenMaya.MFnDependencyNode(mobject)  
        if not mfndependency_node.hasAttribute(shortname):
            mfn_attribute = OpenMaya.MFnTypedAttribute()
            
            _attribute = mfn_attribute.create(
                attribute, shortname, OpenMaya.MFnData.kString)
            mfn_attribute.setKeyable(True)
            mfn_attribute.setWritable(True)
            mfn_attribute.setReadable(True)
            mfn_attribute.setStorable(True)
            mfndependency_node.addAttribute(_attribute)
            
        mpulg = mfndependency_node.findPlug(shortname)
        if value:
            mpulg.setLocked(False)    
            mpulg.setString(value)
        mpulg.setLocked(True)
        
    def getAttributes(self, node):
        mobject = self.getMObject(node)
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        attributes = {}
        for x in range(mfn_dependency_node.attributeCount()):
            attribute = mfn_dependency_node.attribute(x)
            mplug = mfn_dependency_node.findPlug(attribute)
            
            if not mfn_dependency_node.hasAttribute(mplug.partialName()):
                continue   
            if attribute.hasFn(OpenMaya.MFn.kCompoundAttribute):
                continue
            if attribute.hasFn(OpenMaya.MFn.kMessageAttribute):
                continue           
            if mplug.isDefaultValue():
                continue

            value, typed = self.getAttributeValue(mplug.name())
            
            if not value and not typed:
                continue
            
            name = mplug.name().split('.')[1]
            attributes[name] = {
                'value': value,
                'typed': typed,
                'short': mplug.partialName()
                }             
        return attributes
    
    def connect(self, source, target):
        s_mplug = self._getMPlug(source)
        t_mplug = self._getMPlug(target)
        dgMod = OpenMaya.MDGModifier()
        dgMod.connect(s_mplug, t_mplug)
        dgMod.doIt()           
    
    def setConnections(self, node, contents, typed='input'):   
        for attribute, output in contents.items():
            if typed == 'input':
                self.connect(output, '%s.%s' % (node, attribute))
            if typed == 'output':
                self.connect('%s.%s' % (node, attribute), output)
    
    def setAttributes(self, node, attributes):
        for attribute, contents in attributes.items():
            self.setAttributeValue(
                node,
                attribute,
                contents['typed'],
                contents['value']
            )
    
    def setAttributeValue(self, node, attribute, typed, value):        
        mobject = self.getMObject(node)        
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        
        if not mfn_dependency_node.hasAttribute(attribute):
            return
    
        mplug = mfn_dependency_node.findPlug(attribute)

        if typed == 'kInt':
            try:
                mplug.setInt(value)
            except Exception as error:
                print 'error', error, mplug.name()
                         
        if typed == 'kDouble':
            try:
                mplug.setFloat(value)
            except Exception as error:
                print 'error', error, mplug.name()
                
        if typed == 'kString':
            try:
                mplug.setString(value)
            except Exception as error:
                print 'error', error, mplug.name()
                        
        if typed in ['kIntArray', 'kDoubleArray', 'kVector', 'kVectorArray', 'kMatrix']:
            for x in range(mplug.numChildren()):
                child_mplug = mplug.child(x)
                # try:
                child_mplug.setFloat(value[x])
                # except Exception as error:
                #    print 'error', error, mplug.name()
        
        #=======================================================================
        # 7     kString
        # 1     kInt
        # 5     kDouble
        # 0     kInvalid
        # 6     kDoubleArray
        # 3     kIntArray
        # 10     kVectorArray
        # 8     kStringArray
        # 9     kVector
        # 11     kMatrix
        #=======================================================================
    
    def getAttributeValue(self, attribue):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'getAttr \"%s\";' % attribue 
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        result_type = mcommand_result.resultType()
       
        if result_type == OpenMaya.MCommandResult.kInvalid:
            return None, None
   
        if result_type == OpenMaya.MCommandResult.kInt:
            util = OpenMaya.MScriptUtil()
            util.createFromInt(0)
            kint = util.asIntPtr()
            mcommand_result.getResult(kint)
            return OpenMaya.MScriptUtil(kint).asInt(), 'kInt'
            
        if result_type == OpenMaya.MCommandResult.kIntArray:
            mint_Array = OpenMaya.MIntArray()
            mcommand_result.getResult(mint_Array)
            return list(mint_Array), 'kIntArray'
            
        if result_type == OpenMaya.MCommandResult.kDouble:
            util = OpenMaya.MScriptUtil()
            util.createFromDouble(0.0)
            kdouble = util.asDoublePtr()               
            mcommand_result.getResult(kdouble)
            return OpenMaya.MScriptUtil(kdouble).asDouble(), 'kDouble'
        
        if result_type == OpenMaya.MCommandResult.kDoubleArray:
            mdouble_array = OpenMaya.MDoubleArray()
            mcommand_result.getResult(mdouble_array)
            return list(mdouble_array), 'kDoubleArray'
            
        if result_type == OpenMaya.MCommandResult.kString:
            kstring = mcommand_result.stringResult()
            return kstring, 'kString'
        
        if result_type == OpenMaya.MCommandResult.kStringArray:
            kstring_array = []
            mcommand_result.getResult(kstring_array)
            return kstring_array, 'kStringArray'
            
        if result_type == OpenMaya.MCommandResult.kVector:
            mvector = OpenMaya.MVector()
            mcommand_result.getResult(mvector)
            return mvector, 'kVector'
            
        if result_type == OpenMaya.MCommandResult.kVectorArray:
            mvector_array = OpenMaya.MVectorArray()
            mcommand_result.getResult(mvector_array)
            return list(mvector_array), 'kVectorArray'
            
        if result_type == OpenMaya.MCommandResult.kMatrix:
            mmatrix = OpenMaya.MMatrix()
            mcommand_result.getResult(mmatrix)
            return mmatrix, 'kMatrix'  
        
    def findAttributeType(self):
        ktyped = {
        'kInvalid': OpenMaya.MCommandResult.kInvalid,
        'kInt':OpenMaya.MCommandResult.kInt,
        'kIntArray':OpenMaya.MCommandResult.kIntArray ,
        'kDouble':OpenMaya.MCommandResult.kDouble,
        'kDoubleArray':OpenMaya.MCommandResult.kDoubleArray,
        'kString':OpenMaya.MCommandResult.kString,
        'kStringArray':OpenMaya.MCommandResult.kStringArray,
        'kVector':OpenMaya.MCommandResult.kVector,
        'kVectorArray':OpenMaya.MCommandResult.kVectorArray,
        'kMatrix':OpenMaya.MCommandResult.kMatrix
        }
        for k, v in ktyped.items():
            print v, '\t', k
            
    def setOverrides(self, node, attributes):
        for attribute, contents in attributes.items():
            self.setOverride(
                node,
                attribute,
                contents['typed'],
                contents['value']
            )
           
    def setOverride(self, node, attribute, typed, value):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'editRenderLayerAdjustment \"%s.%s\";' % (node, attribute)
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)

        self.setAttributeValue(node, attribute, typed, value)
    
    def getOverrides(self, layer, nodes, shape=False):
        overrides = {}
        for node in nodes:
            attributes = self.getOverride(layer, node)
            if not attributes:
                continue 
            overrides[node] = attributes
        return overrides
                                
    def getOverride(self, layer, mobject):        
        if isinstance(mobject, str) or isinstance(mobject, unicode):
            mobject = self.getMObject(mobject)            
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        layer_mobject = self.getMObject(layer)                
        attributes = {}
        for x in range(mfn_dependency_node.attributeCount()):
            attribute = mfn_dependency_node.attribute(x)
            mplug = mfn_dependency_node.findPlug(attribute)            
            if not mplug.isConnected():
                continue            
            connected_mobject = self.getConnectedObject(
                mplug, OpenMaya.MFn.kRenderLayer)            
            if not connected_mobject:
                continue                         
            if connected_mobject != layer_mobject:
                continue                
            value, typed = self.getAttributeValue(mplug.name())
            name = mplug.name().split('.')[1]
            attributes[name] = {
                'value': value,
                'typed': typed,
                'short': mplug.partialName()
                }
        return attributes
            
    def getConnectedObject(self, mplug, typed):
        connections = OpenMaya.MPlugArray()
        mplug.connectedTo (connections, False, True)   
        if not connections.length():
            return None
        for index in range (connections.length()) :  
            connected_mobject = connections[index].node() 
            if not connected_mobject.hasFn(typed):
                continue
            return connected_mobject
        return None
                      
    def getDependencies(self, node, types=[], output=True, input=False):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'listConnections -c on -scn on -p on -d on -s on \"%s\";' % node
        if output and not input:
            command = 'listConnections -c on -scn on -p on -d on -s off \"%s\";' % node
        if not output and input:
            command = 'listConnections -c on -scn on -p on -d off -s on \"%s\";' % node
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        connections = []
        mcommand_result.getResult(connections)
        _dependencies = dict(zip(connections[::2], connections[1::2]))
        if not types:
            return _dependencies        
        dependencies = {}
        for each in _dependencies:
            node_type = self.nodeType(_dependencies[each])            
            if node_type not in types:
                continue
            # attribute = each.split('.')[-1]     
            attribute = each.rsplit('%s.' % node, 1)[-1]
            dependencies[attribute] = _dependencies[each]        
        return dependencies            

    def nodeTypes(self, typed):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'listNodeTypes \"%s\";' % typed
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        nodes = []
        mcommand_result.getResult(nodes)
        return nodes
    
    def nodeType(self, node):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'nodeType \"%s\"' % node
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, False)
        node_type = mcommand_result.stringResult()
        return node_type
    
    def createNode(self, typed, name):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'createNode \"%s\" -ss -n \"%s\";' % (typed, name)
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, False)
        node_type = mcommand_result.stringResult()
        return node_type
    
    def removeNode(self, node):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'delete \"%s\";' % node
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, False)
        return True
    
    def nextAvailableAttr(self, attribute):
        mplug = self._getMPlug('defaultArnoldRenderOptions.aovList')
        num_elements = mplug.evaluateNumElements()
        next_attr = '%s[%s]' % (attribute, num_elements)
        return next_attr
           
