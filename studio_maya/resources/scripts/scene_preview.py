'''
scene_preview.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to create preview movie of the sccene
'''


import os
import shutil
import tempfile
import platform
import subprocess

from pymel import core

# inputs
RENDER_ENGINE = 'mayaSoftware'
CAMERA = None
WIDTH = 1920
HEIGHT = 1080
OUTPUT_DIR = None
LIGHT_SETUP = True


def get_camera(input_camera):
    if input_camera and core.objExists(input_camera):
        current_camera = core.PyNode(input_camera)
        return current_camera
    else:
        default_camera = [
            'frontShape',
            'perspShape',
            'sideShape',
            'topShape'
        ]
        cameras = core.ls(type='camera')
        current_camera = None
        presp_camera = None
        for each in cameras:
            if each.name() == 'perspShape':
                presp_camera = each
            if each.name() in default_camera:
                continue
            current_camera = each
        if not current_camera:
            return presp_camera
        return current_camera


def get_render_parameters(render_engine, width, height, start, end):
    parameters = {
        'defaultRenderGlobals': {
            'currentRenderer': render_engine,
            'imageFilePrefix': '<Scene>',
            'imageFormat': 22,
            'gammaCorrection': 1,
            'exrCompression': 0,
            'exrPixelType': 0,
            'animation': True,
            'startFrame': start,
            'endFrame': end,
            'byFrameStep': 1,
            'animationRange': 1,
            'enableDefaultLight': 1,
            'modifyExtension': False,
            'shadowsObeyLightLinking': True,
            'shadowsObeyShadowLinking': False,
            'motionBlur': True,
            'motionBlurByFrame': 1,
            'motionBlurUseShutter': False,
            'motionBlurShutterOpen': -0.5,
            'motionBlurShutterClose': 0.5,
            'smoothColor': False,
            'tileWidth': 64,
            'tileHeight': 64,
            'animation': True,
            'encodingIndex': 4,
            'encodingQuality': 100,
            'encoding': 'raw'
        },
        'defaultResolution': {
            'width': width,
            'height': height,
            'pixelAspect': 1,
            'deviceAspectRatio': 1.7777777910232544
        },
        'defaultRenderQuality': {
            'caching': False,
            'isHistoricallyInteresting': 2,
            'nodeState': 0,
            'frozen': False,
            'reflections': 10,
            'refractions': 10,
            'shadows': 10,
            'rayTraceBias': 0,
            'edgeAntiAliasing': 0,
            'renderSample': False,
            'useMultiPixelFilter': True,
            'pixelFilterType': 2,
            'pixelFilterWidthX': 2.2000000476837158,
            'pixelFilterWidthY': 2.2000000476837158,
            'plugInFilterWeight': 1,
            'shadingSamples': 2,
            'maxShadingSamples': 8,
            'visibilitySamples': 1,
            'maxVisibilitySamples': 4,
            'volumeSamples': 1,
            'particleSamples': 1,
            'enableRaytracing': False,
            'redThreshold': 0.40000000596046448,
            'greenThreshold': 0.30000001192092896,
            'blueThreshold': 0.60000002384185791,
            'coverageThreshold': 0.125
        }
    }
    return parameters


