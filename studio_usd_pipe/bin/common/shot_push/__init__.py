#!/usr/bin/python

NAME = 'Shot Push'
ORDER = 5
VALID = True # upadte with True
TYPE = 'common_application'
KEY = 'shot_push'
ICON = 'shot_push.png'
OWNER = 'Subin Gopi'
COMMENTS = 'shot push/publish such as model, uv, surface, puppet!...'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


if __name__ == '__main__':
    from studio_usd_pipe.gui import shot_push
    shot_push.show_window(standalone=True)
