import sys

from PySide import QtCore
from PySide import QtGui

from crowd import resource
from crowd.api import crowdPublish

'''
from crowd.resource.ui import comment_ui
reload(comment_ui)
window = comment_ui.Connect()
window.show()
'''
reload(crowdPublish)


class Connect(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Connect, self).__init__(parent=parent)
        self.type = type
        self.tag = None
        self.data = None
        self.name = None
        self.message = None
        self.description = None
        self.scene_name = None
        self.extract = None
        self.font_size, self.font_type = resource.getFontSize()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('comment')
        self.setWindowTitle('Comment 0.0.1')
        self.resize(400, 320)
        self.setStyleSheet('font: 14pt \"Sans Serif\";')
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.label = QtGui.QLabel(self)
        self.label.setObjectName('label')
        self.label.setText('Comment')
        self.verticallayout.addWidget(self.label)
        self.textedit = QtGui.QTextEdit(self)
        self.textedit.setObjectName('textedit')
        self.textedit.setStyleSheet(
            'font: %spt \"%s\";' % (self.font_size, self.font_type))       
        self.verticallayout.addWidget(self.textedit)
        self.button = QtGui.QPushButton(self)
        self.button.setObjectName('button')
        self.button.setStyleSheet(
            'font: %spt \"%s\";' % (self.font_size, self.font_type))            
        self.button.setText('Apply')
        self.verticallayout.addWidget(self.button)
        self.button.clicked.connect(self.publish)

    def publish(self):
        self.message = str(self.textedit.toPlainText())
        if not self.message:
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Can not publish with out comment!...',
                QtGui.QMessageBox.Ok
            )
            return
        crowd_publish = crowdPublish.Connect(
            type=self.type, tag=self.tag)
        
        # commit        
        result, message = crowd_publish.commit()
        if not result:
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Failed your publis <%s>!...' % message,
                QtGui.QMessageBox.Ok
            )
            self.close()
            return
        
        crowd_publish.push(
            extract_bundle=self.extract,
            comment=self.message,
            description=self.description,
            remote=self.scene_name
        )     

        self.close()
        QtGui.QMessageBox.information(
            self,
            'Information',
            'Publish Success!...',
            QtGui.QMessageBox.Ok
        )


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
