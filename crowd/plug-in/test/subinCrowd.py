import sys

from maya import OpenMaya
from maya import OpenMayaMPx
from crowd.api import crowdNode
from crowd.api import proxyNode
reload(crowdNode)
reload(proxyNode)

CROWD_NODE = crowdNode.Connect()

# PLUGIN_NAME = CROWD_NODE.plugin_name
# NODE_ID = CROWD_NODE.node_id

PROXY_NODE = proxyNode.Connect()

PLUGIN_NAME = proxyNode.node_name
NODE_ID = proxyNode.node_Id



def initializePlugin(mobject): # initialize the script plug-in
    '''
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(
            PLUGIN_NAME, NODE_ID, crowdNode.nodeCreator, crowdNode.nodeInitializer)
    except:
        sys.stderr.write("Failed to register node: %s" % PLUGIN_NAME)
        raise
    '''    
    plugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        plugin.registerNode(
            PLUGIN_NAME, NODE_ID,
            proxyNode.nodeCreator,
            proxyNode.nodeInitializer, 
            OpenMayaMPx.MPxNode.kLocatorNode)
    except:
        sys.stderr.write("Failed to register node: %s" % PLUGIN_NAME)
        raise    


def uninitializePlugin(mobject): # uninitialize the script plug-in
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(PLUGIN_NAME, NODE_ID)
    except:
        sys.stderr.write("Failed to deregister node: %s" % PLUGIN_NAME)
        raise




#===============================================================================
# class _CrowdNode(OpenMayaMPx.MPxNode):
#             
#     position = OpenMaya.MObject()
#     animation = OpenMaya.MObject()
#     shader = OpenMaya.MObject()
#      
#     type = OpenMaya.MObject()
#     count = OpenMaya.MObject()
#     row = OpenMaya.MObject()
#     column = OpenMaya.MObject()
#     offset = OpenMaya.MObject()
#     random = OpenMaya.MObject()
#    
#     output = OpenMaya.MObject()  
#     input = OpenMaya.MObject()  
#    
#            
# 
#     def __init__(self):
#         OpenMayaMPx.MPxNode.__init__(self)
#         
#     def compute(self, plug, dataBlock):
#         print 'plug\t', plug
#         print 'dataBlock\t', dataBlock
#         
# 
#     def compute(self, plug, data):
#         
#         print '\nyes workinggggggggggggggggggggggggg'
#         print plug
#         
#         print help(data.inputValue)
#         
#         # print '\n', data.inputValue(CrowdNode.type)
#         
# #===============================================================================
# #         # dataHandle = OpenMaya.MDataHandle(data.inputValue(CrowdNode.type))
# #         
# #         # print '\n', dataHandle
# # 
# #         if plug == CrowdNode.output:            
# #             print 'skeleton type'
# #             
# #         if plug == CrowdNode.count:
# #             print 'skeleton count'  
# #===============================================================================
#             
# #===============================================================================
# #             
# #             timeData = data.inputValue(animCube.time)
# #             tempTime = timeData.asTime()
# # 
# #             outputHandle = data.outputValue(animCube.outputMesh)
# # 
# #             dataCreator = OpenMaya.MFnMeshData()
# #             newOutputData = dataCreator.create()
# # 
# #             self.createMesh(tempTime, newOutputData)
# # 
# #             outputHandle.setMObject(newOutputData)
# #             data.setClean(plug)
# #         else:
# #             return OpenMaya.kUnknownParameter        
# #===============================================================================
# 
# 
# def nodeCreator():  # creator
#     return OpenMayaMPx.asMPxPtr(CrowdNode())
# 
# 
# def nodeInitializer():  # initializer
#     
#     crowd_attr = attributes.Connect(CrowdNode)
#     crowd_attr.createGeneric()
#     
#     
#     
#     
# #===============================================================================
# #     enum_attribute = OpenMaya.MFnEnumAttribute()
# #     
# #     CrowdNode.types = enum_attribute.create(kTypeAttrName, kTypesAttrShortName, 0)
# #     enum_attribute.addField('biped', 0)
# #     enum_attribute.addField('bug', 1)    
# #     
# #     numeric_attribute = OpenMaya.MFnNumericAttribute()
# #     CrowdNode.count = numeric_attribute.create(kCountAttrName, kCountAttrShortName, OpenMaya.MFnNumericData.kInt, 1)
# # 
# #     CrowdNode.output = numeric_attribute.create(kOutputAttrName, kOutputAttrShortName, OpenMaya.MFnNumericData.kInt, 1)
# # 
# #     CrowdNode.addAttribute(CrowdNode.types)
# #     CrowdNode.addAttribute(CrowdNode.count)
# #     CrowdNode.addAttribute(CrowdNode.output)
# #     
# #     CrowdNode.attributeAffects(CrowdNode.types, CrowdNode.output)
# #     CrowdNode.attributeAffects(CrowdNode.count, CrowdNode.output)
# #===============================================================================
#     
#     
#     #===========================================================================
#     # nAttr = OpenMaya.MFnNumericAttribute()
#     # CrowdNode.input = nAttr.create(
#     #     "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0)
#     # nAttr.setStorable(1)       
#     # CrowdNode.position = nAttr.create("position", "pos", OpenMaya.MFnNumericData.kFloat, 10.0)
#     # nAttr.setStorable(True)
#     # CrowdNode.addAttribute(CrowdNode.input)
#     # CrowdNode.addAttribute(CrowdNode.position)      
#     # CrowdNode.attributeAffects(CrowdNode.input, CrowdNode.position)
#     #===========================================================================
# 
# 
#===============================================================================
