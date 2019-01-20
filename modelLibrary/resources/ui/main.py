'''
main.py 0.0.1 
Date: January 01, 2019
Last modified: January 15, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''


import os
import sys
import webbrowser

from pprint import pprint

path = '/mnt/venture/subins_tutorials'

if path not in sys.path:
    sys.path.append(path)

from PySide import QtCore
from PySide import QtGui
from functools import partial

from maya import OpenMaya
from maya import cmds

from modelLibrary import resources
from modelLibrary.resources.ui import catalogue
from modelLibrary.resources.ui import model
from modelLibrary.utils import platforms

from modelLibrary.resources.ui import preferences
from modelLibrary.modules import readWrite
from modelLibrary.modules import studioFolder

reload(model)
reload(platforms)
reload(catalogue)
reload(resources)
reload(preferences)
reload(readWrite)
reload(studioFolder)


class MainWindow(QtGui.QMainWindow):

    # def __init__(self, parent=platforms.get_qwidget()):
    def __init__(self, parent=None):        
        super(MainWindow, self).__init__(parent)
        
        # to check the preferencees        
        rw = readWrite.ReadWrite(t='preference')
        rw.file_path = os.path.join(rw.path, 'library_preferences.%s' % rw.extention)
        self.bundles = rw.get()               
        if not self.bundles:
            self.preferences()
            
        self.library_path = None        
        if '0' in self.bundles:            
            self.library_path = self.bundles['0'] 
            
        self.folder = studioFolder.Folder(path=self.library_path)            
            
                    
        self.catalogue = catalogue.Catalogue(parent=None)
        self.model = model.Model(parent=None)
              
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [900, 500]

        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)
        self.setup_ui()
        # self.parent_maya_layout()        
        self.set_icons()
        
        self.load_library_folders(self.treewidget)
        


    def setup_ui(self):
        self.resize(self.width, self.height)
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')        
        self.setObjectName('model_library')
        self.setWindowTitle(self.tool_kit_titile)
        
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.addWidget(self.catalogue.splitter)

        self.catalogue.splitter.addWidget(self.model.groupbox_model)
        self.catalogue.splitter.setSizes([200, 500, 200])
        
        self.treewidget = self.catalogue.treewidget_folder        
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(partial (self.on_context_menu, self.treewidget))
        self.treewidget.itemClicked.connect(partial (self.load_current_folder, self.treewidget))  # Load Pose to UI
        
        self.menu_bar = QtGui.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 960, 25))
        self.menu_bar.setObjectName('menu_bar')
        self.setMenuBar(self.menu_bar)
        
        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName('menu_file')
        self.menu_file.setTitle('File')        
        
        self.menu_settings = QtGui.QMenu(self.menu_bar)
        self.menu_settings.setObjectName('menu_settings')
        self.menu_settings.setTitle('Settings')       
        
        self.menu_help = QtGui.QMenu(self.menu_bar)
        self.menu_help.setObjectName('menu_help')
        self.menu_help.setTitle('Help')               

        self.action_create = QtGui.QAction(self)
        self.action_create.setObjectName('action_create')
        self.action_create.setText('Create Folder')      
        
        self.action_remove = QtGui.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove Folder')

        self.action_rename = QtGui.QAction(self)
        self.action_rename.setObjectName('action_rename')
        self.action_rename.setText('Rename Folder')
        
        self.action_quit = QtGui.QAction(self)
        self.action_quit.setObjectName('action_quit')
        self.action_quit.setText('Quit')
        
        self.action_preferences = QtGui.QAction(self)
        self.action_preferences.setObjectName('action_preferences')
        self.action_preferences.setText('Preferences')        
        
        self.action_aboutool = QtGui.QAction(self)
        self.action_aboutool.setObjectName('action_aboutool')
        self.action_aboutool.setText('About Tool')        
        
        self.action_abouttoolkits = QtGui.QAction(self)
        self.action_abouttoolkits.setObjectName('action_abouttoolkits')
        self.action_abouttoolkits.setText('About Tool Kits') 
        
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())          
        
        self.menu_file.addAction(self.action_create)          
        self.menu_file.addAction(self.action_rename)
        self.menu_file.addAction(self.action_remove)        
        self.menu_file.addSeparator()        
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_preferences)
        self.menu_help.addAction(self.action_aboutool)
        self.menu_help.addAction(self.action_abouttoolkits)
        
        self.contex_menu = QtGui.QMenu(self)
        self.contex_menu.addAction(self.action_create)          
        self.contex_menu.addAction(self.action_rename)        
        self.contex_menu.addAction(self.action_remove)

        self.action_preferences.triggered.connect(self.preferences)
        self.action_create.triggered.connect(self.create)
        self.action_rename.triggered.connect(self.rename)
        self.action_remove.triggered.connect(self.remove)
        self.action_quit.triggered.connect(self.close)
        
    
    def set_icons(self):
        actions = self.findChildren(QtGui.QAction)
        for each_action in actions:
            objectName = each_action.objectName()
            if not objectName:
                continue           
            
            current_icon = '{}.png'.format(objectName.split('_')[-1]) 
            icon_path = os.path.join(resources.getIconPath(), current_icon)              
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)                
            each_action.setIcon(icon)

    def toolkit_link(self):
        webbrowser.BaseBrowser(resources.getToolKitLink())
        OpenMaya.MGlobal.displayInfo(resources.getToolKitLink())

    def toolkit_help_link(self):
        webbrowser.open(resources.getToolKitHelpLink())
        OpenMaya.MGlobal.displayInfo(resources.getToolKitHelpLink())

    def parent_maya_layout(self):
        object_name = str(self.objectName())
        self.floating_layout = cmds.paneLayout(
            cn='single', w=self.width, p=platforms.get_main_window())
        cmds.dockControl(self.tool_kit_object, l=self.tool_kit_titile, area='right',
                         content=self.floating_layout, allowedArea=['right', 'left'])
        cmds.control(object_name, e=1, p=self.floating_layout)
        
    def preferences(self): 
        self.hide()
        preference_window = preferences.Preference(parent=None, child=self)
        preference_window.show()        
    
    def on_context_menu(self, treewidget, paint):
        self.contex_menu.exec_(treewidget.mapToGlobal(paint))
        
    def create(self):
        folder_name, ok = QtGui.QInputDialog.getText(self, 'Input', 'Enter the folder name:', QtGui.QLineEdit.Normal)
        if not ok:
            OpenMaya.MGlobal.displayWarning('abort the folder creation!...')
            return   
        current_path = folder_name    
        if self.treewidget.selectedItems():
            current_item = self.treewidget.selectedItems()[-1]
            tool_tip = str(current_item.toolTip(0))            
            current_path = '{}/{}'.format(tool_tip, folder_name)        
        result, message = self.folder.create(basename=current_path)        
        if not result:
            QtGui.QMessageBox.warning(self, 'Warning', message, QtGui.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Create folder  - faild!...')
            return
                
        self.folder.load_folder_structure(self.treewidget)        
        OpenMaya.MGlobal.displayInfo('\"%s\" Folder create - success!...' % message)  
        
    
    def rename(self):
        folder_name, ok = QtGui.QInputDialog.getText(self, 'Input', 'Enter the new name:', QtGui.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        
        if not self.treewidget.selectedItems():
            QtGui.QMessageBox.warning(self, 'Warning', 'Not found any selection\nSelect the folder and try', QtGui.QMessageBox.Ok)
            return            
            
        current_item = self.treewidget.selectedItems()[-1]
        tool_tip = str(current_item.toolTip(0))            
        result, message = self.folder.rename(basename=tool_tip, name=folder_name)
        if not result:
            QtGui.QMessageBox.warning(self, 'Warning', message, QtGui.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Rename folder - faild!...')
            return          
        
        self.folder.load_folder_structure(self.treewidget)        
        OpenMaya.MGlobal.displayInfo('\"%s\" Rename folder - success!...' % message)                       
    
    def remove(self):
        
        if not self.treewidget.selectedItems():
            QtGui.QMessageBox.warning(self, 'Warning', 'Not found any selection\nSelect the folder and try', QtGui.QMessageBox.Ok)
            return
        
        replay = QtGui.QMessageBox.question(self, 'Question', 'Are you sure, you want to remove folder', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)        
    
        if replay == QtGui.QMessageBox.No:
            OpenMaya.MGlobal.displayWarning('abort the remove folder!...')
            return       
            
        current_item = self.treewidget.selectedItems()[-1]
        tool_tip = str(current_item.toolTip(0))            
        result, message = self.folder.remove(basename=tool_tip)
        
        if not result:
            QtGui.QMessageBox.warning(self, 'Warning', message, QtGui.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Remove folder - faild!...')
            return          
        
        self.folder.load_folder_structure(self.treewidget)        
        OpenMaya.MGlobal.displayInfo('\"%s\" Remove folder - success!...' % message)    


        
    def load_library_folders(self, treewidget):
        data = self.folder.get_folder_structure()
        self.folder.set_folder_structure(data, parent=treewidget)
        
    def load_current_folder(self, treewidget, *args):        
        current_items = treewidget.selectedItems()
        paths = []
        for each_items in current_items:            
            tool_tip = each_items.toolTip(0)
            current_path = os.path.join(self.library_path, tool_tip)            
            paths.append(current_path)
            
        self.model.groupbox_model.setStatusTip('\n'.join(paths))    

        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
