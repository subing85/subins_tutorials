import os
import json
import shutil
import tempfile
import warnings

from pxr import Usd
from pxr import Sdf
from pxr import UsdGeom
from maya import cmds
from maya import OpenMaya

from studio_usd_pipe.core import smaya

reload(smaya)


def pack_source_images(dirname, stamped_time=None, assign=True):
    mobjects = smaya.get_nodes(OpenMaya.MFn.kFileTexture)
    bundles = smaya.get_string_attribute_values(mobjects, 'fileTextureName')
    print '\n// Result: source images'
    for mplug, source_file in bundles.items():
        target_file = os.path.join(dirname, os.path.split(source_file)[-1])
        shutil.copy2(source_file, target_file)
        print '{}: {}'.format(mplug.name(), source_file)
        if stamped_time:
            os.utime(target_file, (stamped_time, stamped_time))
        if assign:
            mplug.setString(target_file)


def pack_static_usd(node, dirname, stamped_time=None):
    path = {
        'model': os.path.join(dirname, 'model.usda'),
        'uv': os.path.join(dirname, 'uv.usda'),
        'shader': os.path.join(dirname, 'shader.usda')
        }
    model_usd = model(node, path['model'], stamped_time=stamped_time)
    uv_usd = model(node, path['uv'], stamped_time=stamped_time)
    shader_usd = model(node, path['shader'], stamped_time=stamped_time)
    path['model'] = model_usd
    path['uv'] = uv_usd
    path['shader'] = shader_usd    
    print '\n// Result: usd export\n', json.dumps(path, indent=4)    
    return model_usd, uv_usd, shader_usd


def pack_active_usd(node, path=None):
    pass


def static_usd(node, path=None):
    if not path:
        temp_usd = os.path.join(
            tempfile.gettempdir(), 'temp_static.usda')
    smaya.remove_file(temp_usd)
    OpenMaya.MGlobal.selectByName(node)
    cmds.usdExport(
        mergeTransformAndShape=True,
        selection=True,
        kind='component',
        shadingMode='displayColor',
        exportUVs=True,
        defaultMeshScheme='catmullClark',
        file=temp_usd
    )
    return temp_usd


def active_usd(node, path=None):
    pass


def set_default_prim(source, target):
    default_prim = source.GetDefaultPrim()
    target.SetDefaultPrim(default_prim)
    axis = UsdGeom.GetStageUpAxis(source)
    UsdGeom.SetStageUpAxis(target, axis)


def model(node, path, stamped_time=None):
    if not smaya.has_exists(node):
        raise TypeError('No object matches name: {}'.format(node))
    temp_usd = static_usd(node)
    stage = Usd.Stage.Open(temp_usd)
    for prim in stage.TraverseAll():
        if prim.GetTypeName() != 'Scope':
            continue
        stage.RemovePrim(prim.GetPrimPath())
        break
    stage.GetRootLayer().Save()
    usd_path = '{}.usd'.format(os.path.splitext(path)[0])
    shutil.move(temp_usd, usd_path)
    if stamped_time:
        os.utime(usd_path, (stamped_time, stamped_time))
    print '# Saving stage', usd_path
    return usd_path


def uv(node, path, stamped_time=None):
    '''
        from studio_usd_pipe.core import export
        node = 'Hires_Geo_Group'
        path = '/venture/test_show/test/uv.usda'
        export.uv(node, path)      
    '''
    if not smaya.has_exists(node):
        raise TypeError('No object matches name: {}'.format(node))
    temp_usd = static_usd(node)
    usd_path = '{}.usd'.format(os.path.splitext(path)[0])
    static_stage = Usd.Stage.Open(temp_usd)
    layer = Sdf.Layer.CreateNew(usd_path, args={'format': 'usda'})
    stage = Usd.Stage.Open(layer)
    set_default_prim(static_stage, stage)
    for prim in static_stage.TraverseAll():
        if prim.GetTypeName() == 'Xform':
            xform_prim = UsdGeom.Xform.Define(stage, prim.GetPath())
        if prim.GetTypeName() == 'Mesh':
            mesh_prim = UsdGeom.Mesh.Define(stage, prim.GetPath())
            # u and v values attribute
            st_attribute = prim.GetAttribute('primvars:st')
            st_primvar = mesh_prim.CreatePrimvar(
                'st',
                Sdf.ValueTypeNames.Float2Array,
                UsdGeom.Tokens.faceVarying
            )
            st_primvar.Set(st_attribute.Get())
            # uv id values
            indices_attribute = prim.GetAttribute('primvars:st:indices')
            indices_primvar = mesh_prim.CreatePrimvar(
                'st',
                Sdf.ValueTypeNames.IntArray,
                UsdGeom.Tokens.faceVarying
            )
            indices_primvar.SetIndices(indices_attribute.Get())
    stage.GetRootLayer().Save()
    if stamped_time:
        os.utime(usd_path, (stamped_time, stamped_time))
    print '# Saving stage', usd_path
    return usd_path


def shader(node, path, stamped_time=None):
    '''
        from studio_usd_pipe.core import export
        node = 'Hires_Geo_Group'
        path = '/venture/test_show/test/shader.usda'
        export.shader(node, path)      
    '''
    if not smaya.has_exists(node):
        raise TypeError('No object matches name: {}'.format(node))
    temp_usd = static_usd(node)
    stage = Usd.Stage.Open(temp_usd)
    for index, prim in enumerate(stage.TraverseAll()):
        if index < 1:
            continue
        stage.RemovePrim(prim.GetPrimPath())
        break
    stage.GetRootLayer().Save()
    usd_path = '{}.usd'.format(os.path.splitext(path)[0])
    shutil.move(temp_usd, usd_path)
    if stamped_time:
        os.utime(usd_path, (stamped_time, stamped_time))
    print '# Saving stage', usd_path
    return usd_path
