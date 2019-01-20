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
import tempfile

from PySide import QtCore
from PySide import QtGui
from functools import partial

#from maya import OpenMaya
#from maya import cmds

from modelLibrary.modules import studioMaya
from modelLibrary.modules import studioImage

from modelLibrary import resources
#from modelLibrary.utils import platforms

#reload(platforms)

reload(studioImage)
reload(studioMaya)



class Model(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Model, self).__init__(parent=None)        
        
        self.studio_image = studioImage.ImageCalibration()        
        self._width, self._height = 150, 150   
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
        
        self.horizontallayout_snapshot.setSpacing(5)
        self.horizontallayout_snapshot.setContentsMargins(5, 5, 5, 5)        
        
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
        self.button_snapshot.setMinimumSize(QtCore.QSize(self._width, self._height))
        self.button_snapshot.setMaximumSize(QtCore.QSize(self._width, self._height))
        self.horizontallayout_snapshot.addWidget(self.button_snapshot)
        
        snapshot_image = os.path.join(resources.getIconPath(), 'snapshot.png')        
        self.image_to_button(self.button_snapshot, snapshot_image, self._width, self._height)
        
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
        
        self.button_snapshot.clicked.connect(partial (self.snapshot, self.button_snapshot))
        self.button_publish.clicked.connect(self.publish)
        
        
    def snapshot(self, button):         
        self.studio_image.image_file = os.path.join(tempfile.gettempdir(),
                                    'studio_image_snapshot.png') 
        result = self.studio_image.create()
        if not result:
            QtGui.QMessageBox.warning(self, 'Warning', 'Not able to process snap shot!..', QtGui.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Snap shot - faild!...')
            return  
        self.image_to_button(button, result, self._width, self._height)
        self.button_snapshot.setStatusTip(result)      
      
    def image_to_button(self, button, path, width, height):  # Load Image to button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(width-5, height-5))
        
        
    def publish(self):       
        status_tip = self.groupbox_model.statusTip()        
        source_path = status_tip.split('\n')[-1]      

        print source_path
        
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Model(parent=None)
    window.show()
    sys.exit(app.exec_())        
        