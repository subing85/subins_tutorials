#!/usr/bin/python

NAME = 'Casting Sheet'
ORDER = 2
VALID = True # upadte with True
TYPE = 'common_application'
KEY = 'castingsheet'
ICON = 'castingsheet.png'
OWNER = 'Subin Gopi'
COMMENTS = 'to create casting data preset for shots!...'
VERSION = '0.0.0'
MODIFIED = 'May 17, 2020'


if __name__ == '__main__':
    from studio_usd_pipe.gui import castingsheet
    castingsheet.show_window(standalone=True)