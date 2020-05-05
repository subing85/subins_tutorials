import os
import sys
import ast
import copy
import json

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial
from distutils import version

from studio_usd_pipe import resource
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPush
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioEnviron

from pprint import pprint

reload(swidgets)


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, mode=None):  
        super(Window, self).__init__(parent)
        # self.setParent(parent)
        self.mode = mode      
        self.pipe = 'assets'          
        self.title = 'Create Asset USD'
        self.subfield = 'usd'
        self.width = 572
        self.height = 800
        
        self.caption_data = {}        
        self.composition_bundles = {}

        self.version, self.label = self.set_tool_context() 
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
        
        # self.db_data = self.pub.get()
        
        self.setup_ui()
        self.setup_menu()
        
        self.set_default()       
        self.icon_configure()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_pullusd')
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
        self.horizontallayout.setObjectName('horizontallayout_output')
        self.verticallayout_item.addLayout(self.horizontallayout)
        
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None) 
        
        self.line = QtWidgets.QFrame(self)
        self.line.setObjectName('line')        
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticallayout_item.addWidget(self.line)

        self.horizontallayout_main = QtWidgets.QHBoxLayout()
        self.horizontallayout_main.setObjectName('horizontallayout_main')
        self.verticallayout_item.addLayout(self.horizontallayout_main)
        
        self.treewidget_input = QtWidgets.QTreeWidget(self)
        self.treewidget_input.setObjectName('treewidget_input')
        self.treewidget_input.header().setVisible(False)
        
        # self.treewidget_input.headerItem().setText(0, 'Assets')
        
        self.treewidget_input.header().resizeSection (0, 250)
        self.treewidget_input.setStyleSheet('font: 12pt \'Sans Serif\';')
        self.treewidget_input.setAlternatingRowColors(True)
        self.treewidget_input.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.treewidget_input.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.treewidget_input.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget_input))        
        # self.treewidget_input.itemClicked.connect (self.current_item_select)
        # self.treewidget_input.currentItemChanged.connect (self.current_item_select)        
                
        self.horizontallayout_main.addWidget(self.treewidget_input) 
       
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName('gridlayout')
        self.horizontallayout_main.addLayout(self.gridlayout)               
        
        self.label_caption = QtWidgets.QLabel(self.groupbox)
        self.label_caption.setObjectName('label_caption')
        self.label_caption.setText('Caption')
        self.label_caption.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_caption, 0, 0, 1, 1)
        self.combobox_caption = QtWidgets.QComboBox(self.groupbox)
        self.combobox_caption.setObjectName('combobox_caption')
        self.combobox_caption.setEditable(True)
        self.combobox_caption.setEnabled(True)
        self.combobox_caption.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_caption, 0, 1, 1, 1)   
        
        self.label_composition = QtWidgets.QLabel(self.groupbox)
        self.label_composition.setObjectName('label_composition')
        self.label_composition.setText('Composition')
        self.label_composition.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_composition, 2, 0, 1, 1)
        
        self.treewidget_composition = QtWidgets.QTreeWidget(self)
        self.treewidget_composition.setObjectName('treewidget_composition')
        self.treewidget_composition.header().setVisible(False)
        # self.treewidget_composition.headerItem().setText(0, 'Composition')
        # self.treewidget_composition.sheader().resizeSection (0, 250)
        self.treewidget_composition.setStyleSheet('font: 12pt \'Sans Serif\';')
        self.treewidget_composition.setAlternatingRowColors(True)        
        self.treewidget_composition.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.treewidget_composition.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget_composition))                 
        
        self.gridlayout.addWidget(self.treewidget_composition, 2, 1, 1, 1)
                
        self.label_thumbnail = QtWidgets.QLabel(self.groupbox)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_thumbnail, 3, 0, 1, 1)
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox)
        self.button_thumbnail.setObjectName('button_thumbnail')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        swidgets.image_to_button(
            self.button_thumbnail, 256, 180, path=os.path.join(resource.getIconPath(), 'screenshot.png'))          
        self.button_thumbnail.clicked.connect(partial(self.take_thumbnail, self.button_thumbnail))
        self.gridlayout.addWidget(self.button_thumbnail, 3, 1, 1, 1)  
        self.label_description = QtWidgets.QLabel(self.groupbox)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.label_description.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_description, 4, 0, 1, 1)
        self.textedit_description = QtWidgets.QTextEdit(self.groupbox)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 90))          
        self.gridlayout.addWidget(self.textedit_description, 4, 1, 1, 1)  
        self.label_version = QtWidgets.QLabel(self.groupbox)
        self.label_version.setObjectName('label_version')
        self.label_version.setText('version')
        self.label_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_version, 5, 0, 1, 1)
        self.combobox_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_version.setObjectName('combobox_version')
        self.combobox_version.setEditable(True)
        self.combobox_version.setEnabled(True)
        self.combobox_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_version, 5, 1, 1, 1)                  
        self.label_latest_version = QtWidgets.QLabel(self.groupbox)
        self.label_latest_version.setObjectName('label_latest_version')
        self.label_latest_version.setText('Latest Version')
        self.label_latest_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_latest_version, 6, 0, 1, 1)
        self.combobox_latest_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_latest_version.setObjectName('combobox_latest_version')
        self.combobox_latest_version.setEditable(True)
        self.combobox_latest_version.setEnabled(False)
        self.combobox_latest_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_latest_version, 6, 1, 1, 1)
        self.label_next_version = QtWidgets.QLabel(self.groupbox)
        self.label_next_version.setObjectName('label_next_version')
        self.label_next_version.setText('Next Version')
        self.label_next_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_next_version, 7, 0, 1, 1)
        self.combobox_next_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_next_version.setObjectName('combobox_next_version')
        self.combobox_next_version.setEditable(True)
        self.combobox_next_version.setEnabled(False)
        self.combobox_next_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_next_version, 7, 1, 1, 1)  
        self.horizontallayout_button = QtWidgets.QHBoxLayout()
        self.horizontallayout_button.setObjectName('horizontallayout_button')
        self.horizontallayout_button.setSpacing(10)
        self.horizontallayout_button.setContentsMargins(5, 5, 5, 5)        
        self.verticallayout.addLayout(self.horizontallayout_button)  
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_button.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout_button.addWidget(self.button_cancel)
        self.button_publish = QtWidgets.QPushButton(self)
        self.button_publish.setObjectName('button_create')
        self.button_publish.setText('Publish')
        self.horizontallayout_button.addWidget(self.button_publish)
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)        
        self.combobox_caption.editTextChanged.connect(self.set_current_caption)
        self.combobox_version.currentIndexChanged.connect(self.set_current_version)
        self.button_publish.clicked.connect(self.publish)        
        self.button_cancel.clicked.connect(self.close)     
                                
    def setup_menu(self):        
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')
        self.action_add = QtWidgets.QAction(self)
        self.action_add.setObjectName('action_add')
        self.action_add.setToolTip('Add to composition') 
        self.action_add.setText('Add to Composition')
        self.action_remove = QtWidgets.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setToolTip('Remove from composition') 
        self.action_remove.setText('Remove')                          
        self.menu.addAction(self.action_add)
        self.menu.addAction(self.action_remove)
        self.action_add.triggered.connect(
            partial(self.add_to_composition, self.treewidget_input, self.treewidget_composition))
        self.action_remove.triggered.connect(
            partial(self.remove_from_composition, self.treewidget_composition, self.treewidget_input))
    
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
        current_item = widget.selectedItems()[-1]       
        contents = current_item.statusTip(0)
        if not contents:
            return
        contents = ast.literal_eval(contents)
        subfield = contents['hierarchy'].split('|')[1]        
        self.set_menu_options(widget)        
        self.menu.exec_(widget.mapToGlobal(point))
        
    def set_menu_options(self, widget):
        actions = [
            self.action_add,
            self.action_remove
            ]
        for action in actions:
            action.setVisible(True)                
        invisibile = {
            'treewidget_input': [
                # self.action_add,
                self.action_remove,
                ],
            'treewidget_composition': [
                self.action_add,
                # self.action_remove,
                ]     
            }
        if widget.objectName() in invisibile:
            for action in invisibile[widget.objectName()]:
                action.setVisible(False)
 
    def set_tool_context(self):
        config = sheader.Header()
        config.tool()
        return config.version, config.pretty
    
    def set_default(self):
        self.clear_widget()
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
        pub_data = self.spipe.get()
        captions = ['']
        if pub_data:  # add caption from database
            captions = [''] + pub_data.keys()
        self.combobox_caption.addItems(captions)
        self.combobox_version.addItems(['major', 'minor', 'patch'])            
        size = self.button_thumbnail.minimumSize()
        swidgets.image_to_button(
            self.button_thumbnail,
            size.width(),
            size.height(),
            path=os.path.join(resource.getIconPath(), 'screenshot.png')
            )

    def clear_widget(self):
        self.combobox_caption.clear()
        self.textedit_description.clear()
        self.combobox_version.clear()
        self.combobox_latest_version.clear()
        self.combobox_next_version.clear()
        self.treewidget_composition.clear()
        self.treewidget_input.clear()         

    def set_current_version(self, caption=None):
        if not caption:
            caption = self.combobox_caption.currentText()
        semantic_version = self.combobox_version.currentIndex()
        self.combobox_latest_version.clear() 
        self.combobox_next_version.clear()   
             
        versions = self.spipe.get_versions(caption, subfield=self.subfield)
        
        if not versions:
            versions = [None]
        self.combobox_latest_version.addItems(versions)
        next_version = self.spipe.get_next_version(caption, semantic_version, self.subfield)
        self.combobox_next_version.addItem(next_version)        
       
    def set_current_caption(self):
        caption = self.combobox_caption.currentText()
        self.set_current_version(caption=caption)
        self.load_current_caption(caption)
        
    def load_current_caption(self, caption):        
        self.caption_data = self.spipe.get_subfields(caption)
        self.treewidget_input.clear()
        valid_subfields = self.spipe.pipe_inputs['subfield']['values']
        for subfield in valid_subfields:
            if subfield not in self.caption_data:
                continue
            if subfield == 'puppet':
                continue   
            subfield_item = swidgets.add_treewidget_item(
                self.treewidget_input, subfield, icon=subfield, foreground=[255, 255, 255])
            versions = sorted(self.caption_data[subfield].keys(), key=version.StrictVersion)
            versions.reverse()
            for each in versions:
                version_item = swidgets.add_treewidget_item(
                    subfield_item, each, icon='version', foreground=[255, 255, 255])
                ver_contents = copy.deepcopy(self.caption_data[subfield][each])
                more_contents = self.spipe.get_more_data(caption, subfield, each)
                ver_contents['hierarchy'] = '{}|{}|{}'.format(caption, subfield, each)
                ver_contents['subfield'] = subfield
                ver_contents.update(more_contents)
                version_item.setStatusTip(0, str(ver_contents))
        self.treewidget_input.expandAll()
    
    def get_parent_items(self, treewidget):
        widget_item = treewidget.invisibleRootItem()
        subfields = {}
        for parent in range (widget_item.childCount()):
            parent_item = widget_item.child(parent)
            parent_contents = {
                'widget': parent_item,
                'child': {}
                }
            subfields.setdefault(parent_item.text(0), parent_contents)
            for child in range(parent_item.childCount()):
                child_item = parent_item.child(child)
                subfields[parent_item.text(0)]['child'].setdefault(
                    child_item.text(0), child_item)
        return subfields   
    
    def add_to_composition(self, from_widget, to_widget):
        current_items = from_widget.selectedItems()
        for item in current_items:
            contents = item.statusTip(0)
            if not contents:
                return
            contents = ast.literal_eval(contents)
            subfield = contents['hierarchy'].split('|')[1]
            exists_subfields = self.get_parent_items(to_widget)
            if subfield in exists_subfields:
                children = exists_subfields[subfield]['child']
                if item.text(0) in children:
                    message = '%s already exists!..' % item.text(0)
                    QtWidgets.QMessageBox.warning(
                        self, 'Warning', message, QtWidgets.QMessageBox.Ok)
                    continue
                subfield_item = exists_subfields[subfield]['widget']
            else:
                subfield_item = swidgets.add_treewidget_item(to_widget, subfield, icon=subfield)
            version_item = swidgets.add_treewidget_item(subfield_item, item.text(0), icon='version')
            self.composition_bundles.setdefault(version_item, item)
            version_item.setStatusTip(0, str(contents))
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(0, brush)
            item.setDisabled (True)
            to_widget.setItemExpanded(subfield_item, 1)
        from_widget.clearSelection()
            
    def remove_from_composition(self, from_widget, to_widget):
        current_items = from_widget.selectedItems()
        widget_item = from_widget.invisibleRootItem()
        for item in current_items: 
            widget_item.removeChild (item)
            self.composition_bundles[item].setDisabled(False)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            self.composition_bundles[item].setForeground(0, brush)
        
    def take_thumbnail(self, button):
        smaya = studioMaya.Maya()
        output_path, w, h = smaya.vieport_snapshot(
            output_path=None,
            width=768,
            height=768,
            )
        qsize = button.minimumSize()
        swidgets.image_to_button(
            button,
            qsize.width(),
            qsize.height(),
            path=output_path
            )        
        self.button_thumbnail.setToolTip(output_path)
        
    def get_caption_tag(self, caption):
        tag_data = self.spipe.get_tag_caption()
                
    def get_widget_data(self):        
        caption = self.combobox_caption.currentText()
        tag = self.spipe.get_caption_tag(caption)
        swidgets = {
            'caption': caption,
            'subfield': self.subfield,
            'type': self.types,
            'tag': tag,
            'thumbnail': self.button_thumbnail,
            'description': self.textedit_description,
            'version': self.combobox_next_version       
            }
        widget_data = {}        
        for key, widget in swidgets.items():
            widget_value = widget
            if isinstance(widget, QtWidgets.QComboBox):
                widget_value = widget.currentText().encode()
            if isinstance(widget, QtWidgets.QTextEdit):
                widget_value = widget.toPlainText().encode()
            if isinstance(widget, QtWidgets.QPushButton):
                widget_value = widget.toolTip().encode()
            if not widget_value:
                widget_value = None
            widget_data.setdefault(key, widget_value)
        return widget_data
    
    def get_composition_data(self):

        widget_item = self.treewidget_composition.invisibleRootItem()
        composition_data = {}
        for parent in range (widget_item.childCount()):
            parent_item = widget_item.child(parent)
            composition_data.setdefault(parent_item.text(0), {})
            for child in range(parent_item.childCount()):
                child_item = parent_item.child(child)
                contents = ast.literal_eval(child_item.statusTip(0))
                inputs = {
                    'usd': contents['usd'],
                    'location': contents['location']
                    }
                composition_data[parent_item.text(0)].setdefault(
                    child_item.text(0), inputs)
        return composition_data     
                
    def publish(self):
        widget_data = self.get_widget_data()
        composition_data = self.get_composition_data()
        
        if None in widget_data.values() or not composition_data:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty inputs!...', QtWidgets.QMessageBox.Ok)
            return
        
        self.spipe.bundle = copy.deepcopy(widget_data)
        self.spipe.bundle['source_file'] = None
        
        print '\n#inputs\t'
        print json.dumps(self.spipe.bundle, indent=4)
        print json.dumps(composition_data, indent=4)
        
        self.spipe.pack(composition=composition_data)
        
        self.spipe.release()
        self.set_default()       
        self.set_current_version()
        QtWidgets.QMessageBox.information(
            self, 'Success', 'Done!...', QtWidgets.QMessageBox.Ok)                    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, mode='assets')
    window.show()
sys.exit(app.exec_()) 
