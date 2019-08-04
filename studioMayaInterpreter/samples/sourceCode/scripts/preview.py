# Embedded file name: F:/My Work/dumps/My script/pythonApplication/smartTool/Applications/smartMaya/sourceCode/scripts\preview.py
"""
Playblast Preview
Date : July 02, 2016
Last modified: July 02, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
"""
import os, datetime
import maya.cmds as cmds
import maya.mel as mel
previewCamera = 'NCamera:Camera_CamShape'
category = 'Demo-2016'
episod = 'Tony'
sequence = 'Sequence-0001'
shots = 'Shot-001'
prewPath = 'C:\\Users\\Subin\\Desktop\\mov'

def preview():
    projectName = 'Demo'
    fileName = cmds.file(q=1, sn=1, shn=1)
    userName = os.getenv('USERNAME')
    copyRight = 'Copyright 2016 Subin. Gopi - All Rights Reserved.'
    dtaeAndTime = datetime.datetime.now().strftime('%A, %B %d, %Y %H:%M:%S %p')
    fpsName = 'FPS :- ' + str(mel.eval('currentTimeUnitToFPS'))
    presPanel = cmds.getPanel(withFocus=1)
    cmds.modelEditor(presPanel, e=1, allObjects=0)
    cmds.modelEditor(presPanel, e=1, grid=0)
    cmds.modelEditor(presPanel, e=1, nurbsSurfaces=0)
    cmds.modelEditor(presPanel, e=1, polymeshes=1)
    cmds.modelEditor(presPanel, e=1, cameras=1)
    cmds.modelEditor(presPanel, e=1, dimensions=1)
    cmds.select(cl=1)
    startFrame = cmds.playbackOptions(q=1, ast=1)
    endFrame = cmds.playbackOptions(q=1, aet=1)
    cmds.playbackOptions(e=1, min=startFrame, max=endFrame)
    frameRange = '(' + str(int(startFrame)) + '-' + str(int(endFrame)) + ')'
    hudNames = ('HUDprojectName', 'HUDscence', 'HUDdate', 'HUDuser', 'HUDframeCount', 'HUDcopyRight', 'HUDframeRate')
    for hudName in hudNames:
        hudVis = cmds.headsUpDisplay(hudName, q=1, ex=1)
        if hudVis == 1:
            cmds.headsUpDisplay(hudName, rem=1)

    cmds.headsUpDisplay('HUDprojectName', s=0, b=7, bs='medium', ao=1, label=projectName, lfs='large')
    cmds.headsUpDisplay('HUDscence', s=1, b=0, bs='medium', label=fileName, lfs='small')
    cmds.headsUpDisplay('HUDdate', s=4, b=6, bs='medium', label=dtaeAndTime, lfs='small')
    cmds.headsUpDisplay('HUDuser', s=5, b=1, bs='small', label=userName, lfs='small')
    cmds.headsUpDisplay('HUDframeCount', s=6, b=0, bs='small', label='Frame ' + frameRange + ' :-', lfs='small', command='cmds.currentTime(q=1)', atr=1)
    cmds.headsUpDisplay('HUDcopyRight', s=7, b=1, bs='small', label=copyRight, lfs='small')
    cmds.headsUpDisplay('HUDframeRate', s=8, b=0, bs='small', label=fpsName, lfs='small')
    mel.eval('displayColor headsUpDisplayLabels -dormant 16;')
    mel.eval('displayColor headsUpDisplayLabels -dormant 16;')
    pbWidth = 900
    pbHeight = 495
    cmds.setAttr('defaultResolution.pixelAspect', 1)
    cmds.setAttr('defaultResolution.width', pbWidth)
    cmds.setAttr('defaultResolution.height', pbHeight)
    cmds.modelEditor(presPanel, e=1, udm=0, da='smoothShaded', displayTextures=1, ao=0)
    movFile = '%s/%s/%s' % (prewPath, fileName.split('.')[0], '.avi')
    cmds.playblast(st=startFrame, et=endFrame, fmt='movie', fo=1, f=movFile, cc=1, v=1, orn=1, p=100, c='none', wh=[pbWidth, pbHeight])
    os.startfile(movFile)
    print movFile


preview()