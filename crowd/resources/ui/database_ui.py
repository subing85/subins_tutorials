'''
database_ui.py 0.0.1 
Date: June 10, 2019
Last modified: June 14, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys
import logging

from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.core import database
from crowd.utils import platforms


class Connect(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Connect, self).__init__(parent)
        self.object_name = 'publish_mainwindow'
        self.heading = '[Subin CROwd]\t Publish Informations'
        valid = platforms.had_tool_valid()
        if not valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resource.getDownloadLink())
            QtGui.QMessageBox.critical(
                self, 'Critical', message, QtGui.QMessageBox.Ok)
            return
        tool_kit = platforms.get_tool_kit()
        self.tool_kit_object, self.tool_kit_name, self.version = tool_kit['publish']
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [800, 600]
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.font_size, self.font_type = resource.getFontSize()
        self.setup_ui()
        self.modify_ui()
        self.set_contex_menu()

    def setup_ui(self):
        self.setObjectName(self.object_name)
        self.resize(self.width, self.height)
        self.setWindowTitle(self.tool_kit_titile)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.setStyleSheet('font: 14pt \"Sans Serif\";')
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.label_title = QtGui.QLabel(self)
        self.label_title.setObjectName('label')
        self.label_title.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_title.setText(self.heading)
        self.verticallayout.addWidget(self.label_title)
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizepolicy.setHorizontalStretch(0)
        sizepolicy.setVerticalStretch(0)
        self.groupbox_input = QtGui.QGroupBox(self)
        self.groupbox_input.setObjectName('groupbox_input')
        self.groupbox_input.setTitle('Inputs')
        self.groupbox_input.setSizePolicy(sizepolicy)
        self.verticallayout.addWidget(self.groupbox_input)
        self.horizontallayout_input = QtGui.QHBoxLayout(self.groupbox_input)
        self.horizontallayout_input.setObjectName('horizontalLayout_input')
        self.horizontallayout_input.setSpacing(4)
        self.horizontallayout_input.setContentsMargins(4, 30, 4, 4)
        self.combobox_input = QtGui.QComboBox(self.groupbox_input)
        self.combobox_input.setObjectName('comboBox_layout')
        self.combobox_input.setStyleSheet(
            'font: %spt \"%s\";' % (self.font_size, self.font_type))
        self.horizontallayout_input.addWidget(self.combobox_input)
        self.lineedit_input = QtGui.QLineEdit(self.groupbox_input)
        self.lineedit_input.setObjectName('lineEdit_bundle')
        self.lineedit_input.setStyleSheet(
            'font: %spt \"%s\";' % (self.font_size, self.font_type))
        self.horizontallayout_input.addWidget(self.lineedit_input)
        self.groupbox_records = QtGui.QGroupBox(self)
        self.groupbox_records.setObjectName('groupbox_records')
        self.groupbox_records.setTitle('Records')
        self.verticallayout.addWidget(self.groupbox_records)
        self.verticallayout_records = QtGui.QVBoxLayout(
            self.groupbox_records)
        self.verticallayout_records.setObjectName('verticallayout_records')
        self.verticallayout_records.setSpacing(4)
        self.verticallayout_records.setContentsMargins(10, 10, 5, 5)
        self.treewidget = QtGui.QTreeWidget(self.centralwidget)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget))
        self.verticallayout_records.addWidget(self.treewidget)
        self.combobox_input.currentIndexChanged.connect(
            partial(self.load_data, self.combobox_input, self.treewidget))

    def modify_ui(self):
        db = database.Connect()
        tables = db.get_tables()
        tables = ['None'] + tables
        self.combobox_input.addItems(tables)

    def on_context_menu(self, treewidget, point):
        index = treewidget.indexAt(point)
        if not index.isValid():
            return
        # self.contex_menu.exec_ (QtGui.QCursor.pos())
        item = treewidget.indexAt(point)
        self.contex_menu.exec_(treewidget.mapToGlobal(point))

    def set_contex_menu(self):
        self.contex_menu = QtGui.QMenu(self)
        self.contex_menu.setObjectName('contex_menu')
        self.contex_menu.setTitle('Edit')
        self.action_reload = QtGui.QAction(self)
        self.action_reload.setObjectName('action_reload')
        self.action_reload.setText('Reload')
        self.action_reload.triggered.connect(self.reload)
        self.contex_menu.addAction(self.action_reload)      
        self.action_remove = QtGui.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove')
        self.action_remove.triggered.connect(self.remove)
        self.contex_menu.addAction(self.action_remove)
        self.contex_menu.addSeparator()

    def load_data(self, combobox, treewidget, *args):
        treewidget.clear()
        table = str(combobox.itemText(args[0]))
        if not table or table == 'None':
            return
        db = database.Connect(table=table)
        columns = db.get_columns()
        if not columns:
            return
        treewidget.clear()
        for index, each in enumerate(columns):
            treewidget.headerItem().setText(index, each)
            treewidget.header().resizeSection(index, 250)
        treewidget.header().resizeSection(0, 100)
        treewidget.header().resizeSection(1, 200)
        treewidget.header().resizeSection(2, 200)
        treewidget.header().resizeSection(3, 300)
        contents = db.select()
        for content in contents:
            item = QtGui.QTreeWidgetItem(treewidget)
            for index, each in enumerate(content):
                item.setText(index, str(each))
                
    def reload(self):
        index = self.combobox_input.currentIndex()
        self.load_data(self.combobox_input, self.treewidget, index)

    def remove(self):
        replay = QtGui.QMessageBox.question(
            self,
            'Question',
            'Are you sure\nWant to reomve?...',
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No)
        if replay == QtGui.QMessageBox.No:
            logging.warning('abort!...')
            return
        table = str(self.combobox_input.currentText())
        if not table or table == 'None':
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Select the any one in the table and try!...',
                QtGui.QMessageBox.Ok)
            return
        if not self.treewidget.selectedItems():
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Select the any one in the items and try!...',
                QtGui.QMessageBox.Ok)
            return
        select_items = self.treewidget.selectedItems()
        result = True
        for item in select_items:
            id = str(item.text(0))
            tag = str(item.text(1))
            db = database.Connect(table=table)
            try:
                db.delete(id, tag)
                result = True
            except Exception as error:
                QtGui.QMessageBox.warning(
                    self, 'Warning', str(error), QtGui.QMessageBox.Ok)
                result = False
        if result:
            logging.info('Remove success!...')
        else:
            logging.warning('Remove failed!...')
        self.reload()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
