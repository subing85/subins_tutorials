import os
import copy
import json
import shutil

from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets


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
        from studio_usd_pipe.api import studioNurbscurve  
        from studio_usd_pipe.api import studioShader
        
        scurve = studioNurbscurve.Nurbscurve()
        sshader = studioShader.Shader()
        root = get_root()
        world = get_world()             
        # remove depend nodes
        depend_nodes = scurve.extract_depend_nodes(default=False)
        for x in range(depend_nodes.length()):
            scurve.remove_node(depend_nodes[x]) 
        scurve.remove_nodes(depend_nodes)                
        # make model group             
        mesh_mobjects = scurve.extract_transform_primitive(OpenMaya.MFn.kMesh, shape=False)
        model_dag_node = scurve.create_group(root)        
        # make geometry hierarchy  
        for x in range (mesh_mobjects.length()):
            scurve.set_locked(mesh_mobjects[x].node(), attributes=None, locked=False)
            scurve.disconnect_chanelbox(mesh_mobjects[x].node())
            scurve.set_parent(mesh_mobjects[x], model_dag_node.object())
            # assigin default shader
            sshader.assign_shading_engine(mesh_mobjects[x], shading_group=None)  
        # remove unwanted dag nodes    
        trans_dagpath_array = scurve.extract_top_transforms(default=False)
        for x in range (trans_dagpath_array.length()):
            if trans_dagpath_array[x].node() == model_dag_node.object():
                continue                       
            scurve.remove_node(trans_dagpath_array[x].node())
        # scurve.remove_nodes(transform_mobjects)        
        # reset transforms
        for x in range (mesh_mobjects.length()):
            scurve.delete_history(mesh_mobjects[x])
            scurve.freeze_transformations(mesh_mobjects[x])
            scurve.set_default_position(mesh_mobjects[x].node())
        # create world control   
        world_dependency_node = scurve.create_world(model_dag_node, parent=True) 
        # set the name
        model_dag_node.setName(root)
        world_dependency_node.setName(world)
        # create asset id
        id_data = resource.getAssetIDData()                   
        scurve.create_maya_ids(model_dag_node.object(), id_data)        
        # OpenMaya.MGlobal.selectByName(model_dag_node.fullPathName())
        OpenMaya.MGlobal.clearSelectionList()
        scurve.set_perspective_view()
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


def get_asset_ids():
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    root = get_root()
    if not smaya.object_exists(root):
        return None
    mobject = smaya.get_mobject(root)
    id_data = smaya.get_maya_id_data(mobject, id_data=None)
    return id_data


