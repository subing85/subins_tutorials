NAME = 'Validate Scene Hierarchy'
ORDER = 1
VALID = True
TYPE = 'validator'
KEY = 'geometry'
OWNER = 'Subin Gopi'
COMMENTS = 'To check the hierarchy as per our workflow'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'


def execute(**kwargs):
     
    values = ['ball', 'bat']
    message = 'found in the scene'
    
    from maya import cmds    
    values = cmds.ls(type='mesh')    
    
    return True, values, message


def repair(**kwargs):
    values = ['ball', 'bat']
    message = 'not able to fix'
    return True, values, message
    
    
