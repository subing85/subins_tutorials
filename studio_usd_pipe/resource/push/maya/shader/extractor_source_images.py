NAME = 'extract shader source images'
ORDER = 2
VALID = True
TYPE = 'extractor'
KEY = 'shader_source_images'
OWNER = 'Subin Gopi'
COMMENTS = 'to create shader source images file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'

def execute(output_path=None, **kwargs):
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    source_images = maya_asset.create_shader_source_images(
        kwargs['caption'], output_path, kwargs['location'])
    return True, [source_images], 'success!...'

    
 
