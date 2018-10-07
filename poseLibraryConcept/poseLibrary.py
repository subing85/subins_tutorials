'''
Pose Library Concept and Development- v0.1
Date: April 11, 2017
Last modified: April 15, 2017
Author: Subin. Gopi
subing85@gmail.com
Copyright 2018 Subin. Gopi - All Rights Reserved.

# WARNING! All changes made in this file will be lost!
'''

import sys
import os
import datetime
import json
import shutil
from functools import partial
import maya.OpenMayaUI as omu
import maya.cmds as cmds

#===============================================================================
# pyqtPath = 'C:/Python27/Lib/site-packages'
# if pyqtPath not in sys.path:
#     sys.path.append(pyqtPath)
#===============================================================================

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import PyQt4.uic as uic
import sip

pyObject = omu.MQtUtil.mainWindow()
mainWindow = sip.wrapinstance(long(pyObject), QtGui.QWidget)

# UI_FILE  = 'Z:/Demo2016/Script/PoseLibrary/ui/poseLibrary_ui.ui'
CURRENT_PATH = os.path.dirname(__file__)
UI_FILE = os.path.join(CURRENT_PATH, 'ui', 'poseLibrary_ui.ui') 

formClass, baseClass = uic.loadUiType(UI_FILE)


class POSELIBRARY(formClass, baseClass):
    
    def __init__(self, parent=mainWindow):
        super(POSELIBRARY, self).__init__(parent)
        self.setupUi(self)
        self.show()

        print '\n\n..................................\nMy Pose Library v0.1'
        print 'Data           : April 11, 2017'
        print 'last modified  : April 15, 2017'
        print 'Author         : Subin Gopi'
        print 'subing85@gmail.com\n..................................\n'

        # Global variables
        self.libraryDirectory = 'Z:/Demo2016/PoseLibrary'
        self.currentDirectory = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
        self.tempDirectory = os.path.abspath(os.getenv('TEMP')).replace('\\', '/')
        self.sanpshotPath = '%s/MyPose_Snapshot.png' % self.tempDirectory
        self.controlDataList = {}
        self.currentMode = 'export'
        self.currentPoseData = None

        # Call functions
        self.uiConfigure()
        self.iconConfigure()
        self.loadFolderStructure(self.libraryDirectory)

    def uiConfigure(self):
        self.setWindowTitle('My Pose Library v0.1')
        self.splitter.setSizes([200, 500, 200])
        self.resize(985, 620)

        # Folder menu
        self.folderMenu = QtGui.QMenu(self)
        self.folderMenu.addAction(self.action_createFolder)
        self.folderMenu.addSeparator()
        self.folderMenu.addAction(self.action_expand)
        self.folderMenu.addAction(self.action_collapse)
        self.folderMenu.addSeparator()
        self.folderMenu.addAction(self.action_rename)        
        self.folderMenu.addAction(self.action_remove)        

        self.action_createFolder.triggered.connect(self.createFolder)
        self.action_expand.triggered.connect(self.expandFolder)
        self.action_collapse.triggered.connect(self.collapseFolder)
        self.action_rename.triggered.connect(self.renameFolder)        
        self.action_remove.triggered.connect(self.removeFolder)

        # Custom Contex Menu
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.onFolderContextMenu)
        self.button_snapShot.clicked.connect(self.takeSnapshot)  # Snapshot of curreent pose        
        self.button_save.clicked.connect(self.savePose)  # Save the current Pose        
        self.treeWidget_folderList.itemClicked.connect(self.loadCurrentFolder)  # Load Pose to UI
        self.button_blendValue.clicked.connect(self.sliderReset)  # Pose blending
        self.slider_poseBlend.valueChanged.connect(self.poseSlider)
        self.lineEdit_poseLabel.returnPressed.connect(self.renamePose)  # Rename Pose
        self.switchToExportImport('export')
    
    def iconConfigure(self):  # Connect Icon to Widgets
        menuList = self.findChildren(QtGui.QAction)
        for index in range(len(menuList)):
            objectName = menuList[index].objectName()
            if objectName:
                currentIcon = objectName.split('_')[1]                
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('%s/icons/%s.png' % (self.currentDirectory, currentIcon)), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)                
                menuList[index].setIcon(icon)
    
    def onFolderContextMenu(self, paint):  # ContextMenu - treeWidget_folderList
        self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(paint))
    
    def loadFolderStructure(self, path):  # Load Exists Folder structure to QTreeWidget(treeWidget_folderList)
        self.treeWidget_folderList.clear()
        directoryList = self.getFolderStructure(path)
        self.folderPath = path
        self.loadFolderToTreeWidget(directoryList[path], self.treeWidget_folderList, path)        
    
    def loadFolderToTreeWidget(self, directoryList, parent, path):  # Load folder structure to QTreeWidget
        for eachDirectory in directoryList:
            if eachDirectory:
                self.folderPath = '%s/%s' % (path, eachDirectory)
                item = QtGui.QTreeWidgetItem(parent)
                item.setText(0, eachDirectory)
                item.setToolTip(0, self.folderPath)
                # Connect Icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('%s/icons/folder.png' % self.currentDirectory), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(0, icon)
                self.loadFolderToTreeWidget(directoryList[eachDirectory], item, self.folderPath)
        self.folderPath = path
    
    def getFolderStructure(self, path):  # Collect Folder structure
        directoryList = {}
        for root, dirs, files in os.walk(path):
            folderList = root.split(os.sep)
            folders = directoryList
            for eachFolder in folderList:
                folders = folders.setdefault(eachFolder, {})               
        return directoryList        
    
    def createFolder(self):  # Create New Folder
        folderName, ok = QtGui.QInputDialog.getText(self,
                                                    'Folder Name',
                                                    'Enter the folder name:',
                                                    QtGui.QLineEdit.Normal)
        if ok:
            parent = self.treeWidget_folderList
            currentPath = self.libraryDirectory
            if self.treeWidget_folderList.selectedItems():
                parent = self.treeWidget_folderList.selectedItems()[-1]
                currentPath = str(parent.toolTip(0))

            if not os.path.isdir('%s/%s' % (currentPath, str(folderName))):                
                item = QtGui.QTreeWidgetItem(parent)
                item.setText(0, str(folderName))
                item.setToolTip(0, '%s/%s' % (currentPath, str(folderName)))

                # Connect Icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('%s/icons/folder.png' % self.currentDirectory),
                               QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                if parent != self.treeWidget_folderList:
                    self.treeWidget_folderList.setItemExpanded(parent, 1)                    
                    self.treeWidget_folderList.setItemSelected(parent, 0)
                    
                self.treeWidget_folderList.setItemSelected(item, 1)
                os.makedirs('%s/%s' % (currentPath, str(folderName)))
    
    def expandFolder(self):  # Expand the QTreeWidget 
        if self.treeWidget_folderList.selectedItems():
            currentItem = self.treeWidget_folderList.selectedItems()[-1]
            self.dependentList = [currentItem]
            self.collectChildItems(currentItem)
            for eachDependent in self.dependentList:
                self.treeWidget_folderList.setItemExpanded(eachDependent, 1)
        else:
            self.treeWidget_folderList.expandAll()

    def collapseFolder(self):  # Collapse the QTreeWidget 
        currentItem = self.treeWidget_folderList.invisibleRootItem()        
        if self.treeWidget_folderList.selectedItems():            
            currentItem = self.treeWidget_folderList.selectedItems()[-1]
            
        self.dependentList = [currentItem]
        self.collectChildItems(currentItem)
        for eachDependent in self.dependentList:                
            self.treeWidget_folderList.collapseItem(eachDependent)
    
    def renameFolder(self):  # Rename selected folder
        selectedItems = self.treeWidget_folderList.selectedItems()
        if selectedItems:
            newName, ok = QtGui.QInputDialog.getText(self,
                                                     'Folder Name',
                                                     'Enter the new name:',
                                                      QtGui.QLineEdit.Normal)
            if ok:                
                currentFolderPath = str(selectedItems[-1].toolTip(0))                
                newFolderPath = '%s/%s' % (os.path.dirname(currentFolderPath), str(newName))

                replay = 0
                try:
                    os.chmod(currentFolderPath, 0777)
                    os.rename(currentFolderPath, newFolderPath)
                    replay = 1
                except Exception, result:
                    replay = 0
                    print result

                if replay == 1:
                    selectedItems[-1].setText(0, newName)
                    selectedItems[-1].setToolTip(0, newFolderPath)
                # self.loadFolderStructure(self.libraryDirectory)
        else:
            QtGui.QMessageBox.warning(self,
                                      'Warning',
                                      'No folder selected\nPlease select the folder',
                                       QtGui.QMessageBox.Ok)
            print 'No folder selected\t- Please select the folder'

    def removeFolder(self):  # Remove Selected folder
        selectedItems = self.treeWidget_folderList.selectedItems()
        if selectedItems:
            replay = QtGui.QMessageBox.question(self,
                                                'Question',
                                                'Are you sure, you want to remove folder',
                                                QtGui.QMessageBox.Yes,
                                                QtGui.QMessageBox.No)
            if replay == QtGui.QMessageBox.Yes:
                for eachItem in selectedItems:
                    folderPath = str(eachItem.toolTip(0))
                    try:
                        os.chmod(folderPath, 0777)
                        shutil.rmtree(folderPath)
                        print 'Removed\t', folderPath
                    except Exception, result:
                        print result
                self.loadFolderStructure(self.libraryDirectory)
        else:
            QtGui.QMessageBox.warning(self,
                                      'Warning',
                                      'No folder selected\nPlease select the folder',
                                       QtGui.QMessageBox.Ok)
            print 'No folder selected\t- Please select the folder'  
            
    def collectChildItems(self, parent):  
        # Collect all dependent child from parent QTreeWidget Item
        for index in range(parent.childCount()):
            currentChild = parent.child(index)
            self.dependentList.append(currentChild)
            self.collectChildItems(currentChild)
    
    def takeSnapshot(self):  # Take snapshot of current pose
        if self.currentMode == 'export':
            if os.path.isfile(self.sanpshotPath):
                try:
                    os.chmod(self.sanpshotPath, 0777)
                    os.remove(self.sanpshotPath)
                except Exception, result:
                    print result

            modelPanelList = cmds.getPanel(type='modelPanel')
            for eachModelPanel in modelPanelList:
                cmds.modelEditor(eachModelPanel, e=1, alo=0)
                cmds.modelEditor(eachModelPanel, e=1, pm=1)            
            currentFrame = cmds.currentTime(q=1)      
            playBlast = cmds.playblast(st=currentFrame, et=currentFrame, fmt='image',
                                                  cc=1, v=0, orn=0, fp=1, p=100, c='png', wh=[512, 512],
                                                  cf=self.sanpshotPath)
            self.loadImageToButton(self.button_snapShot, self.sanpshotPath, [150, 150])
            cmds.modelEditor(eachModelPanel, e=1, nc=1)         
            cmds.modelEditor(eachModelPanel, e=1, ns=1)         

    def loadImageToButton(self, button, path, size):  # Load Image to button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(size[0], size[1]))

    def savePose(self):  # Save the current Pose
        poseLabel = str(self.lineEdit_poseLabel.text())
        if not poseLabel:
            QtGui.QMessageBox.warning(self,
                                      'Warning',
                                      'No pose name specified\nPlease set the name before saving',
                                      QtGui.QMessageBox.Ok)
            print 'No pose name specified\t- Please set the name before saving'
            return
                    
        currentItem = self.treeWidget_folderList.selectedItems()
        if not currentItem:
            QtGui.QMessageBox.warning(self,
                                      'Warning',
                                      'No folder selected\nPlease select the folder',
                                       QtGui.QMessageBox.Ok)
            print 'No folder selected\t- Please select the folder'            
            return            
            
        # 1.Export the pose data to custom format. #Collect selected Control attribute and attribute values
        selectionList = cmds.ls(sl=1)
        if not selectionList: 
            QtGui.QMessageBox.warning(self, 'Warning', 'No controls selected\nPlease select at least one control',
                                       QtGui.QMessageBox.Ok)
            print 'No controls selected\t- Please select at least one control'
            return
           
        controlInfoList = {}
        for eachSelection in selectionList:    
            attributeList = cmds.listAttr(eachSelection, k=1, u=1, sn=1)    
            attributeInfoList = {}     
            if attributeList:  
                for eachAttribute in attributeList:
                    attriValue = cmds.getAttr('%s.%s' % (eachSelection, eachAttribute))
                    attributeInfoList.setdefault(eachAttribute.encode(), attriValue)
                currentControl = eachSelection
                # Check the Reference        
                if cmds.referenceQuery(eachSelection, inr=1):
                    referencePath = cmds.referenceQuery(eachSelection, f=1)
                    nameSpace = cmds.file(referencePath, q=1, ns=1)
                    currentControl = eachSelection.replace('%s:' % nameSpace, '')            
                controlInfoList.setdefault(currentControl.encode(), attributeInfoList)                    
        # print  controlInfoList

        # Data history
        owner = os.getenv('USERNAME')
        time = datetime.datetime.now().strftime("%A, %B %d, %Y %H:%M %p")
        mayaVersion = cmds.about(q=1, v=1)
        version = '0.1'
        dataList = {'control':controlInfoList, 'history':[owner, time, mayaVersion, version]}

        # Write Pose Data
        # dataPath = '%s/%s.pose'%(self.libraryDirectory, poseLabel)
        currentFolderPath = str(currentItem[-1].toolTip(0))
        dataPath = '%s/%s.pose' % (currentFolderPath, poseLabel)

        if os.path.isfile(dataPath):
            try:
                os.chmod(dataPath, 0777)
                os.remove(dataPath)
            except Exception, result:
                print result
                
        # Write Data
        poseData = open(dataPath, 'w')
        jsonData = json.dumps(dataList, indent=4)
        poseData.write(jsonData)
        poseData.close()
        
        # Pose Icon
        currentPoseIcon = self.sanpshotPath                    
        if not os.path.isfile(currentPoseIcon):
            currentPoseIcon = '%s/icons/poseTemplate.png' % self.currentDirectory                    
        currentPosePath = dataPath.replace('.pose', '.png')

        if currentPoseIcon == '%s/icons/poseTemplate.png' % self.currentDirectory:
            try:
                shutil.copy2(currentPoseIcon, currentPosePath)
            except Exception, result:
                print result
        else:                    
            try:
                shutil.move(currentPoseIcon, currentPosePath)
            except Exception, result:
                print result
                
        # self.lineEdit_poseLabel.clear()
        # self.loadImageToButton(self.button_snapShot, currentPosePath, [150,150])
        self.loadCurrentFolder()                    
        print 'Successfully export My Pose Data.'

    def loadCurrentFolder(self):  # Load Pose to UI
        currentItems = self.treeWidget_folderList.selectedItems()
        # Add Child items with selected QTree Item
        self.dependentList = []        
        for eachItems in currentItems:
            self.dependentList.append(eachItems)
            self.collectChildItems(eachItems)
            
        self.removeExistWidget(self.gridLayout_poseList)
        self.loadPoseToLayout(self.dependentList)
        self.switchToExportImport('export')
    
    def removeExistWidget(self, layout):  # Remove exists widget from Layout
        for index in range(layout.count()):
            if layout.itemAt(index).widget():
                layout.itemAt(index).widget().deleteLater()
    
    def loadPoseToLayout(self, itemList):  # Load pose to layout
        poseList = []
        for eachItem in itemList:
            currentPath = str(eachItem.toolTip(0))
            if not os.path.isdir(currentPath):
                continue
            directoryList = os.listdir(currentPath)
            for eachFile in directoryList:
                if not os.path.isfile('%s/%s' % (currentPath, eachFile)):
                    continue
                if not eachFile.endswith('.pose'):
                    continue
                poseList.append('%s/%s' % (currentPath, eachFile))

        row = -1
        column = 0
        coordinateList = []
        for index in range(len(poseList)):            
            if index % 3:
                column += 1        
                coordinateList.append([row, column])
            else:
                row += 1
                column = 0
                coordinateList.append([row, column])
                       
        for index in range(len(poseList)):
            poseLabel = os.path.splitext(os.path.basename(poseList[index]))[0]            
            toolButton = QtGui.QToolButton(self.scrollAreaWidget_pose)
            toolButton.setObjectName('toolButton_%s' % poseLabel)
            toolButton.setText(poseLabel)
            toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            toolButton.setMinimumSize(QtCore.QSize(170, 170))
            toolButton.setMaximumSize(QtCore.QSize(170, 170))

            poseIconPath = poseList[index].replace('.pose', '.png')

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(poseIconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            toolButton.setIcon(icon)
            toolButton.setIconSize(QtCore.QSize(140, 140))
            self.gridLayout_poseList.addWidget(toolButton, coordinateList[index][0], coordinateList[index][1], 1, 1)
            toolButton.clicked.connect(partial(self.setCurrentPose, poseList[index]))
    
    def setCurrentPose(self, posePath):  # Set the Pose to charcter
        # 2. Import the pose data to scene.
        readData = open(posePath, 'r')
        dataList = json.load(readData)

        selectionList = cmds.ls(sl=1)

        self.controlDataList = {}
        print self.controlDataList

        for eachSelection in selectionList:            
            currentControl = eachSelection
            if cmds.referenceQuery(eachSelection, inr=1):  
                referencePath = cmds.referenceQuery(eachSelection, f=1)
                nameSpace = cmds.file(referencePath, q=1, ns=1)    
                currentControl = eachSelection.replace('%s:' % nameSpace, '')

            if currentControl in dataList['control']:
                attributeList = dataList['control'][currentControl]
                for eachAttribute in attributeList:            
                    poseValue = attributeList[eachAttribute]
                    currentValue = cmds.getAttr('%s.%s' % (eachSelection, eachAttribute))
                    # cmds.setAttr('%s.%s'%(eachSelection, eachAttribute), attributeValue)
                    self.controlDataList.setdefault('%s.%s' % (eachSelection, eachAttribute), [currentValue, poseValue])

        print self.controlDataList
        currentIconPath = posePath.replace('.pose', '.png')       
        self.loadImageToButton(self.button_snapShot, currentIconPath, [150, 150])
        currentPoseLabel = os.path.splitext(os.path.basename(posePath))[0] 
        self.lineEdit_poseLabel.setText(currentPoseLabel)

        # Load history
        historyData = dataList['history']
        historyList = ['Owner%s: %s' % ('\t'.rjust(5), historyData[0]),
                               'Created%s: %s' % ('\t'.rjust(5), historyData[1]),
                               'Maya version%s: %s' % ('\t'.rjust(5), historyData[2]),
                               'Module Version%s: %s' % ('\t'.rjust(5), historyData[3])
                               ]                               
        self.textEdit_history.setText('\n'.join(historyList))
        # self.slider_poseBlend.setValue(100)
        self.poseSlider()
        self.switchToExportImport('import')
        self.currentPoseData = posePath
        print '#Successfully import My Pose'

    def sliderReset(self):
        self.slider_poseBlend.setValue(100)
                
    def poseSlider(self):
        sliderValue = self.slider_poseBlend.value()
        self.button_blendValue.setText(str(sliderValue))
        self.poseBlending()

    def poseBlending(self):
        if not self.controlDataList:
            return
        sliderValue = float(self.slider_poseBlend.value())

        for eachControl in self.controlDataList:
            currentValue = self.controlDataList[eachControl][0]
            poseValue = self.controlDataList[eachControl][1]
            
            length = poseValue - currentValue
            percentage = (length * sliderValue) / 100.00
            setValue = currentValue + percentage
            cmds.setAttr(eachControl, setValue)
    
    def switchToExportImport(self, mode):  # Pose Export and import Mode
        self.button_save.hide()
        self.groupBox_blend.hide()

        if mode == 'export':
            self.lineEdit_poseLabel.clear()
            self.textEdit_history.clear()
            self.button_save.show()
            self.loadImageToButton(self.button_snapShot, '%s/icons/snapshot.png' % self.currentDirectory, [150, 150])
            self.currentMode = 'export'

        if mode == 'import':
            self.groupBox_blend.show()
            self.currentMode = 'import'

    def renamePose(self):  # Rename Pose
          
        if self.currentMode != 'import':
            return
        if not self.currentPoseData:
            return
        
        newPoseLabel = str(self.lineEdit_poseLabel.text())
        if newPoseLabel:
            newPosePath = '%s/%s.pose' % (os.path.dirname(self.currentPoseData), newPoseLabel)
            existsIconPath = self.currentPoseData.replace('.pose', '.png')
            newIconPath = newPosePath.replace('.pose', '.png')

            if os.path.isfile(self.currentPoseData):
                try:
                    os.chmod(self.currentPoseData, 0777)
                    os.rename(self.currentPoseData, newPosePath)
                except Exception, result:
                    print result
                
                if os.path.isfile(existsIconPath):
                    try:
                        os.chmod(existsIconPath, 0777)
                        os.rename(existsIconPath, newIconPath)
                    except Exception, result:
                        print result       

                self.loadCurrentFolder()
                
#End ###############################################################################################################                
