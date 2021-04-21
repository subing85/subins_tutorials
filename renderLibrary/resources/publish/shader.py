NAME = 'Extract Shader'
ORDER = 2
ENABLE = False
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract shader from the geometries'
VERSION = '0.0.0'
MODIFIED = '2021:March:24:Wednesday-10:34:28:AM'
ACTION = 'renderLibrary.resources.publish.shader'


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
    root_node = getMaya.rootNode(nodes[-1])
    
    # get geometries hierarchy    
    _shaders, _nodes = getMaya.shaders(layer, root_node)
    # get override data
    _overrides = getMaya.overrides(layer, _nodes)    
    
    # get render memeber
    _members = getMaya.renderMembers(layer, _nodes)
    
    output_path = context.get('path')
   
    output_data = {
        'shader': _shaders,
        'nodes': _nodes,
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
        'tag': 'shader',        
        'time_stamp': context.get('time_stamp')
        }
    
    result, results = _export.studio_shader(
        output_path, output_data, format='mayaAscii', preserved=False, **kwrags)

    return True, 'success!...', result, results
     