def get_light_data():
    light_data = {
        'sun': {
            'parameter': {
                'intensity': 0.05,
                'color': [0.8, 0.9, 0.9],
                'emitDiffuse': True,
                'emitSpecular': False,
                'useDepthMapShadows': True,
                'dmapResolution': 128,
                'dmapFilterSize': 4
            },
            'position': {
                0: {'rotate': [0.0, 0.0, 0.0], 'translate': [0.0, 0.0, 100.0]},
                1: {'rotate': [180.0, -0.0, 0.0], 'translate': [0.0, -0.0, -100.0]},
                2: {'rotate': [-160.0, -0.0, 0.0], 'translate': [0.0, 34.2, -93.97]},
                3: {'rotate': [-140.0, -0.0, 0.0], 'translate': [0.0, 64.28, -76.6]},
                4: {'rotate': [-120.0, -0.0, 0.0], 'translate': [0.0, 86.6, -50.0]},
                5: {'rotate': [-100.0, -0.0, 0.0], 'translate': [0.0, 98.48, -17.36]},
                6: {'rotate': [-80.0, -0.0, 0.0], 'translate': [0.0, 98.48, 17.36]},
                7: {'rotate': [-60.0, -0.0, 0.0], 'translate': [0.0, 86.6, 50.0]},
                8: {'rotate': [-40.0, -0.0, 0.0], 'translate': [0.0, 64.28, 76.6]},
                9: {'rotate': [-20.0, -0.0, 0.0], 'translate': [0.0, 34.2, 93.97]},
                10: {'rotate': [20.0, -0.0, 90.0], 'translate': [34.2, -0.0, 93.97]},
                11: {'rotate': [40.0, -0.0, 90.0], 'translate': [64.28, -0.0, 76.6]},
                12: {'rotate': [60.0, -0.0, 90.0], 'translate': [86.6, -0.0, 50.0]},
                13: {'rotate': [80.0, -0.0, 90.0], 'translate': [98.48, -0.0, 17.36]},
                14: {'rotate': [100.0, -0.0, 90.0], 'translate': [98.48, -0.0, -17.36]},
                15: {'rotate': [120.0, -0.0, 90.0], 'translate': [86.6, -0.0, -50.0]},
                16: {'rotate': [140.0, -0.0, 90.0], 'translate': [64.28, -0.0, -76.6]},
                17: {'rotate': [160.0, -0.0, 90.0], 'translate': [34.2, -0.0, -93.97]},
                18: {'rotate': [-160.0, -0.0, 90.0], 'translate': [-34.2, 0.0, -93.97]},
                19: {'rotate': [-140.0, -0.0, 90.0], 'translate': [-64.28, 0.0, -76.6]},
                20: {'rotate': [-120.0, -0.0, 90.0], 'translate': [-86.6, 0.0, -50.0]},
                21: {'rotate': [-100.0, -0.0, 90.0], 'translate': [-98.48, 0.0, -17.36]},
                22: {'rotate': [-80.0, -0.0, 90.0], 'translate': [-98.48, 0.0, 17.36]},
                23: {'rotate': [-60.0, -0.0, 90.0], 'translate': [-86.6, 0.0, 50.0]},
                24: {'rotate': [-40.0, -0.0, 90.0], 'translate': [-64.28, 0.0, 76.6]},
                25: {'rotate': [-20.0, -0.0, 90.0], 'translate': [-34.2, 0.0, 93.97]},
                26: {'rotate': [-0.0, 90.0, 0.0], 'translate': [100.0, 0.0, 0.0]},
                27: {'rotate': [180.0, 90.0, 0.0], 'translate': [-100.0, -0.0, -0.0]},
                28: {'rotate': [-160.0, 90.0, 0.0], 'translate': [-93.97, 34.2, 0.0]},
                29: {'rotate': [-140.0, 90.0, 0.0], 'translate': [-76.6, 64.28, -0.0]},
                30: {'rotate': [-120.0, 90.0, 0.0], 'translate': [-50.0, 86.6, -0.0]},
                31: {'rotate': [-100.0, 90.0, 0.0], 'translate': [-17.36, 98.48, -0.0]},
                32: {'rotate': [-80.0, 90.0, 0.0], 'translate': [17.36, 98.48, 0.0]},
                33: {'rotate': [-60.0, 90.0, 0.0], 'translate': [50.0, 86.6, 0.0]},
                34: {'rotate': [-40.0, 90.0, 0.0], 'translate': [76.6, 64.28, 0.0]},
                35: {'rotate': [-20.0, 90.0, 0.0], 'translate': [93.97, 34.2, 0.0]},
                36: {'rotate': [0.0, 45.0, 0.0], 'translate': [70.71, 0.0, 70.71]},
                37: {'rotate': [180.0, 45.0, 0.0], 'translate': [-70.71, -0.0, -70.71]},
                38: {'rotate': [-160.0, 45.0, 0.0], 'translate': [-66.45, 34.2, -66.45]},
                39: {'rotate': [-140.0, 45.0, 0.0], 'translate': [-54.17, 64.28, -54.17]},
                40: {'rotate': [-120.0, 45.0, 0.0], 'translate': [-35.36, 86.6, -35.36]},
                41: {'rotate': [-100.0, 45.0, 0.0], 'translate': [-12.28, 98.48, -12.28]},
                42: {'rotate': [-80.0, 45.0, 0.0], 'translate': [12.28, 98.48, 12.28]},
                43: {'rotate': [-60.0, 45.0, 0.0], 'translate': [35.36, 86.6, 35.36]},
                44: {'rotate': [-40.0, 45.0, 0.0], 'translate': [54.17, 64.28, 54.17]},
                45: {'rotate': [-20.0, 45.0, 0.0], 'translate': [66.45, 34.2, 66.45]},
                46: {'rotate': [0.0, -45.0, 0.0], 'translate': [-70.71, 0.0, 70.71]},
                47: {'rotate': [180.0, -45.0, 0.0], 'translate': [70.71, -0.0, -70.71]},
                48: {'rotate': [-160.0, -45.0, 0.0], 'translate': [66.45, 34.2, -66.45]},
                49: {'rotate': [-140.0, -45.0, 0.0], 'translate': [54.17, 64.28, -54.17]},
                50: {'rotate': [-120.0, -45.0, 0.0], 'translate': [35.36, 86.6, -35.36]},
                51: {'rotate': [-100.0, -45.0, 0.0], 'translate': [12.28, 98.48, -12.28]},
                52: {'rotate': [-80.0, -45.0, 0.0], 'translate': [-12.28, 98.48, 12.28]},
                53: {'rotate': [-60.0, -45.0, 0.0], 'translate': [-35.36, 86.6, 35.36]},
                54: {'rotate': [-40.0, -45.0, 0.0], 'translate': [-54.17, 64.28, 54.17]},
                55: {'rotate': [-20.0, -45.0, 0.0], 'translate': [-66.45, 34.2, 66.45]}}
        },
        'ground': {
            'parameter': {
                'intensity': 0.1,
                'color': [0.8, 0.8, 0.7],
                'emitDiffuse': True,
                'emitSpecular': False,
                'useDepthMapShadows': True,
                'dmapResolution': 128,
                'dmapFilterSize': 4
            },
            'position': {
                0: {'rotate': [20.0, -0.0, 0.0], 'translate': [0.0, -34.2, 93.97]},
                1: {'rotate': [40.0, -0.0, 0.0], 'translate': [0.0, -64.28, 76.6]},
                2: {'rotate': [60.0, -0.0, 0.0], 'translate': [0.0, -86.6, 50.0]},
                3: {'rotate': [80.0, -0.0, 0.0], 'translate': [0.0, -98.48, 17.36]},
                4: {'rotate': [100.0, -0.0, 0.0], 'translate': [0.0, -98.48, -17.36]},
                5: {'rotate': [120.0, -0.0, 0.0], 'translate': [0.0, -86.6, -50.0]},
                6: {'rotate': [140.0, -0.0, 0.0], 'translate': [0.0, -64.28, -76.6]},
                7: {'rotate': [160.0, -0.0, 0.0], 'translate': [0.0, -34.2, -93.97]},
                8: {'rotate': [20.0, 90.0, 0.0], 'translate': [93.97, -34.2, 0.0]},
                9: {'rotate': [40.0, 90.0, 0.0], 'translate': [76.6, -64.28, 0.0]},
                10: {'rotate': [60.0, 90.0, 0.0], 'translate': [50.0, -86.6, 0.0]},
                11: {'rotate': [80.0, 90.0, 0.0], 'translate': [17.36, -98.48, 0.0]},
                12: {'rotate': [100.0, 90.0, 0.0], 'translate': [-17.36, -98.48, -0.0]},
                13: {'rotate': [120.0, 90.0, 0.0], 'translate': [-50.0, -86.6, -0.0]},
                14: {'rotate': [140.0, 90.0, 0.0], 'translate': [-76.6, -64.28, -0.0]},
                15: {'rotate': [160.0, 90.0, 0.0], 'translate': [-93.97, -34.2, -0.0]},
                16: {'rotate': [20.0, 45.0, 0.0], 'translate': [66.45, -34.2, 66.45]},
                17: {'rotate': [40.0, 45.0, 0.0], 'translate': [54.17, -64.28, 54.17]},
                18: {'rotate': [60.0, 45.0, 0.0], 'translate': [35.36, -86.6, 35.36]},
                19: {'rotate': [80.0, 45.0, 0.0], 'translate': [12.28, -98.48, 12.28]},
                20: {'rotate': [100.0, 45.0, 0.0], 'translate': [-12.28, -98.48, -12.28]},
                21: {'rotate': [120.0, 45.0, 0.0], 'translate': [-35.36, -86.6, -35.36]},
                22: {'rotate': [140.0, 45.0, 0.0], 'translate': [-54.17, -64.28, -54.17]},
                23: {'rotate': [160.0, 45.0, 0.0], 'translate': [-66.45, -34.2, -66.45]},
                24: {'rotate': [20.0, -45.0, 0.0], 'translate': [-66.45, -34.2, 66.45]},
                25: {'rotate': [40.0, -45.0, 0.0], 'translate': [-54.17, -64.28, 54.17]},
                26: {'rotate': [60.0, -45.0, 0.0], 'translate': [-35.36, -86.6, 35.36]},
                27: {'rotate': [80.0, -45.0, 0.0], 'translate': [-12.28, -98.48, 12.28]},
                28: {'rotate': [100.0, -45.0, 0.0], 'translate': [12.28, -98.48, -12.28]},
                29: {'rotate': [120.0, -45.0, 0.0], 'translate': [35.36, -86.6, -35.36]},
                30: {'rotate': [140.0, -45.0, 0.0], 'translate': [54.17, -64.28, -54.17]},
                31: {'rotate': [160.0, -45.0, 0.0], 'translate': [66.45, -34.2, -66.45]}}
        }
    }
    return light_data


