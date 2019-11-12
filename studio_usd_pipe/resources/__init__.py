import os
import json
import platform

from studio_usd_pipe.utils import platforms

CURRENT_PATH = os.path.dirname(__file__)


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getInputPath():
    return os.path.join(CURRENT_PATH, 'inputs')


def getMayaFormats():
    formats = '(*.ma *.mb)'
    return formats


def getImageFormats():
    formats = '(*.bmp *.jpg *.jpeg *.png *.ppm *.tiff *.xbn *.xpm)'
    return formats


def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.abspath(
            os.getenv('USERPROFILE') + '/Documents').replace('\\', '/')
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents')


def getPreferencesPath():
    preferences_path = os.path.join(
        getWorkspacePath(),
        platforms.get_tool_name(),
        'preference',
        '.json'
    )
    return preferences_path


def getScriptPath():
    return os.path.join(CURRENT_PATH, 'scripts')


def getScriptSourceScripts(key=None):
    script_path = getScriptPath()
    source_scripts = {
        'export_source_images': os.path.join(script_path, 'export_source_images.py'),
        'export_asset_usd': os.path.join(script_path, 'export_asset_usd.py')
        }    
    if key in source_scripts:
        return source_scripts[key]    
    return source_scripts
        

def getOperatingSystem():
    return platform.system()


def getInputDirname():
    preference_path = getPreferencesPath()
    with (open(preference_path, 'r')) as open_data:
        data = json.load(open_data)
        if not data['enable']:
            return None
        return data['data']
    


    
