NAME = 'validate shader asset ids'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'shader_assetids'
OWNER = 'Subin Gopi'
COMMENTS = 'to check shader asset ids exists.'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.removed_pipe_ids()    
    return valid, values, message


def repair(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.update_pipe_ids()
    if not valid:
        return valid, values, message
    return True, values, message
    
