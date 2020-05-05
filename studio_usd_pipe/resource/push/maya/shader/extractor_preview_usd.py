NAME = 'extract shader preview usd'
ORDER = 5
VALID = True
TYPE = 'extractor'
KEY = 'shader_preview_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'to create shader preview usd file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs): 
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    output_usd = os.path.join(
        output_path,
        '{}_preview.usd'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_usd, True)
    if not premission:
        return False, [output_usd], 'not able to save studio model!...' 
    shader_preview_usd = maya_asset.create_shader_usd(output_usd)
    return True, [shader_preview_usd], 'success!...'
