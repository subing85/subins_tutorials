#!/usr/bin/python

NAME = 'Spread Sheet'
ORDER = 13
VALID = True
TYPE = 'maya_tool'
KEY = 'spreadsheet'
SEPARATOR = True
ICON = 'spreadsheet.png'
OWNER = 'Subin Gopi'
COMMENTS = 'assets and shots spreadsheet!...'
VERSION = '0.0.0'
MODIFIED = 'May 19, 2020'


def execute():
    from studio_usd_pipe.gui import spreadsheet
    spreadsheet.show_window(standalone=False)

