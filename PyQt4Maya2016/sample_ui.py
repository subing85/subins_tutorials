import sys

PYQT_PATH = 'Z:/module/maya2016/Python27/Lib/site-packages'
if PYQT_PATH not in sys.path :
    sys.path.append(PYQT_PATH)

import PyQt4.QtCore as QtCore   
import PyQt4.QtGui as QtGui
import maya.OpenMayaUI as omu
import maya.OpenMaya as om
import sip
import maya.cmds as cmds

PY_OBJECT = omu.MQtUtil.mainWindow()
MAYA_MAIN_WINOW = sip.wrapinstance(long(PY_OBJECT), QtCore.QObject)


class MYWINDOW(object) :
    
    def __init__(self):
        pass
        
    def windowGUI(self):
        # Create UI
        self.mainWindow = QtGui.QMainWindow(parent=MAYA_MAIN_WINOW)
        self.mainWindow.setWindowTitle('Test UI v0.1')
        self.mainWindow.resize(300, 150)
        self.mainWindow.setObjectName('mainWindow')
        
        # QWidget        
        self.centralWidget = QtGui.QWidget(parent=self.mainWindow)
        self.centralWidget.setObjectName('centralWidget')
        
        # QVBoxLaout(verticalLayout)        
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName('verticalLayout')        
       
        # Group box
        self.groupBox_category = QtGui.QGroupBox(parent=self.mainWindow)
        self.groupBox_category.setObjectName('groupBox_category')
        self.groupBox_category.setGeometry(QtCore.QRect(10, 10, 280, 60))
        self.groupBox_category.setTitle('Categories')
        
        # QHBoxLayout(horizontalLayout)        
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_category)
        self.horizontalLayout.setObjectName('horizontalLayout')   
        
        # Radiobutton
        self.radioButton_cricle = QtGui.QRadioButton(parent=self.groupBox_category)
        self.radioButton_cricle.setObjectName('radioButton_cricle')
        self.radioButton_cricle.setGeometry(QtCore.QRect(20, 25, 60, 20))
        self.radioButton_cricle.setText('Cricle')
        
        self.radioButton_cube = QtGui.QRadioButton(parent=self.groupBox_category)
        self.radioButton_cube.setObjectName('radioButton_cube')
        self.radioButton_cube.setGeometry(QtCore.QRect(100, 25, 60, 20))
        self.radioButton_cube.setText('Cube')
        
        self.radioButton_sphere = QtGui.QRadioButton(parent=self.groupBox_category)
        self.radioButton_sphere.setObjectName('radioButton_sphere')
        self.radioButton_sphere.setGeometry(QtCore.QRect(180, 25, 60, 20))
        self.radioButton_sphere.setText('Sphere')
        
        # Add radiobutton to horizontal Layout        
        self.horizontalLayout.addWidget(self.radioButton_cricle)
        self.horizontalLayout.addWidget(self.radioButton_cube)
        self.horizontalLayout.addWidget(self.radioButton_sphere)
        
        # Pushbutton
        self.button_create = QtGui.QPushButton(parent=self.mainWindow)
        self.button_create.setObjectName('button_create')
        self.button_create.setGeometry(QtCore.QRect(10, 80, 280, 30))
        self.button_create.setText('Create') 
        self.button_create.clicked.connect(self.createMObject) 
        
        # Add groupBox and button to verticalLayout
        self.verticalLayout.addWidget(self.groupBox_category) 
        self.verticalLayout.addWidget(self.button_create)  
        
        # Set Central Widget  to QWidget      
        self.mainWindow.setCentralWidget(self.centralWidget)         
                               
        # mainWindow.show()   
        return self.mainWindow
        
    def createMObject(self) :        
        currentObject = ''
        if self.radioButton_cricle.isChecked() :
            currentObject = cmds.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1, n='My_Cricle')

        if self.radioButton_cube.isChecked() :
            currentObject = cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[0, 1, 0], cuv=4, ch=1, n='My_Cube')

        if self.radioButton_sphere.isChecked() :
            currentObject = cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1, n='My_Sphere')
            
        if currentObject :
            om.MGlobal.displayInfo('Successfully created My Maya Object\t Object name  - %s' % currentObject)
        else :
            om.MGlobal.displayWarning('Please select the object type from Categories')            

                
try :
    gui_01.close()
except :
    pass         
        
myWind = MYWINDOW()
gui_01 = myWind.windowGUI()
gui_01.show()

