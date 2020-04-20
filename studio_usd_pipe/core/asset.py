import os
import copy
import json

from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import common


def get_root():
    return 'asset'


def get_world():
    return 'world'


def check_model_hierarchy():
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    top_level_nodes = smaya.extract_top_transforms()    
    if top_level_nodes.length() == 0:        
        return False, [None], 'not found any transform nodes'    
    elif top_level_nodes.length() > 1:
        nodes = []
        for x in range(top_level_nodes.length()):
            nodes.append(top_level_nodes[x].fullPathName())                
        return False, nodes, 'found more than one top level transform nodes'    
    elif not smaya.object_exists(get_root()):
        return False, [None], 'not found %s' % get_root()    
    return True, [get_root()], 'suitable hierarchy'


def create_model():        
        '''
        :example
            from studio_usd_pipe.core import asset
            mpack.asset()      
        '''
        from maya import OpenMaya
        from studio_usd_pipe.api import studioShader
        from studio_usd_pipe.api import studioNurbscurve  
        smaya = studioShader.Shader()  
        scurve = studioNurbscurve.Nurbscurve() 
        root = get_root()
        world = get_world()             
        # remove depend nodes
        depend_nodes = smaya.extract_depend_nodes(default=False)
        for x in range(depend_nodes.length()):
            smaya.remove_node(depend_nodes[x]) 
        smaya.remove_nodes(depend_nodes)                
        # make model group             
        mesh_mobjects = smaya.extract_transform_primitive(OpenMaya.MFn.kMesh, shape=False)
        model_dag_node = smaya.create_group(root)        
        # make geometry hierarchy  
        for x in range (mesh_mobjects.length()):
            smaya.set_locked(mesh_mobjects[x].node(), attributes=None, locked=False)
            smaya.disconnect_chanelbox(mesh_mobjects[x].node())
            smaya.set_parent(mesh_mobjects[x], model_dag_node.object())
            # assigin default shader
            smaya.assign_shading_engine(mesh_mobjects[x], shading_group=None)  
        # remove unwanted dag nodes    
        trans_dagpath_array = smaya.extract_top_transforms(default=False)
        for x in range (trans_dagpath_array.length()):
            if trans_dagpath_array[x].node() == model_dag_node.object():
                continue                       
            smaya.remove_node(trans_dagpath_array[x].node())
        # smaya.remove_nodes(transform_mobjects)        
        # reset transforms
        for x in range (mesh_mobjects.length()):
            smaya.delete_history(mesh_mobjects[x])
            smaya.freeze_transformations(mesh_mobjects[x])
            smaya.set_default_position(mesh_mobjects[x].node())
        # create world control   
        world_dependency_node = scurve.create_world(model_dag_node, parent=True) 
        # set the name
        model_dag_node.setName(root)
        world_dependency_node.setName(world)
        # create asset id
        id_data = resource.getAssetIDData()                   
        smaya.create_maya_ids(model_dag_node.object(), id_data)        
        # OpenMaya.MGlobal.selectByName(model_dag_node.fullPathName())
        OpenMaya.MGlobal.clearSelectionList()
        smaya.set_perspective_view()
        return True, [root], 're-generate hierarchy'

   
def removed_asset_ids():
    from maya import OpenMaya
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    root = get_root()
    mobject = smaya.get_mobject(root)        
    id_data = resource.getAssetIDData()
    removed_ids = smaya.removed_asset_ids(mobject, id_data=id_data)
    if not removed_ids:
        return True, [], 'asset ids are valid'
    return False, removed_ids, 'asset ids are invalid'


def create_maya_ids(**kwargs):
    from studio_usd_pipe.api import studioMaya    
    reload(studioMaya)
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
    
    id_data = resource.getAssetIDData()    
    for k, v in inputs.items():
        id_data[k]['value'] = v    
    smaya = studioMaya.Maya()
    root = get_root()
    mobject = smaya.get_mobject(root) 
    created_data = smaya.create_maya_ids(mobject, id_data)
    result = []    
    for k, v in created_data.items():
        result.append([k.encode(), v.encode()])
    return True, result


def update_asset_ids(id_data=None):
    from maya import OpenMaya
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    root = get_root()    
    mobject = smaya.get_mobject(root) 
    if not id_data:
        id_data = resource.getAssetIDData()
    smaya.update_asset_ids(mobject, id_data=id_data)
    return True, [id_data.keys()], 'updated with valid asset ids'


