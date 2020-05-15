import os

from shaderLibrary_maya2017.utils import platforms

CURRENT_PATH = os.path.dirname(__file__)
MODULE = platforms.get_tool_kit()[0]


def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs', '{}.json'.format(module))


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getPreferencePath():
    return os.path.join(getWorkspacePath(), 'preference')


def getWorkspacePath():
    return os.path.join(os.getenv('HOME'), 'Documents', MODULE)


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')


def getResourceTypes():
    data = {'preference': getPreferencePath(
    ), 'shader': getWorkspacePath(), 'generic': None}
    return data


def getToolKitLink():
    return 'https://www.subins-toolkits.com'


def getToolKitHelpLink():
    return 'https://vimeo.com/314966208'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/shader-library'

# end ####################################################################
