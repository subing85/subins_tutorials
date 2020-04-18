
import os
import json
import platform


CURRENT_PATH = os.path.dirname(__file__)


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getInputPath():
    return os.path.join(CURRENT_PATH, 'inputs')


def getToolKitPath():
    return os.path.join(CURRENT_PATH, 'toolkit')


def getPreferenceFormat():    
    return '.pref'


def getPreferenceData(path=None):  
    if not path:
        path = os.path.join(getInputPath(), 'preferences.json')
    data = get_input_data(path)
    return data


def getPipeData():
    path = os.path.join(getInputPath(), 'pipe.json')
    data = get_input_data(path)
    return data


def getStudioData():
    path = os.path.join(getInputPath(), 'studio.json')
    data = get_input_data(path)
    return data

def getPluginData(path=None):  
    if not path:
        path = os.path.join(getInputPath(), 'plugins.json')
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


def getNodeData():
    path = os.path.join(getInputPath(), 'nodes.json')
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
    

def getPublishBundlePath(mode):
    path = os.path.join(CURRENT_PATH, 'publish', mode)
    return path
    

 
