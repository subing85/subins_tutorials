NAME = 'Extract Model Thumbnail'
ORDER = 1
VALID = True
TYPE = 'extractor'
KEY = 'model_thumbnail'
OWNER = 'Subin Gopi'
COMMENTS = 'To create model thumbnail file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'


def execute(output_path=None, **kwargs):
    import os
    from studio_usd_pipe.core import asset
    from studio_usd_pipe.core import common
    reload(asset)    
    reload(common)
    
    if not os.path.isfile(kwargs['thumbnail']):
        return False, [kwargs['thumbnail']], 'not found input thumbnail!...'
     
    ouput_path = os.path.join(
        output_path,
        '{}.png'.format(kwargs['caption'])
        )
    premission = common.data_exists(ouput_path, True)
    if not premission:
        return False, [ouput_path], 'not able to save thumbnail!...'
    thumbnail = asset.create_thumbnail(kwargs['thumbnail'], ouput_path)
    thumbnail = kwargs['thumbnail']
    return True, [thumbnail], 'success!...'
