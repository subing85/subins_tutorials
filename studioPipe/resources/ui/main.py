'''
main.py 0.0.1 
Date: March 09, 2019
Last modified: March 09, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys
import os
import tempfile

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime

from studioPipe import resources
from studioPipe.modules import studioDataBase
from studioPipe.modules import studioImage
from studioPipe.utils import platforms


class Main(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.brows_directory = resources.getWorkspacePath()
        self.brows_directory = '/mnt/bkp/Icons gallery/icons_04'
        self.studio_pipe_path = '/home/shreya/Documents/studio_pipe'
        self.module, self.lable, self.version = platforms.get_tool_kit()
        self.icon_format = 'png'
        self._width, self._height = 256, 144
        input_file = os.path.join(resources.getInputPath(), 'show.json')
        self.read_db = studioDataBase.Connect(full_path=input_file)
        self.input_data = self.read_db.getData()
        self.setup_ui()
        self.load_widgets()

    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            'Show Inputs ({} {})'.format(self.lable, self.version))
        self.resize(500, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('Create your show')
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.verticallayout_item.addLayout(self.horizontalLayout)
        self.label_logo = QtGui.QLabel(self.groupbox)
        self.label_logo.setObjectName('label_subins_toolkits')
        self.label_logo.setPixmap(QtGui.QPixmap(
            os.path.join(resources.getIconPath(), 'subins_toolkits.png')))
        self.label_logo.setScaledContents(True)
        self.label_logo.setMinimumSize(QtCore.QSize(128, 128))
        self.label_logo.setMaximumSize(QtCore.QSize(128, 128))
        self.horizontalLayout.addWidget(self.label_logo)
        self.button_show = QtGui.QPushButton(self.groupbox)
        self.button_show.setFlat(True)
        self.button_show.setSizePolicy(
            QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred))
        self.button_show.setObjectName('button_show')
        self.button_show.setMinimumSize(QtCore.QSize(256, 144))
        self.button_show.setMaximumSize(QtCore.QSize(256, 144))
        self.horizontalLayout.addWidget(self.button_show)
        self.gridlayout = QtGui.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)
        spacer_item = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(10, 10, 10, 10)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_create = QtGui.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout.addWidget(self.button_create)
        self.button_create.clicked.connect(self.create_show)
        self.button_cancel.clicked.connect(self.close)


    
    
    
    
    
    
    
    
    
    def image_to_button(self, button=None, path=None, width=None, height=None):
        if not button:
            button = self.button_snapshot
        if not path:
            path = os.path.join(resources.getIconPath(), 'template.png')
        if not width:
            width = self._width
        if not height:
            height = self._height
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(self._width - 5, self._height - 5))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Show(parent=None)
    window.Main()
    sys.exit(app.exec_())
