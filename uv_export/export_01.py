# Read and Write (export) UVs to custom data format

import os
import tempfile
import json

from maya.api import OpenMaya

# Input - store polygon shape node to variable
shape_node = 'polySurfaceShape2'

# Input polygon shape to MDagPath
mselection = OpenMaya.MSelectionList()
mselection.add(shape_node)
mdag_path = mselection.getDagPath(0)

# Polygon shape MDagPath to MFnMesh
mfn_mesh = OpenMaya.MFnMesh(mdag_path)

# get the all uv set names from polygon shape
set_names = mfn_mesh.getUVSetNames()

uv_data = {}
for index, set_name in enumerate(set_names):
    # get u and v values
    u_values, v_values = mfn_mesh.getUVs(set_name)
    
    # get number of uvs assigned to each face of the mesh 
    # get face vertices uv ids
    uv_numbers, uv_ids = mfn_mesh.getAssignedUVs(set_name) 
    
    # store uv values to dictionary variable
    current_set = {
        'set_name': set_name.encode(),
        'u_values': list(u_values),
        'v_values': list(v_values),
        'uv_numbers': list(uv_numbers),
        'uv_ids': list(uv_ids)
    }
    uv_data.setdefault(index, current_set)
    
final_data = {
    'uv_sets': uv_data,
    'shape_node': mfn_mesh.name().encode()
}

# Write final dictionary variable to custom data format
file_path = os.path.join(
    tempfile.gettempdir(), 'head_test_uvs.uv')

with open(file_path, 'w') as file:
    file.write(json.dumps(final_data, indent=4))

# os.startfile(file_path)
print file_path
OpenMaya.MGlobal.displayInfo('\nUV Export Success!...')
