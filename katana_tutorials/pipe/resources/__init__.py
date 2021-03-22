import os

CURRENT_PATH = os.path.dirname(__file__)


def get_icon_path():
    icon_path = os.path.join(CURRENT_PATH, 'icons')
    return icon_path


def get_shelves_path():
    shelves_path = os.path.join(CURRENT_PATH, 'Shelves')
    return shelves_path


def get_toolkit_path():    
    toolkit_path = os.path.join(CURRENT_PATH, 'toolkits')
    return toolkit_path


def get_show_path():
    if 'SHOW_PATH' in os.environ:
        show_path = os.environ['SHOW_PATH']
    else:
        show_path = '/venture/shows/katana_tutorials'
    return show_path


def get_template_path():
    template_path = os.path.join(get_show_path(), 'template')
    return template_path
    
