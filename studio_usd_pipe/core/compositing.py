from pxr import Usd
from pxr import Sdf
from pxr import UsdGeom



def asset_sublayer():
    pass


def asset_reference(path, tag, components):
    layer = Sdf.Layer.CreateNew(path, args={'format': 'usda'})
    stage = Usd.Stage.Open(layer)
    location = '/Asset/{}'.format(tag)
    for usd in components:
        prim = stage.DefinePrim(location, 'Xform')
        prim.GetReferences().AddReference(usd)
    stage.GetRootLayer().Save()
    return path