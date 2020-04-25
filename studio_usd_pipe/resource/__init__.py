
import os
import json
import platform

CURRENT_PATH = os.path.dirname(__file__)


def getInputData(path):
    if not path:
        raise IOError('not found path <{}>'.format(path))
    with (open(path, 'r')) as open_data:
        data = json.load(open_data)
        if not data['enable']:
            return None
        return data['data']
    
def getData(path):
    if not path:
        raise IOError('not found path <{}>'.format(path))
    with open(path, 'r') as file:
        data = file.read()
        return data
    
def getPresetFormat():
    return '.preset'
        
    
def getShowConfigureData():
    path = os.path.join(getInputPath(), 'show.json')
    data = getInputData(path)
    return data

def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getPackagePath():    
    if 'PACKAGE_PATH' in os.environ:
        return os.environ['PACKAGE_PATH']
    path = os.path.dirname(os.path.dirname(CURRENT_PATH))
    return path


def getPackageName():
    if 'PACKAGE_NAME' in os.environ:
        return os.environ['PACKAGE_NAME']
    name = os.path.basename(os.path.dirname(CURRENT_PATH))
    return name


def getTemplatePath():    
    path = os.path.join(getPackagePath(), getPackageName(), 'template')
    return path


def getBrowsPath():
    if 'BROWS_PATH' in os.environ:
        return os.environ['BROWS_PATH']        
    return getPackagePath()


def getIdentityKey():
    return '##..##'





def getInputPath():
    return os.path.join(CURRENT_PATH, 'inputs')


def getScriptPath():
    return os.path.join(CURRENT_PATH, 'scripts')


def getToolKitPath():
    return os.path.join(CURRENT_PATH, 'toolkit')


def getHeaderData():
    path = os.path.join(getInputPath(), 'header.json')
    data = getInputData(path)
    return data



def getStudioData():
    path = os.path.join(getInputPath(), 'studio.json')
    data = getInputData(path)
    return data











def getPreferenceFormat():  # to remove  
    return '.pref'


def getPreferenceData(path=None):  # to remove  
    if not path:
        path = os.path.join(getInputPath(), 'preferences.json')
    data = getInputData(path)
    return data


def getPipeData():
    path = os.path.join(getInputPath(), 'pipe.json')
    data = getInputData(path)
    return data


def getPluginData():  
    path = os.path.join(getInputPath(), 'plugins.json')
    data = getInputData(path)
    return data


def getAssetIDData():
    path = os.path.join(getInputPath(), 'assetid.json')
    data = getInputData(path)
    return data

        
def getWroldData():
    path = os.path.join(getInputPath(), 'world.json')
    data = getInputData(path)
    return data


def getNodeData():
    path = os.path.join(getInputPath(), 'nodes.json')
    data = getInputData(path)
    return data

        


        
def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.abspath(
            os.getenv('USERPROFILE') + '/Documents').replace('\\', '/')
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents')
    

def getPublishBundlePath(mode):
    path = os.path.join(CURRENT_PATH, 'publish', mode)
    return path

