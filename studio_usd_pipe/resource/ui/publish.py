import os
import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import preference
from studio_usd_pipe.api import studioMaya
from studio_usd_pipe.api import studioPublish
from studio_usd_pipe.resource.ui import inputs
reload(studioPublish)
reload(inputs)
reload(studioMaya)

from pprint import pprint

class Window(inputs.Window):

    def __init__(self, parent=None, **kwargs):  
        super(Window, self).__init__(parent, **kwargs)
        # self.setParent(parent)
        self.pub = studioPublish.Publish(self.mode)
        self.pref = preference.Preference()
        self.set_current()
        self.update_ui()     
        
    def update_ui(self):
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout)
        
        studio_maya = studioMaya.Maya()
        current_file, file_type = studio_maya.get_current_file()
        
        source_file = 'Current File: {}\nFile Type: {}'.format(current_file, file_type)
        self.label_source = QtWidgets.QLabel()
        self.label_source.setObjectName('label_source')
        self.label_source.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_source.setStyleSheet('font: 12pt;')
        self.label_source.setText(source_file)
        self.label_source.setToolTip(file_type)
        self.horizontallayout_input.addWidget(self.label_source)        
        
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_publish = QtWidgets.QPushButton(self)
        self.button_publish.setObjectName('button_create')
        self.button_publish.setText('Publish')
        self.horizontallayout.addWidget(self.button_publish)
        self.button_publish.clicked.connect(self.publish)        
        self.button_cancel.clicked.connect(self.close)  
        
        
    def set_current(self, bundle_data=None): 
        data = self.get_widget_data(self.gridlayout)
        self.get_widgets(data) 

        if not bundle_data:
            bundle_data = self.pref.get()

        qsize = self.show_widget.minimumSize()            
        widgets.image_to_button(
            self.show_widget,
            qsize.width(),
            qsize.height(),
            path=bundle_data['show_icon']
            )

        
        pub_data = self.pub.get()
        
        captions = [''] + pub_data.keys()
        self.caption_widget.addItems(captions)
        self.subfield_widget.addItems(self.pub.valid_modes[self.mode]['subfield'])
        self.type_widget.addItems(self.pub.valid_modes[self.mode]['type'])
        self.tag_widget.addItems(self.pub.valid_modes[self.mode]['tag']) 
        self.version_widget.addItems(['major', 'minor', 'patch'])
       
        # self.latest_version_widget.addItem('0.0.0')
        # self.next_version_widget.addItem('0.0.0')   
           
        thumbnail_icon = os.path.join(resource.getIconPath(), 'screenshot.png')
        unknown_image = os.path.join(resource.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.thumbnail_widget, 256, 180, path=thumbnail_icon)           
        # self.thumbnail_widget.setToolTip(unknown_image)       
        self.thumbnail_widget.clicked.connect(partial(self.take_thumbnail, self.thumbnail_widget))
        # self.caption_widget.currentIndexChanged.connect(self.set_current_version)
        self.caption_widget.editTextChanged.connect(self.set_current_version)
        self.subfield_widget.currentIndexChanged.connect(self.set_current_version)
        self.version_widget.currentIndexChanged.connect(self.set_current_version)
            
    def get_widgets(self, data):
        self.show_widget = data['icon']['widget']
        self.subfield_widget = data['subfield']['widget']
        self.caption_widget = data['caption']['widget']
        self.type_widget = data['type']['widget']
        self.tag_widget = data['tag']['widget']
        self.thumbnail_widget = data['thumbnail']['widget']
        self.description_widget = data['description']['widget']
        self.version_widget = data['version']['widget']
        self.latest_version_widget = data['latest_version']['widget']
        self.next_version_widget = data['next_version']['widget'] 
        
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
        self.thumbnail_widget.setToolTip(output_path)
                
            
    def set_current_version(self):
        caption = self.caption_widget.currentText()
        subfield = self.subfield_widget.currentText()
        semantic_version =  self.version_widget.currentIndex()
        
        self.latest_version_widget.clear() 
        self.next_version_widget.clear()        

        versions = self.pub.get_versions(caption, subfield)
        if not versions:
            versions = [None]
        
        self.latest_version_widget.addItems(versions)
        next_version = self.pub.get_next_version(versions[0], semantic_version)
        self.next_version_widget.addItem(next_version)
            
            
    def publish(self):
        data = self.get_widget_data(self.gridlayout)
        keys = self.pub.valid_publish_keys[self.mode]

        self.pub.bundle = {
            'subfield': data['subfield']['value'],
            'type': data['type']['value'],
            'tag': data['tag']['value'],
            'caption': data['caption']['value'],
            'version': data['next_version']['value'],
            'thumbnail': data['thumbnail']['value'],     
            'description': data['description']['value'],
            'source_file': '/venture/shows/my_hero/dumps/batman_finB.ma'
            }
        self.pub.pack()   
        self.pub.release()
        self.set_current_version()
        
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(
        parent=None,
        type='asset',
        value=None,
        title='Asset Publish',
        width=570,
        height=314
    )
    window.show()
    sys.exit(app.exec_())        
