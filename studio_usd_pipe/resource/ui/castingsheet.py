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
from studio_usd_pipe.core import swidgets

from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioEnviron
from studio_usd_pipe.resource.ui import catalogue


class Window(QtWidgets.QMainWindow):
 
    def __init__(self, parent=None, standalone=None):
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.title = 'Casting Sheet'
        self.width = 1000
        self.height = 716
        self.pipe = 'assets'
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
        self.show_icon = self.environ.get_show_icon()
        self.comp_catalogue = catalogue.Catalogue()
        
        self.setup_ui()
        self.setup_menu()
        self.setup_icons()
        self.set_default()
        
    def setup_ui(self):  
        self.setObjectName('mainwindow_castingsheet')
        self.resize(self.width, self.height) 
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)        
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.verticallayout_item, self.button_show = swidgets.set_header(
            self, self.title, self.verticallayout, show_icon=self.show_icon)  
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
        self.splitter.setObjectName('splitter')        
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.verticallayout_item.addWidget(self.splitter)
        self.treewidget_shots = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_shots.setObjectName('treewidget_shots')
        self.treewidget_shots.headerItem().setText(0, 'Shots')
        self.treewidget_shots.setAlternatingRowColors(True)
        self.treewidget_shots.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treewidget_assets = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_assets.setObjectName('treewidget_assets')
        self.treewidget_assets.headerItem().setText(0, 'Assets')
        self.treewidget_assets.setAlternatingRowColors(True)
        self.treewidget_assets.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treewidget_assets.currentItemChanged.connect(self.current_asset_select)        
        self.splitter.addWidget(self.comp_catalogue) 
        self.horizontallayout_create = QtWidgets.QHBoxLayout()
        self.horizontallayout_create.setObjectName('horizontallayout_toolbar')
        self.verticallayout.addLayout(self.horizontallayout_create)    
        spaceritem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_create.addItem(spaceritem)
        self.button_close = QtWidgets.QPushButton(self)
        self.button_close.setObjectName('button_close')
        self.button_close.setText('close')                
        self.horizontallayout_create.addWidget(self.button_close)
        self.button_close.clicked.connect(self.close)
        self.button_create = QtWidgets.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('create')
        self.horizontallayout_create.addWidget(self.button_create)
        self.button_create.clicked.connect(self.create_castingsheet)

    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)
    
    def set_default(self):
        self.setup_assets()
        self.setup_shots()
        castingsheet_path = self.get_castingsheet_path()
        if os.path.isfile(self.get_castingsheet_path()):
            self.treewidget_assets.hide()
            self.comp_catalogue.hide()

    def setup_menu(self):
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')         
        actions = ['reload', 'add', 'instance', 'remove', 'clear', 'parent', 'edit', 'rename']
        for each in actions:        
            action = QtWidgets.QAction(self)
            action.setObjectName('action_%s' % each)
            action.setToolTip(each) 
            action.setText(each)        
            self.menu.addAction(action)      
            self.toolbar.addAction(action)
            action.triggered.connect(partial(self.menu_actions, each))
    
    def setup_shots(self):        
        castingsheet_path = self.get_castingsheet_path()
        if not os.path.isfile(self.get_castingsheet_path()):
            return
        casting_data = resource.getInputData(castingsheet_path)
        self.treewidget_shots.clear()
        toplevels = sorted(casting_data.keys())
        for toplevel in toplevels:
            toplevel_item = swidgets.add_treewidget_item(
                self.treewidget_shots, toplevel, icon='toplevel')
            sublevels = sorted(casting_data[toplevel].keys())
            for sublevel in sublevels:
                sublevel_item = swidgets.add_treewidget_item(toplevel_item, sublevel, icon='sublevel') 
                for asset in casting_data[toplevel][sublevel]:
                    asset_item = swidgets.add_treewidget_item(sublevel_item, asset, icon='asset')
                    asset_item.setStatusTip(0, asset)
            
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
                    more_contents = self.spipe.get_more_data(caption, subfield, version)
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
    
    def get_castingsheet_path(self):
        show_path = self.environ.get_show_path() 
        castingsheet_path = resource.getSpecificPreset(show_path, 'castingsheet')
        #if not os.path.isfile(castingsheet_path):
        #    return None
        return castingsheet_path
    
    def menu_actions(self, menu):        
        if menu == 'reload':
            self.reload()        
        if menu == 'add':
            self.add_item(self.treewidget_shots)
        if menu == 'instance':
            self.add_instance(self.treewidget_shots)
        if menu == 'remove':
            self.remove_item(self.treewidget_shots)            
        if menu == 'clear':
            self.clear_item(self.treewidget_shots)               
        if menu == 'parent':
            self.parent_item()    
        if menu == 'edit':
            self.edit_item()
        if menu == 'rename':
            self.rename_item(self.treewidget_shots)
                                                                
    def reload(self):
        self.set_default()
        self.treewidget_shots.clear()
    
    def add_item(self, treewidget):            
        item_name, ok = QtWidgets.QInputDialog.getText(
            self, 'input', 'enter the item name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the name'
            return
        parent_item = self.find_parent_item(treewidget)
        if self.has_item_exists(parent_item, item_name):
            QtWidgets.QMessageBox.critical(
                self, 'critical', 'already found <%s>' % item_name, QtWidgets.QMessageBox.Ok)            
            return
        
        icon = 'toplevel'
        if isinstance(parent_item, QtWidgets.QTreeWidgetItem):
            icon = 'sublevel'
        
        current_item = swidgets.add_treewidget_item(
            parent_item, item_name, icon=icon, foreground=None)        
        # current_item.setWhatsThis(0, 'child')
        
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
            
        icon = 'toplevel'
        if isinstance(parent_item, QtWidgets.QTreeWidgetItem):
            icon = 'sublevel'            
            
        for index in range(number_copies):            
            next_item_name = self.find_next_item_name(parent_item, current_item)
            current_item = swidgets.add_treewidget_item(
                parent_item, next_item_name, icon=icon, foreground=None)   

    def remove_item(self, treewidget):
        if not treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'please select any item', QtWidgets.QMessageBox.Ok) 
            return None
        items = [each.text(0) for each in treewidget.selectedItems()]
        if len(items) > 10:
            items = items[0:10] + ['etc ...']            
        replay = QtWidgets.QMessageBox.question(
            self,
            'question',
            'Are you sure, you want to remove \n%s' % ('\n'.join(items)),
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
        current_assets = self.find_children_items(self.treewidget_assets)
        current_shots = self.find_children_items(self.treewidget_shots, tag=True)
        if not current_assets:
            QtWidgets.QMessageBox.critical(
                self,
                'critical',
                'please select any item from assets',
                QtWidgets.QMessageBox.Ok
                )
            return             
        if not current_shots:
            QtWidgets.QMessageBox.critical(
                self,
                'critical',
                'please select any item from shots',
                QtWidgets.QMessageBox.Ok
                )
            return        
        
        for current_shot in current_shots:
            for current_asset in current_assets:
                contents = ast.literal_eval(current_asset.statusTip(0))
                location = '%s|%s|%s' % (
                    contents['caption'],
                    contents['subfield'],
                    contents['version']
                    )
                current_item = swidgets.add_treewidget_item(
                    current_shot, location, icon='asset', foreground=None)
                current_item.setStatusTip(0, location)

                
    def edit_item(self):
        self.treewidget_shots.show()
        self.treewidget_assets.show()
        self.comp_catalogue.show()
        
    def rename_item(self, treewidget):
        if not treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'please select any item', QtWidgets.QMessageBox.Ok) 
            return
        current_item = treewidget.selectedItems()[-1]
        if not current_item.childCount():
            QtWidgets.QMessageBox.warning(
                self, 'warning', 'not able to rename', QtWidgets.QMessageBox.Ok) 
            return        
        item_name, ok = QtWidgets.QInputDialog.getText(
            self, 'input', 'enter the new name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        parent_item = self.treewidget_shots
        if current_item.parent():
            parent_item = current_item.parent()
        if self.has_item_exists(parent_item, item_name):
            QtWidgets.QMessageBox.critical(
                self, 'critical', 'already found <%s>' % item_name, QtWidgets.QMessageBox.Ok)            
            return        
        current_item.setText(0, item_name)

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
            return '%s1' % current_name
        suffix = current_name.rsplit(str(digits[-1]), 1)
        return '%s%s' % (''.join(suffix), digits[-1] + 1)       

    def find_children_items(self, treewidget, tag=False):
        selected_items = treewidget.selectedItems()
        stack = selected_items
        asset_items = set()
        while stack:
            current = stack.pop()
            if current.childCount():
                chidren = [current.child(index) for index in range (current.childCount())]
                stack.extend(chidren)
                continue
            if not tag:
                asset_items.add(current)
                continue
            if current.statusTip(0):
                asset_items.add(current.parent())
            else:
                asset_items.add(current)
        return asset_items
    
    def get_children_items(self, item):        
        children = []        
        for x in range(item.childCount()):
            children.append(item.child(x))
        return children
    
    def get_casting_data(self):
        widget_item = self.treewidget_shots.invisibleRootItem()
        casting_data = {}        
        toplevels = self.get_children_items(widget_item) 
        for toplevel in toplevels:
            casting_data.setdefault(toplevel.text(0), {})
            sublevels = self.get_children_items(toplevel) 
            for sublevel in sublevels:
                casting_data[toplevel.text(0)].setdefault(sublevel.text(0), [])
                children = self.get_children_items(sublevel)
                for child in children:    
                    casting_data[toplevel.text(0)][sublevel.text(0)].append(child.text(0))
        return casting_data
    
    def create_castingsheet(self):
        casting_data = self.get_casting_data()
        castingsheet_path = self.get_castingsheet_path()
        description = 'casting data preset for shots'
        key = 'casting'
        output_path = common.create_presets(castingsheet_path, description, key, casting_data)
        if not output_path:
            QtWidgets.QMessageBox.critical(
                self, 'critical', 'not able to create casting sheet', QtWidgets.QMessageBox.Ok)            
        QtWidgets.QMessageBox.information(
            self, 'Success', '%s\nDone!...' % output_path, QtWidgets.QMessageBox.Ok)
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_())         
