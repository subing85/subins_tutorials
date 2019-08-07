'''
studio_menu.py 0.0.1 
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

import pkgutil

from pymel import core
from functools import partial
from studio_uv import resources

MENU_NAME = 'studio_uv_menu'
MENU_LABEL = 'Studio Uv\'s Sets'


def create_menu():
    tool_kit_path = resources.getToolKitPath()
    modules = get_packages(tool_kit_path)
    studio_uv_menu = make_menu(
        MENU_NAME, MENU_LABEL)
    sorted_index = sorted(modules)
    for index in sorted_index:
        for module in modules[index]:
            lable = module.NAME
            core.ui.MenuItem(
                l=module.NAME,
                p=studio_uv_menu,
                c=partial(executeModule, module)
            )
    core.displayInfo('// Result: %s menu created' % MENU_LABEL)


def remove_menu():
    make_menu(MENU_NAME, MENU_LABEL, remove=True)


def executeModule(module, *args):
    if not module:
        core.displayWarning('publish build not valid')
        return
    try:
        result = module.execute()
        core.displayInfo('Success!... %s' % result)
    except Exception as error:
        core.displayWarning('Failed!... %s' % str(error))


def make_menu(menu_name, label, remove=False):
    main_window = core.ui.Window(
        core.mel.eval('$tmpVar=$gMainWindow')
    )
    for each in main_window.getMenuArray():
        if each != menu_name:
            continue
        studio_uv_menu = core.ui.Menu(each)
        studio_uv_menu.delete()
    if remove:
        return
    studio_uv_menu = core.ui.Menu(
        menu_name, l=label, p=main_window, to=True)
    return studio_uv_menu


def get_packages(root_path):
    module_data = {}
    for module_loader, name, ispkg in pkgutil.iter_modules([root_path]):
        loader = module_loader.find_module(name)
        module = loader.load_module(name)
        if not hasattr(module, 'VALID'):
            continue
        current_order = 0
        if hasattr(module, 'ORDER'):
            current_order = module.ORDER
        module_data.setdefault(
            current_order, []).append(module)
    return module_data
