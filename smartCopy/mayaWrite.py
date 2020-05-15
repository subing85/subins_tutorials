'''
Write Data module - v0.1
Date : August 20, 2016
Last modified: August 20, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

fullPath = 'C:/Users/Desktop/temp.txt'
types = 'pose'  
dataContent = {}          
from smartCopy import mayaWrite 
mw = mayaWrite.MayaWrite(dataFile=fullPath, types=types)
mp = mWrite(dataContent)  

# WARNING! All changes made in this file will be lost!
'''

import os
import sys
import warnings
import json
import pprint
from datetime import datetime


class MayaWrite():
    
    '''
    Description
        This Class can write and read the custom data formart.
        :param    dataFile <str>     example 'C:/Users/Desktop/temp.txt'
        :types    dataFile <str>     example 'pose or anim'        
        :example to execute        
            fullPath = 'C:/Users/Desktop/temp.txt'
            types = 'pose'  
            dataContent = {}          
            from smartCopy import mayaWrite 
            mw = mayaWrite.MayaWrite(dataFile=fullPath, types=types)
            mp = mWrite(dataContent)            
    '''        
    
    def __init__(self, dataFile, types):
        
        if not dataFile:
            warnings.warn('class \"MayaWrite\" Initializes a new file <str>')
            return None 
        
        self._fullPath = dataFile        
        self._fileDirname = os.path.splitext(dataFile)[0]
        self._fileType = os.path.splitext(dataFile)[1]
        self._types = types       
    
    def mWrite(self, dataContent=None):
        
        '''
        Description            
            Function for write the dictionary data to custom format.
            
            :Type - class function                  
            :param  dataContent <dict>     example {}            
            :return result                   
            :example to execute                 
                data = {}
                dataType = 'json'
                from smartCopy import mayaWrite    
                mayaWrite.MayaWrite (dataContent)                    
        '''    

        if not dataContent:
            warnings.warn('function set \"mWrite\" argument data none')
            return None
                 
        writeData(path=self._fileDirname, data=dataContent, dataType=self._fileType, types=self._types)

    def mRead(self):
        
        '''
        Description            
            Function for read the dictionary data from custom format.
            
            :Type - class function                  
            :param  None <dict>     example {}            
            :return self.fileData                   
            :example to execute            
                fullPath = self._fullPath                             
                mw = mayaWrite.MayaWrite(fullPath, None)            
                poseData = mw.mRead()                
                mp.paste(dataContent=poseData)             
        '''   
        
        if not os.path.isfile(self._fullPath):
            warnings.warn('function set \"mRead\" file does not exists {}'.format(self._fullPath))
            return None     
        
        self._fileData = readData(self._fullPath)        


def writeData(path=None, data=None, dataType=None, types=None):    
    
    '''
    Description            
        Function for write the dictionary data to custom format.
        
        :Type - standalone function        
        :param  path <str>     example os.getenv('TEMP')    
        :param  data <dict>     example {}
        :param  dataType    <str> example ['resources', 'plugins', 'bin', 'icons']        
        :return None                
        :example to execute                
            data = {}
            dataType = 'json'
            from smartCopy import mayaWrite    
            mayaWrite.writeData (data, dataType)                    
    '''    
    
    if not path:
        warnings.warn('function \"writeData\" argument path none')
        return None  
    
    if not data:
        warnings.warn('function \"writeData\" argument data none')
        return None  
    
    if not dataType:
        warnings.warn('function \"writeData\" argument dataType none')
        return None   

    dataPath = '{}{}'.format(path, dataType)
    
    if os.path.isfile(dataPath):
    
        try :
            os.chmod (dataPath, 0777)
            os.remove (dataPath)
        except Exception as result :
            print result
        
    comments = {1: {}}
    comments[1]['Name'] = types
    comments[1]['Date'] = datetime.now().strftime("%A, %B %d, %Y %H:%M:%S %p")  
    comments[1]['Author'] = 'Subin. Gopi (subing85@gmail.com)'
    comments[1]['Copyright'] = '(c) 2018, Subin Gopi All rights reserved.'    
    comments[1]['WARNING'] = '# WARNING! All changes made in this file will be lost!'  
    
    finalData = {2: data}         
    finalData.update(comments)    

    openData = open (dataPath, 'w')
    jsonData = json.dumps (finalData, indent=4)    
    openData.write(jsonData)
    openData.close ()
    
    print '\n#Successfully write your data', dataPath
    

def readData(fullPath): 
    
    '''
    Description            
        Function for read the custom file.
        
        :Type - standalone function        
        :param  fullPath <str>     example os.getenv('TEMP')        
        :return data
        :example to execute
            data = {}
            dataType = 'json'
            from smartCopy import mayaWrite    
            mayaWrite.readData (fullPath)                
    '''     
    
    if not fullPath:
        warnings.warn('function \"readData\" argument fullPath none')
        return None     

    if not os.path.isfile(fullPath):
        warnings.warn('function \"readData\" file does not exists {}'.format(fullPath))
        return None           
       
    openData = open (fullPath, 'r')
    jsonData = json.load (openData)
    openData.close () 
    
    if '2' in jsonData: 
        return jsonData['2']
    
    return jsonData
        
#End########################################################################################
