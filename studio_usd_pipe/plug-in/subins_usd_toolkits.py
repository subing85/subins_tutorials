#!/usr/bin/python

from studio_usd_pipe.core import menu


def initializePlugin(plugin):  # Initialize the script plug-in
    menu.create_menu()


def uninitializePlugin(plugin):  # Uninitialize the script plug-in
    menu.remove_menu()
