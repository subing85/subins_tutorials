NAME = 'Create UV Asset IDs'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'uv_assetids'
OWNER = 'Subin Gopi'
COMMENTS = 'To create uv asset ids'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 19, 2020'


def execute(output_path=None, **kwargs):   
    from studio_usd_pipe.core import asset
    reload(asset)

    valid, values = asset.create_maya_ids(**kwargs)
    if not valid:
        return valid, values, 'not found attributes!...'
    return True, values, 'success!...'

