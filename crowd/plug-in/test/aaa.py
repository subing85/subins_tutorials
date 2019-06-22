import sys

from maya import OpenMaya
from maya import OpenMayaMPx
from crowd.api import attributes
reload(attributes)

PLUGIN_NAME = 'subinsCrowd'
NODE_ID = OpenMaya.MTypeId(0x87000)

kTypeAttrName = 'type'
kTypesAttrShortName = 'typ'
kCountAttrName = 'count'
kCountAttrShortName = 'cnt'
kRowAttrName = 'row'
kRowAttrShortName = 'r'
kColumnAttrName = 'column'
kColumnAttrShortName = 'c'
kOffsetAttrName = 'offset'
kOffsetAttrShortName = 'of'
kRandomAttrName = 'random'
kRandomAttrShortName = 'rm'
kOutputAttrName = 'output'
kOutputAttrShortName = 'out'    

class CrowdNode(OpenMayaMPx.MPxNode):
        
    position = OpenMaya.MObject()
    animation = OpenMaya.MObject()
    shader = OpenMaya.MObject()
     
    type = OpenMaya.MObject()
    count = OpenMaya.MObject()
    row = OpenMaya.MObject()
    column = OpenMaya.MObject()
    offset = OpenMaya.MObject()
    random = OpenMaya.MObject()
   
    output = OpenMaya.MObject()  
    input = OpenMaya.MObject()  
   
           

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self, plug, dataBlock):
        print 'plug\t', plug
        print 'dataBlock\t', dataBlock
        

    def compute(self, plug, data):
        print plug
        if plug == CrowdNode.position:            
            print 'yessssssssssssssss'
            
#===============================================================================
#             
#             timeData = data.inputValue(animCube.time)
#             tempTime = timeData.asTime()
# 
#             outputHandle = data.outputValue(animCube.outputMesh)
# 
#             dataCreator = OpenMaya.MFnMeshData()
#             newOutputData = dataCreator.create()
# 
#             self.createMesh(tempTime, newOutputData)
# 
#             outputHandle.setMObject(newOutputData)
#             data.setClean(plug)
#         else:
#             return OpenMaya.kUnknownParameter        
#===============================================================================


def nodeCreator():  # creator
    return OpenMayaMPx.asMPxPtr(CrowdNode())


def nodeInitializer():  # initializer
    
    enum_attribute = OpenMaya.MFnEnumAttribute()
    CrowdNode.type = enum_attribute.create(kTypeAttrName, kTypesAttrShortName, 0)
    enum_attribute.addField('biped', 0)
    enum_attribute.addField('bug', 1)
    
    enum_attribute.setHidden(False)
    enum_attribute.setKeyable(True)
    enum_attribute.setWritable(True)
    enum_attribute.setReadable(True)
    enum_attribute.setStorable(True)
    
    numeric_attribute = OpenMaya.MFnNumericAttribute()
    CrowdNode.input = numeric_attribute.create(
         "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0)
    numeric_attribute.setStorable(1) 

    
    CrowdNode.addAttribute(CrowdNode.input)         
    CrowdNode.addAttribute(CrowdNode.type)
    
    CrowdNode.attributeAffects(CrowdNode.input, CrowdNode.type)

    #===========================================================================
    # nAttr = OpenMaya.MFnNumericAttribute()
    # CrowdNode.input = nAttr.create(
    #     "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0)
    # nAttr.setStorable(1) 
    #  
    # CrowdNode.position = nAttr.create("position", "pos", OpenMaya.MFnNumericData.kFloat, 10.0)
    # nAttr.setStorable(True)    
    #  
    # CrowdNode.addAttribute(CrowdNode.input)
    # CrowdNode.addAttribute(CrowdNode.position)
    #  
    # CrowdNode.attributeAffects(CrowdNode.input, CrowdNode.position)
    #===========================================================================


def initializePlugin(mobject): # initialize the script plug-in
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(
            PLUGIN_NAME, NODE_ID, nodeCreator, nodeInitializer)
    except:
        sys.stderr.write("Failed to register node: %s" % PLUGIN_NAME)
        raise



def uninitializePlugin(mobject): # uninitialize the script plug-in
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(NODE_ID)
    except:
        sys.stderr.write("Failed to deregister node: %s" % PLUGIN_NAME)
        raise
 
