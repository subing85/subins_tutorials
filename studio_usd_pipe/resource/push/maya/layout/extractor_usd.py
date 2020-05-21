NAME = 'extracte layout usd'
ORDER = 3
VALID = True
TYPE = 'extractor'
KEY = 'layout_usd'
OWNER = 'Subin Gopi'
COMMENTS = 'to create layout usd'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute(output_path=None, **kwargs):   
    from studio_usd_pipe.utils import maya_asset
    
    
    
    valid, values = maya_asset.create_pipe_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

