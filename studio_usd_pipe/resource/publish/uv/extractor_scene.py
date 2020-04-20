NAME = 'Extract Maya Ascii'
ORDER = 4
VALID = True
TYPE = 'extractor'
KEY = 'maya_uv_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To create uv maya ascii file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 19, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import asset
    from studio_usd_pipe.core import common
    reload(asset)    
    reload(common)    
    
    output_maya_scene = os.path.join(
        output_path,
        '{}.ma'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_maya_scene, True)
    if not premission:
        return False, [output_maya_scene], 'not able to save studio model!...' 
    maya_scene = asset.create_maya_scene(output_maya_scene)
    return True, [maya_scene], 'success!...'
