NAME = 'Extract studio shader'
ORDER = 3
VALID = True
TYPE = 'extractor'
KEY = 'studio_shader'
OWNER = 'Subin Gopi'
COMMENTS = 'To create studio shader (custom data) file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs):  
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    output_shader = os.path.join(
        output_path,
        '{}.shader'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_shader, True)
    if not premission:
        return False, [output_shader], 'not able to save studio shader!...' 
    studio_shader = maya_asset.create_studio_shader(output_shader)
    return True, [studio_shader], 'success!...'

    
