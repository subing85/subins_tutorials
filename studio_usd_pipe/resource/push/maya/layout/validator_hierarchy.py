NAME = 'validate layout scene hierarchy'
ORDER = 0
VALID = True
TYPE = 'validator'
KEY = 'layout_hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'to check the layout hierarchy'
VERSION = '0.0.0'
MODIFIED = 'May 21, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_scene
    reload(maya_scene)
    valid, values, message = maya_scene.check_shot_hierarchy(kwargs['subfield'])
    return valid, values, message


def repair(**kwargs):
    from studio_usd_pipe.utils import maya_scene
    valid, values, message = maya_scene.create_shot(**kwargs)
    return valid, values, message    
