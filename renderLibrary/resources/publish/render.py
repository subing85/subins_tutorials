NAME = 'Extract Render Global Settings'
ORDER = 5
ENABLE = False
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract render global settings'
VERSION = '0.0.0'
MODIFIED = '2021:April:07:Wednesday-01:11:49:PM'
ACTION = 'renderLibrary.resources.publish.render'


def execute(context, **kwargs):
    import os  
      
    from maya import OpenMaya
        
    from renderLibrary.core import _export
    from renderLibrary.utils import getMaya
  
    layer = context.get('layer')
    
    # get render layer    
    _render_globals = getMaya.renderGlobals(layer)
    
    # get override data
    _overrides = getMaya.overrides(layer, _render_globals.keys())    

    output_path = context.get('path')
        
    output_data = {
        'renderGlobal': _render_globals,
        'overrides': _overrides
        }
        
    kwrags = {
        'name': context.get('name'),
        'type': context.get('type'),
        'order': context.get('order'),
        'action': context.get('action'),
        'comments': context.get('comments'),
        'enable': context.get('enable'),
        'tag': 'layer',
        'time_stamp': context.get('time_stamp')
        }  
            
    result = _export.studio_render(output_path, output_data, **kwrags)
    
    return True, 'success!...', result, None    
    
    
