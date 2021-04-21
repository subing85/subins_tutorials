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
        
    from renderLibrary.core import _export
    from renderLibrary.api import mayaRender

    layer = context.get('layer')
    
    mr = mayaRender.Connect()
    
    if not mr.selectedNodes:
        message = 'not found any selection'
        return False, message
        
    mr.selectLayer(layer)
    
    _root = mr.getRootNode(mr.selectedNodes[-1])  # get root node
    _members = mr.getGeometryMembers(layer, hierarchy=_root)  # geometry memebrs
    _overrides = mr.getOverrides(layer, _members, shape=True)  # get override data
    
    output_path = context.get('path')
         
    output_data = {
        'root': _root.fullPathName(),
        'members': _members,
        'overrides': _overrides        
        }
        
    
    from pprint import pprint
    pprint(_overrides)
             
    kwrags = {
        'name': context.get('name'),
        'type': context.get('type'),
        'order': context.get('order'),
        'action': context.get('action'),
        'comments': context.get('comments'),
        'enable': context.get('enable'),
        'tag': 'geometry',
        'time_stamp': context.get('time_stamp')
        }  
             
    result = _export.studio_geometry(output_path, output_data, **kwrags)
     
    # pass to next level
    context['root'] = _root.fullPathName()
     
    return True, 'success!...', result, None

