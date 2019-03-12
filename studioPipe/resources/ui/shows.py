'''
show.py 0.0.1 
Date: March 05, 2019
Last modified: March 08, 2019
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
from studioPipe.core import studioImage

from studioPipe.utils import platforms
from studioPipe.api import studioShows


class Show(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Show, self).__init__(parent)
        self.brows_directory = resources.getWorkspacePath()
        self.brows_directory = '/mnt/bkp/Icons gallery/icons_04'
        self.studio_pipe_path = '/home/shreya/Documents/studio_pipe'
        self.module, self.lable, self.version = platforms.get_tool_kit()
        self.icon_format = '.png'
        self.width, self.height = 256, 144
        
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
            os.path.join(resources.getIconPath(), 'subins_toolkits_1.png')))
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

    def load_widgets(self):
        studio_show = studioShows.Connect()
        input_data, sort_data = studio_show.getInputData()
        for index in range(len(sort_data)):
            current_item = input_data[sort_data[index]]
            label = QtGui.QLabel(self.groupbox)
            label.setObjectName('label_%s' % sort_data[index])
            label.setText(current_item['display_name'])
            label.setStatusTip(current_item['tooltip'])
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.gridlayout.addWidget(label, index, 0, 1, 1)
            widget = QtGui.QLineEdit(self.groupbox)
            widget.setObjectName('lineedit_%s' % sort_data[index])
            widget.setStatusTip(sort_data[index])
            widget.setToolTip('\n'.join(current_item['example']))
            widget.setText(current_item['value'])
            self.gridlayout.addWidget(widget, index, 1, 1, 1)
            if 'widget' in current_item:
                button = QtGui.QPushButton(self.groupbox)
                button.setObjectName(
                    'button_%s' % current_item['widget']['name'])
                button.setText(current_item['widget']['label'])
                button.clicked.connect(
                    partial(self.find_paths, widget, current_item['widget']['description']))
                self.gridlayout.addWidget(button, index, 2, 1, 1)
                widget.setReadOnly(True)

    def find_paths(self, widget, title):
        current_format = 'image {}'.format(resources.getImageFormats())
        current_file = QtGui.QFileDialog.getOpenFileName(
            self, title, self.brows_directory, current_format)
        if not os.path.isfile(current_file[0]):
            return False, None
        widget.setText(current_file[0])
        self.brows_directory = os.path.dirname(current_file[0])
        self.snapshot(self.button_show, current_file[0])

    def create_show(self):
        input_datas = self.get_source_paths(self.gridlayout)
        if '' in input_datas.values() or None in input_datas.values():
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not completed, please set the all parameters', QtGui.QMessageBox.Ok)
            return
        if not os.path.isfile(self.q_image_path):
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Can not found show icon', QtGui.QMessageBox.Ok)
            return
        studio_show = studioShows.Connect()
        studio_show.create(
            na=input_datas['show_name'],
            dn=input_datas['display_name'],
            sn=input_datas['short_name'],
            tp=input_datas['tooltip'],
            ic=input_datas['show_icon']
        )
        self.close()

    def get_source_paths(self, layout):
        data = {}
        ing = 0
        for index in range(layout.rowCount()):
            widget = layout.itemAtPosition(index, 1).widget()
            text = widget.text()
            tag = widget.statusTip()
            data.setdefault(tag.encode(), text.encode())
        return data

    def snapshot(self, button, image_file):
        self.studio_image = studioImage.ImageCalibration(imgae_file=image_file)
        self.q_image, self.q_image_path = self.studio_image.setStudioSize(
            width=self.width, height=self.height)
        if not self.q_image:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not able to process image!..', QtGui.QMessageBox.Ok)
            return
        self.image_to_button(button, self.q_image_path)
        return self.q_image, self.q_image_path

    def image_to_button(self, button=None, path=None, width=None, height=None):
        if not button:
            button = self.button_snapshot
        if not path:
            path = os.path.join(resources.getIconPath(), 'template.png')
        if not width:
            width = self.width
        if not height:
            height = self.height
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(self.width - 5, self.height - 5))
        

        



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Show(parent=None)
    window.show()
    sys.exit(app.exec_())
