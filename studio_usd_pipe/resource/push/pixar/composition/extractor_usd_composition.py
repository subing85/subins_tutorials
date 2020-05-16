NAME = 'create asset usd composition'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'usd_asset_composition'
OWNER = 'Subin Gopi'
COMMENTS = 'to create asset composition usd'
VERSION = '0.0.0'
MODIFIED = 'May 16, 2020'


def execute(output_path=None, **kwargs):
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset
    output_composition_usd = os.path.join(
        output_path,
        '{}.usda'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_composition_usd, True)
    if not premission:
        return False, [output_composition_usd], 'not able to save studio model!...' 
    maya_scene = maya_asset.create_asset_composition_usd(
        kwargs['composition'], output_composition_usd)
    return True, [maya_scene], 'success!...'








