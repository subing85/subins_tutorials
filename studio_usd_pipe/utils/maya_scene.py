import os
import platform

from studio_usd_pipe.core import common

import json


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
    smaya.reference_maya(scene, deferred=False, locked=True, namespace=namespace)
    return True, scene, 'success'


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
        
      
    
