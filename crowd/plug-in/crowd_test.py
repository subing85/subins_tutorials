import os
import sys

from maya import OpenMaya 
from maya import OpenMayaMPx 


class SubinCrowds(OpenMayaMPx.MPxCommand):
    kPluginCmdName = "spHelloWorld"

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    @staticmethod
    def cmd_creator():
        return OpenMayaMPx.asMPxPtr( HelloWorldCmd() )

    def doIt(self,argList):
        self.get_environ()
        
    def get_environ(self):
        paths = os.environ['MAYA_PLUG_IN_PATH']    
        for path in paths.split(':'):
            print '\t', path 
            

# Initialize the script plug-in
def initializePlugin(plugin):
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            SubinCrowds.kPluginCmdName, SubinCrowds.cmd_creator
        )
    except:
        sys.stderr.write(
            "Failed to register command: %s\n" % SubinCrowds.kPluginCmdName
        )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(plugin):
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(SubinCrowds.kPluginCmdName)
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % SubinCrowds.kPluginCmdName
        )
        raise





