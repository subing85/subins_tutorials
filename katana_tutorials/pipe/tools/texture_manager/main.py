import os
import sys
import UI4

from PyQt4 import QtGui
from PyQt4 import QtCore
from functools import partial

from tools.texture_manager import texture


class TextureManager(QtGui.QWidget):
    
    def __init__(self, parent=None):
        '''
        :example
            from tools.texture_manager import main
            window = main.TextureManager(parent=None)
            window.show()
        '''       
        super(TextureManager, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.setup_ui()          
        
    def setup_ui(self):
        self.setObjectName('qwidget_file_texture_manager')
        self.resize(900, 650)
        self.setWindowTitle('File Texture Manager') 
        align_right = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter        
        self.gridlayout = QtGui.QGridLayout(self)
        self.gridlayout.setContentsMargins(10, 10, 10, 10)
        self.gridlayout.setHorizontalSpacing(1)
        self.gridlayout.setVerticalSpacing(2)
        self.gridlayout.setObjectName('gridlayout')
        self.label_node = QtGui.QLabel(self)
        self.label_node.setObjectName('label_node')
        self.label_node.setAlignment(align_right)        
        self.label_node.setText('node')        
        self.gridlayout.addWidget(self.label_node, 0, 0, 1, 1)        
        self.lineedit_node = QtGui.QLineEdit(self)
        self.lineedit_node.setObjectName('lineedit_node')
        self.lineedit_node.setEnabled(False)
        self.gridlayout.addWidget(self.lineedit_node, 0, 1, 1, 1)        
        self.button_node = QtGui.QPushButton(self)
        self.button_node.setObjectName('button_node')
        self.button_node.setText('+')
        self.gridlayout.addWidget(self.button_node, 0, 2, 1, 1)       
        self.treewidget = QtGui.QTreeWidget(self)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.headerItem().setText(0, 'no')        
        self.treewidget.headerItem().setText(1, 'node')
        self.treewidget.headerItem().setText(2, 'path')
        self.treewidget.headerItem().setText(3, 'material')
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.gridlayout.addWidget(self.treewidget, 1, 1, 1, 1)
        self.label_search = QtGui.QLabel(self)
        self.label_search.setObjectName('label_search')
        self.label_search.setAlignment(align_right)
        self.label_search.setText('search_for ')              
        self.gridlayout.addWidget(self.label_search, 2, 0, 1, 1)
        self.lineedit_search = QtGui.QLineEdit(self)
        self.lineedit_search.setObjectName('lineedit_search')
        self.gridlayout.addWidget(self.lineedit_search, 2, 1, 1, 1)
        self.label_replace = QtGui.QLabel(self)
        self.label_replace.setObjectName('label_replace')
        self.label_replace.setText('replace_with ')        
        self.label_replace.setAlignment(align_right)        
        self.gridlayout.addWidget(self.label_replace, 3, 0, 1, 1)
        self.lineedit_replace = QtGui.QLineEdit(self)
        self.lineedit_replace.setObjectName('lineedit_replace')
        self.gridlayout.addWidget(self.lineedit_replace, 3, 1, 1, 1)        
        self.button_replace = QtGui.QPushButton(self)
        self.button_replace.setObjectName('button_replace')
        self.button_replace.setText('search and replace')
        self.gridlayout.addWidget(self.button_replace, 4, 1, 1, 1)
        self.button_node.clicked.connect(
            partial(self.load_node, self.lineedit_node, self.treewidget))   
        self.button_replace.clicked.connect(
            partial(
                self.search_replace,
                self.lineedit_search,
                self.lineedit_replace,
                self.treewidget
                )
            )
        
    def load_node(self, widget, treewidget):
        current_node = texture.get_current_node()   
        widget.clear()     
        if not current_node:
            print '#warnings: invalid node'
            return        
        widget.setText(current_node)
        UI4.Util.Caches.FlushCaches()
        valid, materials, message = texture.find_materials(current_node)
        if not valid:
            QtGui.QMessageBox.warning(
                None, 'Warning', message, QtGui.QMessageBox.Ok) 
            return            
        self.load_materials(treewidget, materials)
        
    def load_materials(self, treewidget, materials):
        treewidget.clear()
        brush = QtGui.QBrush(QtGui.QColor('red'))
        brush.setStyle(QtCore.Qt.NoBrush)
        index = 1
        for material, contents in materials.items():            
            for texture_map, nodes in contents.items():                
                for node in nodes:
                    item = QtGui.QTreeWidgetItem(treewidget)
                    item.setText(0, str(index))
                    item.setText(1, node)
                    item.setText(2, texture_map)
                    item.setText(3, material)
                    item.setCheckState(1, QtCore.Qt.Unchecked)                    
                    if not os.path.isfile(texture_map):
                        item.setForeground(2, brush)
                        item.setCheckState(1, QtCore.Qt.Checked)
                    index += 1
        treewidget.header().resizeSection(0, 50)
        treewidget.header().resizeSection(1, 200)
        treewidget.header().resizeSection(2, 800)
    
    def search_replace(self, search_widget, replace_widget, treewidget):
        search_for = str(search_widget.text())
        replace_with = str(replace_widget.text())
        message = None
        if not search_for:
            message = 'not found search key'
        if not replace_with:
            message = 'not found replace key'
        widget_item = treewidget.invisibleRootItem()
        children = []
        for index in range (widget_item.childCount()):
            item = widget_item.child(index)
            if not item.checkState(1):
                continue
            children.append(item)
        if not children:
            message = 'not found items'
        if message:
            QtGui.QMessageBox.warning(
                None, 'Warning', message, QtGui.QMessageBox.Ok) 
            return               
        for child in children:
            texture_node = str(child.text(1))
            texture_path = str(child.text(2))            
            texture.search_and_replace(texture_node, texture_path, search_for, replace_with)
        self.load_node(self.lineedit_node, treewidget)
        QtGui.QMessageBox.information(
            None, 'infomation', 'done!...', QtGui.QMessageBox.Ok)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TextureManager(parent=None)
    window.show()
    sys.exit(app.exec_()) 

