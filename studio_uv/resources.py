import os

CURRENT_PATH = os.path.dirname(__file__)


def getToolKitPath():
    path = os.path.join(CURRENT_PATH, 'toolkit')
    return path
