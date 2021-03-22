import os
import sys
import resources

from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial

from core import versions
from tools.template_publish import publish


class TemplatePublish(QtGui.QWidget):
    
    def __init__(self, parent=None, **kwargs):
        '''
        :example
            from tools.template_publish import main
            window = main.TemplatePublish(parent=None)
            window.show()
        '''        
        super(TemplatePublish, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.template_path = resources.get_template_path()
        self.setup_ui()
        self.set_current_versions()        
    
    def setup_ui(self):
        self.setObjectName('template_publish')
        self.resize(350, 250)
        self.setWindowTitle('Template Publish')          
        align_right = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter        
        self.gridlayout = QtGui.QGridLayout(self)
        self.gridlayout.setObjectName('gridLayout')        
        self.gridlayout.setContentsMargins(10, 10, 10, 10)
        self.gridlayout.setHorizontalSpacing(1)
        self.gridlayout.setVerticalSpacing(2)        
        self.label_type = QtGui.QLabel(self)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('template_type')      
        self.label_type.setAlignment(align_right)  
        self.gridlayout.addWidget(self.label_type, 0, 0, 1, 1)
        self.combobox_type = QtGui.QComboBox(self)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.addItems(['lookdev', 'lighting'])
        self.combobox_type.currentIndexChanged.connect(partial(self.set_current_versions, None))
        self.gridlayout.addWidget(self.combobox_type, 0, 1, 1, 1)
        self.label_versions = QtGui.QLabel(self)
        self.label_versions.setObjectName('label_versions')
        self.label_versions.setText('versions') 
        self.label_versions.setAlignment(align_right)  
        self.gridlayout.addWidget(self.label_versions, 1, 0, 1, 1)
        self.combobox_versions = QtGui.QComboBox(self)
        self.combobox_versions.setObjectName('combobox_versions')
        self.combobox_versions.addItems(['major', 'minor', 'patch'])
        self.combobox_versions.currentIndexChanged.connect(partial(self.set_current_versions, None))
        self.gridlayout.addWidget(self.combobox_versions, 1, 1, 1, 1)
        self.label_latest = QtGui.QLabel(self)
        self.label_latest.setObjectName('label_latest')
        self.label_latest.setText('latest_versions')
        self.label_latest.setAlignment(align_right)              
        self.gridlayout.addWidget(self.label_latest, 2, 0, 1, 1)
        self.lineedit_latest = QtGui.QLineEdit(self)
        self.lineedit_latest.setReadOnly(True)
        self.lineedit_latest.setObjectName('lineedit_latest')        
        self.gridlayout.addWidget(self.lineedit_latest, 2, 1, 1, 1)
        self.label_next = QtGui.QLabel(self)
        self.label_next.setObjectName('label_next')
        self.label_next.setText('next_versions')
        self.label_next.setAlignment(align_right)              
        self.gridlayout.addWidget(self.label_next, 3, 0, 1, 1)
        self.lineedit_next = QtGui.QLineEdit(self)
        self.lineedit_next.setReadOnly(True)
        self.lineedit_next.setObjectName('lineedit_latest')                
        self.gridlayout.addWidget(self.lineedit_next, 3, 1, 1, 1)
        self.button_publish = QtGui.QPushButton(self)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('publish')
        self.button_publish.clicked.connect(partial(self.set_publish, None))
        self.gridlayout.addWidget(self.button_publish, 4, 1, 1, 1)
        
    def set_current_versions(self, *args):        
        current_type = str(self.combobox_type.currentText())
        current_version = str(self.combobox_versions.currentText())        
        temp_version = versions.get_latest_version(self.template_path, current_type)
        latest_version = None
        if temp_version:
            latest_version = temp_version      
        index = versions.PATTERN[current_version]   
        next_version = versions.get_next_version(index, latest_version)   
        if not latest_version:
            latest_version = 'None'        
        self.lineedit_latest.setText(latest_version)
        self.lineedit_next.setText(next_version)
    
    def set_publish(self, *args):
        current_type = str(self.combobox_type.currentText())
        next_version = str(self.lineedit_next.text())        
        publish_dirname = os.path.join(
            self.template_path,
            current_type,
            next_version
            )
        publish.start_publish(publish_dirname, current_type)
        self.set_current_versions()
        messages = [
            '<tempale publish success>',
            publish_dirname,
            'template type: '.rjust(10) + current_type,
            'version: '.rjust(10) + next_version
            ]
        message_box = QtGui.QMessageBox.information(
            None, 'Success', '\n'.join(messages), QtGui.QMessageBox.Ok)
        if message_box:
            print '\n'.join(messages)
            os.system('xdg-open \"%s\"' % publish_dirname)          

            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TemplatePublish(parent=None)
    window.show()
    sys.exit(app.exec_())         
        
