NAME = 'Validate Model Scene Hierarchy'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'model_hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'To check the model hierarchy'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'


def execute(**kwargs):
    from studio_usd_pipe.core import asset
    reload(asset)
    valid, values, message = asset.check_model_hierarchy()
    return valid, values, message


def repair(**kwargs):
    from studio_usd_pipe.core import asset
    reload(asset)
    valid, values, message = asset.create_model()
    return True, values, message    
