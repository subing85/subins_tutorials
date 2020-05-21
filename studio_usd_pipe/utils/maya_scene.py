import os
import platform

from studio_usd_pipe import resource
from studio_usd_pipe.core import common

import json


def get_root():
    return 'shot'


def get_world():
    return 'world'


def open_maya_scene(scene):
    if not os.path.isfile(scene):
        return False, None, 'not found scene'
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()    
    smaya.open_maya(scene, file_type=None)
    return True, scene, 'success'

        
def import_maya_scene(scene, namespace):
    if not os.path.isfile(scene):
        return False, None, 'not found scene'
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    smaya.import_maya(scene, file_type=None, namespace=namespace)
    return True, scene, 'success'


def reference_maya_scene(scene, namespace):
    if not os.path.isfile(scene):
        return False, None, 'not found scene'
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    smaya.reference_maya(scene, deferred=False, locked=False, namespace=namespace)
    return True, scene, 'success'


def references_maya_scene(input_data, new_scene=False):
    if new_scene:
        from studio_usd_pipe.api import studioMaya
        smaya = studioMaya.Maya()
        smaya.new_maya_scene()
    valids = {}
    for namespace, path in input_data.items():
        valid, value, message = reference_maya_scene(path, namespace)
        valids.setdefault(valid, []).append(value)
    return valids


def open_location(dirname):
    if platform.system() == 'Windows':
        try:
            os.startfile(dirname)
        except Exception:
            return False, None, 'not found dirname'
    if platform.system() == 'Linux':    
        try:
            os.system('xdg-open \"%s\"' % dirname)
        except Exception:
            return False, None, 'not found dirname'
    return True, dirname, 'success'


def insert_studio_model(studio_model):
    # create instance
    valid, value, message = create_studio_model(studio_model, False)
    return valid, value, message


def merge_studio_model(studio_model):
    # merge with exists instance
    valid, value, message = create_studio_model(studio_model, True)
    return valid, value, message


def insert_studio_uv(studio_model):
    # create instance
    valid, value, message = create_studio_uv(studio_model, False)
    return valid, value, message


def merge_studio_uv(studio_model):
    # merge with exists instance
    valid, value, message = create_studio_uv(studio_model, True)
    return valid, value, message


def create_studio_model(studio_model_path, merge):
    from maya import OpenMaya    
    from studio_usd_pipe.api import studioModel
    from studio_usd_pipe.api import studioNurbscurve   
    # create polygon mesh
    studio_model = common.read_json(studio_model_path)
    model_data = studio_model['mesh']
    model_nodes = common.sort_dictionary(model_data)
    smodel = studioModel.Model()    
    contents = {}
    for node in model_nodes:
        node_contents = model_data[node]
        mfn_mesh = smodel.create_model(node, node_contents, merge=merge)
        contents.setdefault(node.split('|')[-1], mfn_mesh.parent(0))
    # create nurbs curve
    scurve = studioNurbscurve.Nurbscurve()
    curve_data = studio_model['curve']
    curve_nodes = common.sort_dictionary(curve_data)
    for node in curve_nodes:
        node_contents = curve_data[node]
        mfn_curve = scurve.create_curve(node, node_contents, merge=merge)
        contents.setdefault(node.split('|')[-1], mfn_curve.parent(0))
    # create transform
    transform_data = studio_model['transform']
    for node, node_contents in transform_data.items():
        mfn_transform = smodel.create_transform(node, node_contents, merge=merge)
        contents.setdefault(node.split('|')[-1], mfn_transform.object())
    locations = model_nodes + curve_nodes + transform_data.keys()        
    hierarchy = common.flatten_to_dictionary(locations, '|')
    stack = hierarchy.items()    
    while stack:
        parent, children = stack.pop()
        if not children:
            continue
        if not isinstance(children, dict): 
            continue 
        mfndag_parent = OpenMaya.MFnDagNode(contents[parent])
        for child in children:    
            mfndag_child = OpenMaya.MFnDagNode(contents[child])
            smodel.set_parent(mfndag_child, mfndag_parent)        
        stack.extend(children.items())
    return True, studio_model_path, 'success'


def create_studio_uv(studio_uv_path, merge):
    from studio_usd_pipe.api import studioModel
    smodel = studioModel.Model()
    studio_uv = common.read_json(studio_uv_path)
    uv_data = studio_uv['mesh']
    for node, contenst in uv_data.items():
        mfn_mesh = smodel.create_uv(node, contenst)
    return True, studio_uv_path, 'success'


def insert_studio_shader(studio_shader):
    create_studio_shader(studio_shader, False)


