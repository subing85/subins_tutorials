# make composition [model + shader]

import os
from pxr import Usd
from pxr import Sdf

dirname = '/venture/shows/katana_tutorials/dumps/shader/'
asset_name = 'batman'
comp_usd =  os.path.join(dirname, 'comp1.usd')

layer, comp_stage = None, None 
layer = Sdf.Layer.CreateNew(comp_usd, args={'format': 'usda'})
comp_stage = Usd.Stage.Open(layer)

path = '/root/world/character/batman'

comp_prim = comp_stage.DefinePrim(path)

# model
model_path = os.path.join(dirname, asset_name, 'model.usd')
model_reference = comp_prim.GetReferences()
model_reference.AddReference(model_path)

# shader
shader_prim = comp_stage.GetPrimAtPath('/root')
shader_path = os.path.join(dirname, asset_name, 'shader.usd')
shader_reference = shader_prim.GetReferences()
shader_reference.AddReference(shader_path)

comp_stage.GetRootLayer().Save()
print comp_stage.GetRootLayer().ExportToString()
