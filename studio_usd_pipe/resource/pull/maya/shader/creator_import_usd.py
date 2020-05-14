NAME = 'import usd'
ORDER = 4
VALID = True
TYPE = 'creator'
KEY = 'shader_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'to import the shader usd scene'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'import_usd.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    namespace = kwargs['caption'].encode()
    valid, value, message = maya_scene.import_maya_scene(current_scene, namespace)
    return valid, [value], message
    
