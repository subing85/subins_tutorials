import os
import sys
import copy
import json
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.api import studioMaya
from studio_usd_pipe.api import studioPublish
from studio_usd_pipe.core import configure
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import preferences

reload(studioPublish)


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None, mode=None):
        super(Window, self).__init__(parent)        
        # self.setParent(parent)
        self.setWindowFlags(QtCore.Qt.Window) 
        self.mode = mode        
        self.title = 'Asset Publish/Push'
        self.width = 572
        self.height = 716
        self.version, self.label = self.set_tool_context()        
        self.pub = studioPublish.Publish(self.mode)                
        self.pref = preferences.Preferences()
        self.setup_ui()
        self.set_current()
        
    def setup_ui(self):
        self.setObjectName('widget_preferences')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version))        
        self.resize(self.width, self.height)         
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('{} <{}>'.format(self.label, self.title))  
        self.verticallayout.addWidget(self.groupbox)             
        self.verticallayout_item = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)                
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.button_logo, self.button_show = widgets.set_header(
            self.horizontallayout, show_icon=None)         
        self.horizontallayout_output = QtWidgets.QHBoxLayout()
        self.horizontallayout_output.setObjectName('horizontallayout_output')
        self.horizontallayout_output.setSpacing(10)
        self.horizontallayout_output.setContentsMargins(5, 5, 5, 5)
        self.verticallayout_item.addLayout(self.horizontallayout_output)
        studio_maya = studioMaya.Maya()
        self.current_file, file_type = studio_maya.get_current_file()        
        source_file = 'Current File: {}\nFile Type: {}'.format(self.current_file, file_type)
        self.label_source = QtWidgets.QLabel()
        self.label_source.setObjectName('label_source')
        self.label_source.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_source.setStyleSheet('font: 12pt;')
        self.label_source.setText(source_file)
        self.label_source.setToolTip(file_type)
        self.horizontallayout_output.addWidget(self.label_source)
        # space
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout_input.setObjectName('horizontallayout_input') 
        self.verticallayout_item.addLayout(self.horizontallayout_input)        
        self.gridlayout = QtWidgets.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)        
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
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
        self.label_subfield = QtWidgets.QLabel(self.groupbox)
        self.label_subfield.setObjectName('label_subfield')
        self.label_subfield.setText('Subfield')
        self.label_subfield.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_subfield, 1, 0, 1, 1)
        self.combobox_subfield = QtWidgets.QComboBox(self.groupbox)
        self.combobox_subfield.setObjectName('combobox_subfield')
        self.combobox_subfield.setEditable(True)
        self.combobox_subfield.setEnabled(True)
        self.combobox_subfield.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combobox_subfield.addItems(self.pub.valid_modes[self.mode]['subfield'])
        self.gridlayout.addWidget(self.combobox_subfield, 1, 1, 1, 1)  
        self.label_type = QtWidgets.QLabel(self.groupbox)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('Type')
        self.label_type.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_type, 2, 0, 1, 1)
        self.combobox_type = QtWidgets.QComboBox(self.groupbox)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.setEditable(True)
        self.combobox_type.setEnabled(True)
        self.combobox_type.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combobox_type.addItems(self.pub.valid_modes[self.mode]['type'])        
        self.gridlayout.addWidget(self.combobox_type, 2, 1, 1, 1)  
        self.label_tag = QtWidgets.QLabel(self.groupbox)
        self.label_tag.setObjectName('label_tag')
        self.label_tag.setText('Tag')
        self.label_tag.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_tag, 3, 0, 1, 1)
        self.combobox_tag = QtWidgets.QComboBox(self.groupbox)
        self.combobox_tag.setObjectName('combobox_tag')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setEnabled(True)
        self.combobox_tag.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combobox_tag.addItems(self.pub.valid_modes[self.mode]['tag'])         
        self.gridlayout.addWidget(self.combobox_tag, 3, 1, 1, 1)          
        self.label_thumbnail = QtWidgets.QLabel(self.groupbox)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_thumbnail, 4, 0, 1, 1)
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox)
        self.button_thumbnail.setObjectName('button_thumbnail')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        thumbnail_icon = os.path.join(resource.getIconPath(), 'screenshot.png')
        widgets.image_to_button(
            self.button_thumbnail, 256, 180, path=thumbnail_icon)          
        self.button_thumbnail.clicked.connect(partial(self.take_thumbnail, self.button_thumbnail))
        self.gridlayout.addWidget(self.button_thumbnail, 4, 1, 1, 1)  
        self.label_description = QtWidgets.QLabel(self.groupbox)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.label_description.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_description, 5, 0, 1, 1)
        self.textedit_description = QtWidgets.QTextEdit(self.groupbox)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 90))          
        self.gridlayout.addWidget(self.textedit_description, 5, 1, 1, 1)  
        self.label_version = QtWidgets.QLabel(self.groupbox)
        self.label_version.setObjectName('label_version')
        self.label_version.setText('version')
        self.label_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_version, 6, 0, 1, 1)
        self.combobox_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_version.setObjectName('combobox_version')
        self.combobox_version.setEditable(True)
        self.combobox_version.setEnabled(True)
        self.combobox_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combobox_version.addItems(['major', 'minor', 'patch'])        
        self.gridlayout.addWidget(self.combobox_version, 6, 1, 1, 1)                  
        self.label_latest_version = QtWidgets.QLabel(self.groupbox)
        self.label_latest_version.setObjectName('label_latest_version')
        self.label_latest_version.setText('Latest Version')
        self.label_latest_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_latest_version, 7, 0, 1, 1)
        self.combobox_latest_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_latest_version.setObjectName('combobox_latest_version')
        self.combobox_latest_version.setEditable(True)
        self.combobox_latest_version.setEnabled(False)
        self.combobox_latest_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_latest_version, 7, 1, 1, 1)
        self.label_next_version = QtWidgets.QLabel(self.groupbox)
        self.label_next_version.setObjectName('label_next_version')
        self.label_next_version.setText('Caption')
        self.label_next_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_next_version, 8, 0, 1, 1)
        self.combobox_next_version = QtWidgets.QComboBox(self.groupbox)
        self.combobox_next_version.setObjectName('combobox_next_version')
        self.combobox_next_version.setEditable(True)
        self.combobox_next_version.setEnabled(False)
        self.combobox_next_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_next_version, 8, 1, 1, 1)  
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
        self.button_publish.clicked.connect(self.publish)        
        self.button_cancel.clicked.connect(self.close)  
        self.combobox_caption.editTextChanged.connect(self.set_current_version)
        self.combobox_subfield.currentIndexChanged.connect(self.set_current_version)
        self.combobox_version.currentIndexChanged.connect(self.set_current_version)
        
    def set_tool_context(self):
        config = configure.Configure()
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
        pub_data = self.pub.get()
        captions = [''] + pub_data.keys()
        self.combobox_caption.clear() 
        self.combobox_caption.addItems(captions)         
        
    def take_thumbnail(self, button):
        smaya = studioMaya.Maya()
        output_path, w, h = smaya.vieport_snapshot(
            output_path=None,
            width=768,
            height=768,
            )
        qsize = button.minimumSize()
        widgets.image_to_button(
            button,
            qsize.width(),
            qsize.height(),
            path=output_path
            )        
        self.button_thumbnail.setToolTip(output_path)

    def set_current_version(self):
        caption = self.combobox_caption.currentText()
        subfield = self.combobox_subfield.currentText()
        semantic_version = self.combobox_version.currentIndex()
        self.combobox_latest_version.clear() 
        self.combobox_next_version.clear()        
        versions = self.pub.get_versions(caption, subfield)
        if not versions:
            versions = [None]
        self.combobox_latest_version.addItems(versions)
        next_version = self.pub.get_next_version(versions[0], semantic_version)
        self.combobox_next_version.addItem(next_version)

    def get_widget_data(self):
        widgets = {
            'caption': self.combobox_caption,
            'subfield': self.combobox_subfield,
            'type': self.combobox_type,
            'tag': self.combobox_tag,
            'thumbnail': self.button_thumbnail,
            'description': self.textedit_description,
            'version': self.combobox_next_version       
            }
        widget_data = {}        
        for key, widget in widgets.items():
            widget_value = None
            if isinstance(widget, QtWidgets.QComboBox):
                widget_value = widget.currentText().encode()
            if isinstance(widget, QtWidgets.QTextEdit):
                widget_value = widget.toPlainText().encode()
            if isinstance(widget, QtWidgets.QPushButton):
                print widget.objectName()
                widget_value = widget.toolTip().encode()
                print 'widget_value', widget_value
            if not widget_value:
                widget_value = None
            widget_data.setdefault(key, widget_value)
        return widget_data      
            
    def publish(self):
        widget_data = self.get_widget_data()
        if None in widget_data.values():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty inputs!...', QtWidgets.QMessageBox.Ok)
            return          
        self.pub.bundle = copy.deepcopy(widget_data)
        self.pub.bundle['source_file'] = self.current_file
        print '\n#inputs\t'
        print json.dumps(self.pub.bundle, indent=4)
        self.pub.pack()   
        self.pub.release()
        self.set_current()       
        self.set_current_version()
        QtWidgets.QMessageBox.information(
            self, 'Success', 'Done!...', QtWidgets.QMessageBox.Ok)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())        
