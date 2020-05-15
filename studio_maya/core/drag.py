'''
drag.py 0.0.1 
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

from PySide import QtCore
from PySide import QtGui

from studio_maya.core import widgets


class DropArea (QtGui.QTreeWidget):
    changed = QtCore.Signal()

    def __init__(self, parent=None, **kwargs):
        super(DropArea, self).__init__(parent=None)
        self.type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.sortByColumn(1, QtCore.Qt.AscendingOrder)
        self.setColumnCount(1)
        self.setLineWidth(10)
        self.headerItem().setTextAlignment(
            0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.setIconSize(QtCore.QSize(30, 30))
        self.clear()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if not mimeData.hasUrls():
            return
        exist_urls = widgets.get_exists_items(self)
        for each_url in mimeData.urls():
            if each_url.toLocalFile() in exist_urls:
                continue
            widgets.create_item(self, self.type, each_url.toLocalFile())
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()
