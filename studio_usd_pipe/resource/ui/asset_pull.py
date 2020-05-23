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

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.api import studioPull
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioEnviron

from studio_usd_pipe.utils import maya_scene

reload(studioPull)
reload(maya_scene)
reload(studioPipe)


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, standalone=None, application=None):  
        super(Window, self).__init__(parent)
        self.standalone = standalone
        self.application = application        
        self.pipe = 'assets'        
        self.title = 'Asset Pull'
        self.width = 550
        self.height = 650
        self.toolbox = False
        self.shows = studioShow.Show()
        self.current_show = self.shows.get_current_show()
        self.current_show = 'btm'  # to remove        
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
        self.show_icon = self.environ.get_show_icon()
        self.setup_ui()
        self.setup_icons()
        self.setup_default()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_asset_pull')
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
        self.label_search = QtWidgets.QLabel(self)
        self.label_search.setObjectName('label_search')
        self.label_search.setText('search: ')       
        self.horizontallayout_toolbar.addWidget(self.label_search)
        self.lineedit_search = QtWidgets.QLineEdit(self)
        self.lineedit_search.setObjectName('lineedit_search')
        self.lineedit_search.textEdited.connect(self.search)
        self.horizontallayout_toolbar.addWidget(self.lineedit_search)  
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setObjectName('horizontallayout_input')        
        self.horizontallayout_input.setSpacing(5)
        self.horizontallayout_input.setContentsMargins(0, 0, 0, 0)   
        self.verticallayout_item.addLayout(self.horizontallayout_input)
        self.treewidget = QtWidgets.QTreeWidget(self)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.headerItem().setText(0, 'Assets')
        self.treewidget.header().resizeSection (0, 250)
        self.treewidget.setStyleSheet('font: 12pt \'Sans Serif\';')
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.treewidget.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget))        
        self.treewidget.itemClicked.connect (self.current_item_select)
        self.treewidget.currentItemChanged.connect (self.current_item_select)
        self.horizontallayout_input.addWidget(self.treewidget)
        self.groupbox_data = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_data.setObjectName('groupbox_data')
        self.horizontallayout_input.addWidget(self.groupbox_data)
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

    def setup_icons(self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)  
            
    def setup_default(self):
        self.load_captions(input_data=None)
        swidgets.image_to_button(
            self.button_thumbnail,
            256,
            180,
            path=os.path.join(resource.getIconPath(), 'unknown.png')
            )        
        
    def on_context_menu(self, widget, point):
        if not self.toolbox:
            self.toolbox = True
            return
        index = widget.indexAt(point)
        if not index.isValid():
            return        
        # current_item = widget.indexAt(point)
        current_item = widget.selectedItems()
        if not current_item:
            return
        contents = current_item[-1].statusTip(0)
        if not contents:
            return
        # self.menu.exec_(QtGui.QCursor.pos())
        contents = ast.literal_eval(contents)        
        subfield = contents['subfield']
        self.setup_menu()
        self.menu.exec_(widget.mapToGlobal(point))
        
    def setup_toolbox(self, subfield):
        pull = studioPull.Pull(application=self.application, subfield=subfield)
        modules = pull.get_creators()
        if not modules:
            QtWidgets.QMessageBox.critical(
                self,
                'critical',
                'not found any %s creator bundles' % subfield,
                QtWidgets.QMessageBox.Ok
                )            
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu') 
        swidgets.remove_widgets(self.toolbar.actions())
        for index, module in modules.items():
            action = QtWidgets.QAction(self)
            action.setObjectName('action_%s' % module.__name__)
            action.setToolTip(module.NAME) 
            action.setText(module.NAME)
            swidgets.update_widget_icon(action, module.ICON)
            action.triggered.connect(
                partial(self.pull_action, module))
            self.toolbar.addSeparator()        
            self.toolbar.addAction(action)
        self.toolbox = False        
            
    def setup_menu(self):
        for action in self.toolbar.actions():
            self.menu.addAction(action)                   
    
    def load_captions(self, input_data=None):
        self.treewidget.clear()
        if not input_data:
            input_data = self.spipe.get()
        valid_subfields = self.spipe.pipe_inputs['subfield']['values']
        for caption, contents in input_data.items():
            caption_item = swidgets.add_treewidget_item(
                self.treewidget, caption, icon=None)
            self.treewidget.setItemExpanded(caption_item, 1)            
            for subfield in valid_subfields:                
                if subfield not in contents:
                    continue
                subfield_item = swidgets.add_treewidget_item(
                    caption_item, subfield, icon=subfield)
                versions = common.set_version_order(contents[subfield].keys())
                for each in versions:
                    cuttrent_tag = contents[subfield][each]['tag']
                    version_item = swidgets.add_treewidget_item(
                        subfield_item, each, icon=cuttrent_tag)
                    more_contents = self.spipe.get_more_data(caption, subfield, each)
                    ver_contents = copy.deepcopy(contents[subfield][each])
                    ver_contents.update(more_contents)
                    version_item.setStatusTip(0, str(ver_contents))
                    # update root item icon with pipe tag(character, prop, etc)
                    swidgets.update_treewidget_item_icon(caption_item, cuttrent_tag)

    def current_item_select(self, *args):
        self.clear_widget()
        current_item = args[0]        
        contents = current_item.statusTip(0)
        if not contents:
            return
        contents = ast.literal_eval(contents)
        self.setup_toolbox(contents['subfield'])
        self.label_caption.setText(contents['caption'])
        self.label_tag.setText(contents['tag'])
        self.label_type.setText(contents['type'])
        self.label_user.setText(contents['user'])
        self.label_modified.setText(contents['modified'])
        self.label_showpath.setText(contents['show_path'])
        location = '...%s' % (contents['location'].split(contents['show_path'])[-1])
        self.label_location.setText(location) 
        self.textedit_description.setText(contents['description'])
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = contents['thumbnail']
        if not os.path.isfile(thumbnail_icon):
            thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        swidgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)
            
    def clear_widget(self):
        self.label_caption.clear()
        self.label_tag.clear()
        self.label_type.clear()
        self.label_user.clear()
        self.label_modified.clear()
        self.label_showpath.clear()        
        self.label_location.clear()
        self.textedit_description.clear()
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        swidgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon) 
        
    def search(self, *args):
        search_for = args[0].encode().lower()
        if '|' in search_for:
            search_for = search_for.split('|')
        else:
            search_for = [search_for, '']
        input_data = self.spipe.get()
        find_data = {}
        for caption in input_data:
            if search_for[0].endswith('*'):
                if search_for[0].replace('*', '') not in caption.lower():
                    continue
            else:
                if search_for[0] != caption.lower():
                    continue
            find_data.setdefault(caption, input_data[caption])
            for subfiled in input_data[caption]:
                if search_for[1].endswith('*'):
                    if search_for[1].replace('*', '') not in subfiled.lower():
                        continue
                else:
                    if search_for[1] != subfiled.lower():
                        continue
                find_data[caption] = {}
                find_data[caption].setdefault(subfiled, input_data[caption][subfiled])  
        self.load_captions(input_data=find_data)
        
    def pull_action(self, module):
        current_items = self.treewidget.selectedItems()
        if not current_items:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not selected any items!...', QtWidgets.QMessageBox.Ok)            
            print '# warning:  Not selected any items!...'
            return        
        valids = {}        
        for item in current_items:
            contents = item.statusTip(0)
            if not contents:
                print '# warning:  wrong selection!...' 
                continue
            contents = ast.literal_eval(contents)
            print '\n#header: inputs'
            print json.dumps(contents, indent=4)            
            pull = studioPull.Pull(application=self.application)
            valid, message = pull.do_pull(module, **contents)
            valids.setdefault(valid, []).append(message)
        if False in valids:
            QtWidgets.QMessageBox.critical(
                self, 'critical', '\n'.join(valids[False]), QtWidgets.QMessageBox.Ok)
            return
        QtWidgets.QMessageBox.information(
            self, 'Success', 'Done!...', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True, application='maya')
    window.show()
    sys.exit(app.exec_())        
