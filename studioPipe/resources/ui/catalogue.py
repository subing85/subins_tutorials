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
import warnings

from PySide import QtCore
from PySide import QtGui


class Catalogue(QtGui.QListWidget):

    def __init__(self, parent=None, **kwargs):
        super(Catalogue, self).__init__(parent=None)
                
        self.width, self.height = 128, 128
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
            
        self.mouse_scroll = False        
        self.sroll_size = 10
        self.setup_ui()

    def setup_ui(self):
        self.setAlternatingRowColors(True)
        self.setObjectName('listWidget_catalogue')
        self.setSortingEnabled(False)
        self.setFlow(QtGui.QListView.LeftToRight)
        self.setProperty("isWrapping", True)
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setSpacing(4)
        self.setUniformItemSizes(False)
        self.setViewMode(QtGui.QListView.IconMode)
        self.setSelectionRectVisible(True)
        self.setIconSize(
            QtCore.QSize(self.width, self.height))
        self.wheelEvent = self.wheel_event
        self.keyPressEvent = self.key_press_event
        self.keyReleaseEvent = self.key_release_event
        self._ctrl_press = False

    def wheel_event(self, event):
        if not self.mouse_scroll:
            return
        icon_size = self.iconSize()
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
        self.zoom(self, self.sroll_size)

    def key_press_event(self, event):
        if QtGui.QKeyEvent.key(event) == QtCore.Qt.Key_Control:
            self.mouse_scroll = True

    def key_release_event(self, event):
        if QtGui.QKeyEvent.key(event) == QtCore.Qt.Key_Control:
            self.mouse_scroll = False

    def zoom(self, widget, ingrement):
        zoom_size = [self.width + ingrement,
                     self.height + ingrement]
        self.setIconSize(
            QtCore.QSize(zoom_size[0], zoom_size[1]))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Catalogue(parent=None)
    window.show()
    sys.exit(app.exec_())
