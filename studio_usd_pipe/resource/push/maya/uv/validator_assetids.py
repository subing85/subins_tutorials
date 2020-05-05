NAME = 'Validate UV Asset IDs Sets'
ORDER = 1
VALID = True
TYPE = 'validator'
KEY = 'uv_assetids'
OWNER = 'Subin Gopi'
COMMENTS = 'To check uv asset ids exists.'
VERSION = '0.0.0'
MODIFIED = 'April 19, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.removed_asset_ids()    
    return valid, values, message


def repair(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.update_asset_ids()
    if not valid:
        return valid, values, message
    return True, values, message
    
