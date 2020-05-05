NAME = 'open maya'
ORDER = 0
VALID = True
TYPE = 'creator'
KEY = 'model_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To open the maya model scene'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'open_maya.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    valid, value, message = maya_scene.open_maya_scene(current_scene)
    return valid, [value], message
    
