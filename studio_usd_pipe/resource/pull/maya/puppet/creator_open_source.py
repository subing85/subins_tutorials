NAME = 'open source'
ORDER = 9
VALID = True
TYPE = 'creator'
KEY = 'source'
OWNER = 'Subin Gopi'
COMMENTS = 'To open the source the puppet scene'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'open_source.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY].encode()
    valid, value, message = maya_scene.open_maya_scene(current_scene)
    return valid, [value], message
    
