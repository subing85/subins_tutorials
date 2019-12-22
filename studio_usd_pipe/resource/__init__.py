
import os
import json
import platform

from studio_usd_pipe import utils


CURRENT_PATH = os.path.dirname(__file__)


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getInputPath():
    return os.path.join(CURRENT_PATH, 'inputs')


def getPreferenceFormat():    
    return '.pref'


def getPreferenceData(path=None):  
    if not path:
        path = os.path.join(getInputPath(), 'preferences.json')
    data = get_input_data(path)
    return data


def getConfigureData():
    path = os.path.join(getInputPath(), 'configure.json')
    data = get_input_data(path)
    return data


def getAssetIDData():
    path = os.path.join(getInputPath(), 'assetid.json')
    data = get_input_data(path)
    return data

        
def getWroldData():
    path = os.path.join(getInputPath(), 'world.json')
    data = get_input_data(path)
    return data

        
def get_input_data(path):
    if not path:
        raise IOError('not found path <{}>'.format(path))
    with (open(path, 'r')) as open_data:
        data = json.load(open_data)
        if not data['enable']:
            return None
        return data['data']

        
def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.abspath(
            os.getenv('USERPROFILE') + '/Documents').replace('\\', '/')
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents')

 
