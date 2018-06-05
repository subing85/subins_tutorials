'''
Maya Anim - v0.1
Date : August 20, 2016
Last modified: August 20, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

objects = pymel.ls(sl=True)
from smartCopy import mayaAnim
ma = mayaAnim.MayaAnim(objects)
ma = copy()   

# WARNING! All changes made in this file will be lost!
'''

from pymel import core as pymel
import warnings
import pprint

class MayaAnim():
    
    '''
    Description
        This Class can manage get and set the animation curve value of maya objects.
        
        :param    objects <[str]>     example 'mayaObjects'        
        :example to execute        
            objects = pymel.ls(sl=True)
            from smartCopy import mayaAnim 
            ma = mayaAnim.MayaAnim(objects)
            ma.copy()            
    '''    
    
    def __init__(self, objects=None):
        
        if not objects: 
            warnings.warn('class \"MayaAnim\" Initializes a new maya objects <[str]>')
            return None     
                
        pymelObjects = []
                
        for eachObject in objects:
            if not pymel.objExists(eachObject):
                continue
            try:          
                pymelObjects.append(pymel.PyNode(eachObject))
            except:
                pass
            
        self._mObjects = pymelObjects
        
    
    def copy(self):
        
        '''
        Description            
            Function for store(copy) the animation curve value of maya objects.
                        
            :Type - class function                  
            :param  None            
            :return dataList    <dict>    example {'mObect': {'attributes': {animation information}, 'namespace': 'Clifan:'}}                   
            :example to execute            
                from smartCopy import mayaPose
                reload(mayaPose)
                objects = pymel.ls(sl=1)                
                ma = mayaAnim.MayaAnim(objects=objects)      
                animData = ma.copy()   
        '''
        
        if not self._mObjects:
            warnings.warn('function set \"copy\" _mObjects attribute value is none, update the _mObjects attribute value')
            return None  
        
        startFrame = int(pymel.playbackOptions(q=True, min=True))        
        endFrame = int(pymel.playbackOptions(q=True, max=True))
        
        dataList = {} 
        boolInt = {True: 1, False: 0}              

        for eachObject in self._mObjects :
            currentNamespace = 'None'
            currentObject = eachObject.name()
            
            if pymel.referenceQuery(eachObject, inr=True):
                currentNamespace = eachObject.namespace()
                currentObject = eachObject.name().replace(currentNamespace, '')
                
            attriList = eachObject.listAttr(r=True, w=True, k=True, u=True, v=True, m=True, s=True)
            
            if not attriList:
                print 'attributes are does not exists', eachObject.name()               
                continue  
            
            attributesAnimation = {}
            
            for eachAttri in attriList:               

                sourceKey = pymel.keyframe (eachAttri, q=True)                
                if not sourceKey:
                    continue 
                
                animCurves = eachAttri.listConnections(d=False, s=True)                
                if not animCurves:
                    continue
                
                if 'animCurve' not in animCurves[0].type():
                    continue

                weightTangent = int (pymel.keyTangent (animCurves[0], q=True, wt=True)[0])            
                preInfinity = animCurves[0].getAttr('preInfinity')
                postInfinity = animCurves[0].getAttr('postInfinity')  
                              
                inTangentType = pymel.keyTangent (animCurves[0], q=True, t=(startFrame,endFrame), itt=True)                 
                if inTangentType:
                    inTangentType = [eachInTangent.encode () for eachInTangent in inTangentType]                                   
                
                outTangentType = pymel.keyTangent (animCurves[0], q=True, t=(startFrame,endFrame), ott=True) 
                if outTangentType:
                    outTangentType = [eachOutTangent.encode () for eachOutTangent in outTangentType]                                           

                inAngle = pymel.keyTangent (animCurves[0], q=1, t=(startFrame,endFrame), ia=1)
                outAngle = pymel.keyTangent (animCurves[0], q=1, t=(startFrame,endFrame), oa=1) 
                timeChange = pymel.keyframe(eachAttri.nodeName(), at=eachAttri.attrName(), query=True, t=(startFrame,endFrame), tc=True )
                valueChange = pymel.keyframe(eachAttri.nodeName(), at=eachAttri.attrName(), query=True, t=(startFrame,endFrame), vc=True )
                
                currentAnimation = {}
                currentAnimation['animCurve'] = animCurves[0].name().encode ()
                currentAnimation['animCurveType'] = animCurves[0].type().encode ()                
                currentAnimation['weightTangent'] = weightTangent
                currentAnimation['preInfinity'] = preInfinity
                currentAnimation['postInfinity'] = postInfinity
                currentAnimation['inTangentType'] = inTangentType
                currentAnimation['outTangentType'] = outTangentType                
                currentAnimation['inAngle'] = inAngle
                currentAnimation['outAngle'] = outAngle                         
                currentAnimation['timeChange'] = timeChange
                currentAnimation['valueChange'] = valueChange 
                
                attributesAnimation.setdefault(eachAttri.attrName().encode(),  currentAnimation)
                                
            controlDatas = {'namespace': currentNamespace.encode(),
                            'attributes': attributesAnimation}
            
            dataList.setdefault (currentObject, controlDatas)            
            
        pprint.pprint(dataList)  

        return dataList


    def paste(self, dataContent):       
        
        '''
        Description            
            Function for set(paste) the animation curve value of maya objects.
                        
            :Type - class function                  
            :param  dataContent    <dict>    example {'mObect': {'attributes': {animation information}, 'namespace': 'Clifan:'}} 
            :return  None                
            :example to execute               
                from smartCopy import mayaAnim
                reload(mayaAnim)
                data = {}
                ma= mayaAnim.MayaAnim(objects=objects)
                ma.paste(dataContent=data)
        '''
                
        pymel.undoInfo (openChunk=True)
        
        objects = {}
        
        for eachObject in self._mObjects:
                        
            if pymel.referenceQuery(eachObject, inr=True):  
                currentNamespace = eachObject.namespace().encode()
                currentObject = eachObject.name().replace(currentNamespace, '').encode()                  
                
                if currentObject not in dataContent: 
                    continue
                objects.setdefault (currentObject, currentNamespace)

            else:                
                if eachObject.name() not in dataContent: 
                    continue      
                          
                objects.setdefault (eachObject.name().encode(), None)
                
        if not objects:
            warnings.warn('sorry, your selected object can not find in the copy data.')
            return None
        
        startFrame = int(pymel.currentTime(q=1))            
        
        for eachNode, eachNamespace in objects.iteritems():            
            currentNode = '{}{}'.format(eachNamespace, eachNode)
            
            if not eachNamespace:
                currentNode = eachNode                
                
            print '\n'
            
            for eachAttri, eachValue in dataContent[eachNode]['attributes'].iteritems():                
                
                if not pymel.objExists ('{}.{}'.format(currentNode, eachAttri)) :
                    continue
                
                pyNode = pymel.PyNode(currentNode)                
                pyAttributes = pymel.PyNode('{}.{}'.format(currentNode, eachAttri))

                animCurve = eachValue['animCurve']
                animCurveType = eachValue['animCurveType']     
                weightTangent = eachValue['weightTangent']
                preInfinity = eachValue['preInfinity']
                postInfinity = eachValue['postInfinity']
                inTangentType = eachValue['inTangentType']
                outTangentType = eachValue['outTangentType']                
                inAngle = eachValue['inAngle']
                outAngle = eachValue['outAngle']                         
                timeChange = eachValue['timeChange']
                valueChange = eachValue['valueChange']      
                
                animCurves = pyAttributes.listConnections(d=False, s=True)       
                         
                if animCurves:                
                    if animCurves[0].type()=='animCurveTL' or animCurves[0].type()=='animCurveTA' or animCurves[0].type()=='animCurveTU':
                        currentAnimCurve = animCurves[0]
                else:
                    currentAnimCurve = pymel.createNode (animCurveType, n=pyAttributes.name().replace('.', '_'))
                    currentAnimCurve.connectAttr('output', pyAttributes)
                
                pymel.keyTangent (currentAnimCurve, e=True, wt=weightTangent)  #Set weightTangent                                                
                
                currentAnimCurve.setAttr ('preInfinity', preInfinity) #Set preInfinity 
                currentAnimCurve.setAttr ('postInfinity', postInfinity) #Set postInfinity 
                
                #Set frames and key
                for index in range (len(timeChange)) :                                           
                    precentage   = float(valueChange[index]) * 100/100.00                                        
                    currentFrame =  (startFrame + timeChange[index])-1
                                                         
                    pymel.setKeyframe (currentAnimCurve, time=float(currentFrame), value=precentage)                       
                    pymel.keyTangent (currentAnimCurve, e=1, t=(currentFrame, currentFrame), itt=inTangentType[index], ott=outTangentType[index])
                    pymel.keyTangent (currentAnimCurve, e=1, t=(currentFrame, currentFrame), ia=inAngle[index], oa=float(outAngle[index])) 
                    
                print eachNode, eachAttri, eachValue
        pymel.undoInfo (closeChunk=True)
         
#End######################################################################################################