def create_thumbnail(input_path, ouput_path):
    thumbnail = swidgets.image_resize(
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


def check_shader_assigned_geometries():
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()    
    mobject = sshader.get_mobject(root)
    shader_data = sshader.get_scene_shading_engines(mobject)
    geometries = []
    for geometry, shader_engines in shader_data.items():
        if shader_engines:
            continue
        geometries.append(geometry.fullPathName().encode())
    if geometries:
        return False, geometries, 'found geometries with out shader assignment'
    return True, [], 'all geometries are assigned user shader'

def check_default_shader_geometries():
    from maya import OpenMaya
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()
    mobject = sshader.get_mobject(root)
    shader_data = sshader.get_scene_shading_engines(mobject)
    geometries = []
    for geometry, shader_engines in shader_data.items():
        if not shader_engines:
            continue    
        for index in range (shader_engines.length()):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(shader_engines[index])
            if mfn_dependency_node.name()!='initialShadingGroup':
                continue
            if geometry.fullPathName() in geometries:
                continue
            geometries.append(geometry.fullPathName())
    if geometries:
        return False, list(geometries), 'found geometries with default shader assignment'
    return True, [], 'all geometries are user assigned shader' 


def check_source_images():
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()
    mobject = sshader.get_mobject(root)  
    input_data = sshader.get_source_image_data(mobject)
    if not input_data:
        return True, []
    valid = {}
    for node in input_data:
        for attribute in input_data[node]:
            source_image = input_data[node][attribute]['value']
            if not os.path.isfile(source_image):
                valid.setdefault(False, []).append([node, source_image])
                continue
            valid.setdefault(True, []).append([node, source_image])
    if False in valid:
        return False, valid[False]
    return True, valid[True]
            

def create_shader_source_images(caption, temp_output_path, remap_output_path):
    '''
    from studio_usd_pipe.utils import maya_asset
    reload(maya_asset)
    caption = 'batman'
    output_path = '/usr/tmp/test_show/assets/batman/shader/0.0.1/'
    remap_output_path = '/venture/shows/batman/assets/batman/shader/0.0.1/'
    maya_asset.create_shader_source_images(caption, output_path, remap_output_path)
    '''
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()
    mobject = sshader.get_mobject(root)     
    temp_source_image_path = os.path.join(temp_output_path, 'source_images')     
    source_image_path = os.path.join(remap_output_path, 'source_images')
    if not os.path.isdir(temp_source_image_path):
        os.makedirs(temp_source_image_path)    
    input_data = sshader.get_source_image_data(mobject)    
    output_data = sshader.set_source_images(input_data, source_image_path)    
    # copy to temp directory
    source_images = set()
    for node in input_data:
        for attribute in input_data[node]:
            source_images.add(input_data[node][attribute]['value'])
    lores_data = {} 
    all_source_images = []           
    for source_image in source_images:
        temp_source_image = os.path.join(
            temp_source_image_path, os.path.basename(source_image))
        shutil.copy2(source_image, temp_source_image)
        lowres_source_image = sshader.create_lowres_source_images(
            source_image, temp_source_image_path)
        lores_data.setdefault(source_image, lowres_source_image)
        all_source_images.append(temp_source_image)
        all_source_images.append(lowres_source_image)
    source_image_data = os.path.join(temp_output_path, '%s.sourceimage'%caption)        
    final_data = {
        'input': input_data,
        'output': output_data,
        'lowres': lores_data
        }         
    with (open(source_image_data, 'w')) as content:
        content.write(json.dumps(final_data, indent=4))
    final_source_image_data = all_source_images + [source_image_data]
    return final_source_image_data


def create_studio_shader(output_path):
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()   
    mobject = sshader.get_mobject(root)
    mesh_data = sshader.get_surface_data(mobject)
    final_data = {
        'surface': mesh_data,
        }  
    with (open(output_path, 'w')) as content:
        content.write(json.dumps(final_data, indent=4))
    return output_path 


def create_shader_usd(output_path):
    from studio_usd_pipe.api import studioUsd    
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()   
    mobject = sshader.get_mobject(root)
    surface_data = sshader.get_surface_data(mobject)
    asset_ids = sshader.get_maya_id_data(mobject, id_data=None)
    final_data = {
        'surface': surface_data,
        'asset_id': asset_ids            
        }       
    susd = studioUsd.Susd(path=output_path)                
    susd.create_surface_usd(root, final_data)
    return output_path


def create_shader_maya(output_path):
    from maya import OpenMaya
    from studio_usd_pipe.api import studioShader
    sshader = studioShader.Shader()
    root = get_root()     
    mobject = sshader.get_mobject(root)
    shader_data = sshader.get_scene_shading_engines(mobject)
    shading_engines = []
    for geometry in shader_data:
        for index in range (shader_data[geometry].length()):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(shader_data[geometry][index])
            if mfn_dependency_node.name()=='initialShadingGroup':
                continue 
            shading_engines.append(mfn_dependency_node.name())
    sshader.export_selected(shading_engines, output_path, force=True)
    return output_path


def create_puppet_maya(output_path):
    from studio_usd_pipe.api import studioMaya
    smaya = studioMaya.Maya()
    root = get_root()    
    smaya.export_selected(root, output_path, force=True)
    return output_path



def find_asset_usd_inputs(**kwargs):

    
    subfileds = ['model']
    pass
        

def create_asset_usd_composition():
    pass

        

find_asset_usd_inputs()

