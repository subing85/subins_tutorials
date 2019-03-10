'''
asset.py 0.0.1 
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

from PySide import QtCore
from PySide import QtGui
from functools import partial

from assetLibrary import resources
from assetLibrary.modules import studioImage
from assetLibrary.modules import studioPrint


class Asset(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Asset, self).__init__(parent=None)
        self.studio_image = studioImage.ImageCalibration()
        self._width, self._height = 150, 150
        self.brows_directory = resources.getWorkspacePath()
        self.setup_ui()
        self.studio_print = studioPrint.Print(__name__, self.textedit_console)

    def setup_ui(self):
        self.setObjectName('asset')
        self.resize(400, 600)
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox_asset = QtGui.QGroupBox(self)
        self.groupbox_asset.setObjectName('groupbox_asset')
        self.groupbox_asset.setTitle('Asset')
        self.verticallayout.addWidget(self.groupbox_asset)
        self.verticallayout_asset = QtGui.QVBoxLayout(self.groupbox_asset)
        self.verticallayout_asset.setObjectName('verticallayout_asset')
        self.verticallayout_asset.setSpacing(10)
        self.verticallayout_asset.setContentsMargins(10, 10, 10, 10)
        self.groupbox_snapshot = QtGui.QGroupBox(self.groupbox_asset)
        self.groupbox_snapshot.setObjectName('groupBox_snapshot')
        self.verticallayout_asset.addWidget(self.groupbox_snapshot)
        self.horizontallayout_snapshot = QtGui.QHBoxLayout(
            self.groupbox_snapshot)
        self.horizontallayout_snapshot.setObjectName(
            'horizontallayout_snapshot')
        self.horizontallayout_snapshot.setSpacing(10)
        self.horizontallayout_snapshot.setContentsMargins(10, 10, 10, 10)
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
        self.groupbox_path = QtGui.QGroupBox(self.groupbox_asset)
        self.groupbox_path.setObjectName('groupbox_path')
        self.gridlayout_inputs = QtGui.QGridLayout(self.groupbox_path)
        self.gridlayout_inputs.setObjectName('gridLayout')
        self.gridlayout_inputs.setSpacing(10)
        self.gridlayout_inputs.setContentsMargins(10, 10, 10, 10)
        self.label_filepath = QtGui.QLabel(self.groupbox_asset)
        self.label_filepath.setObjectName('label_filepath')
        self.label_filepath.setText('File Path')
        self.label_filepath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_filepath, 0, 0, 1, 1)
        self.lineedit_filepath = QtGui.QLineEdit(self.groupbox_asset)
        self.lineedit_filepath.setObjectName('lineedit_filepath')
        self.gridlayout_inputs.addWidget(self.lineedit_filepath, 0, 1, 1, 1)
        self.pushbutton_filepath = QtGui.QPushButton(self.groupbox_asset)
        self.pushbutton_filepath.setObjectName('pushbutton_filepath')
        self.pushbutton_filepath.setText('...')
        self.gridlayout_inputs.addWidget(self.pushbutton_filepath, 0, 2, 1, 1)
        self.label_imagepath = QtGui.QLabel(self.groupbox_asset)
        self.label_imagepath.setObjectName('label_filepath')
        self.label_imagepath.setText('Image Path')
        self.label_imagepath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_imagepath, 1, 0, 1, 1)
        self.lineedit_imagepath = QtGui.QLineEdit(self.groupbox_asset)
        self.lineedit_imagepath.setObjectName('lineedit_imagepath')
        self.gridlayout_inputs.addWidget(self.lineedit_imagepath, 1, 1, 1, 1)
        self.pushbutton_imagepath = QtGui.QPushButton(self.groupbox_asset)
        self.pushbutton_imagepath.setObjectName('pushbutton_filepath')
        self.pushbutton_imagepath.setText('...')
        self.gridlayout_inputs.addWidget(self.pushbutton_imagepath, 1, 2, 1, 1)
        self.verticallayout_asset.addWidget(self.groupbox_path)
        self.groupbox_label = QtGui.QGroupBox(self.groupbox_asset)
        self.groupbox_label.setObjectName('groupbox_label')
        self.verticallayout_asset.addWidget(self.groupbox_label)
        self.horizontallayout_label = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_label.setObjectName('horizontallayout_label')
        self.horizontallayout_label.setSpacing(10)
        self.horizontallayout_label.setContentsMargins(10, 10, 10, 10)
        self.label_label = QtGui.QLabel(self.groupbox_label)
        self.label_label.setObjectName('label_label')
        self.label_label.setText('Name')
        self.horizontallayout_label.addWidget(self.label_label)
        self.lineedit_label = QtGui.QLineEdit(self.groupbox_label)
        self.lineedit_label.setObjectName('lineEdit_label')
        self.lineedit_label.setText('')
        self.horizontallayout_label.addWidget(self.lineedit_label)
        self.textedit_history = QtGui.QTextEdit(self.groupbox_asset)
        self.textedit_history.setObjectName('textedit_history')
        self.textedit_history.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";')
        self.verticallayout_asset.addWidget(self.textedit_history)
        self.button_publish = QtGui.QPushButton(self.groupbox_asset)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.verticallayout_asset.addWidget(self.button_publish)
        self.button_build = QtGui.QPushButton(self.groupbox_asset)
        self.button_build.setObjectName('button_build')
        self.button_build.setText('Build')
        self.button_build.hide()
        self.verticallayout_asset.addWidget(self.button_build)
        self.button_logo = QtGui.QPushButton(self.groupbox_asset)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setFlat(True)
        self.button_logo.clicked.connect(self.subin_toolkits)
        log_path = os.path.join(resources.getIconPath(), 'logo.png')
        self.image_to_button(self.button_logo, log_path,
                             self._width, self._height)
        self.verticallayout_asset.addWidget(self.button_logo)
        self.label_subin = QtGui.QLabel(self.groupbox_asset)
        self.label_subin.setObjectName('label_logo')
        self.label_subin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subin.setText(
            'Author: Subin. Gopi\nsubing85@gmail.com\nwww.subins-toolkits.com\ncopyright(c) 2019, Subin Gopi')
        self.label_subin.setStyleSheet('font: 11pt \"Sans Serif\";')
        self.verticallayout_asset.addWidget(self.label_subin)
        self.textedit_console = QtGui.QTextEdit(self.groupbox_asset)
        self.textedit_console.setObjectName('textedit_console')
        self.textedit_console.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";')
        self.textedit_console.setMinimumSize(QtCore.QSize(0, 50))
        self.textedit_console.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticallayout_asset.addWidget(self.textedit_console)

    def set_source_path(self, widget, tag):
        self.formats = {'file': '(*.ma *.mb)', 'image': '(*.jpg *.tga *.png)'}
        self.q_image,  self.q_image_path = None, None
        title = 'Browse %s' % tag
        current_format = '%s %s' % (tag, self.formats[tag])
        current_file = QtGui.QFileDialog.getOpenFileName(
            self, title, self.brows_directory, current_format)
        if not os.path.isfile(current_file[0]):
            return False, None
        widget.setText(current_file[0])
        self.brows_directory = os.path.dirname(current_file[0])
        if tag == 'image':
            studio_image = studioImage.ImageCalibration()
            self.q_image,  self.q_image_path = studio_image.setStudioSize(
                source_image=current_file[0])
            self.image_to_button(path=self.q_image_path)
            return self.q_image,  self.q_image_path
        return True, current_file[0]

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

    def snapshot(self, button):
        self.studio_image.image_file = os.path.join(tempfile.gettempdir(),
                                                    'studio_image_snapshot.png')
        image_object, image_path = self.studio_image.create()
        if not image_path:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not able to process snap shot!..', QtGui.QMessageBox.Ok)
            self.studio_print.display_warning('Snap shot - faild!...')
            return
        self.image_to_button(button, image_path, self._width, self._height)
        return image_object, image_path

    def subin_toolkits(self):
        webbrowser.BaseBrowser(resources.getToolKitLink())
        self.studio_print.display_info(resources.getToolKitLink())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Asset(parent=None)
    window.show()
    sys.exit(app.exec_())
