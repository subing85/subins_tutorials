NAME = 'Extract studio uv'
ORDER = 2
VALID = True
TYPE = 'extractor'
KEY = 'studio_uv'
OWNER = 'Subin Gopi'
COMMENTS = 'To create studio uv (custom data) file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 19, 2020'


def execute(output_path=None, **kwargs):       
    import os
    from studio_usd_pipe.core import asset
    from studio_usd_pipe.core import common
    reload(asset)    
    reload(common)    
    
    output_uv = os.path.join(
        output_path,
        '{}.uv'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_uv, True)
    if not premission:
        return False, [output_uv], 'not able to save studio uv!...' 
    studio_uv = asset.create_studio_uv(output_uv)
    return True, [studio_uv], 'success!...'
    
