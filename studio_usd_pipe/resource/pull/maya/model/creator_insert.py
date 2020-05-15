NAME = 'insert'
ORDER = 6
VALID = True
TYPE = 'creator'
KEY = 'studio_model'
OWNER = 'Subin Gopi'
COMMENTS = 'To insert the studio model'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'insert_studio_model.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    studio_model = kwargs[KEY][0].encode()
    valid, value, message = maya_scene.insert_studio_model(studio_model)
    return valid, [value], message
    
    
