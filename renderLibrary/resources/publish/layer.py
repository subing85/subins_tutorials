NAME = 'Extract Render Layer'
ORDER = 4
ENABLE = True
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract render layer and passes data'
VERSION = '0.0.0'
MODIFIED = '2021:March:29:Monday-10:00:35:PM'
ACTION = 'renderLibrary.resources.publish.layer'


def execute(context, **kwargs):
      
    from renderLibrary.core import _export
    from renderLibrary.api import mayaRender
 
    layer = context.get('layer')   

    mr = mayaRender.Connect()
    mr.selectLayer(layer)
    
    _attributes = mr.getLayerAttributes(layer)
    _aovs = mr.getAovs(overrides=True, layer=layer)
   
    output_data = {
        'engine': mr.currentRenderEngine,
        'layer': {
            layer: {
                'attributes': _attributes,
                'aovs': _aovs
                }
            }
        }

    
    output_path = context.get('path')
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
            
    result = _export.studio_layer(output_path, output_data, **kwrags)
    
    return True, 'success!...', result, None
    
    
  