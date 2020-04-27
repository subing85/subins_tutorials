'''
Maya Pose - v0.1
Date : August 20, 2016
Last modified: August 20, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

objects = pymel.ls(sl=True)
from smartCopy import mayaPose 
mp = mayaPose.MayaPose(objects)
mp = copy()   

# WARNING! All changes made in this file will be lost!
'''

from pymel import core as pymel
import warnings
import pprint


class MayaPose():
    
    '''
    Description
        This Class can manage get and set the attribute value of maya objects.
        
        :param    objects <[str]>     example 'mayaObjects'        
        :example to execute        
            objects = pymel.ls(sl=True)
            from smartCopy import mayaPose 
            mp = mayaPose.MayaPose(objects)
            mp.copy()            
    '''    
    
    def __init__(self, objects=None):
        
        if not objects: 
            warnings.warn('class \"MayaPose\" Initializes a new maya objects <[str]>')
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
            Function for store(copy) the maya objects attributes value.
                        
            :Type - class function                  
            :param  None            
            :return dataList    <dict>    example {'mObect': {'attributes': {'rx': 0.0, 'ry': 0.0}, 'namespace': 'Clifan:'}}                   
            :example to execute            
                from smartCopy import mayaPose
                reload(mayaPose)
                objects = pymel.ls(sl=1)
                mp= mayaPose.MayaPose(objects=objects)
                poseData = mp.copy()
        '''
        
        if not self._mObjects:
            warnings.warn('function set \"copy\" _mObjects attribute value is none, update the _mObjects attribute value')
            return None  
        
        dataList = {}               

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
            
            attributeData = {}
            for eachAttri in attriList:                
                currentValue = eachAttri.get()                
                attributeData.setdefault(eachAttri.attrName().encode(), currentValue) 
                
            controlDatas = {'namespace': currentNamespace.encode(),
                            'attributes': attributeData}
            
            dataList.setdefault (currentObject, controlDatas)            
            
        pprint.pprint(dataList)  

        return dataList
    
    def paste(self, dataContent):       
        
        '''
        Description            
            Function for set(paste) the maya objects attributes value.
                        
            :Type - class function                  
            :param  dataContent    <dict>    example {'mObect': {'attributes': {'rx': 0.0, 'ry': 0.0}, 'namespace': 'Clifan:'}}
            :return  None                
            :example to execute               
                from smartCopy import mayaPose
                reload(mayaPose)
                data = {}
                mp= mayaPose.MayaPose(objects=objects)
                mp.paste(dataContent=data)
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
        
        for eachNode, eachNamespace in objects.iteritems():            
            currentNode = '{}{}'.format(eachNamespace, eachNode)
            
            if not eachNamespace:
                currentNode = eachNode                
                
            print '\n'
            
            for eachAttri, eachValue in dataContent[eachNode]['attributes'].iteritems():   
                
                if not pymel.objExists ('{}.{}'.format(currentNode, eachAttri)) :
                    continue                             
                pyNode = pymel.PyNode(currentNode)
                
                try:
                    pyNode.setAttr(eachAttri, eachValue)
                    print eachNode, eachAttri, eachValue
                except Exception as result:
                    warnings.warn('Pose paste error {}'.format(result))
        
        pymel.undoInfo (closeChunk=True)                    
        
#End######################################################################################################
