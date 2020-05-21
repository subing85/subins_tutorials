NAME = 'pipe ids'
ORDER = 2
VALID = True
TYPE = 'creator'
KEY = 'layout_pipeids'
OWNER = 'Subin Gopi'
COMMENTS = 'To create model pipe(shot) ids'
VERSION = '0.0.0'
MODIFIED = 'May 19, 2020'
ICON = 'layout_pipeids.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    valid, values = maya_scene.create_pipe_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'
            
    
