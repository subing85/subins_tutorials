'''
preferences.py 0.0.1 
Date: January 15, 2019
Last modified: January 26, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime

from modelLibrary import resources
from modelLibrary.modules import readWrite
from modelLibrary.utils import platforms


class Preference(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Preference, self).__init__(parent)
        self.brows_directory = resources.getWorkspacePath()
        self.module, self.lable, self.version = platforms.get_tool_kit()
        self.bundles = {}
        self.setup_ui()
        self.create_preference()
        self.create_widgets()

    def setup_ui(self):
        self.setObjectName('model')
        self.setWindowTitle(
            'Preferences ({} {})'.format(self.lable, self.version))
        self.resize(700, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_model')
        self.groupbox.setTitle('Library Directories')
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
        self.button_add = QtGui.QPushButton(self.groupbox)
        self.button_add.setObjectName('button_add')
        self.button_add.setText(u'\u002B')
        self.button_add.setStyleSheet('color: #0000FF;')
        self.button_add.setMinimumSize(QtCore.QSize(25, 25))
        self.button_add.setMaximumSize(QtCore.QSize(25, 25))
        self.button_add.hide()
        self.verticallayout_item.addWidget(self.button_add)
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
        self.button_apply = QtGui.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')
        self.horizontallayout.addWidget(self.button_apply)
        self.button_add.clicked.connect(self.add)
        self.button_cancel.clicked.connect(self.close)

    def create_preference(self):
        comment = '{} {} - preference container'.format(
            self.lable, self.version)
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about model library preference'
        type = 'preference'
        valid = True
        data = {}
        tag = 'model_library'

        resource_path = resources.getResourceTypes()[type].encode()

        rw = readWrite.ReadWrite(c=comment, cd=created_date, d=description,
                                 t=type, v=valid, data=data, tag=tag, path=resource_path, name='library_preferences', format='json')
        self.bundles = rw.get_data()
        if not self.bundles:
            rw.create()
            print '\n#result new preferences created ', rw.file_path

    def add(self):
        row_count = self.gridlayout.rowCount()
        self.add_widgets(row_count)

    def create_widgets(self):
        create_bundles = {'0': ''}
        if self.bundles:
            create_bundles = self.bundles
        keys = create_bundles.keys()
        keys.sort()
        for index in range(len(keys)):
            self.add_widgets(index, create_bundles[keys[index]])

    def add_widgets(self, row, text=None):
        button_remove = QtGui.QPushButton(self.groupbox)
        button_remove.setObjectName('button_remove_%s' % row)
        button_remove.setText(u'\u274C')
        button_remove.setStyleSheet('color: #FF0000;')
        button_remove.setMinimumSize(QtCore.QSize(25, 25))
        button_remove.setMaximumSize(QtCore.QSize(25, 25))
        button_remove.hide()
        self.gridlayout.addWidget(button_remove, row, 0, 1, 1)
        lineedit = QtGui.QLineEdit(self.groupbox)
        lineedit.setObjectName('lineedit_path_%s' % row)
        lineedit.setText(text)
        self.gridlayout.addWidget(lineedit, row, 1, 1, 1)
        button_find = QtGui.QPushButton(self.groupbox)
        button_find.setObjectName('button_find_%s' % row)
        button_find.setText('...')
        button_find.setStyleSheet('color: #0000FF;')
        button_find.setMinimumSize(QtCore.QSize(35, 25))
        button_find.setMaximumSize(QtCore.QSize(35, 25))
        self.gridlayout.addWidget(button_find, row, 2, 1, 1)
        widgets = [button_remove, lineedit, button_find]
        button_remove.clicked.connect(partial(self.remove_widgets, widgets))
        button_find.clicked.connect(partial(self.find_path, widgets))

    def remove_widgets(self, widgets):
        for each_widget in widgets:
            each_widget.deleteLater()

    def find_path(self, widgets):
        path = QtGui.QFileDialog.getExistingDirectory(
            self, 'Browser', self.brows_directory)
        if not path:
            return
        self.brows_directory = path
        widgets[1].setText(path)

    def apply(self):
        directorys = self.get_source_paths(self.gridlayout)
        comment = '{} {} - preference container'.format(
            self.lable, self.version)
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about model library preference'
        type = 'preference'
        valid = True
        data = directorys
        tag = 'model_library'
        resource_path = resources.getResourceTypes()[type]

        rw = readWrite.ReadWrite(c=comment, cd=created_date, d=description,
                                 t=type, v=valid, data=data, tag=tag, path=resource_path, name='library_preferences', format='json')
        rw.create()
        print '\n#result preferences updated ', rw.file_path
        self.close()

    def get_source_paths(self, layout):
        data = {}
        ing = 1
        for index in range(layout.rowCount()):
            if not layout.itemAt(ing):
                continue
            widget = layout.itemAt(ing).widget()
            if not widget:
                continue
            current_path = widget.text().encode()
            data.setdefault(index, current_path)
            ing += layout.columnCount()
        return data


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Preference(parent=None)
    window.show()
    sys.exit(app.exec_())
