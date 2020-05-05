NAME = 'validate source image'
ORDER = 3
VALID = True
TYPE = 'validator'
KEY = 'shader_source_image'
OWNER = 'Subin Gopi'
COMMENTS = 'to check source images are exist'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values = maya_asset.check_source_images()
    
    if not valid:
        return valid, values, 'not found such source images'
    return valid, values, 'valid source images'
    


def repair(**kwargs):   
    return False, [None], 'try to setup the source images'
    