def create_thumbnail(input_path, ouput_path):
    from studio_usd_pipe.core import image    
    thumbnail = image.image_resize(
        input_path,
        ouput_path,
        1024,
        1024,
        )             
    return thumbnail


def create_studio_model(output_path):
    from studio_usd_pipe.api import studioModel
    from studio_usd_pipe.api import studioNurbscurve   
    smodel = studioModel.Model()
    scurve = studioNurbscurve.Nurbscurve()
    root = get_root()   
    mobject = smodel.get_mobject(root)
    mesh_data = smodel.get_model_data(mobject)
    curve_data = scurve.get_curve_data(mobject)
    transform_data = smodel.get_transform_data(mobject)
    final_data = {
        'mesh': mesh_data,
        'curve': curve_data,
        'transform': transform_data
        } 
    with (open(output_path, 'w')) as content:
        content.write(json.dumps(final_data, indent=4))
    return output_path


def create_model_usd(output_path):
    from studio_usd_pipe.api import studioUsd
    from studio_usd_pipe.api import studioModel
    from studio_usd_pipe.api import studioNurbscurve
    smodel = studioModel.Model()
    scurve = studioNurbscurve.Nurbscurve()
    root = get_root()    
    mobject = smodel.get_mobject(root)
    mesh_data = smodel.get_model_data(mobject)
    curve_data = scurve.get_curve_data(mobject)
    asset_ids = smodel.get_maya_id_data(mobject, id_data=None)
    final_data = {
        'mesh': mesh_data,
        'curve': curve_data,
        'asset_id': asset_ids
        }        
    susd = studioUsd.Susd(path=output_path)                
    susd.create_model_usd(root, final_data)
    return output_path    

    
def create_maya_scene(output_path):
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    root = get_root() 
    smaya.export_selected(root, output_path, force=True)
    return output_path


def create_asset_manifest(output_path, **kwargs):
    final_data = {
        "created_by": "subin gopi",
        "author": "Subin. Gopi (subing85@gmail.com)",
        "#copyright": "(c) 2019, Subin Gopi All rights reserved.",
        "last_modified": kwargs['modified'],
        "description": "publish asset manifest",
        "warning": "# WARNING! All changes made in this file will be lost!",
        "enable": True,
        "type": "manifest",
        'data': kwargs
        }        
    with (open(output_path, 'w')) as content:
        content.write(json.dumps(final_data, indent=4))
    return output_path


def validate_uv_sets():
    from maya import OpenMaya
    from studio_usd_pipe.api import studioModel
    reload(studioModel)
    smodel = studioModel.Model()
    root = get_root() 
    mobject = smodel.get_mobject(root)
    transform_mesh = smodel.extract_transform_primitive(
        OpenMaya.MFn.kMesh, shape=True, parent_mobject=mobject)
    data = {}
    for x in range(transform_mesh.length()):
        uvsets = smodel.get_uvsets(transform_mesh[x])        
        for uvset in uvsets:
            valid = smodel.has_valid_uvset(transform_mesh[x], uvset)
            data.setdefault(valid, []).append(
                [transform_mesh[x].fullPathName(), uvset])
    if False in data:
        return False, data[False], 'found in-valid uvsets'
    return True, [None], 'all uv sets are valid'


def create_studio_uv(output_path):
    from studio_usd_pipe.api import studioModel
    from studio_usd_pipe.api import studioNurbscurve  
    smodel = studioModel.Model()
    root = get_root()
    mobject = smodel.get_mobject(root)
    mesh_data = smodel.get_uv_data(mobject)
    final_data = {
        'mesh': mesh_data,
        }      
    with (open(output_path, 'w')) as content:
        content.write(json.dumps(final_data, indent=4))
    return output_path


def create_uv_usd(output_path):
    from studio_usd_pipe.api import studioUsd
    from studio_usd_pipe.api import studioModel    
    reload(studioModel)
    smodel = studioModel.Model()
    root = get_root()
    mobject = smodel.get_mobject(root)    
    mesh_data = smodel.get_uv_data(mobject)
    asset_ids = smodel.get_maya_id_data(mobject, id_data=None)
    final_data = {
        'mesh': mesh_data,
        'asset_id': asset_ids
        }        
    susd = studioUsd.Susd(path=output_path)                
    susd.create_uv_usd(root, final_data)
    return output_path

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
