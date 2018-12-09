import os
import sys
from __builtin__ import super


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial


class Weights(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Weights, self).__init__(parent=None)
        self.setupUi()

    def setupUi(self):
        self.setObjectName('mirror')
        self.resize(300, 400)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)

        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle('Cluster Mirror')
        self.verticallayout.addWidget(self.groupbox)

        self.verticallayout_weight = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_weight.setObjectName('verticallayout_weight')
        self.verticallayout_weight.setSpacing(1)
        self.verticallayout_weight.setContentsMargins(1, 1, 1, 1)

        self.listwidget = QtGui.QListWidget(self.groupbox)
        self.listwidget.setObjectName('listwidget')
        self.listwidget.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listwidget.setAlternatingRowColors(True)
        self.verticallayout_weight.addWidget(self.listwidget)

        self.horizontallayout_weight = QtGui.QHBoxLayout()
        self.horizontallayout_weight.setObjectName('horizontallayout_weight')
        self.horizontallayout_weight.setSpacing(1)
        self.horizontallayout_weight.setContentsMargins(1, 1, 1, 1)
        self.verticallayout_weight.addLayout(self.horizontallayout_weight)

        self.button_export = QtGui.QPushButton(self.groupbox)
        self.button_export.setObjectName('button_export')
        self.button_export.setText('Export')
        self.horizontallayout_weight.addWidget(self.button_export)

        self.button_import = QtGui.QPushButton(self.groupbox)
        self.button_import.setObjectName('button_import')
        self.button_import.setText('Import')
        self.horizontallayout_weight.addWidget(self.button_import)

    def setCurrentButton(self, item):
        self.current_item = item
        return self.current_item


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Weights(parent=None)
    window.show()
    sys.exit(app.exec_())
