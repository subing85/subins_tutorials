import os

import warnings

from maya import OpenMaya
from maya import OpenMayaAnim

from studio_usd_pipe.core import swidgets
from studio_usd_pipe.api import studioMaya


class Animation(studioMaya.Maya):
    
    def __init__(self):
        super(Animation, self).__init__()  
        

    def get_kanimation(self, mobject) :    
        mfnDependencyNode = OpenMaya.MFnDependencyNode(mobject)        
        attributeCount = mfnDependencyNode.attributeCount()        
        anmationData = {}
        
        for attrIndex in range (attributeCount) :
            attribute = mfnDependencyNode.attribute(attrIndex)
            plug = mfnDependencyNode.findPlug (attribute)        
    
            connections = OpenMaya.MPlugArray()
            plug.connectedTo (connections, 1, 0)        
            
            for index in range (connections.length()) :  
                connectedMPlug = connections[index]      
                connectedmobject = connectedMPlug.node() 
                
                if not connectedmobject.hasFn(OpenMaya.MFn.kAnimCurve) :
                    continue
                
                animCurveData = self.get_kanimCurve(connectedmobject)    
                             
                attributemobject = plug.attribute()
                mfnAttribute = OpenMaya.MFnAttribute(attributemobject)            
                currentAttribute = mfnAttribute.name()  
                       
                anmationData.setdefault(currentAttribute.encode(), animCurveData)            
    
        return anmationData           
        
          
        
    def get_kanimCurve(self, mobject) :    
        
        animCurveData = {}   
        
        mfnAnimCurve = OpenMaya.MFnDependencyNode(mobject)
        currentAnimCurve = mfnAnimCurve.name()             
    
        mfnAnimCurve = OpenMayaAnim.MFnAnimCurve(mobject)
         
        # preInfinityType
        preInfinityType = mfnAnimCurve.preInfinityType()
         
        # postInfinityType
        postInfinityType = mfnAnimCurve.postInfinityType()
        numKeys = mfnAnimCurve.numKeys()
        weightedTangent = mfnAnimCurve.isWeighted()
        
        timeList = []
        valueList = []      
            
        inTangentXValueList = []
        inTangentYValueList = []
            
        outTangentXValueList = []
        outTangentYValueList = []
        
        inTangentAngleValueList = []
        inTangentWeightValueList = []
        
        outTangentAngleValueList = []
        outTangentWeightValueList = []    
        
        inTangentTypeList = []
        outTangentTypeList = []
        breakdownList = []
       
        keyData = {}   
         
        for index in range (numKeys) :
            time = mfnAnimCurve.time(index).value()
            value = mfnAnimCurve.value(index)
             
            # In Tangent
            inTangentX = OpenMaya.MScriptUtil().asFloatPtr()
            inTangentY = OpenMaya.MScriptUtil().asFloatPtr()   
            inTangent = mfnAnimCurve.getTangent(index, inTangentX, inTangentY, True)    
            inTangentXValue = OpenMaya.MScriptUtil.getFloat(inTangentX)
            inTangentYValue = OpenMaya.MScriptUtil.getFloat(inTangentY)  
             
            # Out Tangent
            outTangentX = OpenMaya.MScriptUtil().asFloatPtr()
            outTangentY = OpenMaya.MScriptUtil().asFloatPtr()   
            outTangent = mfnAnimCurve.getTangent(index, outTangentX, outTangentY, False)
            outTangentXValue = OpenMaya.MScriptUtil.getFloat(outTangentX)
            outTangentYValue = OpenMaya.MScriptUtil.getFloat(outTangentY)    
            
            # In Tangent angle and weight
            inTangentAngle = OpenMaya.MAngle()
            inTangentweight = OpenMaya.MScriptUtil().asDoublePtr()           
            inTangent = mfnAnimCurve.getTangent(index, inTangentAngle, inTangentweight, True)        
            inTangentAngleValue = inTangentAngle.value()
            inTangentWeightValue = OpenMaya.MScriptUtil.getDouble(inTangentweight) 
            
            # Out Tangent angle and weight
            outTangentAngle = OpenMaya.MAngle()
            outTangentweight = OpenMaya.MScriptUtil().asDoublePtr()         
            outTangent = mfnAnimCurve.getTangent(index, outTangentAngle, outTangentweight, False)
            outTangentAngleValue = outTangentAngle.value()
            outTangentWeightValue = OpenMaya.MScriptUtil.getDouble(outTangentweight)                              
             
            # In Tangent Type    
            inTangentType = mfnAnimCurve.inTangentType(index)
             
            # Out Tangent Type    
            outTangentType = mfnAnimCurve.outTangentType(index)
             
            # isBreakdown
            breakdown = mfnAnimCurve.isBreakdown(index)
            
            timeList.append (time)
            valueList.append (value)
            
            inTangentXValueList.append (inTangentXValue)
            inTangentYValueList.append (inTangentYValue)
            
            outTangentXValueList.append (outTangentXValue)
            outTangentYValueList.append (outTangentYValue)
            
            inTangentAngleValueList.append (inTangentAngleValue)
            inTangentWeightValueList.append (inTangentWeightValue)
            
            outTangentAngleValueList.append (outTangentAngleValue)
            outTangentWeightValueList.append (outTangentWeightValue)        
            
            inTangentTypeList.append (inTangentType)
            outTangentTypeList.append (outTangentType)
            
            breakdownList.append (breakdown) 
            
        print 'Animation curve\t', currentAnimCurve.encode()        
        
        animCurveData['animCurve'] = currentAnimCurve.encode() 
              
        animCurveData['time'] = timeList    
        animCurveData['value'] = valueList    
        
        animCurveData['numKeys'] = numKeys    
        animCurveData['preInfinityType'] = preInfinityType
        animCurveData['postInfinityType'] = postInfinityType
        animCurveData['weightedTangent'] = weightedTangent
        
        animCurveData['inTangentXValue'] = inTangentXValueList
        animCurveData['inTangentYValue'] = inTangentYValueList    
        
        animCurveData['outTangentXValue'] = outTangentXValueList    
        animCurveData['outTangentYValue'] = outTangentYValueList   
        
        animCurveData['inTangentAngleValue'] = inTangentAngleValueList    
        animCurveData['inTangentWeightValue'] = inTangentWeightValueList   
        
        animCurveData['outTangentAngleValue'] = outTangentAngleValueList    
        animCurveData['outTangentWeightValue'] = outTangentWeightValueList          
         
        animCurveData['inTangentType'] = inTangentTypeList    
        animCurveData['outTangentType'] = outTangentTypeList  
          
        animCurveData['breakdown'] = breakdownList      
            
        return animCurveData         
        
   


    def create_kanimation(self, name, data) :
        
        for eachAttribute, animCurveData in attributes.iteritems() :
            if not cmds.objExists ('%s.%s' % (node, eachAttribute)) :
                print '%s.%s' % (node, eachAttribute), ' no object found  '
                continue
            animCurve = animCurveData['animCurve']        
            mfnAnimCurve = createAnimationCurve (node, eachAttribute, animCurve)        
            setAnimattribute_values (mfnAnimCurve, animCurveData)        
            if not mfnAnimCurve :
                return False
            
        return animCurve


    def setAnimattribute_values(self, mfnAnimCurve, attribute_value) :
        
        time = attribute_value['time']
        value = attribute_value['value']
             
        numKeys = attribute_value['numKeys']
        preInfinityType = attribute_value['preInfinityType']
        postInfinityType = attribute_value['postInfinityType']
        weightedTangent = attribute_value['weightedTangent']
             
        inTangentXValue = attribute_value['inTangentXValue']
        inTangentYValue = attribute_value['inTangentYValue']
             
        outTangentXValue = attribute_value['outTangentXValue']
        outTangentYValue = attribute_value['outTangentYValue']
        
        inTangentXValue = attribute_value['inTangentXValue']
        inTangentYValue = attribute_value['inTangentYValue']  
        
        inTangentAngleValue = attribute_value['inTangentAngleValue']
        inTangentWeightValue = attribute_value['inTangentWeightValue']    
        outTangentAngleValue = attribute_value['outTangentAngleValue']
        outTangentWeightValue = attribute_value['outTangentWeightValue']
              
        inTangentType = attribute_value['inTangentType']
        outTangentType = attribute_value['outTangentType']
               
        breakdown = attribute_value['breakdown']        
        
        mfnAnimCurve.setPreInfinityType (preInfinityType)
        mfnAnimCurve.setPostInfinityType (postInfinityType)
        mfnAnimCurve.setIsWeighted (weightedTangent)   
        
        # for index in range (time`)
        
        mTimeArray = OpenMaya.MTimeArray ()
        mDoubleArray = OpenMaya.MDoubleArray ()
    
        for index in range (len(time)) :    
            mTimeArray.append (OpenMaya.MTime(time[index], OpenMaya.MTime.uiUnit()))
            mDoubleArray.append (value[index]) 
        
        mfnAnimCurve.addKeys (mTimeArray, mDoubleArray, 0, 0, 1)     
            
        for index in range (len(time)) :
            
            mfnAnimCurve.setTangent (index, inTangentXValue[index], inTangentYValue[index], True)
            mfnAnimCurve.setTangent (index, outTangentXValue[index], outTangentYValue[index], False)
            
            inTangentMAngle = OpenMaya.MAngle (inTangentAngleValue[index])        
            
            outTangentMAngle = OpenMaya.MAngle (outTangentAngleValue[index])               
            
            mfnAnimCurve.setTangent (index, inTangentMAngle, inTangentWeightValue[index], True)
            mfnAnimCurve.setTangent (index, outTangentMAngle, outTangentWeightValue[index], False)  
                
            mfnAnimCurve.setIsBreakdown (index, breakdown[index])        
            
            mfnAnimCurve.setInTangentType (index, inTangentType[index])       
            mfnAnimCurve.setOutTangentType (index, outTangentType[index])
            
    def createAnimationCurve(self, node, currentAttribute, animCurve) :
        
        mSelectionList = OpenMaya.MSelectionList ()
        mSelectionList.add ('%s.%s' % (node, currentAttribute))
        currentMPlug = OpenMaya.MPlug()
        mSelectionList.getPlug (0, currentMPlug)  
        
        connections = OpenMaya.MPlugArray()
        currentMPlug.connectedTo (connections, 1, 0)
        
        newAnimCurve = True
        
        if connections.length() :                
            connectedNode = connections[0].node() 
                           
            if connectedNode.hasFn (OpenMaya.MFn.kAnimCurve) :
                mfnAnimCurve = OpenMayaAnim.MFnAnimCurve (connectedNode)            
                newAnimCurve = False
                    
        if newAnimCurve :        
            try :
                mfnAnimCurve = OpenMayaAnim.MFnAnimCurve ()        
                animCurveType = mfnAnimCurve.timedAnimCurveTypeForPlug (currentMPlug)            
                mfnAnimCurve.create (currentMPlug, animCurveType)
            except Exception as result :            
                print result
                return False
        
        return mfnAnimCurve

