import os
import sys
import json
import warnings

from PySide import QtCore
from PySide import QtGui
from functools import partial
from distutils import version
from pprint import pprint

from studio_usd_pipe import resources
from studio_usd_pipe.core import inputs
from studio_usd_pipe.core import widgets
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.api import studioPublish
# from studio_usd_pipe.api import studioAsset
from studio_usd_pipe.resources.ui import publish_ui


class Connect(publish_ui.Window):

    def __init__(self, parent, standalone=True):
        super(Connect, self).__init__(parent)
        self.standalone = standalone
        self.formats = {
            '.ma': 'Maya Ascii',
            '.mb': 'Maya Binary'
        }
        self.brows_directory = self.input_dirname['shows_directory']
        self.category = 'asset'        

        self.modify_widgets()

        self.button_open.clicked.connect(partial(self.find_source_file, self.label_source))
        self.button_thumbnail.clicked.connect(partial(self.find_caption_image, self.button_thumbnail))
        self.combobox_caption.editTextChanged.connect(self.load_caption)
        self.combobox_publishtype.currentIndexChanged.connect(self.load_publishtype)
        self.combobox_versions.currentIndexChanged.connect(self.load_version)
        self.button_publish.clicked.connect(self.start_publish)

    def modify_widgets(self):
        publish = studioPublish.Publish(self.category)
        captions = ['None'] + publish.get_captions()
        self.combobox_caption.addItems(captions)
        widget_inputs = {
            'subfield': self.combobox_subfield,
            'type': self.combobox_type,
            'tag': self.combobox_tag
        }
        for k, widget in widget_inputs.items():
            input = inputs.Connect(k)
            input.get(self.category)
            widget.addItems(input.keys)            
        self.set_version()
        
    def clear_version_widgets(self):
        self.combobox_nextversion.clear()
        self.combobox_nextversion.clearEditText ()
        self.combobox_latestversion.clear()
        self.combobox_latestversion.clearEditText ()          

    def has_caption_valiadte(self):
        caption = self.combobox_caption.currentText()
        if not caption:            
            if self.combobox_publishtype.currentIndex()==0:
                return            
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any caption!...', QtGui.QMessageBox.Ok
                )
            self.combobox_publishtype.setCurrentIndex(0)
            self.combobox_versions.setCurrentIndex(0)
            self.clear_version_widgets()
            return
        return True
    
    def load_caption(self, *args):
        self.set_version()        

    def load_publishtype(self, *args):        
        valid = self.has_caption_valiadte()
        if not valid:
            return
        self.combobox_versions.clear()
        if args[0] == 0:
            self.combobox_versions.addItems(self.sem_versions)
            self.combobox_versions.setEnabled(True)
        if args[0] == 1:
            self.combobox_versions.addItem('None')
            self.combobox_versions.setEnabled(False)

    def load_version(self, *args):
        valid = self.has_caption_valiadte()
        if not valid:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any caption!...', QtGui.QMessageBox.Ok
                )            
            self.clear_version_widgets()
            return        
        self.set_version(index=args[0])

    def set_version(self, caption=None, subfield=None, tag=None, index=None):
        if not caption:
            caption = self.combobox_caption.currentText()
        if not subfield:
            subfield = self.combobox_subfield.currentText()
        if not tag:
            tag = self.combobox_tag.currentText()
        if not index:
            index = self.combobox_versions.currentIndex()
        if not caption:
            self.clear_version_widgets()
            return
        publish = studioPublish.Publish(self.category)
        latest_version = publish.get_latest_version(caption, subfield, tag)
        next_version = publish.get_next_version(index, caption, subfield, tag)
        self.clear_version_widgets()        
        self.combobox_nextversion.addItem(next_version)
        self.combobox_latestversion.addItem(latest_version)

    def find_source_file(self, widget):
        current_format = 'image {}'.format(resources.getMayaFormats())
        current_link = QtGui.QFileDialog.getOpenFileName(
            self, 'Browse your source file', self.brows_directory, current_format)
        if not current_link[0]:
            print 'abort!...'
            return
        name, format = os.path.splitext(os.path.basename(current_link[0]))
        if format in self.formats:
            current_format = self.formats[format]
        else:
            current_format = 'unknown'
        widget.setText('\"{}\"\n< {} >'.format(name, current_format))
        widget.setToolTip(current_link[0])
        self.brows_directory = os.path.dirname(current_link[0])
        print os.path.splitext(current_link[0])

    def find_caption_image(self, widget):
        self.brows_directory = '/mnt/bkp/reference'
        current_format = 'image {}'.format(resources.getImageFormats())
        current_link = QtGui.QFileDialog.getOpenFileName(
            self, 'Browse your source file', self.brows_directory, current_format)
        if not current_link[0]:
            print 'abort!...'
            return
        widgets.image_to_button(widget, 256, 180, path=current_link[0])
        widget.setToolTip(current_link[0])
        widget.setStatusTip(current_link[0])
        
    def collect_publish_data(self):        
        input_dict = {
            'category': self.category,
            'caption': self.combobox_caption,
            'subfield': self.combobox_subfield,
            'type': self.combobox_type,
            'tag': self.combobox_tag,
            'version': self.combobox_nextversion,
            'source_file': self.label_source,
            'thumbnail': self.button_thumbnail,
            'description': self.textedit_description
            }
        
        input_data = {}
        
        for k, v in input_dict.items():
            if not v :
                input_data.setdefault(k, None)                     
            if isinstance(v, str):
                input_data.setdefault(k, v)                
            current_value = None                
            if isinstance(v, QtGui.QComboBox):
                current_value = v.currentText()                
            if isinstance(v, QtGui.QLabel):
                current_value = v.toolTip()      
            if isinstance(v, QtGui.QLabel):
                current_value = v.toolTip()
            if isinstance(v, QtGui.QPushButton):
                current_value = v.statusTip()
            if isinstance(v, QtGui.QTextEdit):
                current_value = v.toPlainText()                     
            if not current_value:
                input_data.setdefault(k, None)
            else:
                input_data.setdefault(k, current_value)

        return input_data

    def start_publish(self, **kwargs):
        input_data = self.collect_publish_data()
        
        valid_keys = [
            input_data['caption'],
            input_data['version'],
            input_data['source_file']
            ]
        if None in valid_keys:            
            QtGui.QMessageBox.critical(
                self, 'Critical', 'In valid inputs.', QtGui.QMessageBox.Ok
                )
            return
        
        publish = studioPublish.Publish(
            input_data['category'], standalone=self.standalone)
        release_data = publish.pack(input_data)
        
        return
        
        publish.release(data=release_data)

        message = '{}{}\n{}{}\n{}{}\n{}\n{}{}\n{}{}'.format(
            'category:\t',
            input_data['category'],            
            'tag:\t',
            input_data['tag'],            
            'subfield:\t',
            input_data['subfield'],            
            'type:\t',
            input_data['type'],            
            'caption:\t',             
            input_data['caption'],
            'version:\t',
            input_data['version'],
        )

        QtGui.QMessageBox.information(
            self,
            'Information',
            '{}\n\nPublish Success!...'.format(message),
            QtGui.QMessageBox.Ok
        )
        return True
    
    
    
    
    
    
    
    
            
        
        
        
        
        
        
        
        

    def add_caption(self, category):
        publish = studioPublish.Publish(category)
        captions = publish.get_caption()
        for caption, contents in captions.items():
            input_data = {
                'display': caption,
                'statustip': caption,
                'tooltip': 'published caption name',
                'whatsthis': contents['tag'],
                'icon': os.path.join(contents['tag'], '{}.png'.format(caption)),
            }

            print json.dumps(contents, indent=4)
            # item = widgets.add_treewidget(parent, input_data)



    def load_current(self, *args):
        treewidget = args[0].treeWidget()
        caption = args[0].statusTip(0)
        tag = args[0].whatsThis(0)
        category = self.get_category(args[0])

        self.combobox_subfield.clear()
        self.combobox_tag.clear()

        input = inputs.Connect('subfield')
        input.get(category)
        self.combobox_subfield.addItems(input.keys)
        self.combobox_subfield.setToolTip(
            '{} < {} >'.format(category, caption))
        input = inputs.Connect('tag')
        input.get(category)
        self.combobox_tag.addItems(input.keys)
        self.combobox_tag.setToolTip('{} < {} >'.format(category, caption))
        if tag in input.keys:
            self.combobox_tag.setCurrentIndex(input.keys.index(tag))
        self.set_version(category, tag, caption)

    def _load_version(self, treewidget, *args):
        if not treewidget.selectedItems():
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Not found any selection\nSelect the item and try',
                QtGui.QMessageBox.Ok
            )
            return
        current_item = treewidget.selectedItems()[-1]
        category = self.get_category(current_item)
        tag = current_item.whatsThis(0)
        caption = current_item.statusTip(0)
        self.set_version(category, tag, caption)

    def _set_version(self, category, tag, caption):
        subfield = self.combobox_subfield.currentText()
        version_index = self.combobox_version.currentIndex()
        publish = studioPublish.Publish(category)
        latest_version = publish.get_latest_version(tag, caption, subfield)
        next_version = publish.get_next_version(
            version_index, tag, caption, subfield)
        self.label_current_version.setText(next_version)
        self.label_latest_version.setText(
            'Latest Version ({})'.format(latest_version))

    def add(self, treewidget):
        if not treewidget.selectedItems():
            warnings.warn(
                'Not found any selection\nSelect the item and try', Warning)
            return
        parent_item = treewidget.selectedItems()[-1]
        if treewidget.selectedItems()[-1].parent():
            parent_item = treewidget.selectedItems()[-1].parent()
        caption, ok = QtGui.QInputDialog.getText(
            self, 'Input', 'Enter the name:', QtGui.QLineEdit.Normal)
        if not ok:
            warnings.warn('abort the add!...', Warning)
            return
        input_data = {
            'display': caption,
            'statustip': caption,
            'tooltip': 'un published caption name',
            'whatsthis': 'unknown',
            'icon': os.path.join(self.icon_path, 'unknown.png'),
        }
        widgets.add_treewidget(parent_item, input_data)
        treewidget.setItemExpanded(treewidget.selectedItems()[-1], 1)

    def remove(self, treewidget):
        if not treewidget.selectedItems():
            warnings.warn(
                'Not found any selection\nSelect the item and try', Warning)
            return
        items = treewidget.selectedItems()
        for item in items:
            if item.whatsThis(0) != 'unknown':
                continue
            item.removeChild(item)

    def reload(self, treewidget):
        pass

 


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
