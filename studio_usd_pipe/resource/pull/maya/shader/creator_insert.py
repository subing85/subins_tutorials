NAME = 'insert'
ORDER = 9
VALID = True
TYPE = 'creator'
KEY = 'studio_shader'
OWNER = 'Subin Gopi'
COMMENTS = 'to insert the studio shader'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'insert_studio_shader.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    studio_model = kwargs[KEY][0].encode()
    valid, value, message = maya_scene.insert_studio_shader(studio_model)
    return valid, [value], message
    
    
