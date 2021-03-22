NAME = 'Extract Geometry'
ORDER = 1
ENABLE = True
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract geometry hierarchy data'
VERSION = '0.0.0'
MODIFIED = '2021:March:19:Friday-11:26:53:PM'
ACTION = 'renderLibrary.resources.publish.geometry'


def execute(context, **kwargs):     
    import os  
      
    from maya import OpenMaya
        
    from renderLibrary.core import export
    from renderLibrary.utils import mayaNode

  
    selected = OpenMaya.MSelectionList()
    OpenMaya.MGlobal.getActiveSelectionList(selected)
    nodes = []
    selected.getSelectionStrings(nodes)
   
    if not nodes:
        message = 'not found any selection'
        return False, message

    sm = mayaNode.Connect(node=nodes[-1])
    root_node = sm.getRootNode()
    
    # get geometries hierarchy
    mesh_hierarchy = sm.getMeshHierarchy(root_node)
    
    from renderLibrary.utils import studioMaya
    studioMaya.getRenderMembers('batman', typed=OpenMaya.MFn.kMesh)    
    
    global_geometries = []
    for x in range (mesh_hierarchy.length()):
        global_geometries.append(meshes[x].fullPathName())
        
    geometry_data = {
        'global': global_geometries,
        'members': members,
        'overrides': overrides,
        
        }
    
    geometry_path = os.path.join(
        context.get('path'),
        context.get('name'),
        'geometry.json'
        )
    
    kwrags = {
        'comments': 'scene geometry hierarchy data from the user selection',
        'type': 'publish',
        'tag': 'geometry',
        'valid': True,
        'action': context['action'],
        'order': context['order']
        }  
    
    export.studio_json(geometries, geometry_path, **kwrags)
    
    context['geometry'] = {
        'result': geometry_path,
        'order': context['order'],
        'action': context['action']
        }
    
    print '#result', geometry_path
    
    return True, 'success!...'

