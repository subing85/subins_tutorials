
import os
import json
import platform

from datetime import datetime


CURRENT_PATH = os.path.dirname(__file__)


def getInputPath(): #**
    return os.path.join(CURRENT_PATH, 'inputs')


def getInputData(path): #**
    if not path:
        raise IOError('not found path <{}>'.format(path))
    with (open(path, 'r')) as open_data:
        data = json.load(open_data)
        if not data['enable']:
            return None
        return data['data']


def getData(path): #**
    if not path:
        raise IOError('not found path <{}>'.format(path))
    with open(path, 'r') as file:
        data = file.read()
        return data

    
def getPresetFormat(): #**
    return '.preset'


def getIconPath(): #**
    return os.path.join(CURRENT_PATH, 'icons')


def getPackagePath(): #**   
    if 'PACKAGE_PATH' in os.environ:
        return os.environ['PACKAGE_PATH']
    path = os.path.dirname(os.path.dirname(CURRENT_PATH))
    return path


def getPackageName(): #**
    if 'PACKAGE_NAME' in os.environ:
        return os.environ['PACKAGE_NAME']
    name = os.path.basename(os.path.dirname(CURRENT_PATH))
    return name


def getShowConfigureData(): #**
    path = os.path.join(getInputPath(), 'show.json')
    data = getInputData(path)
    return data


def getApplicationsPath(application_type): #**
    path = os.path.join(getPackagePath(), getPackageName(), 'bin', application_type)
    return path


def getIdentityKey(): #**
    return '##..##'


def getMayaToolKitPath(): #**
    return os.path.join(CURRENT_PATH, 'toolkit/maya')



def getPipeData(): #**
    path = os.path.join(getInputPath(), 'pipe.json')
    data = getInputData(path)
    return data


def getMayaFileTypes(): #**
    file_types = {
        '.ma': 'mayaAscii',
        '.mb': 'mayaBinary'
        }
    return file_types


def getMayaFormats(): #**
    return '(*.ma *.mb)'

def getImageFormats(): #**
    return '(*.bmp *.jpg *.jpeg *.png *.ppm *.tiff *.xbn *.xpm)'


def getCurrentDateKey(): #**
    date = datetime.now().strftime("%Y_%d_%B_%A_%I_%M_%S_%p")
    return  date 

def getCurrentDate(): #***************************************
    date = datetime.now().strftime("%Y %d %B %A, %I:%M:%S %p")    
    return  date 


def getMayapy(maya_path): #**    
    path = os.path.join(maya_path, 'bin/mayapy')
    return path

                
def getBrowsPath(): #**
    if 'BROWS_PATH' in os.environ:
        return os.environ['BROWS_PATH']
    if 'SHOW_PATH' in os.environ:
        return os.environ['SHOW_PATH']
    return getPackagePath()


def getSpecificPreset(dirname, preset): #**
    preset_path = os.path.join(dirname, 'presets', '%s.json'%preset)
    return preset_path  


def getModulePath():
    path = os.path.join(getPackagePath(), getPackageName(), 'module')
    return path

def getModuleApplicationsPath():
    path = os.path.join(getModulePath(), 'applications')
    return path
    


def getTemplatePath():    
    path = os.path.join(getPackagePath(), getPackageName(), 'template')
    return path


def getApplicationTemplatePath(): 
    template_path = getTemplatePath()
    path = os.path.join(template_path, 'application_template.txt')
    return path

def getStudioTemplatePath(): 
    template_path = getTemplatePath()
    path = os.path.join(template_path, 'studiopipe_template.txt')
    return path

def getStudioPipePath(): 
    bin_path = getBinPath()
    path = os.path.join(bin_path, 'pipe/studiopipe')
    return path


def getOperatingSystemBinPath():
    return '/usr/bin'    




def getPresetPath():
    package_path = getPackagePath()
    package_name = getPackageName()
    path = os.path.join(
        package_path, package_name, 'presets')    
    return path  


def getShowPresetPath():
    preset_path = getPresetPath()
    path = os.path.join(preset_path, 'shows')
    return path  


def getBinPath():
    package_path = getPackagePath()
    package_name = getPackageName()
    path = os.path.join(
        package_path, package_name, 'bin')
    return path  


def getBinApplicationPath(show, application):
    bin_path = getBinPath()
    path = os.path.join(bin_path, 'shows', show, application, 'main.sh')
    return path





def getPipeIDData(): #**
    path = os.path.join(getInputPath(), 'pipeid.json')
    data = getInputData(path)
    return data







def getScriptPath(): #**
    return os.path.join(CURRENT_PATH, 'scripts')




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




def getPluginData():  
    path = os.path.join(getInputPath(), 'plugins.json')
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
    

def getBundlePath(application, types, subfiled):
    path = os.path.join(CURRENT_PATH, types, application, subfiled)
    return path

