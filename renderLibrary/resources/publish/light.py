NAME = 'Extract Light'
ORDER = 3
ENABLE = False
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract light from the layer'
VERSION = '0.0.0'
MODIFIED = '2021:March:25:Thursday-01:26:58:PM'
ACTION = 'renderLibrary.resources.publish.light'


def execute(context, **kwargs):
    import os
    
    from maya import OpenMaya
        
    from renderLibrary.core import _export
    from renderLibrary.utils import getMaya    
    
    nodes = [context.get('node')] or getMaya.selectedNodes()
        
    if not nodes:
        message = 'not found any selection'
        return False, message        
    
    layer = context.get('layer')
    
    _lights = getMaya.lights(layer)
    _transform = getMaya.nodesTransform(_lights.keys())
    _attributes = getMaya.nodesAttributes(_lights)
    _overrides = getMaya.overrides(layer, _lights)
    
    output_path = context.get('path')
       
    output_data = {
        'lights': _lights,
        'transform': _transform,
        'attributes': _attributes,
        'overrides': _overrides,
        
        }
           
    kwrags = {
        'name': context.get('name'),
        'type': context.get('type'),
        'order': context.get('order'),
        'action': context.get('action'),
        'comments': context.get('comments'),
        'enable': context.get('enable'),
        'tag': 'light',         
        'time_stamp': context.get('time_stamp')
        }

    result = _export.studio_light(output_path, output_data, **kwrags)

    return True, 'success!...', result, None   
