import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class TREEWIDGET (QtGui.QWidget):
    
    def __init__(self):
        super(TREEWIDGET, self).__init__()        
        self.initUI()        
        
    def initUI(self):        

        self.button_color = QtGui.QPushButton(self)
        self.button_color.setGeometry(QtCore.QRect(10, 10, 150, 25))
        self.button_color.setObjectName('button_color')
        self.button_color.setText ('Color')
        
        self.button_color.clicked.connect (self.color)
        #self.button_color.clicked.connect (self.enable)

        self.lineEdit_qt = QtGui.QLineEdit(self)
        self.lineEdit_qt.setGeometry(QtCore.QRect(10, 40, 150, 25))        
        self.lineEdit_qt.setObjectName ('lineEdit')
        
        self.lineEdit_rgb = QtGui.QLineEdit(self)
        self.lineEdit_rgb.setGeometry(QtCore.QRect(10, 70, 150, 25))        
        self.lineEdit_rgb.setObjectName ('lineEdit')
                

        self.resize(180, 130)
        #self.addItems () 
        self.show()            
        
    def color (self) :
        colorQt     = QtGui.QColorDialog.getColor ()
        
        print colorQt.name()
        #if colorQt.isvalid() :
        if 1==1 :
            rgb     = [colorQt.red (), colorQt.green (), colorQt.blue ()]            
            print rgb, '\t', colorQt.name()
            
            self.lineEdit_qt.setText (str(colorQt.name()))
            self.lineEdit_rgb.setText (str(rgb)) 
            
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TREEWIDGET()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
