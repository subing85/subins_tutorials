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
        
        mirrors= ['Cluster', 'Skincluster']
        
        for each_mirror in mirrors:

            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox')
            self.groupbox.setTitle('%s Mirror' % each_mirror)
            self.verticallayout.addWidget(self.groupbox)
    
            self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
            self.horizontallayout.setObjectName('horizontallayout_%s' % each_mirror)
            self.horizontallayout.setSpacing(10)
            self.horizontallayout.setContentsMargins(20, 10, 10, 10)
    
            self.radiobutton_x = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_x.setObjectName('radiobutton_x_%s' % each_mirror)
            self.radiobutton_x.setText('X')
            self.radiobutton_x.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_x)
    
            self.radiobutton_y = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_y.setObjectName('radiobutton_y_%s' % each_mirror)
            self.radiobutton_y.setText('Y')
            self.radiobutton_y.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_y)
    
            self.radiobutton_z = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_z.setObjectName('radiobutton_z_%s' % each_mirror)
            self.radiobutton_z.setText('Z')
            self.radiobutton_z.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_z)
    
            self.button_mirror = QtGui.QPushButton(self.groupbox)
            self.button_mirror.setObjectName('button_mirror_%s' % each_mirror)
            self.button_mirror.setText('Mirror')
            self.horizontallayout.addWidget(self.button_mirror)
            
            
            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox_%s' % each_mirror)
            self.groupbox.setTitle(each_mirror)
            self.verticallayout.addWidget(self.groupbox)
            
            self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
            self.horizontallayout.setObjectName('horizontallayout_%s' % each_mirror)
            self.horizontallayout.setSpacing(1)
            self.horizontallayout.setContentsMargins(1, 1, 1, 1)
    
            self.button_combine = QtGui.QPushButton(self.groupbox)
            self.button_combine.setObjectName('button_combine_%s' % each_mirror)
            self.button_combine.setText('Combine %s' % each_mirror)
            self.horizontallayout.addWidget(self.button_combine)
    
            self.button_copy = QtGui.QPushButton(self.groupbox)
            self.button_copy.setObjectName('button_copy_%s' % each_mirror)
            self.button_copy.setText('Copy %s' % each_mirror)
            self.horizontallayout.addWidget(self.button_copy)   
                     
            spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
            self.verticallayout.addItem(spacerItem)            

    def setCurrentButton(self, item):
        self.current_item = item
        return self.current_item


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Mirror(parent=None)
    window.show()
    sys.exit(app.exec_())
