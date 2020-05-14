NAME = 'extract shader maya ascii'
ORDER = 6
VALID = True
TYPE = 'extractor'
KEY = 'shader_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To create shader maya ascii file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset    
    output_shader_scene = os.path.join(
        output_path,
        '{}.ma'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_shader_scene, True)
    if not premission:
        return False, [output_shader_scene], 'not able to save studio model!...' 
    shader_scene = maya_asset.create_shader_maya(output_shader_scene)
    return True, [shader_scene], 'success!...'