def set_camera(render_camera):
    cameras = core.ls(type='camera')
    for current_camera in cameras:
        attribute = current_camera.attr('renderable')
        attribute.set(False)
    camera_parameter = {
        'backgroundColor': [0.318898, 0.318898, 0.318898],
        'renderable': True
    }
    for parameter, values in camera_parameter.items():
        attribute = render_camera.attr(parameter)
        attribute.set(values)
        core.editRenderLayerAdjustment(attribute)


def set_frame_range(start=None, end=None):
    if not start:
        start = core.playbackOptions(q=True, ast=True)
    if not end:
        end = core.playbackOptions(q=True, aet=True)
    core.playbackOptions(e=True, min=int(start), max=int(end))
    return start, end


def render_layer():
    layers = core.ls(type='renderLayer')
    for layer in layers:
        attribute = layer.attr('renderable')
        attribute.set(False)
    geometrys = core.listTransforms(geometry=True)
    layer = 'scene_preview'
    if core.objExists(layer):
        core.editRenderLayerGlobals(crl='defaultRenderLayer')
        core.delete(layer)
    render_layer = core.createRenderLayer(geometrys, n=layer, num=1, nr=1)
    render_layer.setCurrent()


def batch_render(output):
    scene_name = core.sceneName()
    basename = scene_name.basename()
    if not output:
        output = scene_name.dirname()
    render_exe = get_render_cmd()
    if not os.path.isfile(render_exe):
        core.workspace(fileRule=['images', output])
        core.workspace(fileRule=['movie', output])
        core.workspace(s=True)
    temp_path = os.path.join(tempfile.gettempdir(), basename)
    if os.path.isfile(temp_path):
        try:
            os.chmod(temp_path, 0777)
        except:
            pass
        try:
            os.remove(temp_path)
        except:
            pass
    render_file = core.saveAs(temp_path, f=True, iv=True, pmt=True)
    if os.path.isfile(render_exe):
        command = '{} -r file -rd \"{}\" \"{}\"'.format(
            render_exe, output, render_file)
        os.system(command)
    else:
        core.mel.eval('BatchRender;')
    output_file = os.path.join(
        output, 'scene_preview', '%s.mov' % basename.splitext()[0])
    return output_file


