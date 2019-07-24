# Load (import) uv custom data format

import os
import tempfile
import json

from maya.api import OpenMaya

# Source data path
file_path = os.path.join(
    tempfile.gettempdir(), 'head_test_uvs.uv')

# Read uv custom data
file = open(file_path, 'r')
data = json.load(file)
file.close()

# Store shape node name to variable from custom data
shape_node = data['shape_node']

# Shape node to MDagPath
mselection = OpenMaya.MSelectionList()
mselection.add(shape_node)
mdag_path = mselection.getDagPath(0)

# Shape node MDagPath to MFnMesh
mfn_mesh = OpenMaya.MFnMesh(mdag_path)

# Remove exists uv set from shape node
exists_set_names = mfn_mesh.getUVSetNames()
for index, set_name in enumerate(exists_set_names):
    if index>0:
        mfn_mesh.deleteUVSet(set_name)
        print 'removed set\t', '<', set_name, '>'
        
# Store uv information to variable
uv_sets = data['uv_sets']

# Sort the uv set order
sorted_index = sorted(uv_sets.keys())

for index in sorted_index:
    content = uv_sets[index]    
    set_name = content['set_name']
    u_values = content['u_values']
    v_values = content['v_values']
    uv_numbers = content['uv_numbers']
    uv_ids = content['uv_ids']
    
    if int(index)==0:
        # get default set name
        new_set_name = set_name      
        # print 'default set', set_name, index
    else:
        # create new set name
        new_set_name = mfn_mesh.createUVSet(set_name)
        # print 'new set', set_name, index

    # Set u and v values
    mfn_mesh.setUVs(u_values, v_values, new_set_name)
    
    # Set uv coordinate to mesh's face vertices
    mfn_mesh.assignUVs(uv_numbers, uv_ids, new_set_name)

# Redrawn the shape node
mfn_mesh.updateSurface()

OpenMaya.MGlobal.displayInfo('UV Import Success!...')
        
