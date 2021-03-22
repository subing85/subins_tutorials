import sys

from studio_usd_pipe import resource
from studio_usd_pipe.utils import maya_scene

from studio_usd_pipe.api import studioMaya
reload(studioMaya)


def get_pipe_ids(**kwargs):
    from maya import standalone
    standalone.initialize(name="python")
    from maya import OpenMaya    
    maya_file = sys.argv[1]
    smaya = studioMaya.Maya()
    smaya.open_maya(maya_file, None)
    data = maya_scene.get_scene_pipe_ids()
    returncode(data)  
    standalone.uninitialize(name='python')


def returncode(values):
    if isinstance(values, str):
        values = [values]
    print resource.getIdentityKey(), values
    return values


if __name__ == '__main__':
    get_pipe_ids()
