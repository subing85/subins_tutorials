import sys

from maya import OpenMaya
from maya import OpenMayaMPx

from crowd.api import crowdAttributes
from crowd.api import crowdProxy
reload(crowdAttributes)
reload(crowdProxy)

CROWD_ATTRIBUTES = crowdAttributes.Connect()
CROWD_PROXY = crowdProxy.Connect()

PLUGIN_CMD_NAME = CROWD_ATTRIBUTES.getPlugName()


def initializePlugin(mobject):  # initialize the script plug-in
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand(
            PLUGIN_CMD_NAME,
            CROWD_PROXY.cmdCreator,
            CROWD_PROXY.syntaxCreator
        )
    except:
        sys.stderr.write("Failed to register node: %s" % PLUGIN_CMD_NAME)
        raise


def uninitializePlugin(mobject):  # uninitialize the script plug-in
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(PLUGIN_CMD_NAME)
    except:
        sys.stderr.write("Failed to deregister node: %s" % PLUGIN_CMD_NAME)
        raise

#=========================================================================
# PROXY_NODE = proxyNode.Connect()
# PLUGIN_NAME = proxyNode.node_name
# NODE_ID = proxyNode.node_Id
#
#
# def initializePlugin(mobject):  # initialize the script plug-in
#     plugin = OpenMayaMPx.MFnPlugin(mobject)
#     try:
#         plugin.registerNode(
#             PLUGIN_NAME, NODE_ID,
#             proxyNode.nodeCreator,
#             proxyNode.nodeInitializer,
#             OpenMayaMPx.MPxNode.kLocatorNode)
#     except:
#         sys.stderr.write("Failed to register node: %s" % PLUGIN_NAME)
#         raise
#
#
# def uninitializePlugin(mobject):  # uninitialize the script plug-in
#     mplugin = OpenMayaMPx.MFnPlugin(mobject)
#     try:
#         mplugin.deregisterNode(PLUGIN_NAME, NODE_ID)
#     except:
#         sys.stderr.write("Failed to deregister node: %s" % PLUGIN_NAME)
#         raise
#=========================================================================
