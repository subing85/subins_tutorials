#!/usr/bin/python

NAME = 'Asset Push'
ORDER = 0
VALID = True # upadte with True
TYPE = 'common_application'
KEY = 'asset_push'
ICON = 'asset_push.png'
OWNER = 'Subin Gopi'
COMMENTS = 'asset push/publish such as model, uv, surface, puppet!...'
VERSION = '0.0.0'
MODIFIED = 'April 30, 2020'


if __name__ == '__main__':
    from studio_usd_pipe.gui import asset_push
    asset_push.show_window(standalone=True)