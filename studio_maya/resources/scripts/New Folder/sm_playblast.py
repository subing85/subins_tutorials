import sys
from PySide import QtGui
from PySide import QtCore

from pymel import core


class Playblast(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(Playblast, self).__init__(parent)        
        self.setup_ui()
        self.get_cameras()      
        
    def setup_ui(self):
        self.setObjectName('widget_playblast')
        self.resize(385, 166)
        self.setWindowTitle('Studio Playblast 0.0.1')        
        aligin = QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter
        self.gridlayout = QtGui.QGridLayout(self)
        self.gridlayout.setObjectName('gridlayout')
        self.label_camera = QtGui.QLabel(self)
        self.label_camera.setAlignment(aligin)
        self.label_camera.setObjectName('label_camera')
        self.label_camera.setText('Camera')        
        self.gridlayout.addWidget(self.label_camera, 0, 0, 1, 1)
        self.combobox_camera = QtGui.QComboBox(self)
        self.combobox_camera.setObjectName('combobox_camera')
        self.gridlayout.addWidget(self.combobox_camera, 0, 1, 1, 3)
        self.label_resolution = QtGui.QLabel(self)
        self.label_resolution.setAlignment(aligin)
        self.label_resolution.setObjectName('label_resolution')
        self.label_resolution.setText('Resolution')        
        self.gridlayout.addWidget(self.label_resolution, 1, 0, 1, 1)
        self.combobox_resolution = QtGui.QComboBox(self)
        self.combobox_resolution.setObjectName('combobox_resolution')
        self.gridlayout.addWidget(self.combobox_resolution, 1, 1, 1, 3)
        self.label_startframe = QtGui.QLabel(self)
        self.label_startframe.setAlignment(aligin)
        self.label_startframe.setObjectName('label_startframe')
        self.label_startframe.setText('Start Frame')        
        self.gridlayout.addWidget(self.label_startframe, 2, 0, 1, 1)
        self.spinbox_startframe = QtGui.QSpinBox(self)
        self.spinbox_startframe.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinbox_startframe.setObjectName('spinbox_startframe')
        self.gridlayout.addWidget(self.spinbox_startframe, 2, 1, 1, 1)
        self.label_endframe = QtGui.QLabel(self)
        self.label_endframe.setAlignment(aligin)
        self.label_endframe.setText('End Frame')                
        self.label_endframe.setObjectName('label_endframe')
        self.gridlayout.addWidget(self.label_endframe, 2, 2, 1, 1)
        self.spinbox_endframe = QtGui.QSpinBox(self)
        self.spinbox_endframe.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinbox_endframe.setObjectName('spinbox_endframe')
        self.gridlayout.addWidget(self.spinbox_endframe, 2, 3, 1, 1)
        self.button_playblast = QtGui.QPushButton(self)
        self.button_playblast.setObjectName('button_playblast')
        self.button_playblast.setText('Playblast')        
        self.gridlayout.addWidget(self.button_playblast, 3, 0, 1, 4)
        
    
    def get_cameras(self):        
        camera = [each.name()for each in core.ls(type='camera')]        
        self.combobox_camera.addItems(camera)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_window = Playblast()
    my_window.show()
    sys.exit(app.exec_())
