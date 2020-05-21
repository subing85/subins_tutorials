NAME = 'Create shot hierarchy'
ORDER = 1
VALID = True
TYPE = 'creator'
KEY = 'layout_hierarchy'
OWNER = 'Subin Gopi'
COMMENTS = 'To create layout hierarchy'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'
ICON = 'layout_hierarchy.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    reload(maya_scene)
    valid, values, message = maya_scene.create_shot(kwargs)
    return valid, values, message      
    
    
