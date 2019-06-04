import os

CURRENT_PATH = os.path.dirname(__file__)


def getInputPath(input):
    return os.path.join(CURRENT_PATH, input)

def getSkeleonPath():
    return getInputPath('skeletons')


def getToolKitLink():
    return 'https://www.subins-toolkits.com/'


def getToolKitHelpLink():
    return 'https://vimeo.com/user55256190'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/subin-crowds'