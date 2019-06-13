import sys

from PySide import QtCore
from PySide import QtGui

from crowd.api import crowdPublish

'''
from crowd.resource.ui import comment_ui
reload(comment_ui)
window = comment_ui.Connect()
window.show()
'''


class Connect(QtGui.QWidget):

    def __init__(self,  parent=None):
        super(Connect, self).__init__(parent=parent)
        
        self.type = None
        self.tag = None
        self.data = None
        self.name = None
        self.message = None        
        self.description = None
        self.scene_name = None
        self.extract = None
        
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
        self.button.clicked.connect(self.publish)
    
    def publish(self):                
        self.message = self.textedit.toPlainText()
        
        if not self.message:
            QtGui.QMessageBox.warning(
                self,'Warning', 'Can not publish with out comment!...', QtGui.QMessageBox.Ok)
            return
                    
        crowd_publish = crowdPublish.Publish(
            type=self.type, tag=self.tag)
        
        for data, name in self.extract:            
            crowd_publish.do(
                data=data,
                name=name,
                comment=self.message,
                description=self.description)        
        crowd_publish.commit(
            origin=self.scene_name, comment=self.message, description=self.description)
        
        self.close()
        
        QtGui.QMessageBox.information(
            self,'Information', 'Publish Success!...', QtGui.QMessageBox.Ok)
                 
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())