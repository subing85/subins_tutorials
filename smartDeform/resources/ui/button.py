import os
import sys
from __builtin__ import super


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial
from smartDeform import resources
from smartDeform.utils import read
from smartDeform.utils import generic

class Button(QtGui.QWidget):

    def __init__(self, parent=None, input=None):
        super(Button, self).__init__(parent=None)
        self.input_type = input
        path = resources.getInputPath(self.input_type)       
        self.current_item = None
        read_data = read.Data(file=path)
        self.data = read_data.getData()
        self.current_item = None
        self.setupUi()
        self.getCurrentButton()

    def setupUi(self):
        self.setObjectName(self.input_type)
        self.resize(460, 109)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)  
        
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        title = '%s%s'% (self.input_type[0].upper(), self.input_type[1:])
        self.groupbox.setTitle(title)        
        self.verticallayout.addWidget(self.groupbox)

        self.gridlayout = QtGui.QGridLayout(self.groupbox)
        self.gridlayout.setObjectName('gridlayout')        
        self.gridlayout.setSpacing(10)
        self.gridlayout.setContentsMargins(20, 10, 10, 10)        

        sort_data = generic.sortDictionary(self.data['data'])
        index, row, column = 0, -1, 0
        for x, items in sort_data.items():
            for each in items:
                radiobutton = QtGui.QRadioButton(self.groupbox)
                radiobutton.setObjectName(
                    'radiobutton_{}'.format(each.encode()))
                radiobutton.setText(self.data['data'][each]['label'])
                radiobutton.setToolTip('From {}'.format(
                    self.data['data'][each]['tooltip']))
                radiobutton.clicked.connect (partial (self.setCurrentButton, each.encode()))
                if index%3:
                    column += 1
                else:
                    row += 1
                    column = 0
                self.gridlayout.addWidget(radiobutton, row, column, 1, 1)
                index+=1
                
    def setCurrentButton(self, item):
        self.current_item = item
    
    def getCurrentButton(self):
        return self.current_item
                


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Button(parent=None, input='from')
    window.show()
    sys.exit(app.exec_())
