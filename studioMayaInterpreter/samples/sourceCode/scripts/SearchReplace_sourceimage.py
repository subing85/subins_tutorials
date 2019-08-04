'''
search replace sourceimage
Date : July 02, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import os
from maya.cmds import *

searchFor         = '.tga'
replaceWith       = '.png'

fileList          = ls (type='file')

for eachFile in fileList :
    path     = getAttr ('%s.fileTextureName'% eachFile)    
    setAttr ('%s.fileTextureName'% eachFile, path.replace(searchFor, replaceWith), type='string')