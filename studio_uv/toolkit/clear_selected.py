'''
clear_selected.py 0.0.1 
Date: August 08, 2019
Last modified: August 08, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    None
'''

NAME = 'Clear Selected Polygons UV\'s'
ORDER = 6
VALID = True
LAST_MODIFIED = 'August 08, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'Clear selected polygon uvs!...'
SEPARATOR = False

def execute():
    from pymel import core
    core.studioUV(cl=True, s='selected')
    return True