'''
Quarry Shader Ands sourceimage information in maya file
Date : July 02, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import os
from maya.cmds import *

tempDirectory     = os.path.abspath (os.getenv('TEMP')).replace ('\\', '/')
data              = open (tempDirectory + '/sourceimageInfo.rtf', 'w')
data.write ('Shader and sourceimage information\n')

shaderList        = listConnections (':defaultShaderList1.s', s=1, d=0)
deafult           = ['lambert1', 'particleCloud1']

loop              = 1

for eachShader in shaderList :    
    if eachShader not in deafult :
        sahderInfo    = {'Shader':'', 'ShaderType' :'', 'Colors':[]}
        colorType     = listConnections ('%s'%eachShader, s=1, d=0)
        print eachShader, colorType
        
        sahderInfo['Shader'] = eachShader.encode()
        
        sahderInfo['ShaderType'] = objectType (eachShader).encode()
                
        if colorType :
            path     = getAttr ('%s.fileTextureName'% colorType[0])            
            sahderInfo['Colors'] = [colorType[0], path]            
        else :            
            sahderInfo['Colors'] = ['Color', getAttr ('%s.color'% eachShader)]
        
        dataList       = str(loop) + '\tShader\n\t\t"' + sahderInfo['Shader'] + '\"\t(\"' + sahderInfo['ShaderType']  + '\")' + '\n\t\tcolors\t' + sahderInfo['Colors'][0] + '\t\t' + str(sahderInfo['Colors'][1]) + '\n\n'
        print dataList
        data.write (dataList)
        loop+=1
        
data.close ()
os.startfile (tempDirectory + '/sourceimageInfo.rtf')   
