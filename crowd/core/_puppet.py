from pprint import pprint
from crowd.core import skeleton
from crowd.core import generic

reload(skeleton)
reload(generic)


def transform_types():
    types = [
        'transform',
        'joint'
    ]
    return types


def get_puppet_inputs(root=None):
    if not root:
        nodes, message = skeleton.get_root_skeletons()
        if not nodes:
            return 'failed', nodes, message
        root = nodes[0]
            
    nodes = generic.get_hierarchy(root, types=transform_types())
    for node in nodes:        
        transform_data = get_transform_data(node)        
        pprint (transform_data)
        

 


def create_puppet():
    pass

def get_transform_data(node):
    translate = core.xform(node, q=True, ws=True, t=True)
    rotate = core.xform(node, q=True, ws=True, ro=True)
    scale = core.xform(node, q=True, ws=True, s=True)
    parent_node = None
    if node.getParent():
        parent_node = node.getParent().name()
    data = {
        'translate': translate,
        'rotate': rotate,
        'scale': scale,
        'parent': parent_node,
        'snap_node': ''
    }
    return data


def get_snap_node(node):
    
    

