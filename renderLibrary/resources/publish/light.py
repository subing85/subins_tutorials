NAME = 'Extract Light'
ORDER = 3
ENABLE = True
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract light from the layer'
VERSION = '0.0.0'
MODIFIED = '2021:March:25:Thursday-01:26:58:PM'
ACTION = 'renderLibrary.resources.publish.light'


def execute(context, **kwargs):
    import os
    
    from maya import OpenMaya
        
    from renderLibrary.core import export
    from renderLibrary.utils import studioMaya    
    
    nodes = [context.get('node')] or studioMaya.getSelectedNodes()
        
    if not nodes:
        message = 'not found any selection'
        return False, message        
    
    layer = context.get('layer')
    
    _lights = studioMaya.getLights(layer)
    _transform = studioMaya.getNodesTransform(_lights.keys())
    _attributes = studioMaya.getNodesAttributes(_lights)
    _overrides = studioMaya.getOverrides(layer, _lights)
    
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
        'time_stamp': context.get('time_stamp')
        }

    result = export.studio_light(output_path, output_data, **kwrags)

    return True, 'success!...', result, None   
