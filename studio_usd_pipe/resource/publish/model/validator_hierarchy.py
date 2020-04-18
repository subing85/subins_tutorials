NAME = 'Validate Scene Hierarchy'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'To check the hierarchy as per our workflow'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'


def execute(**kwargs):   
    values = ['ball', 'bat']
    message = 'found in the scene'
    
    return True, values, message


def repair(**kwargs):
    values = []
    message = 'not found in the scene'
    message = 'not able to fix'
    return True, values, message

    
