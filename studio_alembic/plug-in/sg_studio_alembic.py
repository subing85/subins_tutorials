import sys

from maya import OpenMaya
from maya import OpenMayaMPx
from studio_alembic.core import parameters

PARAMETERS = parameters.Connect()


def initializePlugin(plugin):  # Initialize the script plug-in
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            PARAMETERS.k_plugin_name,
            PARAMETERS.cmdCreator,
            PARAMETERS.syntaxCreator
        )
    except:
        sys.stderr.write(
            "Failed to register command: %s\n" % PARAMETERS.k_plugin_name
        )
        raise


def uninitializePlugin(plugin):  # Uninitialize the script plug-in
    pluginFn = OpenMayaMPx.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(
            PARAMETERS.k_plugin_name
        )
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % PARAMETERS.k_plugin_name
        )
        raise
