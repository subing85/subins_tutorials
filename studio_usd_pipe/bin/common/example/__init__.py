#!/usr/bin/python

NAME = 'Example'
ORDER = 0
VALID = False # upadte with True
TYPE = 'common_application'
KEY = 'example'
ICON = 'close.png'
OWNER = 'Subin Gopi'
COMMENTS = 'example application'
VERSION = '0.0.0'
MODIFIED = 'April 28, 2020'

import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets


class Window(QtWidgets.QWidget):
    
    def __init__(self, parent=None):  
        super(Window, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window)         

        self.setObjectName('widget_example')
        self.resize(300, 100)
        self.setWindowTitle("Example Application")
        
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName("verticallayout")
        self.button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName("button")
        self.button.setText('Close')
        self.verticallayout.addWidget(self.button)
        self.button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_()) 
