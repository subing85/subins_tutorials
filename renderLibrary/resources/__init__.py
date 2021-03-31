import os
import json

CURRENT_PATH = os.path.dirname(__file__)


def getInputsPath():
    path = os.path.join(CURRENT_PATH, 'inputs')
    return path


def getEnginePath():
    path = os.path.join(CURRENT_PATH, 'engine')
    return path


def getActionPath(typed):
    path = os.path.join(CURRENT_PATH, typed)
    return path


def getInputData(typed):
    inputpath = getInputsPath()
    path = os.path.join(inputpath, '%s.json' % typed)
    input_data = getData(path)
    return input_data


def getEngineData(engine):
    enginepath = getEnginePath()  
    path = os.path.join(enginepath, '%s.json' % engine)
    
    print path, '\n'
    engine_data = getData(path)
    return engine_data
    
    
def getData(path):
    if not os.path.isfile(path):
        raise IOError('not found path <{}>'.format(path))
    with (open(path, 'r')) as open_data:
        data = json.load(open_data)
        if not data.get('valid'):
            return None
        return data['data']        
    
