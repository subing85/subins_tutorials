#!/usr/autodesk/maya2018/bin/mayapy
from maya import standalone
standalone.initialize(name="python")
import sys
#sys.path.append('/venture/source_code/subins_tutorials')
#from studio_usd_pipe.api import studioMaya
#smaya = studioMaya.Maya()
#maya_file = '/venture/shows/batman/tmp/scene_02.ma'
#smaya.open_maya(maya_file, None)

from maya import cmds
maya_file = '/venture/shows/batman/tmp/scene_02.ma'
cmds.file(f=1, new=1)
cmds.file (maya_file, o=True )

