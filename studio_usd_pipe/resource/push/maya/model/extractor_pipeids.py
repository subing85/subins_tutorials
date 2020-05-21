NAME = 'create model pipe ids'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'model_pipeids'
OWNER = 'Subin Gopi'
COMMENTS = 'To create model pipe ids'
VERSION = '0.0.0'
MODIFIED = 'April 19, 2020'


def execute(output_path=None, **kwargs):   
    from studio_usd_pipe.utils import maya_asset
    valid, values = maya_asset.create_pipe_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

