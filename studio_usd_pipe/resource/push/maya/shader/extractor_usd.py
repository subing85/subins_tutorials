NAME = 'extract shader usd'
ORDER = 4
VALID = True
TYPE = 'extractor'
KEY = 'shader_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'to create shader usd file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs): 
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    output_usd = os.path.join(
        output_path,
        '{}.usd'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_usd, True)
    if not premission:
        return False, [output_usd], 'not able to save studio model!...' 
    shader_usd = maya_asset.create_shader_usd(output_usd)
    return True, [shader_usd], 'success!...'
