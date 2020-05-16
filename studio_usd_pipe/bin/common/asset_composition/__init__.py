#!/usr/bin/python

NAME = 'Asset Composition'
ORDER = 1
VALID = True # upadte with True
TYPE = 'common_application'
KEY = 'asset_composition'
ICON = 'asset_composition.png'
OWNER = 'Subin Gopi'
COMMENTS = 'create asset composition usd'
VERSION = '0.0.0'
MODIFIED = 'May 16, 2020'


if __name__ == '__main__':
    from studio_usd_pipe.gui import asset_composition
    asset_composition.show_window(standalone=True)