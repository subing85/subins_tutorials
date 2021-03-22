NAME = 'extract studio animation'
ORDER = 2
VALID = True
TYPE = 'extractor'
KEY = 'studio_animation'
OWNER = 'Subin Gopi'
COMMENTS = 'to create layout studio animation'
VERSION = '0.0.0'
MODIFIED = 'May 20, 2020'


def execute(output_path=None, **kwargs):   
    import os
    from studio_usd_pipe.core import common
    from studio_usd_pipe.utils import maya_scene
    studio_animations = maya_scene.create_stuio_animation(output_path)
    return True, studio_animations, 'success!...'
    