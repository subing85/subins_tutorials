import json
import os
import sys

usd_dirname = '/usr/usd/maya2018/pixar/19.05/lib/python/'

if usd_dirname not in sys.path:
    sys.path.append(usd_dirname)

from studio_usd_pipe.core import common

from studio_usd_pipe.api import studioInputs

from pxr import Vt
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import Kind
from pxr import UsdGeom
from pxr import UsdShade


def find_asset_usd_inputs(input_data):
    if 'composition' not in input_data:
        return
    inputs = studioInputs.Inputs('assets', 'maya')
    usd_extractor_keys = inputs.get_usd_extractor_keys()
    subfields = inputs.find_subfileds()
    asset_usd_inputs = {}
    for index, subfield in enumerate(subfields):        
        if subfield not in input_data['composition']:
            continue
        asset_usd_inputs.setdefault(index, {subfield: {}})
        for version, version_contents in input_data['composition'][subfield].items():
            if usd_extractor_keys[subfield] not in version_contents:
                continue
            usd = version_contents[usd_extractor_keys[subfield]]
            if not usd:
                continue
            asset_usd_inputs[index][subfield].setdefault(version, usd[0])
    # print json.dumps(asset_usd_inputs, indent=4)
    return asset_usd_inputs


def create_stage(path):
    path = '%s.usd'%os.path.splitext(path)[0]
    layer = Sdf.Layer.CreateNew(path, args={'format': 'usda'})
    stage = Usd.Stage.Open(layer)
    return stage    


def create_asset_usd_composition(asset_usd_inputs):
    usd_path = '/venture/shows/batman/tmp/test_2.usda'
    stage = create_stage(usd_path)

    location = Sdf.Path('/{}'.format('asset'))
    prim = stage.DefinePrim(location, 'Xform')
    
    for index in asset_usd_inputs:
        for subfield, version_contents in asset_usd_inputs[index].items():
            if len(version_contents)<2:                
                if not version_contents.values():
                    continue
                add_reference(prim, version_contents.values())
            else:
                add_reference_variant(prim, subfield, version_contents)

    #===========================================================================
                    
    print stage.GetRootLayer().ExportToString()                    
    #stage.Save()      
    #print usd_path
    

def add_reference(prim, components):
    for component in components:
        references = prim.GetReferences()
        references.AddReference(component)

def add_reference_variant(prim, header, contents):    
    prim_path = prim.GetPrimPath()
    
    variant_set = prim.GetVariantSet(header)
    versions = common.set_version_order(contents.keys())
    for version in versions:
        asset_path = contents[version]
        version = version.replace('.', '-')
        variant_set.AddVariant(version)
        variant_set.SetVariantSelection(version)
        with variant_set.GetVariantEditContext():
            referencs = prim.GetReferences()
            referencs.AddReference(assetPath=asset_path, primPath=prim_path)        

    
    return




    


path = '/venture/source_code/subins_tutorials/studio_usd_pipe/tmp/usd_comp.json'

input_data  = common.read_json(path)
asset_usd_inputs = find_asset_usd_inputs(input_data)
create_asset_usd_composition(asset_usd_inputs)
# print json.dumps(asset_usd_inputs, indent=4)

 
