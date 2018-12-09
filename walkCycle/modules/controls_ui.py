
import sys
import os
import warnings


from PySide import QtGui
from PySide import QtCore
from pprint import pprint
from functools import partial

path  = '/venture/subins_tutorials/walkCycle'
if path not in sys.path:
    sys.path.append(path)

from utils import readwrite
from utils import generic
import resources


reload(readwrite)
reload(resources)
reload(generic)

    
    
class Controls(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super (Controls, self).__init__(parent)
        
        self.control_path = resources.getControlsPath()
        self.icon_path = resources.getIconPath()
        self._read = readwrite.Read(file=self.control_path)
        self._data = self._read.getData()
        
        self.setupUi()


    
    def setupUi(self):
        self.resize(500, 800)
        self.setObjectName('Mainwindow_controls')
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        
        self.groupbox = QtGui.QGroupBox(self.centralwidget)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle('Controls')
        self.verticallayout.addWidget(self.groupbox)
        
        self.verticallayout_group = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_group.setObjectName('verticallayout_group')       
        
        self.scrollarea = QtGui.QScrollArea(self.groupbox)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setObjectName('scrollArea')
        self.scrollarea_contents = QtGui.QWidget()
        self.scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 488, 342))
        self.scrollarea_contents.setObjectName('scrollarea_contents')
        self.verticallayout_group.addWidget(self.scrollarea)
        # self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollarea.setWidget(self.scrollarea_contents)          

        self.verticallayout_controls = QtGui.QVBoxLayout(self.scrollarea_contents)
        self.verticallayout_controls.setObjectName('verticallayout_controls')  
        self.verticallayout_controls.setContentsMargins(10, 10, 10, 10)                                                                                 
        self.verticallayout_controls.setSpacing(0) 
                       
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)       
         
        sort_data = generic.sortDictionary(self._data['contols'])
        for each_index, controls in sort_data.items():
            for each_control in controls:
                current_control = self._data['contols'][each_control]
                 
                self.horizontallayout_control = QtGui.QHBoxLayout()
                self.horizontallayout_control.setObjectName('horizontallayout_{}'.format(each_control))
                self.horizontallayout_control.setContentsMargins(0, 0, 0, 0)                                                                                 
                self.horizontallayout_control.setSpacing(1)                  
                self.verticallayout_controls.addLayout(self.horizontallayout_control)
                 
                self.label_name = QtGui.QLabel(self.scrollarea_contents)
                self.label_name.setSizePolicy(size_policy)
                self.label_name.setObjectName('label_name_{}'.format(each_control))
                self.label_name.setMinimumSize(QtCore.QSize(150, 0))
                self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)                
                self.label_name.setText(current_control['label'].encode())
                self.horizontallayout_control.addWidget(self.label_name)
               
                self.lineedit_name = QtGui.QLineEdit(self.scrollarea_contents)
                self.lineedit_name.setObjectName('lineedit_name_{}'.format(each_control))
                self.horizontallayout_control.addWidget(self.lineedit_name)
                 
                self.button_add = QtGui.QPushButton(self.scrollarea_contents)
                self.button_add.setObjectName('button_add_{}'.format(each_control))
                self.button_add.setMinimumSize(QtCore.QSize(30, 0))
                self.button_add.setMaximumSize(QtCore.QSize(30, 16777215))
                self.button_add.setText('+') # u'+02C2'                
                self.horizontallayout_control.addWidget(self.button_add)                
                 
                self.horizontallayout_orient = QtGui.QHBoxLayout()
                self.horizontallayout_orient.setObjectName('horizontallayout_orient_{}'.format(each_control))
                self.horizontallayout_orient.setContentsMargins(0, 0, 0, 0)                                                                                 
                self.horizontallayout_orient.setSpacing(1)                   
                self.verticallayout_controls.addLayout(self.horizontallayout_orient)
                                 
                self.gridlayout_orient = QtGui.QGridLayout()
                self.gridlayout_orient.setObjectName('GridLayout_orient_{}'.format(each_control))
                self.gridlayout_orient.setContentsMargins(0, 0, 0, 0)                                                                                 
                self.gridlayout_orient.setHorizontalSpacing(1)   
                self.gridlayout_orient.setVerticalSpacing(1)                  
                                
                self.horizontallayout_orient.addLayout(self.gridlayout_orient)
                 
                spaceritem_start = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                self.gridlayout_orient.addItem(spaceritem_start, 0, 0, 1, 1)                
                 
                self.label_aim = QtGui.QLabel(self.scrollarea_contents)
                self.label_aim.setObjectName('label_aim_{}'.format(each_control))
                self.label_aim.setText('Aim Vector')  
                self.label_aim.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)                
                self.gridlayout_orient.addWidget(self.label_aim, 0, 1, 1, 1)
                        
                self.spinbox_aimx = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_aimx.setObjectName('spinbox_aimx_{}'.format(each_control))               
                self.spinbox_aimx.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_aimx.setMinimum(-1)
                self.spinbox_aimx.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_aimx, 0, 2, 1, 1)                      
                 
                self.spinbox_aimy = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_aimy.setObjectName('spinbox_aimy_{}'.format(each_control))               
                self.spinbox_aimy.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_aimy.setMinimum(-1)
                self.spinbox_aimy.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_aimy, 0, 3, 1, 1)   
                         
                self.spinbox_aimz = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_aimz.setObjectName('spinbox_aimz_{}'.format(each_control))               
                self.spinbox_aimz.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_aimz.setMinimum(-1)
                self.spinbox_aimz.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_aimz, 0, 4, 1, 1)  
                 
                self.label_up = QtGui.QLabel(self.scrollarea_contents)
                self.label_up.setObjectName('label_up_{}'.format(each_control))
                self.label_up.setText('Up Vector')
                self.label_up.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)                
                self.gridlayout_orient.addWidget(self.label_up, 1, 1, 1, 1)                           
  
                self.spinbox_upx = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_upx.setObjectName('spinbox_upx_{}'.format(each_control))               
                self.spinbox_upx.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_upx.setMinimum(-1)
                self.spinbox_upx.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_upx, 1, 2, 1, 1)                      
                   
                self.spinbox_upy = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_upy.setObjectName('spinbox_upy_{}'.format(each_control))               
                self.spinbox_upy.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_upy.setMinimum(-1)
                self.spinbox_upy.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_upy, 1, 3, 1, 1)   
                           
                self.spinbox_upz = QtGui.QSpinBox(self.scrollarea_contents)
                self.spinbox_upz.setObjectName('spinbox_upz_{}'.format(each_control))               
                self.spinbox_upz.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                self.spinbox_upz.setMinimum(-1)
                self.spinbox_upz.setMaximum(1)
                self.gridlayout_orient.addWidget(self.spinbox_upz, 1, 4, 1, 1)  
                  
                self.label_icon = QtGui.QLabel(self.scrollarea_contents)
                self.label_icon.setObjectName('label_up_{}'.format(each_control))                 
                self.label_icon.setMinimumSize(QtCore.QSize(100, 100))
                self.label_icon.setMaximumSize(QtCore.QSize(100, 100))
                
                current_icon = os.path.join(self.icon_path, 'orient_000_000.png')
                self.label_icon.setPixmap(QtGui.QPixmap(current_icon))
                self.label_icon.setScaledContents(50)
                                              
                self.horizontallayout_orient.addWidget(self.label_icon)
                
                aim_spinebox_list = [self.spinbox_aimx, self.spinbox_aimy, self.spinbox_aimz]
                up_spinebox_list = [self.spinbox_upx, self.spinbox_upy, self.spinbox_upz]
                
                self.spinbox_aimx.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_aimx,
                                                                self.spinbox_aimy, self.spinbox_aimz, self.spinbox_upx,
                                                                aim_spinebox_list, up_spinebox_list,
                                                                self.label_icon))        
                             
                self.spinbox_aimy.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_aimy,
                                                                self.spinbox_aimx, self.spinbox_aimz, self.spinbox_upy,
                                                                aim_spinebox_list, up_spinebox_list,
                                                                self.label_icon)) 
                                    
                self.spinbox_aimz.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_aimz,
                                                                self.spinbox_aimx, self.spinbox_aimy, self.spinbox_upz,
                                                                aim_spinebox_list, up_spinebox_list,
                                                                self.label_icon)) 
                                    
                self.spinbox_upx.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_upx,
                                                               self.spinbox_upy, self.spinbox_upz, self.spinbox_aimx,
                                                               aim_spinebox_list, up_spinebox_list,
                                                               self.label_icon))    
                                 
                self.spinbox_upy.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_upy,
                                                               self.spinbox_upx, self.spinbox_upz, self.spinbox_aimy,
                                                               aim_spinebox_list, up_spinebox_list,
                                                               self.label_icon))
                                     
                self.spinbox_upz.valueChanged.connect(partial (self.setSpineboxValue, self.spinbox_upz,
                                                               self.spinbox_upx, self.spinbox_upy, self.spinbox_aimz,
                                                               aim_spinebox_list, up_spinebox_list,
                                                               self.label_icon))     
                 
                #spaceritem_end = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
                #self.gridlayout_orient.addItem(spaceritem_end, 1, 5, 1, 1)
                
                self.button_add.clicked.connect(partial (self.addControls, self.lineedit_name))             
             
        self.button_publish = QtGui.QPushButton(self.groupbox)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish') # u'+02C2'              
        self.verticallayout_group.addWidget(self.button_publish)
        self.button_publish.clicked.connect(self.publish) 
             
                 
      
    def setSpineboxValue(self, box, x, y, z, aim_boxs, up_boxs, label, value):
        box.setEnabled(True)    
        if value!=0:         
            x.setEnabled(False)    
            y.setEnabled(False) 
            z.setEnabled(False) 
        else:   
            x.setEnabled(True)    
            y.setEnabled(True) 
            z.setEnabled(True)            
        aim_x = int(aim_boxs[0].value())
        aim_y = int(aim_boxs[1].value())
        aim_z = int(aim_boxs[2].value())        
        up_x = int(up_boxs[0].value())
        up_y = int(up_boxs[1].value())
        up_z = int(up_boxs[2].value())        
        icon_name = 'orient_%s%s%s_%s%s%s.png' % (aim_x, aim_y, aim_z, up_x, up_y, up_z)
        current_icon = os.path.join(self.icon_path, icon_name)
        if not os.path.isfile(current_icon):
            current_icon = os.path.join(self.icon_path, 'orient_000_000.png')
        label.setPixmap(QtGui.QPixmap(current_icon))
        label.setScaledContents (50)
        
    def addControls(self, lineedit):
        from maya import cmds
        current_controls = cmds.ls(sl=True)        
        if not current_controls:
            warnings.warn('no selection', Warning)
            return        
        lineedit.setText(current_controls[-1])
        
    def publish(self):
        
        task, ok = QtGui.QInputDialog.getText(self, 'Task Input', 'Enter the Task name')                        
        if not ok:
            warnings.warn('abrot publish!...', Warning)
            return
        
        publish_file = os.path.join(resources.getPublishDirectory(), '%s.json' % task)        
        if not os.path.isdir(os.path.dirname(publish_file)):
            os.makedirs(os.path.dirname(publish_file))
        
        write = readwrite.Write(publish_file, data)
        write.toWrite()
        
        
        
        
        

