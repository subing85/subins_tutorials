import os
import sys
import webbrowser

from PySide import QtCore
from PySide import QtGui
from functools import partial

#from maya import OpenMaya
#from maya import cmds

import sys
path = '/mnt/venture/subins_tutorials'

if path not in sys.path:
    sys.path.append('/mnt/venture/subins_tutorials')

from modelLibrary import resources
#from modelLibrary.utils import platforms

#reload(platforms)

class Preference(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Preference, self).__init__(parent=None) 
        self.clicks = {}
        self.setup_ui()
        self.add_new(0, self.push_button_add)
        


    def setup_ui(self):
        self.setObjectName('model')
        self.setWindowTitle('Preferences')        
        self.resize(700, 100)
        
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
                
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_model')
        self.groupbox.setTitle('Library Directories')
        self.verticallayout.addWidget(self.groupbox)
        
        self.gridlayout = QtGui.QGridLayout(self.groupbox)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(10)
        self.gridlayout.setContentsMargins(10, 10, 10, 10)
                
        self.push_button_add = QtGui.QPushButton(self.groupbox)
        self.push_button_add.setObjectName('push_button_add')
        self.push_button_add.setText(u'\u002B')
        self.push_button_add.setStyleSheet('color: #0000FF;') 
        self.push_button_add.setMinimumSize(QtCore.QSize(25, 25))
        self.push_button_add.setMaximumSize(QtCore.QSize(25, 25))
        self.gridlayout.addWidget(self.push_button_add, 0, 0, 1, 1)
        
        spacer_item = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)        
        
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(5)
        self.horizontallayout.setContentsMargins(10, 10, 10, 10) 
        self.verticallayout.addLayout(self.horizontallayout)
               
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        
        self.button_apply = QtGui.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')        
        self.horizontallayout.addWidget(self.button_apply)
        self.push_button_add.clicked.connect(partial(self.add_new, 0, self.push_button_add))
        
        self.button_cancel.clicked.connect(self.close)
        self.button_apply.clicked.connect(self.apply)

    def set_path(self, lineedit, source_button):        
        path = QtGui.QFileDialog.getExistingDirectory (self, 'Browser', resources.getWorkspacePath())        
        if not path:
            return        
        lineedit.setText(path)
        source_button.setText(u'\u274C')
        source_button.setStyleSheet('color: #FF0000;')
    
    def add_new(self, row, source_button):        
        if row in self.clicks:
            for each_widget in self.clicks[row]:
                each_widget.deleteLater()            
            self.clicks.pop(row)
            return

        lineedit = QtGui.QLineEdit(self.groupbox)
        lineedit.setObjectName('lineedit_path')
        self.gridlayout.addWidget(lineedit, row, 1, 1, 1)
        
        push_button_find = QtGui.QPushButton(self.groupbox)
        push_button_find.setObjectName('push_button_find')
        push_button_find.setText('...')
        push_button_find.setStyleSheet('color: #0000FF;')            
        self.gridlayout.addWidget(push_button_find, row, 2, 1, 1)
        
        push_button_new = QtGui.QPushButton(self.groupbox)
        push_button_new.setObjectName('push_button_addnew')
        push_button_new.setText(u'\u002B')
        push_button_new.setStyleSheet('color: #0000FF;')  
        push_button_new.setMinimumSize(QtCore.QSize(25, 25))
        push_button_new.setMaximumSize(QtCore.QSize(25, 25))        
        self.gridlayout.addWidget(push_button_new, row+1, 0, 1, 1)
        
        push_button_new.clicked.connect(partial(self.add_new, row+1, push_button_new))
        push_button_find.clicked.connect(partial(self.set_path, lineedit, source_button))        
        self.clicks.setdefault(row, [lineedit, push_button_find, push_button_new])
    
    
    def apply(self):
        
        print self.clicks

        
              
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Preference(parent=None)
    window.show()
    sys.exit(app.exec_())  
        
        
        
        
              