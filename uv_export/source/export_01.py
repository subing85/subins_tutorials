import os
import json
import tempfile

from maya.api import OpenMaya
from pprint import pprint

# Input - store polygon shape node to variable
shape_node = 'pPlaneShape1'

# Input to polygon shape MDagPath
mselection = OpenMaya.MSelectionList()
mselection.add(shape_node)
mdag_path = mselection.getDagPath(0)

# Polygon shape MDagPath to MFnMesh
mfn_mesh = OpenMaya.MFnMesh(mdag_path)

# get uv set names from input polygon shape
set_names = mfn_mesh.getUVSetNames()

uvs_data = {}

# Collect uv informations
for index, set_name in enumerate(set_names):
	# get u and v values
    u_array, v_array = mfn_mesh.getUVs(set_name)
	
	# get number of UVs assigned to each face of the mesh and face vertices uv ids
    uv_numbers, uv_ids = mfn_mesh.getAssignedUVs(set_name)
	
	# Store the uv vales to dictionary variable
    current_set = {
        'set_name': set_name,
        'u_array': list(u_array),
        'v_array': list(v_array),
        'uv_face_numbers': list(uv_numbers),
        'uv_ids': list(uv_ids)
        }        
    uvs_data.setdefault(index, current_set)

# Store the uv vales to dictionary variable	
data = {
    'uv_sets': uvs_data
    'shape_node': mfn_mesh.name()
}

# Wrtie dictionary variable data to custom data format
file_path = os.path.join(tempfile.gettempdir(), 'myTestUv.uv')
with open(file_path, 'w') as file:
    file.write(json.dumps(data, indent=4))
	
print 'success', '<%s>'%file_path