def merge_studio_shader(studio_shader):
    create_studio_shader(studio_shader, True)


def create_studio_shader(studio_shader_path, merge):
    from studio_usd_pipe.api import studioShader
    studio_model = common.read_json(studio_shader_path)
    surface_data = studio_model['surface']
    sshader = studioShader.Shader()
    for node, contenst in surface_data.items():
        shading_engine = sshader.create_shadernet(node, contenst, merge=merge)


def check_shot_hierarchy(subfield):   
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    id_data = resource.getPipeIDData()
    transforms = smaya.extract_top_transforms()
    nodes = [transforms[x].fullPathName() for x in range(transforms.length())]
    if transforms.length() > 1:
        return False, nodes, 'broken hierarchy'
    pipe_ids = resource.getPipeIDData()
    scene_subfield = {}
    for index in range (transforms.length()):
        pipe_id_data, valid = smaya.get_pipe_id_data(transforms[index].node(), pipe_ids)
        if not valid:
            continue
        subfield = pipe_id_data['ssubfield']['value']        
        scene_subfield.setdefault(subfield, []).append(transforms[index].fullPathName())
    if subfield in scene_subfield:
        return  True, scene_subfield[subfield], 'suitable hierarchy'
    return False, [], 'not found %s' % get_root()


def create_shot(**kwargs):
    '''
        from studio_usd_pipe.utils import maya_scene
        reload(maya_scene)    
        kwargs = {'pipe': 'shots',
                'caption': 'seq_1001|shot_101',
                'subfield': 'layout',
                'type': 'seq_1001',
                'tag': 'shot_101',
                'dependency': None,
                'version': '0.0.0',
                'modified': '1111111111',
                'location': 'dddddddddd',
                'description': 'ddddddddddd',
                'user': 'sid'
                }              
        valid, values, message = maya_scene.create_shot(kwargs)
    '''
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    smaya = studioMaya.Maya()    
    root = get_root()
    dag_node = smaya.create_group(root)
    valid, values = create_pipe_ids(dag_node.object(), **kwargs)
    if not valid:
        return False, values, 'failed'
    id_data = resource.getPipeIDData()      
    transforms = smaya.extract_null_transform()
    for index in range (transforms.length()):
        pipe_id_data, valid = smaya.get_pipe_id_data(transforms[index].node(), id_data)
        if not valid:
            continue        
        if pipe_id_data['spipe']['value'] != 'assets':
            continue
        smaya.set_parent(transforms[index], dag_node.object())
    transforms = smaya.extract_top_transforms()
    for index in range (transforms.length()):
        if transforms[index].node() == dag_node.object():
            continue                       
        smaya.remove_node(transforms[index].node())
    dag_node.setName(root)
    return True, [root], 'success'

        
def create_pipe_ids(mobject, **kwargs): 
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya() 
    id_data = resource.getPipeIDData()  
    inputs = {    
        'spipe': kwargs['pipe'],
        'scaption': kwargs['caption'],
        'ssubfield': kwargs['subfield'],
        'stype': kwargs['type'],
        'stag': kwargs['tag'],
        'sdependency': kwargs['dependency'],
        'sversion':kwargs['version'],
        'smodified': kwargs['modified'],
        'slocation':kwargs['location'],
        'sdescription': kwargs['description'],
        'suser': kwargs['user']
        }    
    for k, v in inputs.items():
        id_data[k]['value'] = v  
    created_data = smaya.create_pipe_ids(mobject, id_data)
    result = []    
    for k, v in created_data.items():
        result.append([k.encode(), v.encode()])
    return True, result


def update_pipe_ids(**kwargs):
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()     
    valid, mobject = find_shot_node(kwargs['subfield'])
    if not valid:
        return False, mobject, 'found more than one shot nodes'
    valid, values = create_pipe_ids(mobject, **kwargs)
    if not valid:
        return False, values, 'failed'
    return True, values, 'success'
    
    
def find_shot_node(subfield):
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()     
    transforms = smaya.extract_top_transforms()
    pipe_ids = resource.getPipeIDData()
    shot_nodes = [] 
    for index in range (transforms.length()):
        pipe_id_data, valid = smaya.get_pipe_id_data(transforms[index].node(), pipe_ids)
        if not valid:
            continue        
        if pipe_id_data['ssubfield']['value'] != subfield:
            continue  
        shot_nodes.append(transforms[index])
    if not shot_nodes:
        return False, shot_nodes
    if len(shot_nodes) > 1:
        return False, shot_nodes
    return True, shot_nodes[0].node()


def create_stuio_animation(output_path):
    pass
    
