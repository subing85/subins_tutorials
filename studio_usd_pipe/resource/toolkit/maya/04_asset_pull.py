#!/usr/bin/python

NAME = 'Asset Pull'
ORDER = 4
VALID = True
TYPE = 'maya_tool'
KEY = 'asset_pull'
SEPARATOR = False
ICON = 'asset_pull.png'
OWNER = 'Subin Gopi'
COMMENTS = 'pull asset to scene such as model, uv, surface, puppet!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'


def execute():
    from studio_usd_pipe.gui import asset_pull
    asset_pull.show_window(standalone=False)
