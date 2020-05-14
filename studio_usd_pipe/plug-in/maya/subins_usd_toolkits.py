#!/usr/bin/python

from studio_usd_pipe.core import mmenu
reload(mmenu)


def initializePlugin(plugin):  # Initialize the script plug-in
    mmenu.create_menu()


def uninitializePlugin(plugin):  # Uninitialize the script plug-in
    mmenu.remove_menu()
