'''
catalogue.py 0.0.1 
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
import os
import warnings

from PySide import QtCore
from PySide import QtGui
from functools import partial

from assetLibrary import resources
from assetLibrary.core import assets


class Catalogue(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Catalogue, self).__init__(parent=None)
        self.mouse_scroll = False
        self.currnet_size = [128, 128]
        self.brows_directory = resources.getWorkspacePath()
        self.sroll_size = 10
        self.setup_ui()
        self.set_icons()

    def setup_ui(self):
        self.setObjectName('catalogue')
        self.resize(500, 800)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName('splitter')
        self.verticallayout.addWidget(self.splitter)
        self.treewidget_folder = QtGui.QTreeWidget(self.splitter)
        self.treewidget_folder.setObjectName('treewidget_folder')
        self.treewidget_folder.setAlternatingRowColors(True)
        self.treewidget_folder.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.treewidget_folder.setHeaderHidden(True)
        self.treewidget_folder.headerItem().setText(0, 'Folders')
        self.splitter.addWidget(self.treewidget_folder)
        self.listwidget_catalogue = QtGui.QListWidget(self.splitter)
        self.listwidget_catalogue.setAlternatingRowColors(True)
        self.listwidget_catalogue.setObjectName('listWidget_catalogue')
        self.listwidget_catalogue.setSortingEnabled(False)
        self.listwidget_catalogue.setFlow(QtGui.QListView.LeftToRight)
        self.listwidget_catalogue.setProperty("isWrapping", True)
        self.listwidget_catalogue.setResizeMode(QtGui.QListView.Adjust)
        self.listwidget_catalogue.setSpacing(4)
        self.listwidget_catalogue.setUniformItemSizes(False)
        self.listwidget_catalogue.setViewMode(QtGui.QListView.IconMode)
        self.listwidget_catalogue.setSelectionRectVisible(True)
        self.listwidget_catalogue.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listwidget_catalogue.setIconSize(
            QtCore.QSize(self.currnet_size[0], self.currnet_size[1]))
        self.splitter.addWidget(self.listwidget_catalogue)
        self.listwidget_catalogue.wheelEvent = self.wheel_event
        self.listwidget_catalogue.keyPressEvent = self.key_press_event
        self.listwidget_catalogue.keyReleaseEvent = self.key_release_event
        self._ctrl_press = False

    def set_icons(self):
        actions = self.findChildren(QtGui.QAction)
        buttons = self.findChildren(QtGui.QPushButton)
        for each_action in actions + buttons:
            objectName = each_action.objectName()
            if not objectName:
                continue
            current_icon = '{}.png'.format(objectName.split('_')[-1])
            icon_path = os.path.join(resources.getIconPath(), current_icon)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            each_action.setIcon(icon)

    def wheel_event(self, event):
        if not self.mouse_scroll:
            return
        icon_size = self.listwidget_catalogue.iconSize()
        if event.delta() > 0:
            if icon_size.width() > 2048 or icon_size.height() > 2048:
                warnings.warn('Maximum size', Warning)
                return
            self.sroll_size += 10
        else:
            if icon_size.width() < 10 or icon_size.height() < 10:
                warnings.warn('Minimum size', Warning)
                return
            self.sroll_size -= 10
        self.zoom(self.listwidget_catalogue, self.sroll_size)

    def key_press_event(self, event):
        if QtGui.QKeyEvent.key(event) == QtCore.Qt.Key_Control:
            self.mouse_scroll = True

    def key_release_event(self, event):
        if QtGui.QKeyEvent.key(event) == QtCore.Qt.Key_Control:
            self.mouse_scroll = False

    def zoom(self, widget, ingrement):
        zoom_size = [self.currnet_size[0] + ingrement,
                     self.currnet_size[1] + ingrement]
        self.listwidget_catalogue.setIconSize(
            QtCore.QSize(zoom_size[0], zoom_size[1]))

    def search_assets(self, input_widget):
        input = str(input_widget.text())
        search_obj = assets.SearchAssets(input)
        groups = ['Chr', 'prp', 'sachin']
        self.load_assets(self.treewidget_search, search_obj.get_assets, groups)

    def set_root(self, widget):
        path = QtGui.QFileDialog.getExistingDirectory(
            self, 'Browser', self.brows_directory)
        if not path:
            return
        self.brows_directory = path
        widget.setText(path)

    def load_assets(self, treeWidget, paths, groups):
        asset_groups = ['__None__'] + groups
        for index in range(len(paths)):
            item = QtGui.QTreeWidgetItem(treeWidget)
            item.setText(0, str(index + 1))
            item.setText(1, paths[index])
            combobox = QtGui.QComboBox(treeWidget)
            combobox.setObjectName('combobox_%s' % index)
            combobox.setMinimumSize(QtCore.QSize(50, 20))
            combobox.addItems(asset_groups)
            combobox.setCurrentIndex(0)
            combobox.setToolTip('add to asset folders')
            treeWidget.setItemWidget(item, 2, combobox)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Catalogue(parent=None)
    window.show()
    sys.exit(app.exec_())
