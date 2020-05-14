NAME = 'create asset usd composition'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'usd_asset_composition'
OWNER = 'Subin Gopi'
COMMENTS = 'to create asset usd composition'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'


def execute(output_path=None, **kwargs):   
    from studio_usd_pipe.utils import maya_asset
    valid, values = True, ['aaaaaaaaaaaaaaaa', 'bbbbbbbbb']
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

