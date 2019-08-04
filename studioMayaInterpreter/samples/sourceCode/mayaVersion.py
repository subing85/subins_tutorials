'''
Smart Maya Version v0.1
Date : June 16, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import sys, os, imp
docDirectory   = os.path.abspath (os.getenv('USERPROFILE') + '/Documents').replace ('\\', '/')

def version () :
    mayaVersion    = readCurrentMaya()    
    
    os.environ['MAYA_LOCATION'] = 'C:/Program Files/Autodesk/' + mayaVersion
    os.environ['PYTHONHOME']    = 'C:/Program Files/Autodesk/' + mayaVersion + '/Python'
    os.environ['PATH']          = 'C:/Program Files/Autodesk/' + mayaVersion + '/bin;' + os.environ['PATH']

    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages/setuptools-0.6c9-py2.6.egg')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages/pymel-1.0.0-py2.6.egg')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages/ipython-0.10.1-py2.6.egg')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages/ply-3.3-py2.6.egg')                         
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/bin/python26.zip')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/DLLs')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/plat-win')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/lib-tk')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/bin')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/Python/lib/site-packages/maya')
    sys.path.append('C:/Program Files/Autodesk/' + mayaVersion + '/devkit/other/pymel/extras/completion/py')

    print 'mayaVersion\t', mayaVersion


def readCurrentMaya () :
    path        =  docDirectory + '/SmartTool/SmartMaya/smartMayaSetup.py'
    if os.path.isfile (path) :
        database       = os.path.basename (path).split('.')[0]        
        sys.path.append (os.path.dirname (path))
        import smartMayaSetup as smSetup
        imp.reload (smSetup)            
        mayaType    = smSetup.SMARTMAYA_type ()

        mayaVersion = os.path.basename (mayaType.values()[0])
        print 'Current Maya Version\t', mayaVersion
    else :
        mayaVersion    = 'Maya2012'

    return os.path.basename (mayaVersion)
    
