import os
import getpass

CURRENT_PATH = os.path.dirname(__file__)
MODULE = 'smart_deformer'



def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs', '{}.json'.format(module))


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getWeightsPath():
    return os.path.join (getWorkspacePath(), 'weights')


def getWorkspacePath():
    return os.path.join (os.getenv('HOME'), 'Documents', MODULE)


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')

def getResourceTypes():
    data = {'weights': getWeightsPath()}
    
    return data