if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = Controls ()
    window.show ()
    sys.exit (app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/walkCycle/modules/controls_ui.ui'
#
# Created: Sun Dec  2 21:19:43 2018
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(516, 391)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollarea_contents = QtGui.QWidget()
        self.scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 488, 342))
        self.scrollarea_contents.setObjectName(_fromUtf8("scrollarea_contents"))
        self.scrollArea.setWidget(self.scrollarea_contents)
        
        self.verticalLayout_content = QtGui.QVBoxLayout(self.scrollarea_contents)
        self.verticalLayout_content.setObjectName(_fromUtf8("verticalLayout_content"))
        self.horizontalLayout_leg = QtGui.QHBoxLayout()
        self.horizontalLayout_leg.setObjectName(_fromUtf8("horizontalLayout_leg"))
        self.label = QtGui.QLabel(self.scrollarea_contents)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_leg.addWidget(self.label)
        self.lineEdit_leg = QtGui.QLineEdit(self.scrollarea_contents)
        self.lineEdit_leg.setObjectName(_fromUtf8("lineEdit_leg"))
        self.horizontalLayout_leg.addWidget(self.lineEdit_leg)
        self.pushButton_leg = QtGui.QPushButton(self.scrollarea_contents)
        self.pushButton_leg.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_leg.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_leg.setObjectName(_fromUtf8("pushButton_leg"))
        self.horizontalLayout_leg.addWidget(self.pushButton_leg)
        self.verticalLayout_content.addLayout(self.horizontalLayout_leg)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setMargin(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.scrollarea_contents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollarea_contents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 0, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.spinBox_4 = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.gridLayout.addWidget(self.spinBox_4, 1, 4, 1, 1)
        self.spinBox_3 = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout.addWidget(self.spinBox_3, 0, 4, 1, 1)
        self.spinBox_6 = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.gridLayout.addWidget(self.spinBox_6, 1, 3, 1, 1)
        self.spinBox_5 = QtGui.QSpinBox(self.scrollarea_contents)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.gridLayout.addWidget(self.spinBox_5, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.label_image = QtGui.QLabel(self.scrollarea_contents)
        self.label_image.setObjectName(_fromUtf8("label_image"))
        self.horizontalLayout.addWidget(self.label_image)
        self.verticalLayout_content.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollarea_contents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SUbin", None))
        self.pushButton_leg.setText(_translate("MainWindow", "PushButton", None))
        self.label_3.setText(_translate("MainWindow", "Leg", None))
        self.label_2.setText(_translate("MainWindow", "Leg", None))
        self.label_image.setText(_translate("MainWindow", "TextLabel", None))
