import os
import sys


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


class Window(QtWidgets.QMainWindow):
 
    def __init__(self, parent=None, standalone=None):
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.title = 'Casting Sheet'
        self.width = 572
        self.height = 716
        self.version, self.label = self.set_tool_context() 
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        
        self.environ = studioEnviron.Environ(self.current_show)
        #self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
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
        
        self.treewidget_assets = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget_assets.setObjectName("treewidget_assets")
        self.treewidget_assets.headerItem().setText(0, "Assets")
        self.treewidget_assets.setAlternatingRowColors(True)
        
        self.groupbox_data = QtWidgets.QGroupBox(self.splitter)
        self.groupbox_data.setObjectName('groupbox_data')
                
        self.gridlayout_data = QtWidgets.QGridLayout(self.groupbox_data)
        self.gridlayout_data.setObjectName('gridlayout_data')
        self.gridlayout_data.setHorizontalSpacing(5)
        self.gridlayout_data.setContentsMargins(5, 5, 5, 5)
        right_align = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        self.label_captions = QtWidgets.QLabel(self.groupbox_data)
        self.label_captions.setObjectName('label_captions')
        self.label_captions.setText('caption: ')
        self.label_captions.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_captions, 0, 0, 1, 1)        
        self.label_caption = QtWidgets.QLabel(self.groupbox_data)
        self.label_caption.setObjectName('label_caption')
        self.gridlayout_data.addWidget(self.label_caption, 0, 1, 1, 1)        
        self.label_tags = QtWidgets.QLabel(self.groupbox_data)
        self.label_tags.setObjectName('label_tags')
        self.label_tags.setText('tag: ')
        self.label_tags.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_tags, 1, 0, 1, 1)        
        self.label_tag = QtWidgets.QLabel(self.groupbox_data)
        self.label_tag.setObjectName('label_tag')
        self.gridlayout_data.addWidget(self.label_tag, 1, 1, 1, 1)     
        self.label_types = QtWidgets.QLabel(self.groupbox_data)
        self.label_types.setObjectName('label_types')
        self.label_types.setText('type: ')
        self.label_types.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_types, 2, 0, 1, 1)        
        self.label_type = QtWidgets.QLabel(self.groupbox_data)
        self.label_type.setObjectName('label_type')
        self.gridlayout_data.addWidget(self.label_type, 2, 1, 1, 1)  
        self.label_users = QtWidgets.QLabel(self.groupbox_data)
        self.label_users.setObjectName('label_users')
        self.label_users.setText('owner: ')
        self.label_users.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_users, 3, 0, 1, 1)        
        self.label_user = QtWidgets.QLabel(self.groupbox_data)
        self.label_user.setObjectName('label_user')           
        self.gridlayout_data.addWidget(self.label_user, 3, 1, 1, 1) 
        self.label_modifieds = QtWidgets.QLabel(self.groupbox_data)
        self.label_modifieds.setObjectName('label_modifieds')
        self.label_modifieds.setText('modified: ')
        self.label_modifieds.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_modifieds, 4, 0, 1, 1)        
        self.label_modified = QtWidgets.QLabel(self.groupbox_data)
        self.label_modified.setObjectName('label_modified')
        self.gridlayout_data.addWidget(self.label_modified, 4, 1, 1, 1)
        self.label_showpaths = QtWidgets.QLabel(self.groupbox_data)
        self.label_showpaths.setObjectName('label_dates')
        self.label_showpaths.setText('show path: ')
        self.label_showpaths.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_showpaths, 5, 0, 1, 1)        
        self.label_showpath = QtWidgets.QLabel(self.groupbox_data)
        self.label_showpath.setObjectName('label_showpath')
        self.gridlayout_data.addWidget(self.label_showpath, 5, 1, 1, 1)        
        self.label_locations = QtWidgets.QLabel(self.groupbox_data)
        self.label_locations.setObjectName('label_locations')
        self.label_locations.setText('location: ')
        self.label_locations.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_locations, 6, 0, 1, 1)        
        self.label_location = QtWidgets.QLabel(self.groupbox_data)
        self.label_location.setObjectName('label_location')
        self.gridlayout_data.addWidget(self.label_location, 6, 1, 1, 1)
        self.label_description = QtWidgets.QLabel(self.groupbox_data)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.gridlayout_data.addWidget(self.label_description, 7, 0, 1, 1)        
        self.textedit_description = QtWidgets.QTextEdit(self.groupbox_data)
        self.textedit_description.setObjectName('textedit_description')
        self.textedit_description.setReadOnly(True)
        self.textedit_description.setMinimumSize(QtCore.QSize(256, 0))
        self.textedit_description.setMaximumSize(QtCore.QSize(256, 16777215))
        self.gridlayout_data.addWidget(self.textedit_description, 8, 0, 1, 2)   
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox_data)
        self.button_thumbnail.setObjectName('button_thumbnail')
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.gridlayout_data.addWidget(self.button_thumbnail, 9, 0, 1, 2)  
                
        
        self.horizontallayout_create = QtWidgets.QHBoxLayout(self)
        self.horizontallayout_create.setObjectName('horizontallayout_toolbar')
        self.verticallayout_item.addLayout(self.horizontallayout_create)    
        
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

    def setup_menu(self):
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu') 
        
        actions = ['reload', 'add', 'instance', 'remove', 'parent']
        
        for each in actions:        
            action = QtWidgets.QAction(self)
            action.setObjectName('action_%s'%each)
            action.setToolTip(each) 
            action.setText(each)        
            self.menu.addAction(action)      
            self.toolbar.addAction(action)
            action.triggered.connect(partial(self.menu_actions, each))
            
    def menu_actions(self, menu):
        self.add_item(self.treewidget_shots)
        
        
    
    def add_item(self, treewidget):
            
        item_name, ok = QtWidgets.QInputDialog.getText(
            self, 'Input', 'Enter the item name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        
        parent = treewidget
        
        if treewidget.selectedItems():
            parent = treewidget.selectedItems()[-1]
        
        swidgets.add_treewidget_item(
            parent, item_name, icon=None, foreground=None)

             
        
   
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_())         
