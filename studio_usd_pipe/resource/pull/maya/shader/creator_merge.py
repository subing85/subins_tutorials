NAME = 'merge'
ORDER = 10
VALID = True
TYPE = 'creator'
KEY = 'studio_shader'
OWNER = 'Subin Gopi'
COMMENTS = 'to merge the studio shader'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'merge_studio_shader.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    studio_model = kwargs[KEY][0].encode()
    valid, value, message = maya_scene.merge_studio_shader(studio_model)
    return valid, [value], message
    
    
    
