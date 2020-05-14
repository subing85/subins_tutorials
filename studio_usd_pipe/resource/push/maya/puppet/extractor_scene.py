NAME = 'extract puppet maya ascii'
ORDER = 5
VALID = True
TYPE = 'extractor'
KEY = 'puppet_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To create puppet maya ascii file'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_asset    
    output_puppet_scene = os.path.join(
        output_path,
        '{}.ma'.format(kwargs['caption'])
        )
    premission = common.data_exists(output_puppet_scene, True)
    if not premission:
        return False, [output_puppet_scene], 'not able to save studio model!...' 
    puppet_scene = maya_asset.create_puppet_maya(output_puppet_scene)
    return True, [puppet_scene], 'success!...'
