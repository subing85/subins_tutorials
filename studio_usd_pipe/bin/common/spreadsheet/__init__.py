#!/usr/bin/python

NAME = 'Spread Sheet'
ORDER = 3
VALID = True # upadte with True
TYPE = 'common_application'
KEY = 'spreadsheet'
ICON = 'spreadsheet.png'
OWNER = 'Subin Gopi'
COMMENTS = 'spreadsheet for push/publish result!...'
VERSION = '0.0.0'
MODIFIED = 'May 12, 2020'


if __name__ == '__main__':
    from studio_usd_pipe.gui import spreadsheet
    spreadsheet.show_window(standalone=True)