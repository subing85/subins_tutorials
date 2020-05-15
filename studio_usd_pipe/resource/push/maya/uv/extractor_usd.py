NAME = 'Extract UV USD'
ORDER = 3
VALID = True
TYPE = 'extractor'
KEY = 'uv_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'To create uv usd file'
VERSION = '0.0.0'
MODIFIED = 'April 19, 2020'


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
        return False, [output_usd], 'not able to save studio uv!...' 
    uv_usd = maya_asset.create_uv_usd(output_usd)
    return True, [uv_usd], 'success!...'
    
