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

import sys

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime


from studioPipe import resources
from studioPipe.modules import readWrite
from studioPipe.utils import platforms

class Types(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Types, self).__init__(parent)
        
        self.module, self.lable, self.version = platforms.get_tool_kit()
        
        self.rw = readWrite.ReadWrite(
            path=resources.getInputPath(), name='pipe_type', tag='pipe_type')
        self.input_data = self.rw.get_data()
        self.setup_ui()
        
        self.load_widgets()


    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            'Input Type ({} {})'.format(self.lable, self.version))
        self.resize(500, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('Create your custom categories or departments of asset and shot')
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(10, 10, 10, 10)
        
        #=======================================================================
        # self.label_label = QtGui.QLabel(self.groupbox)
        # self.label_label.setObjectName('label_label')
        # self.label_label.setText('Create your custom categorie or department')
        # self.label_label.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        # 
        # self.verticallayout_item.addWidget(self.label_label)
        #=======================================================================
        
                    
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
        print self.input_data         
        sort_data = self.rw.set_order(self.input_data)
        
        for index in range (len(sort_data)):
            
            current_item = self.input_data[sort_data[index]]
            
            label = QtGui.QLabel(self.groupbox)
            label.setObjectName('label_%s' % sort_data[index])
            label.setText(current_item['display_name'])
            label.setStatusTip(current_item['tooltip'])
            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.gridlayout.addWidget(label, index, 0, 1, 1)
            
            if current_item['type']=='str':
                widget = QtGui.QLineEdit(self.groupbox)
                widget.setObjectName('lineedit_%s' % sort_data[index])

            elif current_item['type']=='enum':
                widget = QtGui.QComboBox(self.groupbox)
                widget.setObjectName('combobox_%s' % sort_data[index])
                widget.addItems(current_item['values'])
                widget.setCurrentIndex(current_item['value'])
                
            if current_item['example']:
                 widget.setToolTip('\n'.join(current_item['example']))
            
            self.gridlayout.addWidget(widget, index, 1, 1, 1)            
            
        
                 




    def create_widgets(self):
        keys = self.bundles.keys()
        keys.sort()
        for index in range(len(keys)):
            self.add_widgets(index, self.bundles[keys[index]])

    def add_widgets(self, row, contents=None):
        label_label = QtGui.QLabel(self.groupbox)
        label_label.setObjectName('label_label_%s' % row)
        label_label.setText(contents['label'])
        label_label.setStatusTip(contents['tag'])
        label_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(label_label, row, 0, 1, 1)
        if 'types' in contents:
            widget = QtGui.QComboBox(self.groupbox)
            widget.setObjectName('combobox_types')
            widget.addItems(contents['types'])
            widget.setCurrentIndex(contents['value'])
            widget.setToolTip(contents['label'])
            self.gridlayout.addWidget(widget, row, 1, 1, 1)
        else:
            widget = QtGui.QLineEdit(self.groupbox)
            widget.setObjectName('lineedit_path_%s' % row)
            widget.setText(contents['path'])
            self.gridlayout.addWidget(widget, row, 1, 1, 1)
        button_find = QtGui.QPushButton(self.groupbox)
        button_find.setObjectName('button_find_%s' % row)
        button_find.setText('...')
        button_find.setStyleSheet('color: #0000FF;')
        button_find.setMinimumSize(QtCore.QSize(35, 25))
        button_find.setMaximumSize(QtCore.QSize(35, 25))
        if 'types' in contents:
            button_find.hide()
        self.gridlayout.addWidget(button_find, row, 2, 1, 1)
        widgets = [label_label, widget, button_find]
        button_find.clicked.connect(partial(self.find_path, widgets, contents['label']))

    def find_path(self, widgets, title):
        path = QtGui.QFileDialog.getExistingDirectory(
            self, 'Browse for {} folder'.format(title), self.brows_directory)
        if not path:
            return
        self.brows_directory = path
        widgets[1].setText(path)

    def apply(self):
        directorys = self.get_source_paths(self.gridlayout)
        comment = '{} {} - preference container'.format(
            self.lable, self.version)
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about asset library preference'
        type = 'preference'
        valid = True
        data = directorys
        tag = 'asset_library'
        resource_path = resources.getResourceTypes()[type]
        rw = readWrite.ReadWrite(c=comment, cd=created_date, d=description,
                                 t=type, v=valid, data=data, tag=tag, path=resource_path,
                                 name='library_preferences', format='json')
        rw.create()
        self.close()
        print '\n#result preferences updated ', rw.file_path

    def get_source_paths(self, layout):
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
                print 'content_widget\t', content_widget
                current_path = content_widget.text().encode()
                print current_path
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
    window = Types(parent=None)
    window.show()
    sys.exit(app.exec_())
