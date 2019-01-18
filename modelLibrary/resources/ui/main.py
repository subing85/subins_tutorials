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
