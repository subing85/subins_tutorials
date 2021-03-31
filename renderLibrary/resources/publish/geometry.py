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
    from renderLibrary.utils import studioMaya
  
    nodes = studioMaya.getSelectedNodes()

    if not nodes:
        message = 'not found any selection'
        return False, message
    
    layer = context.get('layer')    
    root_node = studioMaya.getRootNode(nodes[-1])
    
    # get geometries hierarchy    
    _geometries = studioMaya.getGeometries(layer, root_node)
    # get override data
    _overrides = studioMaya.getOverrides(layer, _geometries)    
    
    # get render memeber
    _members = studioMaya.getRenderMembers(layer, _geometries)  

    output_path = context.get('path')
        
    output_data = {
        'geometries': _geometries,
        'overrides': _overrides,
        'members': _members
        }
        
    kwrags = {
        'name': context.get('name'),
        'type': context.get('type'),
        'order': context.get('order'),
        'action': context.get('action'),
        'comments': context.get('comments'),
        'enable': context.get('enable'),
        'time_stamp': context.get('time_stamp')
        }  
            
    result = export.studio_geometry(output_path, output_data, **kwrags)
    
    # pass to next level
    context['node'] = nodes[-1]
    
    return True, 'success!...', result, None

