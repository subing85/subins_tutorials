

from maya import OpenMaya

# from renderLibrary import resources


class Connect(object):

    def __init__(self, **kwargs):        
        pass
            
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
    
    def getMeshHierarchy(self, dagpath): 
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

    def getSelectionStrings(self):
        selected = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selected)
        list = []
        selected.getSelectionStrings(list)
        return list
    
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
            name = mplug.name().split('.')[1]
            attributes[name] = {
                'value': value,
                'typed': typed,
                'short': mplug.partialName()
                }             
        return attributes
    
    def getAttributeValue(self, attribue):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'getAttr \"%s\";' % attribue 
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        result_type = mcommand_result.resultType()
       
        if result_type == OpenMaya.MCommandResult.kInvalid:
            return None, result_type
   
        if result_type == OpenMaya.MCommandResult.kInt:
            util = OpenMaya.MScriptUtil()
            util.createFromInt(0)
            kint = util.asIntPtr()
            mcommand_result.getResult(kint)
            return OpenMaya.MScriptUtil(kint).asInt(), result_type
            
        if result_type == OpenMaya.MCommandResult.kIntArray:
            mint_Array = OpenMaya.MIntArray()
            mcommand_result.getResult(mint_Array)
            return list(mint_Array), result_type
            
        if result_type == OpenMaya.MCommandResult.kDouble:
            util = OpenMaya.MScriptUtil()
            util.createFromDouble(0.0)
            kdouble = util.asDoublePtr()               
            mcommand_result.getResult(kdouble)
            return OpenMaya.MScriptUtil(kdouble).asDouble(), result_type
        
        if result_type == OpenMaya.MCommandResult.kDoubleArray:
            mdouble_array = OpenMaya.MDoubleArray()
            mcommand_result.getResult(mdouble_array)
            return list(mdouble_array), result_type
            
        if result_type == OpenMaya.MCommandResult.kString:
            kstring = mcommand_result.stringResult()
            return kstring, result_type
        
        if result_type == OpenMaya.MCommandResult.kStringArray:
            kstring_array = []
            mcommand_result.getResult(kstring_array)
            return kstring_array, result_type
            
        if result_type == OpenMaya.MCommandResult.kVector:
            mvector = OpenMaya.MVector()
            mcommand_result.getResult(mvector)
            return mvector, result_type
            
        if result_type == OpenMaya.MCommandResult.kVectorArray:
            mvector_array = OpenMaya.MVectorArray()
            mcommand_result.getResult(mvector_array)
            return list(mvector_array), result_type
            
        if result_type == OpenMaya.MCommandResult.kMatrix:
            mmatrix = OpenMaya.MMatrix()
            mcommand_result.getResult(mmatrix)
            return mmatrix, result_type  
        
    def findCommandResult(self):
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
            
    def getOverrides(self, node, layer):
        mobject = self.getMObject(node)
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
    
    def getRenderMembers(self, node):
        mobject = self.getMObject(node)
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        members = []
        for x in range(mfn_dependency_node.attributeCount()):
            attribute = mfn_dependency_node.attribute(x)
            mplug = mfn_dependency_node.findPlug(attribute)
            connections = OpenMaya.MPlugArray()
            mplug.connectedTo (connections, False, True)   
            for index in range (connections.length()) :      
                if '.renderLayerInfo' not in connections[index].name():
                    continue
                dagpath = OpenMaya.MDagPath()
                try:
                    dagpath.getAPathTo(connections[index].node(), dagpath)
                except Exception:
                    pass
                if not dagpath.isValid():
                    continue
                if dagpath.fullPathName() in members:
                    continue
                members.append(dagpath.fullPathName())
        return members
            
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
                      
