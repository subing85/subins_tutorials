NAME = 'extract layout pipe IDs'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'layout_pipeids'
OWNER = 'Subin Gopi'
COMMENTS = 'to create layout pipe ids'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute(output_path=None, **kwargs):   
    from studio_usd_pipe.utils import maya_scene
    valid, values = maya_scene.update_pipe_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

