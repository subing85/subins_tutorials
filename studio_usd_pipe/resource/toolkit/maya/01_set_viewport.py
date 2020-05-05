#!/usr/bin/python

NAME = 'Set Viewport'
ORDER = 1
VALID = True
TYPE = 'maya_tool'
KEY = 'set_viewport'
SEPARATOR = False
ICON = 'viewport.png'
OWNER = 'Subin Gopi'
COMMENTS = 'Set the currnet view to single perspective view!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'

def execute():
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    sm = studioMaya.Maya()
    sm.set_perspective_view()
