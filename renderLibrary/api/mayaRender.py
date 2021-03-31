import json

from maya import OpenMaya

from renderLibrary import resources
from renderLibrary.api import mayaNode

print 'Helloooooooooooooooooooooooooooo'



class Connect(mayaNode.Connect):
    
    def __init__(self, engine):
        
        self.engine = engine
        self.data = self.getInputData()
                
        self._default = self.data['defaultRenderOptions']

        
    def getInputData(self):
        data = resources.getEngineData(self.engine)
        return data
    
    def getLayerAttributes(self, layer):        
        mobject = self.getMObject(layer)        
        attributes = self.getAttributes(mobject)
        return attributes

    def findAovs(self):
        _node, _attribute = self._default['name'], self._default['key']
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
    
    def getAovs(self):
        mobjects = self.findAovs()
        aovs = {}                
        for index in range (mobjects.length()):
            attributes = self.getAttributes(mobjects[index])
            mfn_depnode = OpenMaya.MFnDependencyNode(mobjects[index])
            aovs.setdefault(mfn_depnode.name(), attributes)
        return aovs

                
    def setLayerAttributes(self, layer):
        pass
    
    def setAovs(self, data):
        pass
    
