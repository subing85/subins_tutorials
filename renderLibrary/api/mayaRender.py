import json

from maya import OpenMaya
from maya import OpenMayaRender

from renderLibrary import resources
from renderLibrary.api import mayaNode


class Connect(mayaNode.Connect):
    
    def __init__(self, engine=None):  
        self.engine = engine or self.currentRenderEngine
        self.render_layer = OpenMayaRender.MFnRenderLayer()

    @property
    def currentRenderEngine(self):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'getAttr \"defaultRenderGlobals.currentRenderer\"'
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        render_engine = mcommand_result.stringResult()
        OpenMaya.MGlobal.displayInfo('current render engine: %s' % render_engine)
        return render_engine
    
    @property    
    def inputData(self):
        data = resources.getEngineData(self.engine)
        return data
    
    @property
    def renderDefault(self):
        _default = self.inputData.get('defaultRenderOptions')
        return _default
    
    @property
    def renderGlobals(self):
        _globals = self.inputData.get('renderGlobals')
        return _globals 

    @property
    def aovDependencies(self):
        _aov_types = self.inputData.get('aovDependencies')
        return _aov_types             
        
    @property
    def aovTypes(self):
        _aov_types = self.inputData.get('aovTypes')
        return _aov_types
    
    @property
    def aovFiltersByName(self):
        _aov_filters = self.inputData.get('aovFiltersByName')
        return _aov_filters
   
    @property
    def currentLayer(self):       
        current_layer = self.render_Layer.currentLayer()        
        return current_layer  
      
    @property
    def allLayers(self):
        mobject_array = OpenMaya.MObjectArray()
        self.render_Layer.listAllRenderLayers(mobject_array)
        return mobject_array
    
    @property
    def defaultLayer(self):
        return self.render_Layer.defaultRenderLayer()
    
    @property  
    def renderEngine(self):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'getAttr \"defaultRenderGlobals.currentRenderer\";'
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        render_engine = mcommand_result.stringResult() 
        OpenMaya.MGlobal.displayInfo('current render engine: %s' % render_engine)
        return render_engine  
    
    def getMembers(self, layer):
        mobject = self.getMObject(layer)
        self.render_layer.setObject(mobject)
        mobject_array = OpenMaya.MObjectArray()        
        self.render_layer.listMembers(mobject_array)
        return mobject_array
    
    def getGeometryMembers(self, layer, hierarchy=None):
        nodes = []
        if hierarchy:
            rootnode = self.getRootNode(hierarchy)
            _nodes = self.getGeometryHierarchy(rootnode)
            nodes = [_nodes[x] for x in range(_nodes.length())]
        members = self.getMembers(layer)
        geometries = []
        for index in range(members.length()):    
            dagpath = OpenMaya.MDagPath()
            dagpath.getAPathTo(members[index], dagpath)    
            if not dagpath.hasFn(OpenMaya.MFn.kMesh):
                continue        
            if members[index].hasFn(OpenMaya.MFn.kShape):
                mfndag_node = OpenMaya.MFnDagNode(dagpath)
                parent = mfndag_node.parent(0)  
                dagpath.getAPathTo(parent, dagpath)
            if hierarchy and dagpath not in nodes:
                continue
            geometries.append(dagpath.fullPathName())
        return geometries
    
    def getRenderMembers(self, layer): # to remove
        mobject = self.getMObject(layer)
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
    
    def setRenderEngine(self, engine):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'setAttr -type "string" defaultRenderGlobals.currentRenderer "%s";updateRendererUI;' % engine
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        OpenMaya.MGlobal.displayInfo('current render engine change to: %s' % engine)
        return True
    

    def renderSteup(self):
        '''
        :description
            get the current render steup whether Legacy or New Render Setup
            1 =  (new) Render Setup is active
            0 = Legacy Render Layers is active  
        :example
        from renderLibrary.utils import studioMaya
        studioMaya.getRenderSteup()
                
        '''
        mcommand_result = OpenMaya.MCommandResult()
        command = 'optionVar -q \"renderSetupEnable\";'
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        mscript_util = OpenMaya.MScriptUtil()
        index_ptr = mscript_util.asIntPtr()
        mcommand_result.getResult(index_ptr)    
        _value = mscript_util.getInt(index_ptr)
        
        setups = {
            0: 'Legacy Render Layers',
            1: 'Render Setup'
            }
        OpenMaya.MGlobal.displayInfo('current render: %s' % setups.get(_value))
        return _value     

    def selectLayer(self, layer):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'editRenderLayerGlobals -currentRenderLayer %s;' % layer
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        
    def getLayerAttributes(self, layer):        
        mobject = self.getMObject(layer)        
        attributes = self.getAttributes(mobject)
        return attributes

    def findAovs(self):
        _node, _attribute = self.renderDefault['name'], self.renderDefault['key']
        mplug = self.getMPlug(_node, _attribute)
        mobjects = OpenMaya.MObjectArray()
        for index in range(mplug.numElements()):
            element = mplug.elementByPhysicalIndex(index)
            mplug_array = OpenMaya.MPlugArray()        
            element.connectedTo(mplug_array, True, False)
            if not mplug_array.length():
                continue
            mobjects.append(mplug_array[0].node())
        return mobjects
    
    def getAov(self, mobject):
        attributes = self.getAttributes(mobject)
        mfn_depnode = OpenMaya.MFnDependencyNode(mobject)
        return mfn_depnode.name(), attributes  
    
    def getAovs(self, mobjects=None, overrides=False, layer=None):
        mobjects = mobjects or self.findAovs()
        aovs = {}      
        for index in range (mobjects.length()):
            mfn_depnode = OpenMaya.MFnDependencyNode(mobjects[index])
            name = mfn_depnode.name()
            # attribute value
            attributes = self.getAttributes(mobjects[index])
            # output dependencies
            outputs = self.getDependencies(
                name, types=self.aovDependencies, output=True, input=False)     
            # input dependencies            
            inputs = self.getDependencies(
                name, types=self.aovDependencies, output=False, input=True)
            
            lable = self.getAttributeValue('%s.name' % name)
            typed = self.getAttributeValue('%s.type' % name)
            
            aovs[name] = {
                'attributes': attributes,
                'outputs': outputs,
                'inputs': inputs,
                'lable': {'value': lable[0], 'typed': lable[1]},
                'type':  {'value': typed[0], 'typed': typed[1]}
                } 
            if overrides and layer:
                overrides = self.getOverride(mobjects[index], layer)
                aovs[name]['overrides'] = overrides
        return aovs
    
    def getRenderGlobals(self):        
        render_globals = {}
        for each in self.renderGlobals:
            if not self.objectExists(each):
                continue            
            mobject = self.getMObject(each)            
            attributes = self.getAttributes(mobject)
            render_globals[each] = attributes
        return render_globals
    
    def createRenderLayer(self, name):        
        mcommand_result = OpenMaya.MCommandResult()
        command = 'createRenderLayer -nr -e -mc -n %s' % name
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)
        render_layer = mcommand_result.stringResult()
        return render_layer
        
    def setRenderLayer(self, name, attributes):
        pass
    
    def createAov(self, name, lable):
        aov_node = self.createNode('aiAOV', name)
        _filter = self.aovFiltersByName.get(lable)
        if _filter:
            filter_node = self.createNode('aiAOVFilter', 'aiAOVFilter')
            attributes = {
                'aiTranslator': {
                    "typed": "kString",
                    "value": _filter
                    }
                }
            self.setAttributes(filter_node, attributes)
        else:
            filter_node = 'defaultArnoldFilter'
            
        # input connections    
        self.connect('%s.message' % filter_node, '%s.outputs[0].filter' % aov_node)        
        self.connect('defaultArnoldDriver.message', '%s.outputs[0].driver' % aov_node)
        
        # output connections        
        aov_list = self.nextAvailableAttr('defaultArnoldRenderOptions.aovList')
        self.connect('%s.message' % aov_node, aov_list)
        
        adjustments = self.nextAvailableAttr('defaultRenderLayer.adjustments')
        self.connect('%s.enabled' % aov_node, '%s.plug' % adjustments)

        return aov_node
    

    def setMembers(self, layer, members=[]):
        mcommand_result = OpenMaya.MCommandResult()
        command = 'editRenderLayerMembers -nr \"%s\" \"%s\";' % (layer, ' '.join(members))
        OpenMaya.MGlobal.executeCommand(command, mcommand_result, False, False)        
                

