import sys, os

os.environ['MAYA_LOCATION'] = 'C:/Program Files/Autodesk/Maya2013'
os.environ['PYTHONHOME']    = 'C:/Program Files/Autodesk/Maya2013/Python'
os.environ['PATH']          = 'C:/Program Files/Autodesk/Maya2013/bin;' + os.environ['PATH']

sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/site-packages/setuptools-0.6c9-py2.6.egg')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/site-packages/pymel-1.0.0-py2.6.egg')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/site-packages/ipython-0.10.1-py2.6.egg')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/site-packages/ply-3.3-py2.6.egg')                         
sys.path.append('C:/Program Files/Autodesk/Maya2013/bin/python26.zip')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/DLLs')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/plat-win')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/lib-tk')
sys.path.append('C:/Program Files/Autodesk/Maya2013/bin')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python')
sys.path.append('C:/Program Files/Autodesk/Maya2013/Python/lib/site-packages')

import maya.standalone
maya.standalone.initialize(name='python')
