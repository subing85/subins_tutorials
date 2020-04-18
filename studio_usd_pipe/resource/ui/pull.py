import os
import sys
import ast
import copy
import json
import platform
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial
from distutils import version

from studio_usd_pipe import resource
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import studio
from studio_usd_pipe.core import mayacreate
from studio_usd_pipe.core import preferences

from studio_usd_pipe.api import studioMaya 
from studio_usd_pipe.api import studioPublish

reload(studioPublish)
reload(studioMaya)
reload(mayacreate)
reload(widgets)


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, mode=None):  
        super(Window, self).__init__(parent)
        # self.setParent(parent)
        self.mode = mode        
        self.title = 'Asset Publish/Push'
        self.width = 572
        self.height = 622
        self.maya_format = {
            '.ma': 'mayaAscii',
            '.mb': 'mayaBinary',
            '.usd': 'pxrUsdImport',
            '.usda': 'pxrUsdImport'
            }
        self.version, self.label = self.set_tool_context()
        self.pub = studioPublish.Publish(self.mode)             
        self.pref = preferences.Preferences()        
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.icon_configure()
        self.set_current()
        self.set_current_caption()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_pull')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version)) 
        self.resize(self.width, self.height)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
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
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        
        self.button_logo, self.button_show = widgets.set_header(
            self.horizontallayout, show_icon=None) 
        
        self.line = QtWidgets.QFrame(self)
        self.line.setObjectName('line')        
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticallayout_item.addWidget(self.line)        
        
        self.horizontallayout_toolbar = QtWidgets.QHBoxLayout()
        self.horizontallayout_toolbar.setSpacing(10)
        self.horizontallayout_toolbar.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout_toolbar.setObjectName('horizontallayout_toolbar')
        self.verticallayout_item.addLayout(self.horizontallayout_toolbar)        
        
        self.line = QtWidgets.QFrame(self)
        self.line.setObjectName('line')        
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticallayout_item.addWidget(self.line)          
        
        #=======================================================================
        # self.groupbox_bar = QtWidgets.QGroupBox(self)
        # self.groupbox_bar.setObjectName('groupbox_bar')
        # self.groupbox_bar.setMinimumSize(QtCore.QSize(0, 40))
        # self.groupbox_bar.setMaximumSize(QtCore.QSize(16777215, 40))        
        # self.verticallayout.addWidget(self.groupbox_bar)
        # self.horizontallayout_bar = QtWidgets.QHBoxLayout(self.groupbox_bar)
        # self.horizontallayout_bar.setObjectName('horizontallayout_bar')        
        # self.horizontallayout_bar.setSpacing(0)
        # self.horizontallayout_bar.setContentsMargins(0, 0, 0, 0)
        # self.pushButton_2 = QtWidgets.QPushButton(self)
        # self.pushButton_2.setObjectName('pushButton_2')
        # self.pushButton_2.setMinimumSize(QtCore.QSize(100, 35))
        # self.pushButton_2.setMaximumSize(QtCore.QSize(100, 35))        
        # self.horizontallayout_bar.addWidget(self.pushButton_2)
        #=======================================================================
        
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setObjectName('horizontallayout_input')        
        self.horizontallayout_input.setSpacing(10)
        self.horizontallayout_input.setContentsMargins(5, 5, 5, 5)   
        self.verticallayout_item.addLayout(self.horizontallayout_input)
             
        self.treewidget = QtWidgets.QTreeWidget(self)
        self.treewidget.setObjectName('treewidget')
        # self.treewidget.headerItem().setText(0, 'No')
        self.treewidget.headerItem().setText(0, 'Assets')
        # self.treewidget.headerItem().setText(1, 'Location')
        self.treewidget.header().resizeSection (0, 250)
        self.treewidget.setStyleSheet('font: 12pt \'Sans Serif\';')
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.treewidget.customContextMenuRequested.connect(partial(self.on_context_menu, self.treewidget))        
        self.treewidget.itemClicked.connect (self.current_item_select)
        self.treewidget.currentItemChanged.connect (self.current_item_select)
               
        self.horizontallayout_input.addWidget(self.treewidget)
        
        self.groupbox_data = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_data.setObjectName('groupbox_data')
        self.horizontallayout_input.addWidget(self.groupbox_data)
        
        self.gridlayout_data = QtWidgets.QGridLayout(self.groupbox_data)
        self.gridlayout_data.setObjectName('gridlayout_data')
        self.gridlayout_data.setHorizontalSpacing(10)
        self.gridlayout_data.setContentsMargins(10, 20, 10, 10)
        
        self.label_captions = QtWidgets.QLabel(self.groupbox_data)
        self.label_captions.setObjectName('label_captions')
        self.label_captions.setText('Caption:')
        self.label_captions.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_captions.setMinimumSize(QtCore.QSize(55, 0))
        self.label_captions.setMaximumSize(QtCore.QSize(55, 16777215)) 
                
        self.gridlayout_data.addWidget(self.label_captions, 0, 0, 1, 1)        
        
        self.label_caption = QtWidgets.QLabel(self.groupbox_data)
        self.label_caption.setObjectName('label_caption')
        self.gridlayout_data.addWidget(self.label_caption, 0, 1, 1, 1)        
        
        self.label_tags = QtWidgets.QLabel(self.groupbox_data)
        self.label_tags.setObjectName('label_tags')
        self.label_tags.setText('Tag:')
        self.label_tags.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_tags.setMinimumSize(QtCore.QSize(55, 0))
        self.label_tags.setMaximumSize(QtCore.QSize(55, 16777215))         
        self.gridlayout_data.addWidget(self.label_tags, 1, 0, 1, 1)        
        
        self.label_tag = QtWidgets.QLabel(self.groupbox_data)
        self.label_tag.setObjectName('label_tag')
        self.gridlayout_data.addWidget(self.label_tag, 1, 1, 1, 1)     
                
        self.label_types = QtWidgets.QLabel(self.groupbox_data)
        self.label_types.setObjectName('label_types')
        self.label_types.setText('Type:')
        self.label_types.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_types.setMinimumSize(QtCore.QSize(55, 0))
        self.label_types.setMaximumSize(QtCore.QSize(55, 16777215))         
        self.gridlayout_data.addWidget(self.label_types, 2, 0, 1, 1)        
        
        self.label_type = QtWidgets.QLabel(self.groupbox_data)
        self.label_type.setObjectName('label_type')
        self.gridlayout_data.addWidget(self.label_type, 2, 1, 1, 1)  
        
        self.label_users = QtWidgets.QLabel(self.groupbox_data)
        self.label_users.setObjectName('label_users')
        self.label_users.setText('Owner:')
        self.label_users.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_users.setMinimumSize(QtCore.QSize(55, 0))
        self.label_users.setMaximumSize(QtCore.QSize(55, 16777215))         
        self.gridlayout_data.addWidget(self.label_users, 3, 0, 1, 1)        
        
        self.label_user = QtWidgets.QLabel(self.groupbox_data)
        self.label_user.setObjectName('label_user')           
        self.gridlayout_data.addWidget(self.label_user, 3, 1, 1, 1) 
        
        self.label_dates = QtWidgets.QLabel(self.groupbox_data)
        self.label_dates.setObjectName('label_dates')
        self.label_dates.setText('Date:')
        self.label_dates.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_dates.setMinimumSize(QtCore.QSize(55, 0))
        self.label_dates.setMaximumSize(QtCore.QSize(55, 16777215))          
        self.gridlayout_data.addWidget(self.label_dates, 4, 0, 1, 1)        
        
        self.label_date = QtWidgets.QLabel(self.groupbox_data)
        self.label_date.setObjectName('label_date')
        self.gridlayout_data.addWidget(self.label_date, 4, 1, 1, 1)
        
        self.label_locations = QtWidgets.QLabel(self.groupbox_data)
        self.label_locations.setObjectName('label_locations')
        self.label_locations.setText('Location:')
        self.label_locations.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_locations.setMinimumSize(QtCore.QSize(55, 0))
        self.label_locations.setMaximumSize(QtCore.QSize(55, 16777215))         
        self.gridlayout_data.addWidget(self.label_locations, 5, 0, 1, 1)        
        
        self.label_location = QtWidgets.QLabel(self.groupbox_data)
        self.label_location.setObjectName('label_location')
        self.gridlayout_data.addWidget(self.label_location, 5, 1, 1, 1)
        
        self.label_description = QtWidgets.QLabel(self.groupbox_data)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.gridlayout_data.addWidget(self.label_description, 6, 0, 1, 1)        

        self.textedit_description = QtWidgets.QTextEdit(self.groupbox_data)
        self.textedit_description.setObjectName('textedit_description')
        self.textedit_description.setReadOnly(True)
        self.textedit_description.setMinimumSize(QtCore.QSize(256, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(256, 90))
        self.gridlayout_data.addWidget(self.textedit_description, 7, 0, 1, 2)   
   
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox_data)
        self.button_thumbnail.setObjectName('button_thumbnail')
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.gridlayout_data.addWidget(self.button_thumbnail, 8, 0, 1, 2)  
         
        widgets.image_to_button(
            self.button_thumbnail, 256, 180, path=os.path.join(resource.getIconPath(), 'unknown.png'))
                
        spaceritem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout_data.addItem(spaceritem, 8, 0, 1, 1)
    
    def setup_menu(self):        
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 23))
        # self.menubar.setObjectName('menubar')
        # self.setMenuBar(self.menubar)
        
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')
        
        self.action_import_maya = QtWidgets.QAction(self)
        self.action_import_maya.setObjectName('action_import_maya')
        self.action_import_maya.setToolTip('Import Maya') 
        self.action_import_maya.setText('Import Maya')                   
        
        self.action_reference_maya = QtWidgets.QAction(self)
        self.action_reference_maya.setObjectName('action_reference_maya')
        self.action_reference_maya.setToolTip('Reference Maya')   
        self.action_reference_maya.setText('Reference Maya')   
             
        self.action_import_usd = QtWidgets.QAction(self)
        self.action_import_usd.setObjectName('action_import_usd')
        self.action_import_usd.setToolTip('Import USD')        
        self.action_import_usd.setText('Import USD')        
       
        self.action_reference_usd = QtWidgets.QAction(self)
        self.action_reference_usd.setObjectName('action_reference_usd')
        self.action_reference_usd.setToolTip('Reference USD')        
        self.action_reference_usd.setText('Reference USD')        
        
        self.action_open_source = QtWidgets.QAction(self)
        self.action_open_source.setObjectName('action_open_source')
        self.action_open_source.setToolTip('Open Source')        
        self.action_open_source.setText('Open Source')        
       
        self.action_pull_replace = QtWidgets.QAction(self)
        self.action_pull_replace.setObjectName('action_pull_replace')
        self.action_pull_replace.setToolTip('Pull with Replace')        
        self.action_pull_replace.setText('Pull with Replace')        
        
        self.action_pull_normal = QtWidgets.QAction(self)
        self.action_pull_normal.setObjectName('action_pull_normal')
        self.action_pull_normal.setToolTip('Pull without Replace')        
        self.action_pull_normal.setText('Pull without Replace')        
        
        self.action_open_location = QtWidgets.QAction(self)
        self.action_open_location.setObjectName('action_open_location')
        self.action_open_location.setToolTip('Open Location')        
        self.action_open_location.setText('Open Location')        
        
        self.menu.addAction(self.action_import_maya)
        self.menu.addAction(self.action_reference_maya)
        self.menu.addSeparator()
        self.menu.addAction(self.action_import_usd)
        self.menu.addAction(self.action_reference_usd)
        self.menu.addSeparator()
        self.menu.addAction(self.action_pull_replace)
        self.menu.addAction(self.action_pull_normal)
        self.menu.addSeparator()
        self.menu.addAction(self.action_open_source)
        self.menu.addAction(self.action_open_location)
        # self.menubar.addAction(self.menu.menuAction())
        self.action_import_maya.triggered.connect(partial(self.import_data, 0, self.treewidget))
        self.action_reference_maya.triggered.connect(partial(self.import_data, 1, self.treewidget))
        self.action_import_usd.triggered.connect(partial(self.import_data, 2, self.treewidget))
        self.action_reference_usd.triggered.connect(partial(self.import_data, 3, self.treewidget))
        self.action_open_source.triggered.connect(partial(self.import_data, 4, self.treewidget))
        self.action_pull_replace.triggered.connect(partial(self.import_data, 5, self.treewidget))
        self.action_pull_normal.triggered.connect(partial(self.import_data, 6, self.treewidget))
        self.action_open_location.triggered.connect(partial(self.import_data, 7, self.treewidget))
    
    def setup_toolbar(self):             
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.addSeparator()        
        self.toolbar.addAction(self.action_import_maya)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_reference_maya)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_import_usd)
        self.toolbar.addSeparator()        
        self.toolbar.addAction(self.action_reference_usd)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_pull_replace)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_pull_normal)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_open_source)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_open_location)
        self.toolbar.addSeparator()
        self.horizontallayout_toolbar.addWidget(self.toolbar)

    def icon_configure (self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(resource.getIconPath(), 'pull.png')))
        self.setWindowIcon(icon)
        
        qactions = self.findChildren(QtWidgets.QAction)
        for qaction in qactions :
            icon = QtGui.QIcon()            
            icon_name = qaction.objectName().split('action_')[-1]
            icon_path = (os.path.join(resource.getIconPath(), '{}.png'.format(icon_name)))
            icon.addPixmap(QtGui.QPixmap (icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            qaction.setIcon (icon)  

    def on_context_menu(self, widget, point):
        index = widget.indexAt(point)
        if not index.isValid():
            return        
        # current_item = widget.indexAt(point)
        current_item = widget.selectedItems()[-1]       
        contents = current_item.statusTip(0)
        if not contents:
            return
        # self.menu.exec_(QtGui.QCursor.pos())
        contents = ast.literal_eval(contents)        
        subfield = contents['hierarchy'].split('|')[1]        
        self.set_menu_options(subfield)        
        self.menu.exec_(widget.mapToGlobal(point))
    
    def set_menu_options(self, subfield):
        actions = [
            self.action_import_maya,
            self.action_reference_maya,           
            self.action_import_usd,
            self.action_reference_usd,
            self.action_open_source,
            self.action_pull_normal,
            self.action_pull_replace,          
            self.action_open_location
            ]
        for action in actions:
            action.setVisible(True)                
        invisibile = {
            'uv': [
                self.action_import_maya,
                self.action_reference_maya,           
                self.action_import_usd,
                self.action_reference_usd,
                self.action_pull_normal,
                # self.action_pull_replace     
                ],
            'surface': [
                #self.action_import_maya,
                #self.action_reference_maya,           
                self.action_import_usd,
                self.action_reference_usd,
                # self.action_pull_normal,               
                # self.action_pull_replace     
                ],
        
            'puppet': [
                #self.action_import_maya,
                # self.action_reference_maya,           
                self.action_import_usd,
                self.action_reference_usd,
                self.action_pull_normal,               
                self.action_pull_replace                    
                ]
            }
        if subfield in invisibile:
            for action in invisibile[subfield]:
                action.setVisible(False)

    def set_tool_context(self):
        config = studio.Configure()
        config.tool()
        return config.version, config.pretty          
        
    def set_current(self):
        bundle_data = self.pref.get()   
        if not bundle_data:
            warnings.warn('not found show icon', Warning)
            return        
        size = self.button_show.minimumSize()
        widgets.image_to_button(
            self.button_show, size.width(), size.height(), path=bundle_data['show_icon'])
    
    def set_current_caption(self):
        pub_data = self.pub.get()
        valid_subfields = self.pub.valid_modes[self.mode]['subfield']
        self.treewidget.clear()
        for caption, contents in pub_data.items():
            version_contents = contents[contents.keys()[0]]
            tag = version_contents[version_contents.keys()[0]]['tag']
            caption_item = widgets.add_treewidget_item(self.treewidget, caption, icon=tag)
            for subfield in valid_subfields:                
                if subfield not in contents:
                    continue
                subfield_item = widgets.add_treewidget_item(caption_item, subfield, icon=subfield)
                versions = sorted(contents[subfield].keys(), key=version.StrictVersion)
                versions.reverse()
                for each in versions:
                    version_item = widgets.add_treewidget_item(subfield_item, each, icon='version')
                    ver_contents = copy.deepcopy(contents[subfield][each])
                    more_contents = self.pub.get_more_data(caption, subfield, each)
                    ver_contents['hierarchy'] = '{}|{}|{}'.format(caption, subfield, each)
                    ver_contents['subfield'] = subfield
                    ver_contents.update(more_contents)
                    version_item.setStatusTip(0, str(ver_contents))
        self.treewidget.expandAll()

    def current_item_select(self, *args):
        self.clear_display() 
        current_item = args[0]        
        contents = current_item.statusTip(0)
        if not contents:
            return
        contents = ast.literal_eval(contents)
        self.label_caption.setText(contents['caption'])
        self.label_tag.setText(contents['tag'])
        self.label_type.setText(contents['type'])
        self.label_user.setText(contents['user'])
        self.label_date.setText(contents['date'])
        location = '...{}'.format(contents['location'].split(self.pub.show_path)[-1])
        self.label_location.setText(location) 
        self.textedit_description.setText(contents['description'])
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = contents['thumbnail'][0]
        if not os.path.isfile(thumbnail_icon):
            thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)
        
        subfield = contents['hierarchy'].split('|')[1]        
        self.set_menu_options(subfield)             
            
    def clear_display(self):
        self.label_caption.clear()
        self.label_tag.clear()
        self.label_type.clear()
        self.label_user.clear()
        self.label_date.clear()
        self.label_location.clear()
        self.textedit_description.clear()
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon) 

    def import_data(self, index, treewidget):
        current_items = treewidget.selectedItems()
        if not current_items:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not selected any items!...', QtWidgets.QMessageBox.Ok)            
            print '# Warning: Not selected any items!...'
            return
        
        for item in current_items:
            contents = item.statusTip(0)
            if not contents:
                print '# Warning: Not selected correct item!...' 
                continue
            contents = ast.literal_eval(contents)
            print json.dumps(contents, indent=4)            
            #===================================================================
            # keys = {
            #     'import_maya': 0,
            #     'reference_maya': 1,
            #     'import_usd': 2,
            #     'reference_usd': 3,
            #     'open_source': 4,
            #     'pull_replace': 5,
            #     'pull_normal': 6,
            #     'open_location': 7
            #     }
            #===================================================================                  
            if index == 0:
                self.import_maya(contents['maya'][0])                
            if index == 1:
                self.reference_maya(contents['maya'][0])                            
            if index == 2:
                self.import_maya(contents['usd'][0])             
            if index == 3:
                self.reference_maya(contents['usd'][0])
            if index == 4:
                self.open_maya(contents['source_file'])
            if index == 5:
                self.pull_studio(contents['studio_format'][0], contents['subfield'], replace=True)                               
            if index == 6:
                self.pull_studio(contents['studio_format'][0], contents['subfield'], replace=False)
            if index == 7:
                self.open_location(contents['location'])                                                    
     
    def open_maya(self, file):
        file_type = self.maya_format[os.path.splitext(file)[-1]]
        smaya = studioMaya.Maya()
        smaya.open_maya(file, file_type=file_type)
            
    def import_maya(self, file):
        file_type = self.maya_format[os.path.splitext(file)[-1]]
        namespace = '{}_1'.format(
            os.path.basename(os.path.splitext(file)[0]))
        smaya = studioMaya.Maya()
        smaya.import_maya(file, file_type=file_type, namespace=namespace)
 
    def reference_maya(self, file):
        namespace = os.path.basename(os.path.splitext(file)[0])
        smaya = studioMaya.Maya()
        smaya.reference_maya(file, locked=True, namespace=namespace)

    def pull_studio(self, file, subfield, replace=True):
        
        if subfield=='model':
            mcreate = mayacreate.Create(file)
            mcreate.model(replace=replace)
            
        if subfield=='uv':
            mcreate = mayacreate.Create(file)
            mcreate.uv(replace=True)            

        if subfield=='surface':
            mcreate = mayacreate.Create(file)
            mcreate.surface(replace=replace)
                 
        if subfield=='puppet':
            mcreate = mayacreate.Create(file)
            mcreate.puppet(replace=replace)
            

    
    def open_location(self, location):
        if platform.system() == 'Windows':
            try:
                os.startfile(location)
            except:
                pass
        if platform.system() == 'Linux':    
            try:
                os.system('xdg-open \"%s\"' % location)
            except:
                pass    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, mode='assets')
    window.show()
    sys.exit(app.exec_())        
