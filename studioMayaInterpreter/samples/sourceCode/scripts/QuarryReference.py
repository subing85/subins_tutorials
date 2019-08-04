'''
Quary Reference assets in maya file
Date : June 30, 2016
Last modified: June 30, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import os
from maya.cmds import *

tempDirectory  = os.path.abspath (os.getenv('TEMP')).replace ('\\', '/')

if os.path.isfile (tempDirectory + '/fileInfo.rtf') :
    try :
        os.remove (tempDirectory + '/fileInfo.rtf')
    except :
        pass
        
data     = open (tempDirectory + '/fileInfo.rtf', 'w')

for eachFile in file (q=1, r=1) :
    namespace       = file (eachFile,  q=1, ns=1).encode()
    filterPath      = os.path.abspath (referenceQuery (eachFile,  filename=1, wcn=True)).replace ('\\', '/').encode()
    worldNode       = referenceQuery (eachFile, n=1)[0]    
    
    print filterPath + '\n\tnamespace\t%s\n\tObject\t%s%s'% (namespace, worldNode, '\n\n')  
    data.write (filterPath + '\n\tnamespace\t%s\n\tObject\t%s%s'% (namespace, worldNode, '\n\n'))
    
data.close ()
os.startfile (tempDirectory + '/fileInfo.rtf')
