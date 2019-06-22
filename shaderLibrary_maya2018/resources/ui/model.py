'''
model.py 0.0.1 
Date: January 15, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''


import os
import sys
import tempfile
import webbrowser

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial

from maya import OpenMaya

from shaderLibrary_maya2018.modules import studioMaya
from shaderLibrary_maya2018.modules import studioImage
from shaderLibrary_maya2018 import resources


class Model(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Model, self).__init__(parent=None)
        self.studio_image = studioImage.ImageCalibration()
        self.studio_maya = studioMaya.Maya()
        self._width, self._height = 150, 150
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('model')
        self.resize(400, 600)
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox_model = QtWidgets.QGroupBox(self)
        self.groupbox_model.setObjectName('groupbox_model')
        self.groupbox_model.setTitle('Model')
        self.verticallayout.addWidget(self.groupbox_model)
        self.verticallayout_model = QtWidgets.QVBoxLayout(self.groupbox_model)
        self.verticallayout_model.setObjectName('verticallayout_model')
        self.verticallayout_model.setSpacing(10)
        self.verticallayout_model.setContentsMargins(10, 10, 10, 10)
        self.groupbox_snapshot = QtWidgets.QGroupBox(self.groupbox_model)
        self.groupbox_snapshot.setObjectName('groupBox_snapshot')
        self.verticallayout_model.addWidget(self.groupbox_snapshot)
        self.horizontallayout_snapshot = QtWidgets.QHBoxLayout(
            self.groupbox_snapshot)
        self.horizontallayout_snapshot.setObjectName(
            'horizontallayout_snapshot')
        self.horizontallayout_snapshot.setSpacing(5)
        self.horizontallayout_snapshot.setContentsMargins(5, 5, 5, 5)
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_snapshot.addItem(spacer_item)
        self.button_snapshot = QtWidgets.QPushButton(self.groupbox_snapshot)
        self.button_snapshot.setObjectName('button_snapshot')
        self.button_snapshot.setText('')
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.button_snapshot.sizePolicy().hasHeightForWidth())
        self.button_snapshot.setSizePolicy(size_policy)
        self.button_snapshot.setMinimumSize(
            QtCore.QSize(self._width, self._height))
        self.button_snapshot.setMaximumSize(
            QtCore.QSize(self._width, self._height))
        self.horizontallayout_snapshot.addWidget(self.button_snapshot)
        self.image_to_button()
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_snapshot.addItem(spacer_item)
        self.groupbox_label = QtWidgets.QGroupBox(self.groupbox_model)
        self.groupbox_label.setObjectName('groupbox_label')
        self.verticallayout_model.addWidget(self.groupbox_label)
        self.horizontallayout_label = QtWidgets.QHBoxLayout(
            self.groupbox_label)
        self.horizontallayout_label.setObjectName('horizontallayout_label')
        self.horizontallayout_label.setSpacing(10)
        self.horizontallayout_label.setContentsMargins(10, 10, 10, 10)
        self.label_label = QtWidgets.QLabel(self.groupbox_label)
        self.label_label.setObjectName('label_label')
        self.label_label.setText('Name')
        self.horizontallayout_label.addWidget(self.label_label)
        self.lineEdit_label = QtWidgets.QLineEdit(self.groupbox_label)
        self.lineEdit_label.setObjectName('lineEdit_label')
        self.lineEdit_label.setText('')
        self.horizontallayout_label.addWidget(self.lineEdit_label)
        self.textedit_history = QtWidgets.QTextEdit(self.groupbox_model)
        self.textedit_history.setObjectName('textedit_history')
        self.textedit_history.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";')
        self.verticallayout_model.addWidget(self.textedit_history)
        self.button_publish = QtWidgets.QPushButton(self.groupbox_model)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.verticallayout_model.addWidget(self.button_publish)
        self.checkbox_build = QtWidgets.QCheckBox(self.groupbox_model)
        self.checkbox_build.setObjectName('checkbox_build')
        self.checkbox_build.setText('Assign To Object')
        self.checkbox_build.setToolTip(
            'Assign to the object, if object is exists')
        self.checkbox_build.hide()
        self.verticallayout_model.addWidget(self.checkbox_build)
        self.checkbox_assign = QtWidgets.QCheckBox(self.groupbox_model)
        self.checkbox_assign.setObjectName('checkbox_assign')
        self.checkbox_assign.setText('Assign To Selected Object')
        self.checkbox_assign.setToolTip('Assign to selected object')
        self.checkbox_assign.hide()
        self.verticallayout_model.addWidget(self.checkbox_assign)
        self.button_build = QtWidgets.QPushButton(self.groupbox_model)
        self.button_build.setObjectName('button_build')
        self.button_build.setText('Build')
        self.button_build.hide()
        self.verticallayout_model.addWidget(self.button_build)
        self.button_logo = QtWidgets.QPushButton(self.groupbox_model)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setFlat(True)
        self.button_logo.clicked.connect(self.subin_toolkits)
        log_path = os.path.join(resources.getIconPath(), 'logo.png')
        self.image_to_button(self.button_logo, log_path,
                             self._width, self._height)
        self.verticallayout_model.addWidget(self.button_logo)
        self.label_subin = QtWidgets.QLabel(self.groupbox_model)
        self.label_subin.setObjectName('label_logo')
        self.label_subin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subin.setText(
            'Author: Subin. Gopi\nsubing85@gmail.com\nwww.subins-toolkits.com\ncopyright(c) 2019, Subin Gopi')
        self.label_subin.setStyleSheet('font: 11pt \"Sans Serif\";')
        self.verticallayout_model.addWidget(self.label_subin)

    def snapshot(self, button):
        self.studio_image.image_file = os.path.join(tempfile.gettempdir(),
                                                    'studio_image_snapshot.png')
        image_object, image_path = self.studio_image.create()
        if not image_path:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not able to process snap shot!..', QtGui.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Snap shot - faild!...')
            return
        self.image_to_button(button, image_path, self._width, self._height)
        return image_object, image_path

    # Load Image to button
    def image_to_button(self, button=None, path=None, width=None, height=None):
        if not button:
            button = self.button_snapshot
        if not path:
            path = os.path.join(resources.getIconPath(), 'snapshot.png')
        if not width:
            width = self._width
        if not height:
            height = self._height
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(width - 5, height - 5))

    def subin_toolkits(self):
        webbrowser.BaseBrowser(resources.getToolKitLink())
        OpenMaya.MGlobal.displayInfo(resources.getToolKitLink())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Model(parent=None)
    window.show()
    sys.exit(app.exec_())
