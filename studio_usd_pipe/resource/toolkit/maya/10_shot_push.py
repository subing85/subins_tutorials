#!/usr/bin/python

NAME = 'Shot Push/Publish'
ORDER = 10
VALID = True
TYPE = 'maya_tool'
KEY = 'shot_push'
SEPARATOR = False
ICON = 'shot_push.png'
OWNER = 'Subin Gopi'
COMMENTS = 'push/publish the shot!...'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute():
    from studio_usd_pipe.gui import shot_push
    reload(shot_push)
    shot_push.show_window(standalone=False)