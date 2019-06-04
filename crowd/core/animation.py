
from pymel import core

from crowd.core import generic
from maya import OpenMaya

def create_animation(inputs):
    skeleton_data = generic.get_root_children()
    skeletons = skeleton_data.keys() + skeleton_data.values()
    bake = core.bakeResults(skeletons, sm=True, t=(1,16), sb=True,
         osr=True)
    
    if not bake:
        return
    
      
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds
import json

# Read Animation Curve Informations
selectList = cmds.ls(sl=1)
animDataList = {}

for currentObject in selectList :
    # 1. Current input convert to MObject
    # currentObject = 'pSphere1'
    objSelection = om.MSelectionList() 
    objSelection.add(currentObject)
    objMObject = objSelection.getDependNode(0)
    
    # 2.Find the attributes of current object
    mfnDependencyNode = om.MFnDependencyNode(objMObject)
    attributeCount = mfnDependencyNode.attributeCount()
    
    nodeAnimInfomationList = {}
    
    for attriIndex in range(attributeCount) :    
        attriMObject = mfnDependencyNode.attribute(attriIndex)
        
        mfnAttribute = om.MFnAttribute(attriMObject)    
        attriName = mfnAttribute.name.encode()
        
        # 3. Find the Attribute - Animation curve is connected
        currentPlug = mfnDependencyNode.findPlug(attriName, 1)
        if currentPlug.connectedTo(1, 0) :        
            connectedList = currentPlug.connectedTo(1, 0)
            
            # Find the connected node type
            conNodeMObject = connectedList[0].node()
            
            # Check its is a Animation curve        
            if conNodeMObject.hasFn(om.MFn.kAnimCurve) :
                            
                # Read Anim Curve Attribute valus
                mfnAnimCurve = oma.MFnAnimCurve(conNodeMObject)  
    
                attributeDataList = {'animCurveType':0, 'preInfinity':0, 'postInfinity':0,
                                      'weightedTangents':0, 'time':[], 'value':[],
                                      'inTangentType':[], 'inTangentAngle':[], 'inTangentWeight':[],
                                      'outTangentType':[], 'outTangentAngle':[], 'outTangentWeight':[]}
                
                animCurveType = mfnAnimCurve.animCurveType 
                preInfinity = mfnAnimCurve.preInfinityType
                postInfinity = mfnAnimCurve.postInfinityType
                weightedTangents = int(mfnAnimCurve.isWeighted)               
               
                # Find the number of keys in Anim Curve
                numKyes = mfnAnimCurve.numKeys
                timeList = []
                valueList = []
                inTangentTypeList = []
                inTangentAngleList = []
                inTangentWeightList = []            
                outTangentTypeList = []
                outTangentAngleList = []
                outTangentWeightList = []            
                
                # Find the values of each key
                for keyIndex in range(numKyes) :
                    # Time
                    input = mfnAnimCurve.input(keyIndex)
                    mTime = om.MTime(input)
                    currenttime = mTime.value
                    timeList.append(currenttime)
                    
                    # Value
                    value = mfnAnimCurve.value(keyIndex)
                    valueList.append(value) 
                    
                    # InTangent 
                    inTangentType = mfnAnimCurve.inTangentType(keyIndex)
                    inTangentTypeList.append(inTangentType)
                    inTangentAngleWeight = mfnAnimCurve.getTangentAngleWeight(keyIndex, 1)                 
                    inTangetMAngle = om.MAngle(inTangentAngleWeight[0])
                    inTangentAngleValue = inTangetMAngle.value                
                    inTangentAngleList.append(inTangentAngleValue)
                    inTangentWeightList.append(inTangentAngleWeight[1])                    
                   
                    # OutTangent 
                    outTangentType = mfnAnimCurve.outTangentType(keyIndex)
                    outTangentTypeList.append(outTangentType)
                    outTangentAngleWeight = mfnAnimCurve.getTangentAngleWeight(keyIndex, 0)                 
                    outTangetMAngle = om.MAngle(outTangentAngleWeight[0])
                    outTangentAngleValue = outTangetMAngle.value                
                    outTangentAngleList.append(outTangentAngleValue)
                    outTangentWeightList.append(outTangentAngleWeight[1])
                    
                # Store the attribute vales to dictionary variable
                attributeDataList = {'animCurveType':animCurveType,
                                                 'preInfinity':preInfinity,
                                                 'postInfinity':postInfinity,
                                                 'weightedTangents':weightedTangents,
                                                 'timeList':timeList,
                                                 'valueList':valueList,
                                                 'inTangentTypeList':inTangentTypeList,
                                                 'inTangentAngleList':inTangentAngleList,
                                                 'inTangentWeightList':inTangentWeightList,
                                                 'outTangentTypeList': outTangentTypeList,
                                                 'outTangentAngleList': outTangentAngleList,
                                                 'outTangentWeightList': outTangentWeightList}
                                                                 
                nodeAnimInfomationList.setdefault(attriName, attributeDataList)                
    animDataList.setdefault(currentObject.encode(), nodeAnimInfomationList)
    
# Wrtie dictionary variable data to custom file
filePath = 'C:/Users/Subin/Documents/Animation/My_TestAnimation.animD'
animData = open(filePath, 'w')
data = json.dumps(animDataList, indent=4)
animData.write(data)
animData.close()
print '#Successfully stored My Animation Data.'    
