NAME = 'reference usd'
ORDER = 5
VALID = True
TYPE = 'creator'
KEY = 'shader_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'to reference the shader usd scene'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'reference_usd.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    namespace = kwargs['caption'].encode()
    valid, value, message = maya_scene.reference_maya_scene(current_scene, namespace)
    return valid, [value], message
    
