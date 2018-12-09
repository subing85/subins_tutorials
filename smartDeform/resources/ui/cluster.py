import os
import sys


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial


class Cluster(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Cluster, self).__init__(parent=None)
        self.setupUi()

    def setupUi(self):
        self.setObjectName('mirror')
        self.resize(300, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)

        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle('Cluster')
        self.verticallayout.addWidget(self.groupbox)
        
        self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(1)
        self.horizontallayout.setContentsMargins(1, 1, 1, 1)

        self.button_combine = QtGui.QPushButton(self.groupbox)
        self.button_combine.setObjectName('button_combine')
        self.button_combine.setText('Combine Cluster')
        self.horizontallayout.addWidget(self.button_combine)

        self.button_copy = QtGui.QPushButton(self.groupbox)
        self.button_copy.setObjectName('button_copy')
        self.button_copy.setText('Copy Cluster')
        self.horizontallayout.addWidget(self.button_copy)

    def setCurrentButton(self, item):
        self.current_item = item
        return self.current_item


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Cluster(parent=None)
    window.show()
    sys.exit(app.exec_())
