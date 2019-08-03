'''
export_all.py 0.0.1 
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

NAME = 'Export All'
ORDER = 0
VALID = True
LAST_MODIFIED = 'July 28, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To export the all uv sets!...'


def execute():
    from pymel import core
    replay = core.fileDialog2(
        dir=core.workspace(q=True, dir=True),
        ds=2,
        ff="Uv Set Ascii (*.uv)",
        fm=0,
        okc='Export',
        cap=NAME
    )
    if not replay:
        return None
    export_path = replay[0]
    if not replay[0].endswith('.uv'):
        export_path = '%s.uv' % replay[0]
    core.studioUV(typ='export', s='all', dir=export_path)
    return export_path