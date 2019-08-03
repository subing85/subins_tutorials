'''
import_all.py 0.0.1 
Date: June 24, 2019
Last modified: August 03, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    None
'''

NAME = 'Import All Polygons'
ORDER = 2
VALID = True
LAST_MODIFIED = 'July 28, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To import the all uv sets!...'


def execute():
    from pymel import core
    replay = core.fileDialog2(
        dir=core.workspace(q=True, dir=True),
        ds=2,
        ff="Uv Set Ascii (*.uv)",
        fm=1,
        okc='Import',
        cap=NAME
    )
    if not replay:
        return None
    import_path = replay[0]
    core.studioUV(typ='import', s='all', rp=False, dir=import_path)
    return import_path
