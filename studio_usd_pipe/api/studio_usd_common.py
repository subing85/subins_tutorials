from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade

source = '/venture/shows/my_hero/usd/asset.usd'
target = '/venture/shows/my_hero/usd/asset_03.usd'

stage_1 = Usd.Stage.Open(source)
stage_2 = Usd.Stage.Open(target)

for each in stage_1.Traverse():    
    c = stage_2.GetPrimAtPath(each.GetPath())
    if c:
        continue
    print c