'''
initialize.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import pkgutil
import warnings


def start(*args):
    from maya import standalone
    standalone.initialize(name='python')
    from pymel import core
    core.openFile(args[0], f=True)
    result = None
    if args[1].endswith('.mel'):
        try:
            core.mel.eval('source \"%s\"' % args[1])
            result = True
        except Exception as error:
            warnings.warn(str(error), Warning)
            result = False
    else:
        code_dirname = os.path.dirname(args[1])
        code_name = os.path.splitext(os.path.basename(args[1]))[0]
        for module_loader, name, ispkg in pkgutil.iter_modules([code_dirname]):
            if name != code_name:
                continue
            loader = module_loader.find_module(name)
            try:
                module = loader.load_module(name)
                result = True
            except Exception as error:
                warnings.warn(str(error), Warning)
                result = False
    if not result:
        return
    if args[2] != 'None':
        core.saveAs(args[2], f=True, iv=True, pmt=True)
    standalone.uninitialize(name='python')
