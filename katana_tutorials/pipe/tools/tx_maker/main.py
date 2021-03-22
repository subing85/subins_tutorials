import os
import sys
import resources

from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial

from tools.tx_maker import maker
reload(maker)


class TxMaker(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(TxMaker, self).__init__(parent)   
        self.setup_ui()
        self.set_default()
    
    def setup_ui(self):
        self.setObjectName('qwidget_tx_maker')
        self.resize(900, 500)
        self.setWindowTitle('Studio Pipe - TX Maker') 
        self.setStyleSheet('font: 14pt')
        self.gridlayout = QtGui.QGridLayout(self)
        self.gridlayout.setObjectName('gridlayout')
        align_right = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        self.label_txmake = QtGui.QLabel(self)
        self.label_txmake.setObjectName('label_txmake')
        self.label_txmake.setText('tx_maker') 
        self.label_txmake.setAlignment(align_right)       
        self.gridlayout.addWidget(self.label_txmake, 0, 0, 1, 1)
        self.lineedit_txmake = QtGui.QLineEdit(self)
        self.lineedit_txmake.setObjectName('lineedit_txmake')
        self.gridlayout.addWidget(self.lineedit_txmake, 0, 1, 1, 1)
        self.button_txmake = QtGui.QPushButton(self)
        self.button_txmake.setObjectName('button_txmake')
        self.button_txmake.setText('...')
        self.button_txmake.clicked.connect(partial(self.set_dirname, self.lineedit_txmake, mode=False))
        self.gridlayout.addWidget(self.button_txmake, 0, 2, 1, 1)
        self.label_source = QtGui.QLabel(self)
        self.label_source.setObjectName('label_source')
        self.label_source.setText('source')
        self.label_source.setAlignment(align_right)
        self.gridlayout.addWidget(self.label_source, 1, 0, 1, 1)
        self.lineedit_source = QtGui.QLineEdit(self)
        self.lineedit_source.setObjectName('lineedit_source')
        self.lineedit_source.textChanged.connect(self.load_source_images)
        self.gridlayout.addWidget(self.lineedit_source, 1, 1, 1, 1)
        self.button_source = QtGui.QPushButton(self)
        self.button_source.setObjectName('button_source')
        self.button_source.setText('...')
        self.button_source.clicked.connect(
            partial(self.set_dirname, self.lineedit_source, mode='source', load=True))
        self.gridlayout.addWidget(self.button_source, 1, 2, 1, 1)
        self.treewidget = QtGui.QTreeWidget(self)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.headerItem().setText(0, 'index')
        self.treewidget.headerItem().setText(1, 'path')
        self.treewidget.header().resizeSection (0, 60)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.gridlayout.addWidget(self.treewidget, 2, 1, 1, 1)
        self.label_out = QtGui.QLabel(self)
        self.label_out.setObjectName('label_out')
        self.label_out.setText('out')
        self.label_out.setAlignment(align_right)             
        self.gridlayout.addWidget(self.label_out, 3, 0, 1, 1)
        self.lineedit_out = QtGui.QLineEdit(self)
        self.lineedit_out.setObjectName('lineedit_out')        
        self.gridlayout.addWidget(self.lineedit_out, 3, 1, 1, 1)
        self.button_out = QtGui.QPushButton(self)
        self.button_out.setObjectName('button_out')
        self.button_out.setText('...')
        self.button_out.clicked.connect(partial(self.set_dirname, self.lineedit_out, mode=True))
        self.gridlayout.addWidget(self.button_out, 3, 2, 1, 1)
        self.button_create = QtGui.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('create')
        self.button_create.clicked.connect(self.convert_to_tx)
        self.gridlayout.addWidget(self.button_create, 4, 1, 1, 1)
        
    def set_default(self):        
        if 'RMANTREE' in os.environ:
            rmantree = os.environ['RMANTREE']
        else:
            rmantree = '/opt/pixar/RenderManProServer-21.6'        
        txmake_path = os.path.join(rmantree, 'bin', 'txmake')
        self.lineedit_txmake.setText(txmake_path)
        show_path = resources.get_show_path()
        self.browse_directory = show_path
        
        print show_path
        
    def set_dirname(self, widget, mode=False, **kwargs):
        if mode:
            current_path = QtGui.QFileDialog.getExistingDirectory(
                self, 'Browser', self.browse_directory)
        else:
            current_format = 'txmake (*txmake)'
            current_path = QtGui.QFileDialog.getOpenFileName(
                self, 'Browser', self.browse_directory, current_format)            
        widget.setText(current_path)
        if 'load' in kwargs:
            self.load_source_images(source_dirname=current_path)
        
    def load_source_images(self, source_dirname=None):
        if not source_dirname:
            source_dirname = self.lineedit_source.text()
        if not source_dirname:
            return
        if isinstance(source_dirname, QtCore.QString):
            source_dirname = str(source_dirname)
        if not os.path.isdir(source_dirname):
            return
        self.browse_directory = source_dirname
        self.treewidget.clear()
        contents = os.listdir(source_dirname)
        index = 1
        for content in contents:
            name, format = os.path.splitext(content)        
            if format.upper() not in maker.IMAGE_FORMATS:
                continue
            image_path = os.path.join(source_dirname, content)
            item = QtGui.QTreeWidgetItem(self.treewidget)
            item.setText(0, str(index))
            item.setText(1, image_path)
            item.setCheckState(1, QtCore.Qt.Checked)
            index += 1
            
    def convert_to_tx(self):
        txmake = str(self.lineedit_txmake.text())
        source_dirname = str(self.lineedit_source.text())        
        output_dirname = str(self.lineedit_out.text())
        message = None
        if not os.path.isdir(source_dirname):
            message = 'not found source directory'
        if not output_dirname:
            message = 'not found out put directory'        
        widget_item = self.treewidget.invisibleRootItem()
        source_images = []
        for index in range (widget_item.childCount()):
            item = widget_item.child(index)
            if not item.checkState(1):
                continue
            source_images.append(str(item.text(1)))
        if not source_images:
            message = 'not found items' 
        if message:
            QtGui.QMessageBox.warning(
                None, 'Warning', message, QtGui.QMessageBox.Ok) 
            return  
        maker.converts(txmake, source_images, output_dirname)
        QtGui.QMessageBox.information(
            None, 'Success', 'done!...', QtGui.QMessageBox.Ok) 
        return    


if __name__ == '__main__':
    application = QtGui.QApplication(sys.argv)
    window = TxMaker()
    window.show()
    sys.exit(application.exec_())

