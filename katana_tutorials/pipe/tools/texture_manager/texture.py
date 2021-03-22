from core import shader
from core import scenegraph

from Katana import NodegraphAPI


def get_current_node():    
    knodes = NodegraphAPI.GetAllSelectedNodes()  
    if not knodes:
        return None    
    return knodes[-1].getName()


def find_materials(knode):    
    if isinstance(knode, str) or isinstance(knode, unicode):
        knode = NodegraphAPI.GetNode(knode)        
    if not knode:
        return False, None, 'invalid node <%s>' % knode                  
    producer = scenegraph.get_producer(knode, location=None)  
    material_texture_maps = shader.get_scene_material_texture_maps(producer)  
    message = None
    if not material_texture_maps:        
        message = 'not found any texture maps in %s' % knode.getName()
        return False, None, message  
    return True, material_texture_maps, message


def search_and_replace(node, path, search_for, replace_with):
    knode = NodegraphAPI.GetNode(node)
    if not knode:
        print '#warnings: not found node <%s>' % knode
        return
    parameter = knode.getParameter('parameters.filename.value')
    if not parameter:
        print '#warnings: not found parameter <%s> parameters.filename.value' % knode
        return
    replaced_path = path.replace(search_for, replace_with)
    parameter.setValue(replaced_path, 1.0)
    print '\nnode\t', node
    print '\t', path
    print '\t', replaced_path
    
    
