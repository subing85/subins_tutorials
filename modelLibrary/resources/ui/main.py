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

reload(platforms)
reload(catalogue)
reload(resources)


class MainWindow(QtGui.QMainWindow):

    # def __init__(self, parent=platforms.get_qwidget()):
    def __init__(self, parent=None):        
        super(MainWindow, self).__init__(parent)       
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
        self.menu_file.addAction(self.action_remove)
        self.menu_file.addAction(self.action_rename)
        self.menu_file.addSeparator()        
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_preferences)
        self.menu_help.addAction(self.action_aboutool)
        self.menu_help.addAction(self.action_abouttoolkits)
        
    
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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
