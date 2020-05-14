NAME = 'Extract UV Thumbnail'
ORDER = 1
VALID = True
TYPE = 'extractor'
KEY = 'uv_thumbnail'
OWNER = 'Subin Gopi'
COMMENTS = 'To create uv thumbnail file'
VERSION = '0.0.0'
MODIFIED = 'April 19, 2020'


def execute(output_path=None, **kwargs):
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset    
    if not os.path.isfile(kwargs['thumbnail']):
        return False, [kwargs['thumbnail']], 'not found input thumbnail!...'
    ouput_image_path = os.path.join(
        output_path,
        '{}.png'.format(kwargs['caption'])
        )
    premission = common.data_exists(ouput_image_path, True)
    if not premission:
        return False, [ouput_image_path], 'not able to save thumbnail!...'
    thumbnail = maya_asset.create_thumbnail(kwargs['thumbnail'], ouput_image_path)
    return True, [thumbnail], 'success!...'
