import sys

from PySide import QtCore
from PySide import QtGui

'''
from crowd.resource.ui import comment_ui
reload(comment_ui)
window = comment_ui.Connect()
window.show()
'''


class Connect(QtGui.QWidget):

    def __init__(self,  parent=None):
        super(Connect, self).__init__(parent=parent)
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle('Comment')
        self.setObjectName('comment')
        self.resize(400, 320)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.label = QtGui.QLabel(self)
        self.label.setObjectName('label')
        self.label.setText('Comment')
        self.verticallayout.addWidget(self.label)
        self.textedit = QtGui.QTextEdit(self)
        self.textedit.setObjectName('textedit')
        self.verticallayout.addWidget(self.textedit)
        self.button = QtGui.QPushButton(self)
        self.button.setObjectName('button')
        self.button.setText('Apply')        
        self.verticallayout.addWidget(self.button)

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())