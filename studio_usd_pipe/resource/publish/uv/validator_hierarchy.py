NAME = 'Validate UV Scene Hierarchy'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'uv_hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'To check the uv hierarchy'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 19, 2020'


def execute(**kwargs):
    from studio_usd_pipe.core import asset
    reload(asset)
    valid, values, message = asset.check_model_hierarchy()
    return valid, values, message


def repair(**kwargs):   
    return False, [None], 'try to set the same hierarchy of dependency model'
    
