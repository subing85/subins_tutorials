NAME = 'open usd'
ORDER = 3
VALID = True
TYPE = 'creator'
KEY = 'model_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'To open the model usd scene'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'open_usd.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    valid, value, message = maya_scene.open_maya_scene(current_scene)
    return valid, [value], message
    
