#!/usr/bin/python

NAME = 'Shot Pull/Open'
ORDER = 9
VALID = True
TYPE = 'maya_tool'
KEY = 'shot_pull'
SEPARATOR = False
ICON = 'shot_pull.png'
OWNER = 'Subin Gopi'
COMMENTS = 'pull/open the shot!...'
VERSION = '0.0.0'
MODIFIED = 'May 21, 2020'


def execute():
    from studio_usd_pipe.gui import shot_pull
    reload(shot_pull)
    shot_pull.show_window(standalone=False)