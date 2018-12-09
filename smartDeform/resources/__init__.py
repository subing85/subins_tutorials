import os
import getpass

CURRENT_PATH = os.path.dirname(__file__)


def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs', '{}.json'.format(module))


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')