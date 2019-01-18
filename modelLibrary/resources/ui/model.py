'''
main.py 0.0.1 
Date: January 01, 2019
Last modified: January 15, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''


import os
import sys
import webbrowser

from PySide import QtCore
from PySide import QtGui
from functools import partial

#from maya import OpenMaya
#from maya import cmds

#from modelLibrary import resources
#from modelLibrary.utils import platforms

#reload(platforms)

class Model(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Model, self).__init__(parent=None)
        
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('model')
        self.resize(400, 600)
        
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
                
        self.groupbox_model = QtGui.QGroupBox(self)
        self.groupbox_model.setObjectName('groupbox_model')
        self.groupbox_model.setTitle('Model')
        self.verticallayout.addWidget(self.groupbox_model)
        
        self.verticallayout_model = QtGui.QVBoxLayout(self.groupbox_model)
        self.verticallayout_model.setObjectName('verticallayout_model')
        self.verticallayout_model.setSpacing(10)
        self.verticallayout_model.setContentsMargins(10, 10, 10, 10)

        self.groupbox_snapshot = QtGui.QGroupBox(self.groupbox_model)
        self.groupbox_snapshot.setObjectName('groupBox_snapshot')
        self.verticallayout_model.addWidget(self.groupbox_snapshot)
       
        self.horizontallayout_snapshot = QtGui.QHBoxLayout(self.groupbox_snapshot)
        self.horizontallayout_snapshot.setObjectName('horizontallayout_snapshot')
        
        self.horizontallayout_snapshot.setSpacing(10)
        self.horizontallayout_snapshot.setContentsMargins(10, 10, 10, 10)        
        
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout_snapshot.addItem(spacer_item)
        
        self.button_snapshot = QtGui.QPushButton(self.groupbox_snapshot)
        self.button_snapshot.setObjectName('button_snapshot')
        self.button_snapshot.setText('')        
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.button_snapshot.sizePolicy().hasHeightForWidth())      
        self.button_snapshot.setSizePolicy(size_policy)        
        self.button_snapshot.setMinimumSize(QtCore.QSize(150, 150))
        self.button_snapshot.setMaximumSize(QtCore.QSize(150, 150))
        self.horizontallayout_snapshot.addWidget(self.button_snapshot)
        
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)        
        self.horizontallayout_snapshot.addItem(spacer_item)
        
        self.groupbox_label = QtGui.QGroupBox(self.groupbox_model)
        self.groupbox_label.setObjectName('groupbox_label')
        self.verticallayout_model.addWidget(self.groupbox_label)
        
        self.horizontallayout_label = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_label.setObjectName('horizontallayout_label')        
        self.horizontallayout_label.setSpacing(10)
        self.horizontallayout_label.setContentsMargins(10, 10, 10, 10)  
        
        self.label_label = QtGui.QLabel(self.groupbox_label)
        self.label_label.setObjectName('label_label')
        self.label_label.setText('Name')      
        self.horizontallayout_label.addWidget(self.label_label)
        
        self.lineEdit_label = QtGui.QLineEdit(self.groupbox_label)
        self.lineEdit_label.setObjectName('lineEdit_label')
        self.lineEdit_label.setText('')      
        self.horizontallayout_label.addWidget(self.lineEdit_label)
        
        self.textedit_history = QtGui.QTextEdit(self.groupbox_model)
        self.textedit_history.setObjectName('textedit_history')       
        self.textedit_history.setStyleSheet('')
        self.textedit_history.setReadOnly(True)
        self.verticallayout_model.addWidget(self.textedit_history)
        
        spacer_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout_model.addItem(spacer_item)

        self.button_publish = QtGui.QPushButton(self.groupbox_model)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')        
        self.verticallayout_model.addWidget(self.button_publish)
        
        self.button_build = QtGui.QPushButton(self.groupbox_model)
        self.button_build.setObjectName('button_build')
        self.button_build.setText('Build')        
        self.verticallayout_model.addWidget(self.button_build)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Model(parent=None)
    window.show()
    sys.exit(app.exec_())        
        