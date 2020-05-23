NAME = 'Extract Model USD'
ORDER = 3
VALID = True
TYPE = 'extractor'
KEY = 'model_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'To create model usd file'
VERSION = '0.0.0'
MODIFIED = 'April 14, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    reload(maya_asset)
    output_usd = os.path.join(
        output_path,
        '{}.usd'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_usd, True)
    if not premission:
        return False, [output_usd], 'not able to save studio model!...' 
    model_usd = maya_asset.create_model_usd(output_usd)
    return True, [model_usd], 'success!...'
