import os
import json
import tempfile

from maya.api import OpenMaya
from pprint import pprint

# Read uv custom data format
file_path = os.path.join(tempfile.gettempdir(), 'myTestUv.uv')
file = open(filePath, 'r')
data = json.load(file)       
file.close()

# store polygon shape node to variable from custom data
shape_node = data['shape_node']

# Polygon shape MDagPath
mselection = OpenMaya.MSelectionList()
mselection.add(shape_node)
mdag_path = mselection.getDagPath(0)

# Polygon shape MDagPath to MFnMesh
mfn_mesh = OpenMaya.MFnMesh(mdag_path)
exist_set_names = mfn_mesh.getUVSetNames()

# Remove exists uv set from polygon shape
for index, set_name in enumerate(exist_set_names):
    if index > 0:
        mfn_mesh.deleteUVSet(set_name)
 
# Assign uv informations to polygon shape 
for index, v in uv_sets.items():
    set_name = v['set_name']
        
    if int(index) == 0:
	# get exists uv set name
	new_set_name = exist_set_names[0]  
    else:
	# Create new uv set name
        new_set_name = mfn_mesh.createUVSet(set_name)        
        
    u_array = v['u_array']
    v_array = v['v_array']
    uv_face_numbers = v['uv_face_numbers']
    uv_ids = v['uv_ids']
	
    # Sets all of the texture coordinates (uv's) to polygon shape
    mfn_mesh.setUVs(u_array, v_array, new_set_name)

    # Assigns UV coordinates to the mesh's face-vertices.
    mfn_mesh.assignUVs(uv_face_numbers, uv_ids, new_set_name)
	
# Redrawn the polygonal shpae.
mfn_mesh.updateSurface()
