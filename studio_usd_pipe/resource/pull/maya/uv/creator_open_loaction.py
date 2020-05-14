NAME = 'open location'
ORDER = 2
VALID = True
TYPE = 'creator'
KEY = 'location'
OWNER = 'Subin Gopi'
COMMENTS = 'To open the model location'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'open_location.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_dirname = kwargs[KEY].encode()    
    valid, value, message = maya_scene.open_location(current_dirname)
    return valid, [value], message
    
