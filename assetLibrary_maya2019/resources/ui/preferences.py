'''
preferences.py 0.0.1 
Date: January 15, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial
from datetime import datetime

from assetLibrary_maya2019 import resources
from assetLibrary_maya2019.modules import readWrite
from assetLibrary_maya2019.utils import platforms


class Preference(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Preference, self).__init__(parent)
        self.brows_directory = resources.getWorkspacePath()
        self.module, self.lable, self.version = platforms.get_tool_kit()
        self.bundles = {
            0: {
                'label': 'Maya Directory',
                'tag': 'maya_directory',
                'path': None
            },
            1: {
                'label': 'Library Directory',
                'tag': 'library_directory',
                'path': None
            },
            2: {
                'label': 'Create Type',
                'tag': 'create_type',
                'types': ['None', 'import', 'reference'],
                'value': 0
            },
            3: {
                'label': 'Maya File Type',
                'tag': 'maya_file_type',
                'types': ['None', 'mayaAscii', 'mayaBinary'],
                'value': 0
            },
            4: {
                'label': 'Output Directory',
                'tag': 'output_directory',
                'path': None
            }
        }
        self.setup_ui()
        self.create_preference()
        self.create_widgets()

    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            'Preferences ({} {})'.format(self.lable, self.version))
        self.resize(700, 100)
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('Preferences')
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
        self.button_add = QtWidgets.QPushButton(self.groupbox)
        self.button_add.setObjectName('button_add')
        self.button_add.setText(u'\u002B')
        self.button_add.setStyleSheet('color: #0000FF;')
        self.button_add.setMinimumSize(QtCore.QSize(25, 25))
        self.button_add.setMaximumSize(QtCore.QSize(25, 25))
        self.button_add.hide()
        self.verticallayout_item.addWidget(self.button_add)
        self.gridlayout = QtWidgets.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(10, 10, 10, 10)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_apply = QtWidgets.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')
        self.horizontallayout.addWidget(self.button_apply)
        self.button_cancel.clicked.connect(self.close)

    def create_preference(self):
        comment = '{} {} - preference container'.format(
            self.lable, self.version)
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about asset library preference'
        type = 'preference'
        valid = True
        data = self.bundles
        tag = 'asset_library'
        resource_path = resources.getResourceTypes()[type].encode()
        rw = readWrite.ReadWrite(c=comment, cd=created_date, d=description,
                                 t=type, v=valid, data=data, tag=tag, path=resource_path,
                                 name='library_preferences', format='json')
        if rw.has_file():
            self.bundles = rw.get_data()
            return
        rw.create()

    def create_widgets(self):
        keys = self.bundles.keys()
        keys.sort()
        for index in range(len(keys)):
            self.add_widgets(index, self.bundles[keys[index]])

    def add_widgets(self, row, contents=None):
        label_label = QtWidgets.QLabel(self.groupbox)
        label_label.setObjectName('label_label_%s' % row)
        label_label.setText(contents['label'])
        label_label.setStatusTip(contents['tag'])
        label_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(label_label, row, 0, 1, 1)
        if 'types' in contents:
            widget = QtWidgets.QComboBox(self.groupbox)
            widget.setObjectName('combobox_types')
            widget.addItems(contents['types'])
            widget.setCurrentIndex(contents['value'])
            widget.setToolTip(contents['label'])
            self.gridlayout.addWidget(widget, row, 1, 1, 1)
        else:
            widget = QtWidgets.QLineEdit(self.groupbox)
            widget.setObjectName('lineedit_path_%s' % row)
            widget.setText(contents['path'])
            self.gridlayout.addWidget(widget, row, 1, 1, 1)
        button_find = QtWidgets.QPushButton(self.groupbox)
        button_find.setObjectName('button_find_%s' % row)
        button_find.setText('...')
        button_find.setStyleSheet('color: #0000FF;')
        button_find.setMinimumSize(QtCore.QSize(35, 25))
        button_find.setMaximumSize(QtCore.QSize(35, 25))
        if 'types' in contents:
            button_find.hide()
        self.gridlayout.addWidget(button_find, row, 2, 1, 1)
        widgets = [label_label, widget, button_find]
        button_find.clicked.connect(
            partial(self.find_path, widgets, contents['label']))

    def find_path(self, widgets, title):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Browse for {} folder'.format(title), self.brows_directory)
        if not path:
            return
        self.brows_directory = path
        widgets[1].setText(path)

    def apply(self):
        directorys = self.get_source_paths(self.gridlayout)
        comment = '{} {} - preference container'.format(
            self.lable, self.version)
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about asset library preference'
        type = 'preference'
        valid = True
        data = directorys
        tag = 'asset_library'
        resource_path = resources.getResourceTypes()[type]
        rw = readWrite.ReadWrite(
            c=comment, cd=created_date, d=description,
            t=type, v=valid, data=data, tag=tag, path=resource_path,
            name='library_preferences', format='json')
        rw.create()
        self.close()
        print '\n#result preferences updated ', rw.file_path

    def get_source_paths(self, layout):
        data = {}
        ing = 0
        for index in range(layout.rowCount()):
            if not layout.itemAt(ing) and layout.itemAt(ing + 1):
                continue
            lable_widget = layout.itemAt(ing).widget()
            content_widget = layout.itemAt(ing + 1).widget()
            if not lable_widget and content_widget:
                continue
            current_label = lable_widget.text().encode()
            current_tag = lable_widget.statusTip().encode()
            if isinstance(content_widget, QtWidgets.QComboBox):
                value = content_widget.currentIndex()
                all_items = [str(content_widget.itemText(x))
                             for x in range(content_widget.count())]
                content = {
                    'label': current_label,
                    'tag': current_tag,
                    'types': all_items,
                    'value': value
                }
            else:
                current_path = content_widget.text().encode()
                content = {
                    'label': current_label,
                    'tag': current_tag,
                    'path': current_path
                }
            data.setdefault(index, content)
            ing += layout.columnCount()
        return data


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Preference(parent=None)
    window.show()
    sys.exit(app.exec_())
