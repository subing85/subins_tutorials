import os
import getpass
import datetime
from pymel import core

# inputs
SHOT_CAMERA = 'camera1'
SHOW_NAME = 'Studio Maya'
WIDTH = 900
HEIGHT = 495
START_FRAME = None
END_FRAME = None
OUTPUT_PATH = None


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


def delete_uis():
    ui_list = core.lsUI(wnd=True)
    for each_ui in ui_list:
        if each_ui == 'MayaWindow':
            continue
        try:
            core.deleteUI(each_ui)
        except Exception as error:
            pass


def set_camera(shot_camera):
    delete_uis()
    current_camera = get_camera(shot_camera)
    core.mel.eval('setNamedPanelLayout "Single Perspective View"')
    core.lookThru(current_camera)


def set_model_panel():
    current_panel = core.getPanel(withFocus=True)
    core.modelEditor(current_panel, e=True, allObjects=False)
    core.modelEditor(current_panel, e=True, grid=False)
    core.modelEditor(current_panel, e=True, nurbsSurfaces=True)
    core.modelEditor(current_panel, e=True, polymeshes=True)
    core.modelEditor(current_panel, e=True, cameras=True)
    core.modelEditor(current_panel, e=True, dimensions=False)
    return current_panel


def set_frame_range(start=None, end=None):
    if not start:
        start = core.playbackOptions(q=True, ast=True)
    if not end:
        end = core.playbackOptions(q=True, aet=True)
    core.playbackOptions(e=True, min=int(start), max=int(end))
    return start, end


def set_hud_display(*args):
    default_headsups = [
        'setSelectDetailsVisibility',
        'setObjectDetailsVisibility',
        'setParticleCountVisibility',
        'setPolyCountVisibility',
        'setAnimationDetailsVisibility',
        'setHikDetailsVisibility',
        'setFrameRateVisibility',
        'setCurrentFrameVisibility',
        'setSceneTimecodeVisibility',
        'setCurrentContainerVisibility',
        'setViewportRendererVisibility',
        'setCameraNamesVisibility',
        'setFocalLengthVisibility',
        'setViewAxisVisibility',
        'setToolMessageVisibility',
    ]
    for each in default_headsups:
        core.mel.eval('%s 0;' % each)
    core.toggleAxis(o=False)
    core.viewManip(v=False)
    headsup_list = core.headsUpDisplay(q=True, lh=True)
    if headsup_list:
        for each_headsup in headsup_list:
            if core.headsUpDisplay(each_headsup, q=True, ex=True):
                core.headsUpDisplay(each_headsup,  rem=True)
    scene_name = core.sceneName()
    current_time = datetime.datetime.now().strftime('%A, %B %d, %Y %H:%M:%S %p')
    user_name = getpass.getuser()
    frame_range = '%s - %s' % (int(args[1]), int(args[2]))
    fps = core.mel.eval('currentTimeUnitToFPS')
    copy_right = 'Copyright 2019 Subin. Gopi - All Rights Reserved.'
    headsup_data = {
        "HUDframeRate": {
            "b": 0,
            "ao": True,
            "label": 'FPS-%s' % fps,
            "s": 8,
            "lfs": "large",
            "bs": "medium"
        },
        "HUDuser": {
            "b": 0,
            "ao": True,
            "label": user_name,
            "s": 5,
            "lfs": "large",
            "bs": "medium"
        },
        "HUDframeCount": {
            "b": 0,
            "ao": True,
            "label": frame_range,
            "s": 6,
            "lfs": "large",
            "bs": "medium"
        },
        "HUDscence": {
            "b": 0,
            "ao": True,
            "label": scene_name,
            "s": 1,
            "lfs": "large",
            "bs": "medium"
        },
        "HUDdate": {
            "b": 0,
            "ao": True,
            "label": current_time,
            "s": 4,
            "lfs": "large",
            "bs": "medium"
        },
        "HUDcopyRight": {
            "b": 0,
            "ao": True,
            "label": copy_right,
            "s": 7,
            "lfs": "small",
            "bs": "small"
        },
        "HUDprojectName": {
            "b": 0,
            "ao": True,
            "label": args[0],
            "s": 0,
            "lfs": "large",
            "bs": "medium"
        }
    }

    for headsup, contents in headsup_data.items():
        core.headsUpDisplay(
            headsup,
            s=contents['s'],
            b=contents['b'],
            bs=contents['bs'],
            ao=contents['ao'],
            label=contents['label'],
            lfs=contents['lfs']
        )
        core.headsUpDisplay(headsup, r=True)
    return scene_name


def set_display(cpanel, start, end, width, height, output):
    core.mel.eval('displayColor headsUpDisplayLabels -dormant 16;')
    core.mel.eval('displayColor headsUpDisplayLabels -dormant 16;')

    if width > 900:
        width = 900
    if height > 495:
        height = 495

    core.setAttr('defaultResolution.pixelAspect', True)
    core.setAttr('defaultResolution.width', width)
    core.setAttr('defaultResolution.height', height)
    core.mel.eval('setWireframeOnShadedOption false modelPanel4;')
    core.modelEditor(
        cpanel,
        e=True,
        udm=False,
        da='smoothShaded',
        displayTextures=True,
        ao=False
    )
    scene_name = core.sceneName()
    movie_path = os.path.join(
        output, '%s.mov' % scene_name.basename().splitext()[0])
    playblast = core.playblast(
        st=start,
        et=end,
        fmt='movie',
        fo=True,
        f=movie_path,
        cc=True,
        v=True,
        orn=True,
        p=100,
        c='none',
        wh=[width, height])
    print 'movie_path\t', playblast


def do_playblast(camera, show, width, height, start, end, output):
    core.select(cl=True)
    set_camera(camera)
    current_panel = set_model_panel()
    start, end = set_frame_range(start=start, end=end)
    scene_name = set_hud_display(show, start, end)
    if not output:
        output = scene_name.dirname()
    set_display(current_panel, start, end, width, height, output)


do_playblast(
    SHOT_CAMERA,
    SHOW_NAME,
    WIDTH,
    HEIGHT,
    START_FRAME,
    END_FRAME,
    OUTPUT_PATH
)
