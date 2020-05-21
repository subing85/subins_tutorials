#!/usr/bin/python

NAME = 'Layout Pull'
ORDER = 8
VALID = True
TYPE = 'maya_tool'
KEY = 'layout_pull'
SEPARATOR = False
ICON = 'layout_pull.png'
OWNER = 'Subin Gopi'
COMMENTS = 'create the layout scene!...'
VERSION = '0.0.0'
MODIFIED = 'may 19, 2020'


def execute():
    from studio_usd_pipe.gui import layout_pull
    layout_pull.show_window(standalone=False)