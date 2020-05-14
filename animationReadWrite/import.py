'''
Import Animation Curves.
Data            : February 14, 2017
last modified   : February 27, 2017
Author          : Subin Gopi
subing85@gmail.com

Version         : Autodesk Maya 2016
Select the controls and run the below script.

More videos please visit my vimeo profile link mention below
    https://vimeo.com/user55256190

Subin's Tutorials - Read, Load the Animation Curves, and Write to custom data format using Maya Python API 2.0
This topic describes How to Read, Load the Animation and Write to animation data as a custom format in Maya 2016.

    https://vimeo.com/205665915
    https://vimeo.com/206069467
    https://vimeo.com/207417411
    https://vimeo.com/209857040
    https://vimeo.com/209860928
'''

# Load(Import) Module

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds
import json

# Read animation data
filePath = 'C:/Users/Subin/Documents/Animation/My_TestAnimation.animD'
animData = open(filePath, 'r')
data = json.load(animData)
animData.close()

for eachObject in data :
    for eachAttribute in data[eachObject] :    
        currentObject = eachObject
        currentAttribute = eachAttribute
        objectData = data[currentObject]
        objectAttriData = data[currentObject][currentAttribute]
        
        # Anim Curve data
        animCurveType = objectAttriData['animCurveType']
        preInfinity = objectAttriData['preInfinity']
        postInfinity = objectAttriData['postInfinity']
        weightedTangents = objectAttriData['weightedTangents']
        
        timeList = objectAttriData['timeList']
        valueList = objectAttriData['valueList']
        
        inTangentTypeList = objectAttriData['inTangentTypeList']
        inTangentAngleList = objectAttriData['inTangentAngleList']
        inTangentWeightList = objectAttriData['inTangentWeightList']
        outTangentTypeList = objectAttriData['outTangentTypeList']
        outTangentAngleList = objectAttriData['outTangentAngleList']
        outTangentWeightList = objectAttriData['outTangentWeightList']
        
        # Convert current object and attribute to a new MPlug object
        mSelectionList = om.MSelectionList()
        mSelectionList.add('%s.%s' % (currentObject, currentAttribute))
        currentMPlug = mSelectionList.getPlug(0)  
        
        connectedList = currentMPlug.connectedTo(1, 0)
        newAnimCurve = 1
        if connectedList :
            connectedNode = connectedList[0].node()
                
            if connectedNode.hasFn(om.MFn.kAnimCurve) :
                mfnAnimCurve = oma.MFnAnimCurve(connectedNode)
                newAnimCurve = 0
                
        if newAnimCurve == 1 :
            mfnAnimCurve = oma.MFnAnimCurve()
            mfnAnimCurve.create(currentMPlug, animCurveType)
        
        mfnAnimCurve.setPreInfinityType(preInfinity)
        mfnAnimCurve.setPostInfinityType(postInfinity)
        mfnAnimCurve.setIsWeighted(weightedTangents)
        
        mTimeList = om.MTimeArray()
        mDoubleValueList = om.MDoubleArray()
        
        for keyIndex in range(len(timeList)) :    
            mTimeList.append(om.MTime(timeList[keyIndex], om.MTime.uiUnit()))
            mDoubleValueList.append(valueList[keyIndex])   
        
        mfnAnimCurve.addKeys(mTimeList, mDoubleValueList, 0, 0, 1)
        
        for keyIndex in range(len(timeList)) :
            mfnAnimCurve.setInTangentType(keyIndex, inTangentTypeList[keyIndex])
            mfnAnimCurve.setOutTangentType(keyIndex, outTangentTypeList[keyIndex])
            
            inTangentAngle = om.MAngle(inTangentAngleList[keyIndex])
            outTangentAngle = om.MAngle(outTangentAngleList[keyIndex])
            
            mfnAnimCurve.setAngle(keyIndex, inTangentAngle, 1)
            mfnAnimCurve.setAngle(keyIndex, outTangentAngle, 0)
            
            mfnAnimCurve.setWeight(keyIndex, inTangentWeightList[keyIndex], 1)
            mfnAnimCurve.setWeight(keyIndex, outTangentWeightList[keyIndex], 0)    

print '#Successfully loaded My Animation Data'
