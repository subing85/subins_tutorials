NAME = 'reference maya'
ORDER = 2
VALID = True
TYPE = 'creator'
KEY = 'shader_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To reference the maya shader scene'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'reference_maya.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    namespace = kwargs['caption'].encode()
    valid, value, message = maya_scene.reference_maya_scene(current_scene, namespace)
    return valid, [value], message
    
