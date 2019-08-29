'''
preference.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import sys
import warnings

from PySide import QtGui
from PySide import QtCore
from functools import partial

from studio_maya import resources
from studio_maya.core import inputs
from studio_maya.core import generic
from studio_maya.core import widgets
from studio_maya.core import stylesheet
reload(generic)

class Window(QtGui.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent=None)
        self.main_window = parent
        self.label, self.name, self.version = resources.getToolKit()
        self.preference_path = resources.getPreferenceFile()
        self.roo_path, self.tag, self.mayapy_type = resources.getRootPath()
        self.brows_directory = self.roo_path
        self.labels = []
        if 'lables' in kwargs:
            self.labels = kwargs['lables']
        self.width, self.height = 750, 383
        self.setup_ui()
        self.set_parameters()

    def setup_ui(self):
        self.setObjectName('maya_preference')
        self.setWindowTitle('%s %s Preference' % (self.label, self.version))
        self.resize(self.width, self.height)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(20)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox_versions = QtGui.QGroupBox(self)
        self.groupbox_versions.setObjectName('groupbox_versions')
        self.groupbox_versions.setTitle('Maya Versions')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_versions.setSizePolicy(size_policy)
        self.verticallayout.addWidget(self.groupbox_versions)
        self.gridLayout_versions = QtGui.QGridLayout(self.groupbox_versions)
        self.gridLayout_versions.setObjectName('gridLayout_versions')
        self.gridLayout_versions.setSpacing(1)
        self.gridLayout_versions.setContentsMargins(5, 50, 5, 5)
        self.label_maya = QtGui.QLabel(self.groupbox_versions)
        self.label_maya.setObjectName('label_maya')
        self.label_maya.setText('Maya')
        self.label_maya.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridLayout_versions.addWidget(self.label_maya, 0, 0, 1, 1)
        self.combobox_maya = QtGui.QComboBox(self.groupbox_versions)
        self.combobox_maya.setObjectName('combobox_maya')
        self.gridLayout_versions.addWidget(self.combobox_maya, 0, 1, 1, 1)
        self.checkbox_config = QtGui.QCheckBox(self.groupbox_versions)
        self.checkbox_config.setObjectName('checkbox_config')
        self.checkbox_config.setText('Auto configure')
        self.gridLayout_versions.addWidget(self.checkbox_config, 1, 1, 1, 1)
        self.progressbar = QtGui.QProgressBar(self.groupbox_versions)
        self.progressbar.setObjectName('progressbar')
        self.progressbar.setMinimumSize(QtCore.QSize(210, 10))
        self.progressbar.setMaximumSize(QtCore.QSize(210, 10))
        self.progressbar.setValue(0)
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.progressbar.setSizePolicy(size_policy)
        self.progressbar.hide()
        self.gridLayout_versions.addWidget(self.progressbar, 1, 2, 1, 2)
        self.label_directory = QtGui.QLabel(self.groupbox_versions)
        self.label_directory.setObjectName('label_directory')
        self.label_directory.setText('Directory')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.label_directory.setSizePolicy(size_policy)
        self.label_directory.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridLayout_versions.addWidget(self.label_directory, 2, 0, 1, 1)
        self.lineedit_directory = QtGui.QLineEdit(self.groupbox_versions)
        self.lineedit_directory.setObjectName('lineedit_directory')
        self.gridLayout_versions.addWidget(self.lineedit_directory, 2, 1, 1, 2)
        self.button_directory = QtGui.QPushButton(self.groupbox_versions)
        self.button_directory.setObjectName('button_directory')
        self.button_directory.setText('...')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.button_directory.setSizePolicy(size_policy)
        self.gridLayout_versions.addWidget(self.button_directory, 2, 3, 1, 1)
        self.groupbox_mode = QtGui.QGroupBox(self)
        self.groupbox_mode.setObjectName('groupbox_mode')
        self.groupbox_mode.setTitle('Settings')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_mode.setSizePolicy(size_policy)
        self.groupbox_mode.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticallayout.addWidget(self.groupbox_mode)
        self.gridLayout_settings = QtGui.QGridLayout(self.groupbox_mode)
        self.gridLayout_settings.setObjectName('gridLayout_settings')
        self.gridLayout_settings.setSpacing(10)
        self.gridLayout_settings.setContentsMargins(5, 50, 5, 5)
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.checkbox_query = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_query.setObjectName('checkbox_query')
        self.checkbox_query.setText('Query Only')
        self.checkbox_query.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_query, 0, 0, 1, 1)
        self.checkbox_edit = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_edit.setObjectName('checkbox_edit')
        self.checkbox_edit.setText('Edit And Query')
        self.checkbox_edit.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_edit, 0, 1, 1, 1)
        self.checkbox_overwrite = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_overwrite.setObjectName('checkbox_overwrite')
        self.checkbox_overwrite.setText('Overwrite')
        self.checkbox_overwrite.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_overwrite, 1, 0, 1, 1)
        self.checkbox_version = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_version.setObjectName('checkbox_version')
        self.checkbox_version.setText('Next Version')
        self.checkbox_version.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_version, 1, 1, 1, 1)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(5)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.button_cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_apply = QtGui.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')
        self.button_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontallayout.addWidget(self.button_apply)
        vertical_spacer_item = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(vertical_spacer_item)
        self.checkbox_query.clicked.connect(
            partial(self.set_toggle, self.checkbox_edit))
        self.checkbox_edit.clicked.connect(
            partial(self.set_toggle, self.checkbox_query))
        self.checkbox_overwrite.clicked.connect(
            partial(self.set_toggle, self.checkbox_version))
        self.checkbox_version.clicked.connect(
            partial(self.set_toggle, self.checkbox_overwrite))
        self.combobox_maya.currentIndexChanged.connect(
            partial(self.set_toggle, self.checkbox_config, self.lineedit_directory))
        self.checkbox_config.clicked.connect(partial(
            self.set_versions, self.checkbox_config, self.combobox_maya, self.lineedit_directory))
        self.button_directory.clicked.connect(partial(
            self.set_directory, self.lineedit_directory))
        self.button_cancel.clicked.connect(self.close)
        self.button_apply.clicked.connect(self.apply)

    def set_parameters(self):
        input = 'json'
        if os.path.isfile(self.preference_path):
            input = 'xml'
        data = self.get_preference_data(input=input)
        self.combobox_maya.addItems(data['maya_versions'])
        self.combobox_maya.setCurrentIndex(
            data['current_version']['index'])
        self.checkbox_config.setCheckState(QtCore.Qt.Unchecked)
        self.lineedit_directory.setText(data['current_version']['path'])
        self.checkbox_query.setChecked(data['mode']['query_only'])
        self.checkbox_edit.setChecked(data['mode']['edit_quey'])
        self.checkbox_overwrite.setChecked(data['mode']['overwrite'])
        self.checkbox_version.setChecked(data['mode']['next_version'])

    def get_preference_data(self, input='json'):
        label, name, version = resources.getToolKit()
        if input == 'xml':
            input_data = generic.read_preset(self.preference_path)
        elif input == 'interface':
            maya_versions = self.get_maya_versions()
            settings_data = self.get_settings_data()
            index, name = self.get_current_version()
            input_data = {
                'maya_versions': maya_versions,
                'mode': settings_data,
                'current_version': {
                    'index': index,
                    'name': name
                }
            }
        else:
            maya_input = inputs.Connect()
            input_data = maya_input.get_data()
        return input_data

    def get_settings_data(self):
        query = False
        edit = True
        overwrite = False
        version = True
        if self.checkbox_query.isChecked():
            query = True
            edit = False
        if self.checkbox_overwrite.isChecked():
            overwrite = True
            version = False
        data = {
            'query_only': query,
            'edit_quey': edit,
            'overwrite': overwrite,
            'next_version': version
        }
        return data

    def get_maya_versions(self):
        item_count = self.combobox_maya.count()
        maya_versions = []
        for index in range(item_count):
            current_item = self.combobox_maya.itemText(index)
            maya_versions.append(current_item.encode())
        return maya_versions

    def get_current_version(self):
        index = self.combobox_maya.currentIndex()
        name = self.combobox_maya.currentText()
        return index, name

    def set_toggle(self, checkbox, *args):
        checkbox.setCheckState(QtCore.Qt.Unchecked)
        if args:
            args[0].clear()

    def set_versions(self, checkbox, combobox, lineedit):
        if not checkbox.isChecked():
            return
        self.progressbar.show()
        lineedit.clear()
        current_version = combobox.currentText()
        mayapy_path = generic.get_mayapy(
            current_version.encode(), progress=self.progressbar)
        if not mayapy_path:
            mayapy_path = 'not found mayapy, find it manually'
            warnings.warn('not found mayapy, find it manually')
        lineedit.setText(mayapy_path)
        self.progressbar.hide()

    def set_directory(self, lineedit):
        file, extension = QtGui.QFileDialog.getOpenFileName(
            self, 'Browser', self.brows_directory, 'mayapy (* *.exe)')
        if not file:
            return
        lineedit.setText(file.encode())
        self.brows_directory = os.path.dirname(file)

    def apply(self):
        current_maya = self.combobox_maya.currentText()
        maya_path = self.lineedit_directory.text()
        if not current_maya or current_maya == 'None':
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Not found any maya versions\nSet your respective maya version!...',
                QtGui.QMessageBox.Ok)
            return
        if not os.path.isfile(maya_path):
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Not found any mayapy\nFind your mayapy from maya installed directories!...',
                QtGui.QMessageBox.Ok)
            return
        if not self.checkbox_query.isChecked() and not self.checkbox_edit.isChecked():
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Not found any query or edit mode\nSet Overwrite either Edit and Query mode!...',
                QtGui.QMessageBox.Ok)
            return
        if not self.checkbox_overwrite.isChecked() and not self.checkbox_version.isChecked():
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Not found any save mode\nSet Query Only either Next Version mode!...',
                QtGui.QMessageBox.Ok)
            return
        data = self.collect_data()
        config_path = generic.write_preset(data, self.preference_path)
        QtGui.QMessageBox.information(
            self,
            'Information',
            'Success!...',
            QtGui.QMessageBox.Ok)
        self.labels
        widgets.set_maya_version(
            self.preference_path, self.labels[0], self.labels[1])
        self.close()

    def collect_data(self):
        current_maya = self.combobox_maya.currentText()
        maya_path = self.lineedit_directory.text()
        edit = True
        save = True
        if self.checkbox_query.isChecked():
            edit = False
        if self.checkbox_overwrite.isChecked():
            save = False
        label, name, version = resources.getToolKit()
        maya_versions = self.get_maya_versions()
        data = {
            'parent': {
                'studio_maya': {
                    'label': label,
                    'version': version,
                    'type': 'preset',
                }
            },
            'child': {
                'maya': {
                    'current_version': current_maya.encode(),
                    'path': maya_path.encode(),
                    'maya_versions': maya_versions
                },
                'settings': {
                    'edit': edit,
                    'save': save
                }
            }
        }
        return data

    def closeEvent(self, event):
        if self.main_window:
            self.main_window.setEnabled(True)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
