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

from pprint import pprint

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime


from studioPipe import resources
from studioPipe.core import readWrite
from studioPipe.utils import platforms
from studioPipe.api import studioInput

reload(studioInput)

class Window(QtGui.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent)
        
        self.type = kwargs['type']
        self.value = kwargs['value']
         
        if 'input_datas' in kwargs:
            self.data, self.sort_data = kwargs['input_datas']
        else:            
            self.cursor = studioInput.Connect(self.type, self.value)
            self.data, self.sort_data = self.cursor.getInputData()  
                  
             
        self.module, self.lable, self.version = platforms.get_tool_kit()

        self.setup_ui()
        self.load_widgets()

    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            'Add Discipline ({} {})'.format(self.lable, self.version))
        self.resize(500, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('Create your custom %s to asset or shot'% self.type)
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
       
                    
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
        self.button_create.clicked.connect(self.create)
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
            
            if current_item['type']=='str':
                widget = QtGui.QLineEdit(self.groupbox)
                widget.setObjectName('lineedit_%s' % self.sort_data[index])

            elif current_item['type']=='enum':
                widget = QtGui.QComboBox(self.groupbox)
                widget.setObjectName('combobox_%s' % self.sort_data[index])
                widget.addItems(current_item['values'])
                widget.setCurrentIndex(current_item['value'])
                
            if current_item['example']:
                 widget.setToolTip('\n'.join(current_item['example']))
            
            widget.setStatusTip(self.sort_data[index])
            
            self.gridlayout.addWidget(widget, index, 1, 1, 1)            
            

 

    def create(self):
        input_datas = self.get_source_paths(self.gridlayout)
        studio_input = studioInput.Connect(self.type, self.value)
        studio_input.create(
            en=True,
            na=input_datas['name'],
            dn=input_datas['display_name'],
            tp=input_datas['tooltip'],
            ty=input_datas['type']
        )
        self.close()


    def get_source_paths(self, layout):
        data = {}
        ing = 0
        for index in range(layout.rowCount()):
            widget = layout.itemAtPosition(index, 1).widget()
            if isinstance(widget, QtGui.QComboBox):
                value = widget.currentIndex()
            else:
                value = widget.text().encode()
            tag = widget.statusTip()
            
            print tag
            data.setdefault(tag.encode(), value)
            
        return data







    def _get_source_paths(self, layout):
        data = {}
        ing = 0
        for index in range(layout.rowCount()):
            if not layout.itemAt(ing) and layout.itemAt(ing + 1):
                continue
            lable_widget = layout.itemAt(ing).widget()
            content_widget = layout.itemAt(ing + 1).widget()
            if not lable_widget and content_widget:
                continue
            current_label = lable_widget.text().encode()
            current_tag = lable_widget.statusTip().encode()
            if isinstance(content_widget, QtGui.QComboBox):
                value = content_widget.currentIndex()
                all_items = [str(content_widget.itemText(x))
                             for x in range(content_widget.count())]
                content = {
                    'label': current_label,
                    'tag': current_tag,
                    'types': all_items,
                    'value': value
                }
            else:
                current_path = content_widget.text().encode()
                content = {
                    'label': current_label,
                    'tag': current_tag,
                    'path': current_path
                }
            data.setdefault(index, content)
            ing += layout.columnCount()
        return data

   
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window(parent=None, type='discipline', value='discipline_child_inputs')
    window.show()
    sys.exit(app.exec_())
