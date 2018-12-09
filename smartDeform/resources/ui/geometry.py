import os
import sys
import warnings

path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial
from smartDeform import resources
from smartDeform.utils import read
from smartDeform.utils import generic
#from smartDeform.modules import studioMaya
#reload(studioMaya)

class Geometry(QtGui.QWidget):

    def __init__(self, parent=None, input=None):
        super(Geometry, self).__init__(parent=None)
        self.input_type = input        
        self.current_item = None
        self.title = self.get_titile(input)
        
        self.icon_path = resources.getIconPath() 
        self.input_path = resources.getInputPath(self.input_type)       
        read_data = read.Data(file=self.input_path)
        self.data = read_data.getData()
                        
        self.setupUi()

    def setupUi(self):
        self.setObjectName(self.input_type)
        self.resize(300, 400)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)

        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle(self.title)
        self.verticallayout.addWidget(self.groupbox)

        self.verticallayout_geometry = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_geometry.setObjectName('verticallayout_geometry')
        self.verticallayout_geometry.setSpacing(1)
        self.verticallayout_geometry.setContentsMargins(0, 0, 0, 0)

        self.horizontallayout_geometry = QtGui.QHBoxLayout(self.groupbox)
        self.horizontallayout_geometry.setObjectName(
            'horizontallayout_geometry')
        self.horizontallayout_geometry.setSpacing(1)
        self.horizontallayout_geometry.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_geometry.addLayout(self.horizontallayout_geometry)

        self.lineedit = QtGui.QLineEdit(self.groupbox)
        self.lineedit.setObjectName('lineedit')
        self.lineedit.setReadOnly(True)
        self.horizontallayout_geometry.addWidget(self.lineedit)

        self.button = QtGui.QPushButton(self.groupbox)
        self.button.setObjectName('button')
        self.button.setMinimumSize(QtCore.QSize(25, 25))
        self.button.setMaximumSize(QtCore.QSize(25, 25))
        self.button.setText('+')
        self.horizontallayout_geometry.addWidget(self.button)
        self.button.clicked.connect(self.add_object)        
        
        self.combobox = QtGui.QComboBox(self.groupbox)
        self.combobox.setObjectName('combobox_%s' % self.input_type)                 
        self.combobox.setToolTip('%s Deformers' % (self.title))
        self.verticallayout_geometry.addWidget(self.combobox)
       
        sort_data = generic.sortDictionary(self.data['data'])        
        for x, items in sort_data.items():
            for each in items:                
                current_icon = os.path.join(self.icon_path, '%s.png' % each)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(current_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
                self.combobox.addItem(icon, self.data['data'][each]['label'])     

        self.listwidget = QtGui.QListWidget(self.groupbox)
        self.listwidget.setObjectName('listwidget')
        self.listwidget.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listwidget.setAlternatingRowColors(True)
        self.verticallayout_geometry.addWidget(self.listwidget)
        
    def get_titile(self, label):        
        prefix, suffix = label.split('_')         
        title = prefix[0].upper() + prefix[1:] + ' ' + suffix[0].upper() + suffix[1:]
        return title
        
        

    def add_object(self):                
        # from maya import OpenMaya
                
        self.lineedit.clear()        
        my_maya = studioMaya.Maya()        
        shapes = my_maya.getShapeNode(OpenMaya.MFn.kMesh)        
        if not shapes:
            OpenMaya.MGlobal.displayWarning ('not found mesh in your selection!...')   
            return         
        self.lineedit.setText(shapes[-1].partialPathName())
        
             





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Geometry(parent=None, input='source_geometry')
    window.show()
    sys.exit(app.exec_())
