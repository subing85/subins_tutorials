'''
preferences.py 0.0.1 
Date: January 15, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

# add icon to disciplines

import sys
import os

from pprint import pprint

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime


from studioPipe import resources
from studioPipe.api import studioConnect

from studioPipe.core import studioImage

from studioPipe.utils import platforms



class Window(QtGui.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent)
        
        self.current_show = None
        if 'show' in kwargs:
            self.current_show = kwargs['show']
        self.type = kwargs['type']
        self.value = kwargs['value']
        self.title = kwargs['title']
        self.label = kwargs['label']
        
        self.width = kwargs['width']
        self.height = kwargs['height'] 
        
        self.brows_directory = resources.getWorkspacePath()
        self.brows_directory = '/mnt/bkp/Icons gallery/icons_04'   
        
        self.q_image, self.q_image_path = None, None
        
        # current input file
        self.file_path = os.path.join(resources.getInputPath(), '%s.json'%self.type)
        
        print 'db path', self.file_path
        
        self.connect = studioConnect.Connect(self.file_path, value=self.value)        
        self.data, self.sort_data, self.all_input_data = self.connect.getInputData()
        
        self.module, self.lable, self.version = platforms.get_tool_kit()
        

        self.setup_ui()
        self.load_widgets()

    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            '{} ({} {})'.format(self.title, self.lable, self.version))
        self.resize(self.width, self.height)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle(self.label)
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.verticallayout_item.addLayout(self.horizontalLayout)
        self.label_logo = QtGui.QLabel(self.groupbox)
        self.label_logo.setObjectName('label_subins_toolkits')
        self.label_logo.setPixmap(QtGui.QPixmap(
            os.path.join(resources.getIconPath(), 'subins_toolkits_1.png')))
        self.label_logo.setScaledContents(True)
        self.label_logo.setMinimumSize(QtCore.QSize(128, 128))
        self.label_logo.setMaximumSize(QtCore.QSize(128, 128))
        self.horizontalLayout.addWidget(self.label_logo)        
        
        self.button_show = QtGui.QPushButton(self.groupbox)
        self.button_show.setFlat(True)
        self.button_show.setSizePolicy(
            QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred))
        self.button_show.setObjectName('button_show')
        self.button_show.setMinimumSize(QtCore.QSize(256, 144))
        self.button_show.setMaximumSize(QtCore.QSize(256, 144))
        self.horizontalLayout.addWidget(self.button_show)
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)
                    
        self.gridlayout = QtGui.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)
        spacer_item = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(10, 10, 10, 10)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_create = QtGui.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout.addWidget(self.button_create)
        self.button_cancel.clicked.connect(self.close)

        
    def load_widgets(self):
        for index in range (len(self.sort_data)):
            current_item = self.data[self.sort_data[index]]
            
            label = QtGui.QLabel(self.groupbox)
            label.setObjectName('label_%s' % self.sort_data[index])
            label.setText(current_item['display_name'])
            label.setStatusTip(current_item['tooltip'])
            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.gridlayout.addWidget(label, index, 0, 1, 1)
            
            widget = None
            if current_item['type']=='str' or current_item['type']=='path' or current_item['type']=='directory':
                widget = QtGui.QLineEdit(self.groupbox)
                widget.setObjectName('lineedit_%s' % self.sort_data[index])
                widget.setText(current_item['value'])
                widget.setEnabled(current_item['enable'])

            elif current_item['type']=='enum':
                widget = QtGui.QComboBox(self.groupbox)
                widget.setObjectName('combobox_%s' % self.sort_data[index])
                if current_item['values']:
                    widget.addItems(current_item['values'])
                    widget.setCurrentIndex(current_item['value'])
                    
            elif current_item['type']=='add':     
                widget = QtGui.QPushButton(self.groupbox)
                widget.setObjectName('button_add_%s'%self.sort_data[index])
                widget.setText(u'\u002B')
                widget.setStyleSheet('color: #0000FF;')
                widget.setMinimumSize(QtCore.QSize(20, 20))
                widget.setMaximumSize(QtCore.QSize(20, 20))
                                
                #===============================================================
                # self.gridLayout.addWidget(self.pushButton_l_add, 2, 0, 1, 1)
                # self.gridLayout.addWidget(self.pushButton_add, 2, 1, 1, 1)
                # self.gridLayout.addWidget(self.lineEdit_add, 2, 2, 1, 1)
                #===============================================================
                
            if current_item['type']=='path' or current_item['type']=='directory':
                button_find = QtGui.QPushButton(self.groupbox)
                button_find.setObjectName('button_find_%s'%self.sort_data[index])
                button_find.setText('...')
                button_find.setStyleSheet('color: #0000FF;')
                button_find.setMinimumSize(QtCore.QSize(35, 25))
                button_find.setMaximumSize(QtCore.QSize(35, 25))
                resolution = [256, 256]
                if 'resolution' in current_item:
                    resolution = current_item['resolution']
                button_find.clicked.connect(
                    partial(self.find_paths, widget, current_item['type'], resolution, current_item['description']))
          
                self.gridlayout.addWidget(button_find, index, 2, 1, 1)
                
            if current_item['example']:
                 widget.setToolTip('\n'.join(current_item['example']))
            
            if not widget:
                continue
            widget.setStatusTip(self.sort_data[index])
            self.gridlayout.addWidget(widget, index, 1, 1, 2)            

    def find_paths(self, widget, types, resolution=None, title=None):
        if types=='path':
            current_format = 'image {}'.format(resources.getImageFormats())
            current_link = QtGui.QFileDialog.getOpenFileName(
                self, title, self.brows_directory, current_format)
        if types=='directory':
            current_link = [QtGui.QFileDialog.getExistingDirectory(
                self, 'Browser', self.brows_directory)]
            self.brows_directory = current_link[0]
        if not os.path.exists(current_link[0]):
            return False, None
        widget.setText(current_link[0])
        
        print types
        print resolution
        if types=='path' and resolution:        
            self.snapshot(self.button_show, current_link[0], resolution)
        
        print self.size()


    def snapshot(self, button, image_file, resolution):
        self.studio_image = studioImage.ImageCalibration(imgae_file=image_file)
        self.q_image, self.q_image_path = self.studio_image.set_studio_size(
            width=resolution[0], height=resolution[1])
        if not self.q_image:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not able to process image!..', QtGui.QMessageBox.Ok)
            return
        self.image_to_button(button, self.q_image_path, resolution[0], resolution[1])
        return self.q_image, self.q_image_path
    
    def image_to_button(self, button=None, path=None, width=None, height=None):
        if not button:
            button = self.button_snapshot
        if not path:
            path = os.path.join(resources.getIconPath(), 'template.png')
        if not width:
            width = self.width
        if not height:
            height = self.height
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(width - 5, height- 5))

    def _get_widget_data(self, layout):
        data = {}
        ing = 0
        for index in range(layout.rowCount()):
            if not layout.itemAtPosition(index, 1):
                continue
            widget = layout.itemAtPosition(index, 1).widget()
            if isinstance(widget, QtGui.QComboBox):
                value = widget.currentIndex()
            else:
                value = widget.text().encode()
            tag = widget.statusTip()
            values = {
                'widget': widget,
                'value': value
                }
            data.setdefault(tag.encode(), values)
        return data 
       
    def get_widget_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):            
            widget = None
            for column in range(2, layout.columnCount()):
                if not layout.itemAtPosition(row, column):
                    continue     
                widget = layout.itemAtPosition(row, column).widget()
            if not widget:
                continue
            if isinstance(widget, QtGui.QComboBox):
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
        return data 
    
    def get_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            widget = None
            for column in range(2, layout.columnCount()):
                if not layout.itemAtPosition(row, column):
                    continue     
                widget = layout.itemAtPosition(row, column).widget()
            if not widget:
                continue
            if isinstance(widget, QtGui.QComboBox):
                if not widget.isEditable():
                    value = widget.currentIndex()
                else:
                    value = widget.currentText().encode()
            else:
                value = widget.text().encode()
            data.setdefault(widget.statusTip().encode(), value)
        return data  

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #window = Window(parent=None, show='tom', type='discipline', value='discipline_child_inputs', 
    #                title=None, label=None, width=500, height=100)
    #window = Window(parent=None, type='preferences', value=None, title=None, label=None, width=800, height=300)
    window = Window(parent=None, type='shows', value=None, title='Show Inputs', label='Create your Show', width=500, height=300)
     
    window.show()
    sys.exit(app.exec_())
