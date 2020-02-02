import os
import sys
import ast
import json
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resources
from studio_usd_pipe.core import __inputs
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import subshell
from studio_usd_pipe.api import studioPublish
from studio_usd_pipe.resources.ui import publish


class Connect(publish.Window):

    def __init__(self, parent, standalone=True):
        super(Connect, self).__init__(parent)
        self.standalone = standalone
        self.formats = {
            '.ma': 'Maya Ascii',
            '.mb': 'Maya Binary'
        }
        self.brows_directory = self.input_dirname['shows_directory']
        self.category = 'asset'
        self.publish = studioPublish.Publish(self.category)

        self.modify_widgets()

        self.button_open.clicked.connect(
            partial(self.find_source_file, self.label_source))
        self.button_thumbnail.clicked.connect(
            partial(self.find_caption_image, self.button_thumbnail))
        self.combobox_caption.editTextChanged.connect(self.load_caption)
        self.combobox_subfield.currentIndexChanged.connect(self.load_subfield)

        self.combobox_versions.currentIndexChanged.connect(self.load_version)
        self.button_publish.clicked.connect(self.start_publish)

    def modify_widgets(self):
        captions = ['None'] + self.publish.get_captions()
        self.combobox_caption.addItems(captions)
        widget_inputs = {
            'subfield': self.combobox_subfield,
            'type': self.combobox_type,
            'tag': self.combobox_tag
        }
        for k, widget in widget_inputs.items():
            input = __inputs.Connect(k)
            input.get(self.category)
            widget.addItems(input.keys)
        self.set_version()

    def clear_version_widgets(self):
        self.combobox_nextversion.clear()
        self.combobox_nextversion.clearEditText()
        self.combobox_latestversion.clear()
        self.combobox_latestversion.clearEditText()

    def load_caption(self, *args):
        self.set_version()

    def load_subfield(self, *args):
        self.set_version()

    def load_version(self, *args):
        caption = self.combobox_caption.currentText()
        if caption == 'None' or not caption:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any caption!...', QtWidgets.QMessageBox.Ok
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
        current_link = QtWidgets.QFileDialog.getOpenFileName(
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
        self.load_scene_nodes(self.combobox_dagpath, current_link[0])
        print os.path.splitext(current_link[0])

    def load_scene_nodes(self, combobox, source_file):
        nodes = None
        if self.standalone:
            result = subshell.sub_process(
                self.publish.mayapy_path,
                resources.getScriptSourceScripts('read_scene_dagpth'),
                args=[source_file.encode()]
            )
            print result
            nodes = ast.literal_eval(result[-1])
        else:
            from studio_usd_pipe.core import smaya
            nodes = smaya.get_scene_nodes()

        combobox.clear()
        combobox.clearEditText()
        combobox.addItems(nodes)
        for index in range(combobox.count()):
            if combobox.itemText(index) != self.publish.node:
                continue
            combobox.setCurrentIndex(index)
            break
        return nodes

    def find_caption_image(self, widget):
        self.brows_directory = '/mnt/bkp/reference'
        current_format = 'image {}'.format(resources.getImageFormats())
        current_link = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Browse your source file', self.brows_directory, current_format)
        if not current_link[0]:
            print 'abort!...'
            return
        widgets.image_to_button(widget, 256, 180, path=current_link[0])
        widget.setToolTip(current_link[0])
        widget.setStatusTip(current_link[0])

    def collect_publish_data(self):
        input_dict = {
            'dagpath': self.combobox_dagpath,
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
            if not v:
                input_data.setdefault(k, None)
            if isinstance(v, str):
                input_data.setdefault(k, v)
            current_value = None
            if isinstance(v, QtWidgets.QComboBox):
                current_value = v.currentText()
            if isinstance(v, QtWidgets.QLabel):
                current_value = v.toolTip()
            if isinstance(v, QtWidgets.QLabel):
                current_value = v.toolTip()
            if isinstance(v, QtWidgets.QPushButton):
                current_value = v.statusTip()
            if isinstance(v, QtWidgets.QTextEdit):
                current_value = v.toPlainText()
            if not current_value:
                input_data.setdefault(k, None)
            else:
                input_data.setdefault(k, current_value)

        return input_data

    def start_publish(self, **kwargs):
        input_data = self.collect_publish_data()

        valid_keys = [
            input_data['dagpath'],
            input_data['caption'],
            input_data['version'],
            input_data['source_file']
        ]
        if None in valid_keys:
            QtWidgets.QMessageBox.critical(
                self, 'Critical', 'In valid __inputs.', QtWidgets.QMessageBox.Ok
            )
            return

        publish = studioPublish.Publish(
            self.category, standalone=self.standalone)
        
        
        return
    
    
    
    
        release_data = publish.pack(input_data)

        return

        publish.release(data=release_data)

        message = '{}{}\n{}{}\n{}{}\n{}{}\n{}{}'.format(
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

        QtWidgets.QMessageBox.information(
            self,
            'Information',
            '{}\n\nPublish Success!...'.format(message),
            QtWidgets.QMessageBox.Ok
        )
        self.set_version()
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
