import pkgutil

from pymel import core
from functools import partial
from studio_usd_pipe import resource

MENU_NAME = 'studio_toolkit_menu'
MENU_LABEL = 'Subin\'s USD ToolKit'


def create_menu():
    tool_kit_path = resource.getToolKitPath()
    print tool_kit_path
    modules = get_packages(tool_kit_path)
    studio_uv_menu = make_menu(
        MENU_NAME, MENU_LABEL)
    sorted_index = sorted(modules)
    
    print modules
    for index in sorted_index:
        for module in modules[index]:
            lable = module.NAME
            if hasattr(module, 'SEPARATOR'):
                if module.SEPARATOR:
                    core.ui.MenuItem(d=True, p=studio_uv_menu)
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
