NAME = 'Validate UV Sets'
ORDER = 2
VALID = True
TYPE = 'validator'
KEY = 'uv_sets'
OWNER = 'Subin Gopi'
COMMENTS = 'To check all the geometry contain valid uv sets.'
VERSION = '0.0.0'
MODIFIED = 'April 19, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.validate_uv_sets()    
    return valid, values, message


def repair(**kwargs):
    return False, [None], 'try to fix the uv sets'
    
