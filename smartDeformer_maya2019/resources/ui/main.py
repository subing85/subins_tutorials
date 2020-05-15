'''
main.py 0.0.1 
Date: January 01, 2019
Last modified: April 23, 2019
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

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from functools import partial

from maya import OpenMaya
from maya import cmds

from smartDeformer_maya2019 import resources
from smartDeformer_maya2019.resources.ui import geometry
from smartDeformer_maya2019.resources.ui import mirror
from smartDeformer_maya2019.resources.ui import weights
from smartDeformer_maya2019.utils import platforms


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=platforms.get_qwidget()):
        super(MainWindow, self).__init__(parent)
        valid = platforms.has_valid()
        if not valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resources.getDownloadLink())
            QtWidgets.QMessageBox.critical(
                self, 'Critical', message, QtWidgets.QMessageBox.Ok)
            return
        if False in valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resources.getDownloadLink())
            QtWidgets.QMessageBox.critical(
                self, 'Critical', message, QtWidgets.QMessageBox.Ok)
            return

        self.geometry = geometry.Geometry(parent=self)
        self.my_mirror = mirror.Mirror(parent=self)
        self.weights = weights.Weights(parent=self)
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [500, 800]

        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)

        self.setup_ui()
        self.parent_maya_layout()

    def setup_ui(self):
        self.resize(self.width, self.height)
        self.setObjectName('mainwindow_smart_deformer')
        self.setWindowTitle(self.tool_kit_titile)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.toolbox = QtWidgets.QToolBox(self.centralwidget)
        self.toolbox.setObjectName('toolBox')
        self.verticallayout.addWidget(self.toolbox)
        self.page_convert = QtWidgets.QWidget()
        self.page_convert.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_convert.setObjectName('page_convert')
        self.toolbox.addItem(self.page_convert, 'Convert')
        self.verticallayout_convert = QtWidgets.QVBoxLayout(self.page_convert)
        self.verticallayout_convert.setObjectName('verticallayout_convert')
        self.verticallayout_convert.setSpacing(5)
        self.verticallayout_convert.setContentsMargins(10, 0, 0, 0)
        self.horizontallayout_convert = QtWidgets.QHBoxLayout()
        self.horizontallayout_convert.setObjectName('horizontallayout_convert')
        self.verticallayout_convert.addLayout(self.horizontallayout_convert)
        self.horizontallayout_convert.setSpacing(0)
        self.horizontallayout_convert.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_convert.addWidget(self.geometry)
        self.page_cluster = QtWidgets.QWidget()
        self.page_cluster.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_cluster.setObjectName('page_cluster')
        self.toolbox.addItem(self.page_cluster, 'Mirror and ...')
        self.verticallayout_cluster = QtWidgets.QVBoxLayout(self.page_cluster)
        self.verticallayout_cluster.setObjectName('verticalLayout_cluster')
        self.verticallayout_cluster.addWidget(self.my_mirror)
        self.verticallayout_cluster.setSpacing(0)
        self.verticallayout_cluster.setContentsMargins(10, 0, 0, 0)
        spaceritem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout_cluster.addItem(spaceritem)
        self.page_weights = QtWidgets.QWidget()
        self.page_weights.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_weights.setObjectName('page_cluster')
        self.toolbox.addItem(self.page_weights, 'Weights')
        self.verticallayout_weights = QtWidgets.QVBoxLayout(self.page_weights)
        self.verticallayout_weights.setObjectName('verticalLayout_weights')
        self.verticallayout_weights.addWidget(self.weights)
        self.verticallayout_weights.setSpacing(0)
        self.verticallayout_weights.setContentsMargins(10, 0, 0, 0)
        self.page_credit = QtWidgets.QWidget()
        self.page_credit.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_credit.setObjectName('page_cluster')
        self.toolbox.addItem(self.page_credit, 'Subin\'s Tool Kits')
        self.verticallayout_credit = QtWidgets.QVBoxLayout(self.page_credit)
        self.verticallayout_credit.setObjectName('verticallayout_credit')
        self.verticallayout_credit.setSpacing(0)
        self.verticallayout_credit.setContentsMargins(10, 10, 10, 10)
        self.button_logo = QtWidgets.QPushButton(self.page_credit)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setFlat(True)
        log_path = os.path.join(resources.getIconPath(), 'smart_deformer.png')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(log_path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logo.setIcon(icon)
        self.button_logo.setIconSize(QtCore.QSize(440, 440))
        self.verticallayout_credit.addWidget(self.button_logo)
        self.button_link = QtWidgets.QPushButton(self.page_credit)
        self.button_link.setObjectName('button_link')
        self.button_link.setFlat(True)
        self.button_link.setText('\nwww.subin-toolkits.com')
        self.button_link.setStyleSheet('font: 16pt \"Sans Serif\";')
        self.verticallayout_credit.addWidget(self.button_link)
        self.button_link.clicked.connect(self.toolkit_link)
        self.button_help = QtWidgets.QPushButton(self.page_credit)
        self.button_help.setObjectName('button_link')
        self.button_help.setFlat(True)
        self.button_help.setText('About Smart Deformer 0.0.1 (Help)\n')
        self.button_help.setStyleSheet('font: 16pt \"Sans Serif\";')
        self.verticallayout_credit.addWidget(self.button_help)
        self.button_help.clicked.connect(self.toolkit_help_link)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.label_subin = QtWidgets.QLabel(self.page_credit)
        self.label_subin.setObjectName('label_logo')
        self.label_subin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subin.setSizePolicy(size_policy)
        self.label_subin.setText(
            'Author: Subin. Gopi\nsubing85@gmail.com\n#copyright(c) 2019, Subin Gopi')
        self.label_subin.setStyleSheet('font: 12pt \"Sans Serif\";')
        self.verticallayout_credit.addWidget(self.label_subin)
        self.toolbox.setCurrentIndex(3)

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
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
