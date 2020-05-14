#!/usr/bin/python

NAME = 'Studio Launcher'
VALID = True
TYPE = 'application'
KEY = 'launcher'
OWNER = 'Subin Gopi'
COMMENTS = 'To setup the show'
VERSION = '0.0.0'
MODIFIED = 'April 28, 2020'

if __name__ == '__main__':
    from studio_usd_pipe.gui import studio_launcher
    studio_launcher.show_window()
