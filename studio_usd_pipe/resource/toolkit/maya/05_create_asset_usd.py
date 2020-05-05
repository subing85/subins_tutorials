#!/usr/bin/python

NAME = 'Create Asset USD'
ORDER = 5
VALID = True
TYPE = 'maya_tool'
KEY = 'create_asset_usd'
SEPARATOR = True
ICON = 'asset_usd.png'
OWNER = 'Subin Gopi'
COMMENTS = 'Create USD with complete assets!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'


def execute():
    from studio_usd_pipe.gui import asset_pushusd
    reload(asset_pushusd)
    asset_pushusd.show_window(standalone=False)
