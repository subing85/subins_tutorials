import json

import os
import sys
import tempfile

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import configure
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import image


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent)           
        self.type = kwargs['type']
        self.value = kwargs['value']
        self.title = kwargs['title']
        self.width = kwargs['width']
        self.height = kwargs['height']        
        self.version, self.label = self.set_tool_context()               
        self.brows_directory = resource.getWorkspacePath()        
        self.brows_directory = '/local/references/images/'        
        self.setup_ui()
        self.modify_widgets(self.gridlayout)
        
    def setup_ui(self):
        self.setObjectName('widget_{}'.format(self.type))
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version))
        self.resize(self.width, self.height)        
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle(self.label)  
        self.verticallayout.addWidget(self.groupbox)        
        self.verticallayout_item = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.verticallayout_item.addLayout(self.horizontalLayout)        
        self.button_logo, self.button_show = widgets.set_header(
            self.horizontalLayout, show_icon=None)        
        self.gridlayout = QtWidgets.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)        
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)

    def set_tool_context(self):
        config = configure.Configure()
        config.tool()
        return config.version, config.pretty 
    
    def get_input_data (self):  
        input_path = os.path.join(
            resource.getInputPath(), '{}.json'.format(self.type))       
        input_data = resource.get_input_data(input_path)
        return input_data
        
    def modify_widgets(self, layout):
        input_data = self.get_input_data()
        order_data = self.sort_dictionary(input_data)
        for index, each in enumerate(order_data):
            content = input_data[each]
            if not content['enable']:
                continue
            if content['type'] == 'path':
                self.make_path(each, index, layout, content)
            if content['type'] == 'directory':
                self.make_directory(each, index, layout, content)                
                
    def make_path(self, name, index, layout, content):        
        lineedit, button = self.make_location(name, index, layout, content)
        display = False
        if name == 'show_icon':
            display = True       
        button.clicked.connect(partial(self.find_path, lineedit, content, display=display))
        
    def make_directory(self, name, index, layout, content):
        lineedit, button = self.make_location(name, index, layout, content)
        button.clicked.connect(partial(self.find_directory, lineedit, content))
    
    def make_location(self, name, index, layout, content):
        label = QtWidgets.QLabel(self.groupbox)
        label.setObjectName('label_%s' % name)
        label.setText(content['display'])
        label.setStatusTip(content['tooltip'])
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        layout.addWidget(label, index, 0, 1, 1)
        lineedit = QtWidgets.QLineEdit(self.groupbox)
        lineedit.setObjectName('lineedit_%s' % name)
        if 'value' in content:
            lineedit.setText(content['value'])
        lineedit.setStatusTip(name)        
        layout.addWidget(lineedit, index, 1, 1, 1)   
        button = QtWidgets.QPushButton(self.groupbox)
        button.setObjectName('button_%s' % name)
        button.setText('...')
        button.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        button.setMinimumSize(QtCore.QSize(25, 25))
        button.setMaximumSize(QtCore.QSize(25, 25))      
        layout.addWidget(button, index, 2, 1, 1)
        return lineedit, button   
                
    def find_path(self, widget, content, display=False):    
        current_link = QtWidgets.QFileDialog.getOpenFileName(
            self, content['description'], self.brows_directory, content['format'])
        self.brows_directory = os.path.dirname(current_link[0])
        widget.setText(current_link[0])
        if display:
            qsize = self.button_show.minimumSize()
            resolution = [qsize.width(), qsize.height()]
            self.snapshot(self.button_show, current_link[0], resolution)

    def find_directory(self, widget, content):    
        current_link = QtWidgets.QFileDialog.getExistingDirectory(
            self, content['description'], self.brows_directory)
        self.brows_directory = current_link
        widget.setText(current_link)  

    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order
    
    def get_widget_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            widget = layout.itemAtPosition(row, 1).widget()
            if not widget:
                continue
            if isinstance(widget, QtWidgets.QComboBox):
                if not widget.isEditable():
                    value = widget.currentIndex()
                else:
                    value = widget.currentText().encode()
            else:
                value = widget.text().encode()
            values = {
                'widget': widget,
                'value': value
                }
            data.setdefault(widget.statusTip().encode(), values)
        data.setdefault('icon', {'widget': self.button_show, 'value': None})
        return data
       
    def get_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            widget = layout.itemAtPosition(row, 1).widget()
            if not widget:
                continue
            if isinstance(widget, QtWidgets.QPushButton):
                continue
            if isinstance(widget, QtWidgets.QComboBox):
                if not widget.isEditable():
                    value = widget.currentIndex()
                else:
                    value = widget.currentText().encode()
            else:
                value = widget.text().encode()
            data.setdefault(widget.statusTip().encode(), value)
        return data   

    def snapshot(self, button, image_file, resolution):
        output_path = os.path.join(
            tempfile.gettempdir(), 'studio_image_snapshot.png')
        q_image_path = image.image_resize(
            image_file,
            output_path,
            resolution[0],
            resolution[1],
            )  
        if not q_image_path:
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not able to process image!..',
                QtWidgets.QMessageBox.Ok
                )
            return
        widgets.image_to_button(
            button, resolution[0], resolution[1], path=q_image_path)
        button.setStatusTip(q_image_path)
        return q_image_path

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(
        parent=None,
        type='preferences',
        value=None,
        title='Show Inputs',
        width=572,
        height=155
    )
    window.show()
    sys.exit(app.exec_())
        
