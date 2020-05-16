import os
import re
import sys
import ast
import json
import copy

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import swidgets

from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioEnviron
from studio_usd_pipe.resource.ui import catalogue
from PyQt4.Qt import QWidget
from __builtin__ import True


class Window(QtWidgets.QMainWindow):
 
    def __init__(self, parent=None, standalone=None):
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.title = 'Casting Sheet'
        self.width = 572
        self.height = 716
        self.pipe = 'assets'
        self.version, self.label = self.set_tool_context() 
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
        self.comp_catalogue = catalogue.Catalogue()
        
        self.source_maya = None
        self.asset_ids = {}
        self.setup_ui()
        self.setup_menu()
        self.setup_icons()
        self.set_default()
        
    def setup_ui(self):  
    
        
        self.setObjectName('mainwindow_castingsheet')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version))        
        self.resize(self.width, self.height) 
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)        
                        
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('{} <{}>'.format(self.label, self.title))  
        self.verticallayout.addWidget(self.groupbox)             
        self.verticallayout_item = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout_item')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)                
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None)    
        self.line = QtWidgets.QFrame(self)
        self.line.setObjectName('line')        
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticallayout_item.addWidget(self.line)

        self.groupbox_toolbar = QtWidgets.QGroupBox(self)
        self.groupbox_toolbar.setObjectName('groupbox_toolbar')
        self.groupbox_toolbar.setTitle('.')
        sizepolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.groupbox_toolbar.setSizePolicy(sizepolicy)        
        self.verticallayout_item.addWidget(self.groupbox_toolbar)
        self.horizontallayout_toolbar = QtWidgets.QHBoxLayout(self.groupbox_toolbar)
        self.horizontallayout_toolbar.setSpacing(0)
        self.horizontallayout_toolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_toolbar.setObjectName('horizontallayout_toolbar')
        self.toolbar = QtWidgets.QToolBar(self)
        self.horizontallayout_toolbar.addWidget(self.toolbar)    
        spaceritem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_toolbar.addItem(spaceritem)
        
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setObjectName("splitter")        
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.verticallayout_item.addWidget(self.splitter)
        
        self.treewidget_shots = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_shots.setObjectName("treewidget_shots")
        self.treewidget_shots.headerItem().setText(0, "Shots")
        self.treewidget_shots.setAlternatingRowColors(True)
        self.treewidget_shots.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.treewidget_assets = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_assets.setObjectName("treewidget_assets")
        self.treewidget_assets.headerItem().setText(0, "Assets")
        self.treewidget_assets.setAlternatingRowColors(True)
        self.treewidget_assets.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treewidget_assets.currentItemChanged.connect(self.current_asset_select)        
        
        self.splitter.addWidget(self.comp_catalogue) 
        
        self.horizontallayout_create = QtWidgets.QHBoxLayout(self)
        self.horizontallayout_create.setObjectName('horizontallayout_toolbar')
        self.verticallayout.addLayout(self.horizontallayout_create)    
        
        spaceritem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_create.addItem(spaceritem)
                
        self.button_create = QtWidgets.QPushButton(self)
        self.button_create.setObjectName("button_create")
        self.button_create.setText("Create")
        
        self.horizontallayout_create.addWidget(self.button_create)






    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)

    def set_tool_context(self):
        config = sheader.Header()
        config.tool()
        return config.version, config.pretty      
    
    def set_default(self):
        show_icon, valid = self.environ.get_environ_value('SHOW_ICON')
        if not show_icon:
            show_icon = os.path.join(resource.getIconPath(), 'show.png')
        size = self.button_show.minimumSize()
        swidgets.image_to_button(
            self.button_show,
            size.width(),
            size.height(),
            path=show_icon
            )
        self.setup_assets()

    def setup_menu(self):
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')         
        actions = ['reload', 'add', 'instance', 'remove', 'clear', 'parent', 'edit']
        for each in actions:        
            action = QtWidgets.QAction(self)
            action.setObjectName('action_%s'%each)
            action.setToolTip(each) 
            action.setText(each)        
            self.menu.addAction(action)      
            self.toolbar.addAction(action)
            action.triggered.connect(partial(self.menu_actions, each))
            
            
    def setup_assets(self):
        self.treewidget_assets.clear()            
        contents = self.spipe.get()
        # print json.dumps(contents, indent=4)
        captions = sorted(contents.keys())
        valid_subfields = self.spipe.get_casting_subfields()
        for caption in captions:
            caption_item = swidgets.add_treewidget_item(
                self.treewidget_assets, caption, icon=caption)
            self.treewidget_assets.setItemExpanded(caption_item, 1)            
            for subfield in valid_subfields:                
                if subfield not in contents[caption]:
                    continue
                subfield_item = swidgets.add_treewidget_item(
                    caption_item, subfield, icon=subfield)
                self.treewidget_assets.setItemExpanded(subfield_item, 1)            
                versions = common.set_version_order(contents[caption][subfield].keys())
                for version in versions:
                    cuttrent_tag = contents[caption][subfield][version]['tag']
                    version_item = swidgets.add_treewidget_item(
                        subfield_item, version, icon=cuttrent_tag, foreground=(192, 0, 0))                
                    more_contents = self.spipe.get_more_data(caption, version, subfield)
                    ver_contents = copy.deepcopy(contents[caption][subfield][version])
                    ver_contents.update(more_contents)
                    version_item.setStatusTip(0, str(ver_contents))
                    # update root item icon with pipe tag(character, prop, etc)
                    swidgets.update_treewidget_item_icon(caption_item, cuttrent_tag)                             
    
    def current_asset_select(self, *args):
        if not args[0]:
            return
        contents = args[0].statusTip(0)
        if not contents:
            self.comp_catalogue.setup_default()
            return
        contents = ast.literal_eval(contents)
        self.comp_catalogue.set_catalogue(**contents)
                
        
            
    def menu_actions(self, menu):        
        if menu=='reload':
            self.reload()        
        if menu=='add':
            self.add_item(self.treewidget_shots)
        if menu=='instance':
            self.add_instance(self.treewidget_shots)
        if menu=='remove':
            self.remove_item(self.treewidget_shots)            
        if menu=='clear':
            self.clear_item(self.treewidget_shots)               
        if menu=='parent':
            self.parent_item()    
                                    
    def reload(self):
        self.set_default()
        self.treewidget_shots.clear()
        
    
    def add_item(self, treewidget):            
        item_name, ok = QtWidgets.QInputDialog.getText(
            self, 'input', 'enter the item name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        parent_item = self.find_parent_item(treewidget)
        if self.has_item_exists(parent_item, item_name):
            QtWidgets.QMessageBox.critical(
                self, 'critical', 'already found <%s>'%item_name, QtWidgets.QMessageBox.Ok)            
            return
        swidgets.add_treewidget_item(
            parent_item, item_name, icon=None, foreground=None)
        
    def add_instance(self, treewidget):
        if not treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'please select any item', QtWidgets.QMessageBox.Ok) 
            return None
        number_copies, ok = QtWidgets.QInputDialog.getInt(
            self, 'input', 'number of copies:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return   
        current_item = treewidget.selectedItems()[-1]        
        if current_item.parent():
            parent_item = current_item.parent()
        else:
            parent_item = treewidget
        for index in range(number_copies):            
            next_item_name = self.find_next_item_name(parent_item, current_item)
            current_item = swidgets.add_treewidget_item(
                parent_item, next_item_name, icon=None, foreground=None)       

    def remove_item(self, treewidget):
        if not treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'please select any item', QtWidgets.QMessageBox.Ok) 
            return None
        items = [each.text(0) for each in treewidget.selectedItems()]
        if len(items)>10:
            items = items[0:10] + ['etc ...']            
        replay = QtWidgets.QMessageBox.question(
            self,
            'question',
            'Are you sure, you want to remove \n%s' %('\n'.join(items)),
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No
            ) 
        if replay == QtWidgets.QMessageBox.No:
            print 'abort the remove item!...'
            return
        for item in treewidget.selectedItems():
            item.removeChild(item)
            treewidget.removeItemWidget(item, 0)                 
         
    
    def clear_item(self, treewidget): 
        widget_item = treewidget.invisibleRootItem()
        
        if not widget_item.childCount():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'not found any itmes to clear (already clean)', QtWidgets.QMessageBox.Ok) 
            return None            
                           
        replay = QtWidgets.QMessageBox.question(
            self,
            'question',
            'Are you sure, you want to remove all',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No
            ) 
        if replay == QtWidgets.QMessageBox.No:
            print 'abort the clear!...'
            return        
        treewidget.clear()
        
    
    def parent_item(self):
        self.treewidget_shots.selectedItems()
        self.treewidget_assets.selectedItems()

        pass



    def has_item_exists(self, parent_item, item_name):
        chidren = self.find_children(parent_item)        
        if item_name in chidren:
            return True
        return False
        
    def find_parent_item(self, treewidget):        
        if not treewidget.selectedItems():
            return treewidget
        current_item = treewidget.selectedItems()[-1]        
        if not current_item.parent():
            return current_item        
        return current_item.parent()   
    
    def find_children(self, parent_item):     
        if isinstance(parent_item, QtWidgets.QTreeWidget):
            widget_item = parent_item.invisibleRootItem()
        else:
            widget_item = parent_item
        children = []
        for index in range (widget_item.childCount()):
            child = widget_item.child(index)
            children.append(child.text(0))
        return children        
    
    def find_next_item_name(self, parent_item, current_item):
        next_name = self.get_next_name(current_item.text(0))
        stack = [next_name]
        while stack:
            current = stack.pop()        
            if self.has_item_exists(parent_item, current):
                next_name = self.get_next_name(current)                
                stack.append(next_name)  
                continue
            return current        
    
    def get_next_name(self, current_name):
        digits = map(int, re.findall(r'\d+', current_name))
        if not digits:
            return '%s1'%current_name
        suffix = current_name.rsplit(str(digits[-1]), 1)
        return '%s%s'%(''.join(suffix), digits[-1]+1)       
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_())         
