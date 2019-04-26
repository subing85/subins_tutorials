import os

from smartDeformer_maya2019.utils import platforms

CURRENT_PATH = os.path.dirname(__file__)
MODULE = platforms.get_tool_kit()[0]


def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs', '{}.json'.format(module))


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getWeightsPath():
    return os.path.join(getWorkspacePath(), 'weights')


def getWorkspacePath():
    return os.path.join(os.getenv('HOME'), 'Documents', MODULE)


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')


def getResourceTypes():
    data = {'weights': getWeightsPath()}
    return data

def getToolKitLink():
    return 'https://www.subins-toolkits.com/'


def getToolKitHelpLink():
    return 'https://vimeo.com/user55256190'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/smart-deformer'

# end ####################################################################
