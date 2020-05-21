#!/usr/bin/python

NAME = 'Casting Sheet'
ORDER = 7
VALID = True
TYPE = 'maya_tool'
KEY = 'castingsheet'
SEPARATOR = True
ICON = 'castingsheet.png'
OWNER = 'Subin Gopi'
COMMENTS = 'Create the casting for shots!...'
VERSION = '0.0.0'
MODIFIED = 'May 19, 2020'


def execute():
    from studio_usd_pipe.gui import castingsheet
    castingsheet.show_window(standalone=False)
