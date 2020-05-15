import os
import tempfile
import platform

CURRENT_PATH = os.path.dirname(__file__)


def getToolKit():
    return 'Studio Maya Interpreter', 'smi', '0.0.1'


def getModuleName():
    return 'studio_maya'


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getLogo():
    return os.path.join(CURRENT_PATH, 'icons', 'logo.png')


def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.join(
            os.getenv('USERPROFILE'), 'Documents', 'studio_toolkits', getModuleName())
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents', 'studio_toolkits', getModuleName())


def getPreferenceFile():
    preference_path = os.path.join(getWorkspacePath(), 'preference')
    if not os.path.isdir(preference_path):
        os.makedirs(preference_path)
    return os.path.join(preference_path, 'config.xml')


def getOperatingSystem():
    return platform.system()


def getRootPath():
    operating_system = getOperatingSystem()
    if operating_system == 'Windows':
        return 'C:/', 'Autodesk/Maya', 'mayapy.exe'
    if operating_system == 'Linux':
        return '/', 'autodesk/maya', 'mayapy'


def getEditor():
    operating_system = getOperatingSystem()
    if operating_system == 'Windows':
        return 'start wordpad'
    if operating_system == 'Linux':
        return 'kwrite'


def getFormats():
    formats = {
        'maya': ['.ma', '.mb'],
        'code': ['.py', '.pyc', '.mel']
    }
    return formats


def getImages():
    images = {
        '.ma': 'maya_ascii',
        '.mb': 'maya_binary',
        '.py': 'python',
        '.pyc': 'Python_compile',
        '.mel': 'mel'
    }
    return images


def getTempCodeFile():
    return os.path.join(tempfile.gettempdir(), 'studio_maya_temp.py')


def getInputPath():
    path = os.path.join(CURRENT_PATH, 'inputs').replace('\\', '/')
    return path


def getScriptPath():
    path = os.path.join(CURRENT_PATH, 'scripts')
    return path


def getToolKitLink():
    return 'https://www.subins-toolkits.com'


def getToolKitHelpLink():
    return 'https://www.subins-toolkits.com/studio-maya'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/studio-maya'
