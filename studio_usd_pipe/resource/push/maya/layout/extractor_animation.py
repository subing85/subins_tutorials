NAME = 'extract studio animation'
ORDER = 1
VALID = True
TYPE = 'extractor'
KEY = 'studio_animation'
OWNER = 'Subin Gopi'
COMMENTS = 'to create layout studio animation'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_scene
    output_model = os.path.join(
        output_path,
        '{}.animation'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_model, True)
    if not premission:
        return False, [output_model], 'not able to save studio model!...' 
    studio_model = maya_scene.create_stuio_animation(output_model)
    return True, [studio_model], 'success!...'
    