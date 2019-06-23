'''
catalogue.py 0.0.1 
Date: January 15, 2019
Last modified: June 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''


import sys
import warnings

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets


class Catalogue(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Catalogue, self).__init__(parent=None)
        self.mouse_scroll = False
        self.currnet_size = [128, 128]
        self.sroll_size = 10
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('catalogue')
        self.resize(500, 800)
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName('splitter')
        self.verticallayout.addWidget(self.splitter)
        self.treewidget_folder = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_folder.setObjectName('treewidget_folder')
        self.treewidget_folder.setAlternatingRowColors(True)
        self.treewidget_folder.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treewidget_folder.setHeaderHidden(True)
        self.treewidget_folder.headerItem().setText(0, 'Folders')
        self.splitter.addWidget(self.treewidget_folder)
        self.listWidget_catalogue = QtWidgets.QListWidget(self.splitter)
        self.listWidget_catalogue.setAlternatingRowColors(True)
        self.listWidget_catalogue.setObjectName('listWidget_catalogue')
        self.listWidget_catalogue.setSortingEnabled(False)
        self.listWidget_catalogue.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_catalogue.setProperty("isWrapping", True)
        self.listWidget_catalogue.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget_catalogue.setSpacing(4)
        self.listWidget_catalogue.setUniformItemSizes(False)
        self.listWidget_catalogue.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget_catalogue.setSelectionRectVisible(True)
        self.listWidget_catalogue.setIconSize(
            QtCore.QSize(self.currnet_size[0], self.currnet_size[1]))
        self.splitter.addWidget(self.listWidget_catalogue)
        self.listWidget_catalogue.wheelEvent = self.wheel_event
        self.listWidget_catalogue.keyPressEvent = self.key_press_event
        self.listWidget_catalogue.keyReleaseEvent = self.key_release_event
        self._ctrl_press = False

    def wheel_event(self, event):
        if not self.mouse_scroll:
            return
        icon_size = self.listWidget_catalogue.iconSize()
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
        self.zoom(self.listWidget_catalogue, self.sroll_size)

    def key_press_event(self, event):
        if QtGui.QKeyEvent.key(event) == QtCore.Qt.Key_Control:    
            self.mouse_scroll = True

    def key_release_event(self, event):
        if QtGui.QKeyEventTransition.key(event) == QtCore.Qt.Key_Control:            
            self.mouse_scroll = False

    def zoom(self, widget, ingrement):
        zoom_size = [self.currnet_size[0] + ingrement,
                     self.currnet_size[1] + ingrement]
        self.listWidget_catalogue.setIconSize(
            QtCore.QSize(zoom_size[0], zoom_size[1]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Catalogue(parent=None)
    window.show()
    sys.exit(app.exec_())
