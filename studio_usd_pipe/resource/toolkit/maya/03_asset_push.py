#!/usr/bin/python

NAME = 'Asset Push/Publish'
ORDER = 3
VALID = True
TYPE = 'maya_tool'
KEY = 'asset_push'
SEPARATOR = True
ICON = 'asset_push.png'
OWNER = 'Subin Gopi'
COMMENTS = 'asset push/publish such as model, uv, surface, puppet!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'


def execute():
    from studio_usd_pipe.gui import asset_push
    reload(asset_push)
    asset_push.show_window(standalone=False)
