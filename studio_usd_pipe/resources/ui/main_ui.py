
import os
import sys
import warnings


from PySide import QtCore
from PySide import QtGui
from functools import partial

from studio_usd_pipe import resources
from studio_usd_pipe.core import inputs
from studio_usd_pipe.utils import platforms


class Window(QtGui.QMainWindow):
    
    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent)
        self.child = None
        self.child = kwargs['child']
        self.child_prity_name = platforms.get_child(self.child)    
        self.version = platforms.get_tool_version()
        self.tool_prity_name = platforms.get_tool_prity_name()        
        self.icon_path = resources.getIconPath() 
        self.setup_ui()
        self.modify_widgets()
        
    def setup_ui(self):
        self.setObjectName('main_window')
        self.resize(300, 450)
        self.setWindowTitle('{} <{}> {}'.format(
            self.tool_prity_name, self.child_prity_name, self.version))        

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName('splitter')
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.header().setVisible(False)        
        self.treewidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.treewidget.setIconSize(QtCore.QSize(50, 50))
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(
            partial(self.context_menu, self.treewidget))
        self.verticallayout.addWidget(self.splitter)
        
        self.pop_menu = QtGui.QMenu(self)        
        self.action_add = QtGui.QAction(self)
        self.action_add.setObjectName('action_add')
        self.action_add.setText('Add')
        self.action_add.setToolTip('Add Items')
        self.action_add.setShortcut('Ctrl+A')
        self.pop_menu.addAction(self.action_add)
        
        self.action_remove = QtGui.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove')
        self.action_remove.setToolTip('Remove')
        self.action_remove.setShortcut('Ctrl+D')
        self.pop_menu.addAction(self.action_remove)
                
        self.action_reload = QtGui.QAction(self)
        self.action_reload.setObjectName('action_reload') 
        self.action_reload.setText('Reload')
        self.action_reload.setToolTip('Reload')
        self.action_reload.setShortcut('Ctrl+R')
        self.pop_menu.addAction(self.action_reload)
        
        self.action_add.triggered.connect(partial(self.add, self.treewidget))
        self.action_remove.triggered.connect(partial(self.remove, self.treewidget))
        self.action_reload.triggered.connect(partial(self.reload, self.treewidget))
             
        QtGui.QShortcut(QtGui.QKeySequence('Ctrl+A'), self, (partial(self.add, self.treewidget)))
        QtGui.QShortcut(QtGui.QKeySequence('Ctrl+D'), self, (partial(self.remove, self.treewidget)))

              
    def modify_widgets(self):
        input = inputs.Connect('category')
        for each in input.keys:
            item = QtGui.QTreeWidgetItem(self.treewidget)
            item.setText(0, input.data[each]['display'])
            item.setToolTip(0, input.data[each]['tooltip'])
            item.setStatusTip(0, each)
            current_icon = os.path.join(
                self.icon_path, input.data[each]['icon'])
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(current_icon),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
                )
            item.setIcon(0, icon)    

    def context_menu(self, treeWidget, point):  # Right click menu
        index = treeWidget.indexAt(point)
        if not index.isValid():
            return        
        item = self.treewidget.itemAt(point)
        self.action_remove.setVisible(True)             
        if not item.parent():
            self.action_remove.setVisible(False)
        self.pop_menu.exec_(QtGui.QCursor.pos())
        
    def collect_child_items(self, parent):
        for index in range(parent.childCount()):
            current_child = parent.child(index)
            self.dependent_list.append(current_child)
            self.collect_child_items(current_child)        
    
    def add(self, treewidget):        
        if not treewidget.selectedItems():
            warnings.warn('Not found any selection\nSelect the item and try', Warning)
            return
        parent_item = treewidget.selectedItems()[-1]    
        if treewidget.selectedItems()[-1].parent():
            parent_item = treewidget.selectedItems()[-1].parent()
        name, ok = QtGui.QInputDialog.getText(
            self, 'Input', 'Enter the name:', QtGui.QLineEdit.Normal)
        if not ok:
            warnings.warn('abort the add!...', Warning)
            return        
        item = QtGui.QTreeWidgetItem(parent_item)
        item.setText(0, name)
        current_icon = os.path.join(self.icon_path, 'unknown.png')
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(current_icon),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
            )
        item.setIcon(0, icon)        
        treewidget.setItemExpanded(treewidget.selectedItems()[-1], 1)       
           

    def remove(self, treewidget):
        if not treewidget.selectedItems():
            warnings.warn('Not found any selection\nSelect the item and try', Warning)
            return
        items = treewidget.selectedItems()
        for each in items:
            each.removeChild(each)             
    
    def reload(self, treewidget):
        pass
                    
                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window(parent=None, child='publish')
    # window = Window(parent=None)    
    window.show()
    sys.exit(app.exec_())