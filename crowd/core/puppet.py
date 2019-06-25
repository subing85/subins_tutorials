import logging

from pymel import core


from pprint import pprint
from crowd.core import skeleton
from crowd.core import generic

reload(skeleton)
reload(generic)


def create_puupet_data(data):    
    nodes = skeleton.get_root_skeletons()    
    if not nodes:
        return    
    pynode = core.PyNode(nodes[0][0])   
    if pynode.type() != generic.get_skeleton_type():
        return    
    if not core.objExists('%s.notes'%pynode.name()):        
        pynode.addAttr('notes', dt='string')   
    pynode.setAttr('notes', data)
    return True


def get_puupet_data():
    nodes, message = skeleton.get_root_skeletons()    
    if not nodes:
        return None, message 
    pynode = core.PyNode(nodes[0][0])   
    if pynode.type() != generic.get_skeleton_type():
        return None, 'Node type not match!...' 
    if not core.objExists('%s.notes'%pynode.name()):        
        return None, 'Wrong configure!...' 
    data = pynode.getAttr('notes')
    return data, 'success!...'
   


    
    
               
    
    
    
    
    
    
    




####################################
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
    pass
    
    

