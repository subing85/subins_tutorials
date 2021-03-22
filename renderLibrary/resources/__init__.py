import os

CURRENT_PATH = os.path.dirname(__file__)


def getActionPath(typed):
    path = os.path.join(CURRENT_PATH, typed)
    return path
    
