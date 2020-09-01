NAME = 'extracte layout shot'
ORDER = 1
VALID = True
TYPE = 'extractor'
KEY = 'layout_shot'
OWNER = 'Subin Gopi'
COMMENTS = 'to create layout shot'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_scene
    output_shot = os.path.join(
        output_path,
        '{}.shot'.format(kwargs['caption'])
        )
    print output_shot
    premission = common.data_exists(output_shot, True)
    if not premission:
        return False, [output_shot], 'not able to save studio model!...' 
    studio_shot= maya_scene.create_studio_shot(output_shot)
    return True, [studio_shot], 'success!...'
    