import ast
import logging
import warnings
import json

from pymel import core

from pprint import pprint
from crowd.core import skeleton
from crowd.core import generic
from crowd.core import biped

reload(skeleton)
reload(generic)
reload(biped)




def create_puppet(tag, input):    
    if 'puppet' not in input:
        warnings.warn('valueError: Input data not valid!...')
        return
    core.select(cl=True)
    root_joints = getSkeletonWorld('skeletonType', tag)     
    print  'root_joints\t',  root_joints
    for each_root in root_joints:     
        if tag=='biped':
            biped.create_puppet(each_root.name(), input['puppet'])   
                   

def getSkeletonWorld(parameter, value):    
    joints = core.ls(sl=True)    
    if not joints:
        joints = core.ls(type='joint')        
    world_list = set()
    for each in joints:
        root = each.root()
        if not core.objExists('%s.%s'%(root.name(), parameter)):
            continue        
        if root.getAttr(parameter)!=value:
            continue
        world_list.add(each.root())
    return list(world_list)        
    
def create_puupet_data(data):    
    nodes = skeleton.get_root_skeletons()    
    if not nodes:
        return    
    pynode = core.PyNode(nodes[0])   
    if pynode.type() != generic.get_skeleton_type():
        return    
    if not core.objExists('%s.notes'%pynode.name()):        
        pynode.addAttr('notes', dt='string')   
    pynode.setAttr('notes', data)
    return True

def get_puppet_data():
    node, message = skeleton.get_root_skeletons()
    if not node:
        return None, message 
    pynode = core.PyNode(node)   
    if pynode.type() != generic.get_skeleton_type():
        return None, 'Node type not match!...' 
    if not core.objExists('%s.notes'%pynode.name()):        
        return None, 'Wrong configure!...' 
    data = pynode.getAttr('notes')
    dict_data = ast.literal_eval(data)
    return dict_data, 'success!...'





   


#===============================================================================
# import warnings
# from pprint import pprint
# from crowd.core import readWrite
# from crowd.core import skeleton
# from crowd.core import generic
# from crowd.api import crowdPublish
# 
# reload(readWrite)
# reload(skeleton)
# reload(crowdPublish)
# 
# 
# class Connect(object):
# 
#     def __init__(self, parent=None):
#         self.parent = parent
#         self.proxy_node = []
# 
#     def getTags(self):
#         publish = crowdPublish.Connect(type='skeleton')
#         return publish.getTags()
# 
#     def create(self, tag, position=None):
#         data, orders = self.findInputs()
#         if tag not in data:
#             warnings.warn('not fount tag called %s' % tag, Warning)
#             return
#         root_dag_path, result = skeleton.create_skeleton(
#             tag, data[tag], position=position)
#         return root_dag_path, result
# 
#     def findInputs(self):
#         rw = readWrite.Connect()
#         data, orders = rw.collect('skeletons', 'skeleton')
#         return data, orders
# 
#     def findSkeletons(self):
#         skeletons = generic.get_root_children()
#         return skeletons
# 
#     def make_skeleton(self, **kwargs):
#         pass
# 
# 
# # Skeleton().findSkeletons()
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ####################################
# def transform_types():
#     types = [
#         'transform',
#         'joint'
#     ]
#     return types
# 
# 
# def get_puppet_inputs(root=None):
#     if not root:
#         nodes, message = skeleton.get_root_skeletons()
#         if not nodes:
#             return 'failed', nodes, message
#         root = nodes[0]
# 
#     nodes = generic.get_hierarchy(root, types=transform_types())
#     for node in nodes:
#         transform_data = get_transform_data(node)
#         pprint (transform_data)
# 
# 
# 
# def get_transform_data(node):
#     translate = core.xform(node, q=True, ws=True, t=True)
#     rotate = core.xform(node, q=True, ws=True, ro=True)
#     scale = core.xform(node, q=True, ws=True, s=True)
#     parent_node = None
#     if node.getParent():
#         parent_node = node.getParent().name()
#     data = {
#         'translate': translate,
#         'rotate': rotate,
#         'scale': scale,
#         'parent': parent_node,
#         'snap_node': ''
#     }
#     return data
# 
# 
# def get_snap_node(node):
#     pass
#===============================================================================
    
    

