import os
import logging

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


def getPublishTypes():
    data = [
        'skeleton',
        'puppet',
        'scene']
    return data

def getPublishResource(type=None):    
    path = os.path.join(CURRENT_PATH, 'publish')
    if type:
        path = os.path.join(CURRENT_PATH, 'publish', type)
    if not os.path.isdir(path):
        logging.warning('not found such path called \"%s\"'%path)
        return    
    return path


def getCreateResource(type=None):    
    path = os.path.join(CURRENT_PATH, 'create')
    if type:
        path = os.path.join(CURRENT_PATH, 'create', type)
    if not os.path.isdir(path):
        logging.warning('not found such path called \"%s\"'%path)
        return    
    return path


def getPublishDirectory():    
    # return os.path.join(CURRENT_PATH, 'show') 
    return '/home/shreya/Documents/subin_crowd'

def getDatabaseDirectory():
    return 'crowd', '/home/shreya/Documents/subin_crowd/database'
        
                  
        
        
    
        
        
            
        
    