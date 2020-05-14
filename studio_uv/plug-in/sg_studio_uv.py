'''
sg_studio_uv.py 0.0.1 
Date: June 24, 2019
Last modified: August 03, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    None
'''

import sys

from maya import OpenMaya
from maya import OpenMayaMPx
from studio_uv.core import parameters
from studio_uv.core import studio_menu

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
    studio_menu.create_menu()


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
    studio_menu.remove_menu()
