import os
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
    if platform.system()=='Windows':
        return os.path.abspath (
            os.getenv('USERPROFILE') + '/Documents').replace ('\\', '/')
    if platform.system()=='Linux':
        return os.path.join(os.getenv('HOME'), 'Documents')
    
def getPreferencesPath():
    preferences_path = os.path.join(
        getWorkspacePath(),
        platforms.get_tool_name(),
        'preference',
        '.json'
    )
    return  preferences_path  