def get_render_cmd():
    if 'PYTHONHOME' not in os.environ:
        return None
    operating_system = platform.system()
    if operating_system == 'Linux':
        return os.path.join(os.environ['PYTHONHOME'], 'bin', 'Render')
    if operating_system == 'Windows':
        return os.path.join(os.environ['PYTHONHOME'], 'bin', 'Render.exe')


def create_light():
    light_data = get_light_data()
    light_group = core.group(em=True)
    for k, v in light_data.items():
        intensity = v['parameter']['intensity']
        color = v['parameter']['color']
        diffuse = v['parameter']['emitDiffuse']
        specular = v['parameter']['emitSpecular']
        map_shadows = v['parameter']['useDepthMapShadows']
        resolution = v['parameter']['dmapResolution']
        for index in v['position']:
            translate = v['position'][index]['translate']
            rotation = v['position'][index]['rotate']
            light = core.directionalLight(
                rot=rotation,
                pos=translate,
                i=intensity,
                rgb=color
            )
            light.setAttr('emitDiffuse', diffuse)
            light.setAttr('emitSpecular', specular)
            light.setAttr('useDepthMapShadows', map_shadows)
            light.setAttr('dmapResolution', resolution)
            light.getParent().setParent(light_group)


def create(engine, render_camera, width, height, output, light):
    if not engine:
        engine = 'mayaSoftware'
    start, end = set_frame_range()
    render_layer()
    if light:
        create_light()
    render_parameters = get_render_parameters(
        engine, width, height, start, end)
    for render_global, contents in render_parameters.items():
        global_node = core.PyNode(render_global)
        if render_global == 'defaultRenderGlobals':
            if not core.objExists('defaultRenderGlobals.encoding'):
                global_node.addAttr(
                    'encoding', ci=True, sn='encoding', dt='string')
            if not core.objExists('defaultRenderGlobals.encodingIndex'):
                global_node.addAttr(
                    'encodingIndex', ci=True, sn='encodingIndex', at='long')
            if not core.objExists('defaultRenderGlobals.encodingQuality'):
                global_node.addAttr(
                    'encodingQuality', ci=True, sn='encodingQuality', min=0, max=100, at='long')
        for parameter, value in contents.items():
            attribute = global_node.attr(parameter)
            attribute.set(value)
            core.editRenderLayerAdjustment(attribute)
    current_camera = get_camera(render_camera)
    set_camera(current_camera)
    movie = batch_render(output)
    print "\nhttp://www.subins-toolkits.com", '\n', '-'*41     
    print '\nMovie path: ', movie
    return movie


result = create(RENDER_ENGINE, CAMERA, WIDTH, HEIGHT, OUTPUT_DIR, LIGHT_SETUP)
