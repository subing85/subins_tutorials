#!/usr/bin/python

NAME = 'Set Bounding Box'
ORDER = 2
VALID = True
TYPE = 'maya_tool'
KEY = 'bounding_box'
SEPARATOR = False
ICON = 'bounding_box.png'
OWNER = 'Subin Gopi'
COMMENTS = 'Set the all view to Bounding Box!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'


def execute():
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    sm = studioMaya.Maya()
    sm.set_bounding_box()
