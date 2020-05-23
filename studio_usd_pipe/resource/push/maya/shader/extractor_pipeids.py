NAME = 'create shader pipe ids'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'shader_pipeids'
OWNER = 'Subin Gopi'
COMMENTS = 'To create shader pipe ids'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs):
    from studio_usd_pipe.utils import maya_asset
    valid, values = maya_asset.create_pipe_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

