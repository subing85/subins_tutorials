'''
model.py 0.0.1 
Date: January 15, 2019
Last modified: January 26, 2019
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

from PySide import QtCore
from PySide import QtGui
from functools import partial

from maya import OpenMaya

from modelLibrary.modules import studioMaya
from modelLibrary.modules import studioImage
from modelLibrary.modules import studioModel

from modelLibrary import resources


class Model(QtGui.QWidget):

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
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox_model = QtGui.QGroupBox(self)
        self.groupbox_model.setObjectName('groupbox_model')
        self.groupbox_model.setTitle('Model')
        self.verticallayout.addWidget(self.groupbox_model)
        self.verticallayout_model = QtGui.QVBoxLayout(self.groupbox_model)
        self.verticallayout_model.setObjectName('verticallayout_model')
        self.verticallayout_model.setSpacing(10)
        self.verticallayout_model.setContentsMargins(10, 10, 10, 10)
        self.groupbox_snapshot = QtGui.QGroupBox(self.groupbox_model)
        self.groupbox_snapshot.setObjectName('groupBox_snapshot')
        self.verticallayout_model.addWidget(self.groupbox_snapshot)
        self.horizontallayout_snapshot = QtGui.QHBoxLayout(
            self.groupbox_snapshot)
        self.horizontallayout_snapshot.setObjectName(
            'horizontallayout_snapshot')
        self.horizontallayout_snapshot.setSpacing(5)
        self.horizontallayout_snapshot.setContentsMargins(5, 5, 5, 5)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout_snapshot.addItem(spacer_item)
        self.button_snapshot = QtGui.QPushButton(self.groupbox_snapshot)
        self.button_snapshot.setObjectName('button_snapshot')
        self.button_snapshot.setText('')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout_snapshot.addItem(spacer_item)
        self.groupbox_label = QtGui.QGroupBox(self.groupbox_model)
        self.groupbox_label.setObjectName('groupbox_label')
        self.verticallayout_model.addWidget(self.groupbox_label)
        self.horizontallayout_label = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_label.setObjectName('horizontallayout_label')
        self.horizontallayout_label.setSpacing(10)
        self.horizontallayout_label.setContentsMargins(10, 10, 10, 10)
        self.label_label = QtGui.QLabel(self.groupbox_label)
        self.label_label.setObjectName('label_label')
        self.label_label.setText('Name')
        self.horizontallayout_label.addWidget(self.label_label)
        self.lineEdit_label = QtGui.QLineEdit(self.groupbox_label)
        self.lineEdit_label.setObjectName('lineEdit_label')
        self.lineEdit_label.setText('')
        self.horizontallayout_label.addWidget(self.lineEdit_label)
        self.textedit_history = QtGui.QTextEdit(self.groupbox_model)
        self.textedit_history.setObjectName('textedit_history')
        self.textedit_history.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";')
        self.verticallayout_model.addWidget(self.textedit_history)
        self.button_publish = QtGui.QPushButton(self.groupbox_model)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.verticallayout_model.addWidget(self.button_publish)
        self.button_build = QtGui.QPushButton(self.groupbox_model)
        self.button_build.setObjectName('button_build')
        self.button_build.setText('Build')
        self.button_build.hide()
        self.verticallayout_model.addWidget(self.button_build)
        self.button_logo = QtGui.QPushButton(self.groupbox_model)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setFlat(True)
        log_path = os.path.join(resources.getIconPath(), 'logo.png')
        self.image_to_button(self.button_logo, log_path,
                             self._width, self._height)
        self.verticallayout_model.addWidget(self.button_logo)
        self.label_subin = QtGui.QLabel(self.groupbox_model)
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
            QtGui.QMessageBox.warning(
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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Model(parent=None)
    window.show()
    sys.exit(app.exec_())
