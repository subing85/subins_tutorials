import os

CURRENT_PATH = os.path.dirname(__file__)


def getInputPath(input):
    return os.path.join(CURRENT_PATH, input)

def getSkeleonPath():
    return getInputPath('skeletons')