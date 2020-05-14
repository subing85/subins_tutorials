import sys

from studio_usd_pipe import resource
from studio_usd_pipe.core import asset

from studio_usd_pipe.api import studioMaya
reload(studioMaya)


def get_asset_ids(**kwargs):
    from maya import standalone
    standalone.initialize(name="python")
    from maya import OpenMaya    
    maya_file = sys.argv[1]
    smaya = studioMaya.Maya()
    smaya.open_maya(maya_file, None)
    root = asset.get_root()    
    mobject = smaya.get_mobject(root)
    data = smaya.get_maya_id_data(mobject, id_data=None)
    returncode(data)  
    standalone.uninitialize(name='python')


def returncode(values):
    if isinstance(values, str):
        values = [values]
    print resource.getIdentityKey(), values
    return values


if __name__ == '__main__':
    get_asset_ids()
