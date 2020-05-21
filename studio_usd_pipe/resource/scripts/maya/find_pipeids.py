import sys

from studio_usd_pipe import resource
from studio_usd_pipe.utils import maya_asset


def get_pipe_ids(**kwargs):
    from maya import standalone
    standalone.initialize(name="python")
    from maya import OpenMaya    
    maya_file = sys.argv[1]
    data = maya_asset.get_pipe_ids()
    returncode(data)  
    standalone.uninitialize(name='python')


def returncode(values):
    if isinstance(values, str):
        values = [values]
    print resource.getIdentityKey(), values
    return values


if __name__ == '__main__':
    get_asset_ids()
