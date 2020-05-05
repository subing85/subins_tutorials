NAME = 'Validate Model Scene Hierarchy'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'model_hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'To check the model hierarchy'
VERSION = '0.0.0'
MODIFIED = 'April 14, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset
    valid, values, message = maya_asset.check_model_hierarchy()
    return valid, values, message


def repair(**kwargs):
    from studio_usd_pipe.utils import maya_asset
    valid, values, message = maya_asset.create_model()
    return valid, values, message    
