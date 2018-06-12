'''
Animation Playblast Script- v0.1
Date : March 25, 2017
Last modified: March 25, 2017
Author: Subin. Gopi
subing85@gmail.com
Copyright 2018 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

#

import maya.cmds as cmds
import maya.mel as mel
import os
import datetime

#Set the camera
currentCamera = 'Animation_CameraShape'

#Delete unused UIs
uiList = cmds.lsUI (wnd=1)
for eachUi in uiList :
    if eachUi!='MayaWindow' :
        try :
            cmds.deleteUI (eachUi)
        except Exception, result :
            print result    

mel.eval ('setNamedPanelLayout "Single Perspective View";') 
cmds.lookThru (currentCamera, 'prespView')
cmds.setAttr ('%s.displayResolution'% currentCamera, 1) 
cmds.setAttr ('%s.displayGateMaskColor'% currentCamera, 0.3, 0.0, 0.0, type='double3')
cmds.setAttr ('%s.overscan'% currentCamera, 1.1) 

modelPanelList = cmds.getPanel (typ='modelPanel')

for eachModelPanel in modelPanelList :
    cmds.modelEditor (eachModelPanel, e=1, allObjects=0)
    cmds.modelEditor (eachModelPanel, e=1, polymeshes=1)
    
#Collect shot details    
projectName = 'The Wolf'
shotName = os.path.splitext (cmds.file (q=1, sn=1, shn=1))[0]
time = datetime.datetime.now ().strftime("%A, %B %d, %Y %H:%M %p")
userName = os.getenv ('USERNAME')

startTime = int (cmds.playbackOptions (q=1, min=1))
endTime = int (cmds.playbackOptions (q=1, max=1))
timeLable = 'Farme  [ %i - %i ]'% (startTime, endTime)
currentFps = mel.eval ('currentTimeUnitToFPS')

#Remove Exists headsUpDisplay
headsUpDisplayList = cmds.headsUpDisplay (q=1, lh=1)

if headsUpDisplayList :
    for eachHeadsUpDisplay in headsUpDisplayList :
        cmds.headsUpDisplay (eachHeadsUpDisplay, rem=1)    
    
#Set HeadsUp Display
cmds.headsUpDisplay ('HUDProjectName', s=0, b=0, bs='large', lfs='large', l=projectName)
cmds.headsUpDisplay ('HUDShotName', s=2, b=0, bs='large', lfs='small', l=shotName)
cmds.headsUpDisplay ('HUDTime', s=4, b=0, bs='large', lfs='small', l=time)
cmds.headsUpDisplay ('HUDUserName', s=5, b=0, bs='small', lfs='small', l=userName)
cmds.headsUpDisplay ('HUDFrame', s=6, b=0, bs='small', lfs='small', l=timeLable, c='cmds.currentTime (q=1)', atr=1)
cmds.headsUpDisplay ('HUDMyLabel', s=7, b=0, bs='small', lfs='small', l='Copyright 2017 Subin. Gopi - All Rights Reserved')
cmds.headsUpDisplay ('HUDFps', s=9, b=0, bs='small', lfs='small', l='Fps- %s'% currentFps)

#Set the Playback Option
sTime = cmds.playbackOptions (q=1, ast=1)
eTime = cmds.playbackOptions (q=1, aet=1)
cmds.playbackOptions (e=1, min=sTime, max=eTime)

mayaFilePath = cmds.file (q=1, sn=1)
moviePath = '%s/%s.mov'% (os.path.dirname (mayaFilePath), shotName)

if os.path.isfile (moviePath) :
    try :
        os.chmod (moviePath, 0777)
        os.remove (moviePath)
    except Exception, result :
        print result
        
cmds.select (cl=1) 

currentPanel = cmds.getPanel (wf=1)
try :
    cmds.modelEditor (currentPanel, e=1, udm=0, da='smoothShaded', dtx=1, ao=0)
except Exception, result :
    print result
        
playblastFile = cmds.playblast (st=sTime, et=eTime, fmt='qt', f=moviePath, cc=1, v=1, orn=1, p=100, c='H.264', quality=100, wh=[1280,720])

#Remove Exists headsUpDisplay
headsUpDisplayList = cmds.headsUpDisplay (q=1, lh=1)

if headsUpDisplayList :
    for eachHeadsUpDisplay in headsUpDisplayList :
        cmds.headsUpDisplay (eachHeadsUpDisplay, rem=1)  

#Set all model panel to boundingBox
for eachModelPanel in modelPanelList :
    #cmds.modelEditor (eachModelPanel, e=1, allObjects=0)
    cmds.modelEditor (eachModelPanel, e=1, da='boundingBox')    
    
print '#Successfully created Playblast movie\t- %s'% playblastFile

#End#############################################################################
