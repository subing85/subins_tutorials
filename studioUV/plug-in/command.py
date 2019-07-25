"""
To use, make sure that helloWorldCmd.py is in your MAYA_PLUG_IN_PATH (and the
C++ version is not) then do the following:

import maya.cmds
maya.cmds.loadPlugin("helloWorldCmd.py")
maya.cmds.spHelloWorld()
"""

import sys
from maya import OpenMaya
from maya import OpenMayaMPx

from studioUV.bin import main
reload(main)

STUDIO_UV = main.Connect()
print '\nplugin name', STUDIO_UV.k_plugin_name


def initializePlugin(plugin):  # Initialize the script plug-in
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            STUDIO_UV.k_plugin_name,
            STUDIO_UV.cmdCreator,
            STUDIO_UV.syntaxCreator
        )
    except:
        sys.stderr.write(
            "Failed to register command: %s\n" % STUDIO_UV.k_plugin_name
        )
        raise


def uninitializePlugin(plugin):  # Uninitialize the script plug-in
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(STUDIO_UV.k_plugin_name)
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % STUDIO_UV.k_plugin_name
        )
        raise
