#!/usr/bin/python

NAME = 'Set Show'
ORDER = 0
VALID = True
TYPE = 'maya_tool'
KEY = 'set_show'
SEPARATOR = False
ICON = 'set_show.png'
OWNER = 'Subin Gopi'
COMMENTS = 'set the maya project settings with current show!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'


def execute():
    from studio_usd_pipe.snippet.utils.smaya import show
    show.set()
