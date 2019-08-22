import os
import pkgutil
import warnings

import sys

paths = [
    '/usr/lib64/python2.7',
    '/usr/lib64/python2.7/plat-linux2',
    '/usr/lib64/python2.7/lib-tk',
    '/usr/lib64/python2.7/lib-dynload',
    '/usr/lib64/python2.7/site-packages',
    '/usr/lib64/python2.7/site-packages/gtk-2.0',
    '/usr/lib/python2.7/site-packages'
    ]


def start(*args):   
    from maya import standalone
    standalone.initialize(name='python')
    from pymel import core
    data = {}
    core.openFile(args[0], f=True)
    code_dirname = os.path.dirname(args[1])
    code_name = os.path.splitext(os.path.basename(args[1]))[0]
    result = None
    for module_loader, name, ispkg in pkgutil.iter_modules([code_dirname]):
        if name != code_name:
            continue        
        loader = module_loader.find_module(name)
        try:
            print '#&&#code&##&'
            module = loader.load_module(name)
            print '#&&#code_end&##&'
            print '#&&#status&##&'
            print 'success'
            result = True
        except Exception as error:
            warnings.warn(str(error), Warning)
            print '#&&#status&##&'
            print 'failed'
            result = False
    if not result:
        return
    if args[2] != 'None':
        core.saveAs(args[2], f=True, iv=True, pmt=True)
    standalone.uninitialize(name='python')
