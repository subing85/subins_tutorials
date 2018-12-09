import os
import sys
from __builtin__ import super


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial


class Mirror(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Mirror, self).__init__(parent=None)
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
        self.groupbox.setTitle('Cluster Mirror')
        self.verticallayout.addWidget(self.groupbox)

        self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(20, 10, 10, 10)

        self.radiobutton_x = QtGui.QRadioButton(self.groupbox)
        self.radiobutton_x.setObjectName('radiobutton_x')
        self.radiobutton_x.setText('X')
        self.radiobutton_x.setMinimumSize(QtCore.QSize(0, 10))
        self.horizontallayout.addWidget(self.radiobutton_x)

        self.radiobutton_y = QtGui.QRadioButton(self.groupbox)
        self.radiobutton_y.setObjectName('radiobutton_y')
        self.radiobutton_y.setText('Y')
        self.radiobutton_y.setMinimumSize(QtCore.QSize(0, 10))
        self.horizontallayout.addWidget(self.radiobutton_y)

        self.radiobutton_z = QtGui.QRadioButton(self.groupbox)
        self.radiobutton_z.setObjectName('radiobutton_z')
        self.radiobutton_z.setText('Z')
        self.radiobutton_z.setMinimumSize(QtCore.QSize(0, 10))
        self.horizontallayout.addWidget(self.radiobutton_z)

        self.button_mirror = QtGui.QPushButton(self.groupbox)
        self.button_mirror.setObjectName('button_mirror')
        self.button_mirror.setText('Mirror')
        self.horizontallayout.addWidget(self.button_mirror)

    def setCurrentButton(self, item):
        self.current_item = item
        return self.current_item


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Mirror(parent=None)
    window.show()
    sys.exit(app.exec_())
