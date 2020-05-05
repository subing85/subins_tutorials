import os

from pymel import core
from functools import partial
from studio_usd_pipe import resource
from studio_usd_pipe.core import common

MENU_NAME = 'studio_toolkit_menu'
MENU_LABEL = 'Subin\'s USD ToolKit'


def create_menu():
    tool_kit_path = resource.getMayaToolKitPath()    
    icon_path = resource.getIconPath()
    modules = common.get_modules(tool_kit_path, module_types=['maya_tool'])
    if 'maya_tool' not in modules:
        core.displayWarning('Failed!...  not found any toolkits')
        return
    maya_modules = modules['maya_tool'] 
    studio_uv_menu = make_menu(MENU_NAME, MENU_LABEL)   
    for index, module in maya_modules.items():
        lable = module.NAME
        if hasattr(module, 'SEPARATOR'):
            if module.SEPARATOR:
                core.ui.MenuItem(d=True, p=studio_uv_menu)
        module_icon = 'unknown.png'     
        if hasattr(module, 'ICON'):
            module_icon = module.ICON
        core.ui.MenuItem(
            l=module.NAME,
            p=studio_uv_menu,
            i=os.path.join(icon_path, module_icon),
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

