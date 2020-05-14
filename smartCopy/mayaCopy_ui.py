'''
Smart Copy - v0.1
Date : August 20, 2016
Last modified: August 20, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.

from smartCopy import mayaCopy_ui
reload(mayaCopy_ui)
mayaCopy_ui.runMayaUiDemo()

# WARNING! All changes made in this file will be lost!
'''

import os
import warnings
from PySide import QtCore
from PySide import QtGui
from shiboken import wrapInstance
from functools import partial
from maya import OpenMayaUI as openMayaUI
from maya import OpenMaya as openMaya
from pymel import core as pymel
from smartCopy import mayaPose   
from smartCopy import mayaAnim 
from smartCopy import mayaWrite       
reload(mayaPose)
reload(mayaWrite)
reload(mayaAnim)

MAYA_MAIN_WINOW = wrapInstance(long(openMayaUI.MQtUtil.mainWindow()), QtGui.QWidget)


def runMayaUiDemo():
    
    '''
    Description            
        Function for load the class and delete the exists 'UI' in the scene.
        
        :Type - standalone function        
        :param    None        
        :return   None        
        :example to execute        
            from assets import assetTool
            reload(assetTool)
            wind = assetTool.runMayaUiDemo()   
            wind.show()     
    '''    
    
    if (pymel.window("MainWindow_poseCopy", ex=True)):
        pymel.deleteUI ('MainWindow_poseCopy')       
    
    wind = UI_MainWindow()


class UI_MainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=MAYA_MAIN_WINOW):
        
        super(UI_MainWindow, self).__init__(parent)
        
        self.setupUi() 
        
        self.poseFile = os.path.abspath (os.path.join(os.getenv('TEMP'), 'subin_pose.pose')).replace ('\\', '/')   
        self.animFile = os.path.abspath (os.path.join(os.getenv('TEMP'), 'subin_anim.anim')).replace ('\\', '/') 
    
    def setupUi(self):
        
        # Create QMainWindow        
        # self = QtGui.QMainWindow (parent=MAYA_MAIN_WINOW)
        self.setWindowTitle ('Pose and Animation Copy v0.1')
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')
        self.setObjectName ('MainWindow_poseCopy')        
        self.resize (350, 160)

        # QWidget        
        self.centralWidget = QtGui.QWidget (parent=self)
        self.centralWidget.setObjectName ('centralWidget')
        
        # QVBoxLaout (verticalLayout)        
        self.verticalLayout = QtGui.QVBoxLayout (self.centralWidget)
        self.verticalLayout.setObjectName ('verticalLayout') 
        
        # Group box
        self.groupBox = QtGui.QGroupBox (parent=self)
        self.groupBox.setObjectName ('groupBox_category')
        self.groupBox.setGeometry (QtCore.QRect(10, 10, 280, 60))
        # self.groupBox.setTitle ('Categories')        
        self.verticalLayout.addWidget (self.groupBox)
        
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName('gridLayout')
        
        # QHBoxLayout (horizontalLayout)        
        self.horizontalLayout = QtGui.QHBoxLayout (self.groupBox)
        self.horizontalLayout.setObjectName ('horizontalLayout')  
        
        # QPushButton                
        self.button_copyPose = QtGui.QPushButton(self.groupBox)
        self.button_copyPose.setObjectName('button_copyPose')
        self.button_copyPose.setText("Copy Pose")        
        self.gridLayout.addWidget(self.button_copyPose, 0, 0, 1, 1)               
               
        self.button_pastePose = QtGui.QPushButton(self.groupBox)
        self.button_pastePose.setObjectName('button_pastePose')
        self.button_pastePose.setText('Paste Pose')
        self.gridLayout.addWidget(self.button_pastePose, 0, 1, 1, 1)    
        
        self.button_copyAnim = QtGui.QPushButton(self.groupBox)
        self.button_copyAnim.setObjectName('button_copyAnim')
        self.button_copyAnim.setText('Copy Animation')    
        self.button_copyAnim.setStyleSheet('color: rgb(170, 0, 0);')             
        self.gridLayout.addWidget(self.button_copyAnim, 1, 0, 1, 1)               
               
        self.button_pasteAnim = QtGui.QPushButton(self.groupBox)
        self.button_pasteAnim.setObjectName('button_pasteAnim')
        self.button_pasteAnim.setText('Paste Animation')     
        self.button_pasteAnim.setStyleSheet('color: rgb(170, 0, 0);')           
        self.gridLayout.addWidget(self.button_pasteAnim, 1, 1, 1, 1)   

        self.label = QtGui.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setText('Author: Subin. Gopi\nsubing85@gmail.com\nCopyright 2018 Subin. Gopi - All Rights Reserved.')        
        self.label.setObjectName('label')
        self.label.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";background-color: rgb(100, 100, 100);')        
        
        self.verticalLayout.addWidget(self.label)
        self.setCentralWidget (self.centralWidget)
        
        self.button_copyPose.clicked.connect(partial (self.myCopy, 'pose'))
        self.button_pastePose.clicked.connect(partial (self.myPaste, 'pose'))
        self.button_copyAnim.clicked.connect(partial (self.myCopy, 'animation'))
        self.button_pasteAnim.clicked.connect(partial (self.myPaste, 'animation'))
        
        self.show()
        
    def myCopy(self, value):        
       
        objects = pymel.ls(sl=True) 
        
        if not objects:
            warnings.warn('#nyour selection is empty.')
            return None
        
        if value == 'pose':   
            mp = mayaPose.MayaPose(objects=objects)
            poseData = mp.copy() 
                       
            mw = mayaWrite.MayaWrite(self.poseFile, 'Pose')
            mw.mWrite(dataContent=poseData) 
            openMaya.MGlobal.displayInfo ('#Thanks, Pose copy done!')            
        
        if value == 'animation':            
            ma = mayaAnim.MayaAnim(objects=objects)      
            animData = ma.copy()
            
            mw = mayaWrite.MayaWrite(self.animFile, 'Anim')
            mw.mWrite(dataContent=animData) 
            openMaya.MGlobal.displayInfo ('#Thanks, Animation copy done!')
            
        pymel.select (objects)     
        
    def myPaste(self, value):
        
        objects = pymel.ls(sl=1) 
        
        if not objects:
            warnings.warn('#nyour selection is empty.')
            return None
        
        if value == 'pose':
            mw = mayaWrite.MayaWrite(self.poseFile, None)            
            mw.mRead()  
              
            mp = mayaPose.MayaPose(objects=objects)          
            mp.paste(dataContent=mw._fileData)
            openMaya.MGlobal.displayInfo ('#Thanks, Pose paste done!')
            
        if value == 'animation':
            mw = mayaWrite.MayaWrite(self.animFile, None)            
            mw.mRead()    

            ma = mayaAnim.MayaAnim(objects=objects)                      
            ma.paste(dataContent=mw._fileData)
            openMaya.MGlobal.displayInfo ('#Thanks, Animation paste done!')
            
        pymel.select (objects) 
        
#End###########################################################################################################
