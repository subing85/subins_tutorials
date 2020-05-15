NAME = 'Extract studio model'
ORDER = 2
VALID = True
TYPE = 'extractor'
KEY = 'studio_model'
OWNER = 'Subin Gopi'
COMMENTS = 'To create studio model (custom data) file'
VERSION = '0.0.0'
MODIFIED = 'April 14, 2020'


def execute(output_path=None, **kwargs):       
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    output_model = os.path.join(
        output_path,
        '{}.model'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_model, True)
    if not premission:
        return False, [output_model], 'not able to save studio model!...' 
    studio_model = maya_asset.create_studio_model(output_model)
    return True, [studio_model], 'success!...'
    
