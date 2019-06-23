'''
create_ui.py 0.0.1 
Date: June 14, 2019
Last modified: June 14, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys
import json
import logging

from pprint import pprint
from pymel import core

from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.core import controls
from crowd.core import puppet
from crowd.core import generic

reload(controls)
reload(puppet)

joint label repate error

class Connect(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Connect, self).__init__(parent)
        self.object_name = 'configure_widget'
        platforms.remove_exists_window(self.object_name)
        self.type = type
        self.heading = '[Subin CROwd]\t skeleton Configure'
        valid = platforms.has_valid()
        if not valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resource.getDownloadLink())
            QtGui.QMessageBox.critical(
                self, 'Critical', message, QtGui.QMessageBox.Ok)
            return
        if False in valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resource.getDownloadLink())
            QtGui.QMessageBox.critical(
                self, 'Critical', message, QtGui.QMessageBox.Ok)
            return

        self.type_count = {'ik': 9, 'fk': 7}
        self.added_nodes = []
        self.font_size = 10

        tool_kit = platforms.get_tool_kit()
        self.tool_kit_object, self.tool_kit_name, self.version = tool_kit['create']
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [500, 125]
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.setup_ui()
        self.default_addon('ik', self.horizontallayout_ik, self.gridlayout_ik)
        self.default_addon('fk', self.horizontallayout_fk, self.gridlayout_fk)

    def setup_ui(self):
        self.setObjectName(self.object_name)
        self.resize(800, 500)
        self.setWindowTitle(self.tool_kit_titile)
        self.setStyleSheet('font: 14pt \"Sans Serif\";')
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(20, 20, 20, 20)
        self.label_title = QtGui.QLabel(self)
        self.label_title.setObjectName('label')
        self.label_title.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_title.setText(self.heading)
        self.verticallayout.addWidget(self.label_title)
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizepolicy.setHorizontalStretch(0)
        sizepolicy.setVerticalStretch(0)
        self.scrollarea_ik = QtGui.QScrollArea(self)
        self.scrollarea_ik.setWidgetResizable(True)
        self.scrollarea_ik.setObjectName('scrollarea_ik')
        self.verticallayout.addWidget(self.scrollarea_ik)
        self.content_ik = QtGui.QWidget()
        self.content_ik.setObjectName('content_ik')
        self.scrollarea_ik.setWidget(self.content_ik)
        self.verticallayout_ik = QtGui.QVBoxLayout(self.content_ik)
        self.verticallayout_ik.setObjectName('verticallayout_ik')
        self.verticallayout_ik.setSpacing(1)
        self.label_ik = QtGui.QLabel(self)
        self.label_ik.setObjectName('label_ik')
        self.label_ik.setText(' IK')
        self.label_ik.setStyleSheet('background-color: #393939;')
        self.label_ik.setSizePolicy(sizepolicy)
        self.verticallayout_ik.addWidget(self.label_ik)       
                
        self.gridlayout_ik = QtGui.QGridLayout(None)
        self.gridlayout_ik.setObjectName('gridlayout_ik')
        self.gridlayout_ik.setSpacing(5)
        self.gridlayout_ik.setContentsMargins(30, 5, 5, 5)
        self.verticallayout_ik.addLayout(self.gridlayout_ik) 
        
        self.horizontallayout_ik = QtGui.QHBoxLayout()
        self.horizontallayout_ik.setObjectName('horizontallayout_ik') 
        self.horizontallayout_ik.setContentsMargins(30, 5, 5, 5)               
        self.verticallayout_ik.addLayout(self.horizontallayout_ik)              
               
        spaceritem_ik = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout_ik.addItem(spaceritem_ik)        
        self.scrollarea_fk = QtGui.QScrollArea(self)
        self.scrollarea_fk.setWidgetResizable(True)
        self.scrollarea_fk.setObjectName('scrollarea_fk')
        self.verticallayout.addWidget(self.scrollarea_fk)
        self.content_fk = QtGui.QWidget()
        self.content_fk.setObjectName('content_fk')
        self.scrollarea_fk.setWidget(self.content_fk)
        self.verticallayout_fk = QtGui.QVBoxLayout(self.content_fk)
        self.verticallayout_fk.setObjectName('verticallayout_fk')
        self.verticallayout_fk.setSpacing(0)
        self.label_fk = QtGui.QLabel(self)
        self.label_fk.setObjectName('label_fk')
        self.label_fk.setText(' FK')
        self.label_fk.setStyleSheet('background-color: #393939;')
        self.label_fk.setSizePolicy(sizepolicy)
        self.verticallayout_fk.addWidget(self.label_fk)
        
        self.gridlayout_fk = QtGui.QGridLayout(None)
        self.gridlayout_fk.setObjectName('gridlayout_fk')
        self.gridlayout_fk.setSpacing(5)
        self.gridlayout_fk.setContentsMargins(30, 5, 5, 5)
        self.verticallayout_fk.addLayout(self.gridlayout_fk)         
        
        self.horizontallayout_fk = QtGui.QHBoxLayout()
        self.horizontallayout_fk.setObjectName('horizontallayout_fk')
        self.horizontallayout_fk.setContentsMargins(30, 5, 5, 5)
        self.verticallayout_fk.addLayout(self.horizontallayout_fk)        
               
        spaceritem_fk = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout_fk.addItem(spaceritem_fk)                
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        spaceritem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spaceritem)
        self.button_reset = QtGui.QPushButton(self)
        self.button_reset.setObjectName('button_reset')
        self.button_reset.setText('Reset')
        self.button_reset.setMinimumSize(QtCore.QSize(150, 16777215))
        self.horizontallayout.addWidget(self.button_reset)
        self.button_apply = QtGui.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')
        self.button_apply.setMinimumSize(QtCore.QSize(150, 16777215))
        self.horizontallayout.addWidget(self.button_apply)
        self.verticallayout.addLayout(self.horizontallayout)
        self.button_reset.clicked.connect(self.reset)
        self.button_apply.clicked.connect(self.apply)

    def default_addon(self, type, parent, layout):
        button_plus = QtGui.QPushButton(None)
        button_plus.setObjectName('button_plus_%s' % type)
        button_plus.setMinimumSize(QtCore.QSize(35, 25))
        button_plus.setMaximumSize(QtCore.QSize(35, 25))
        button_plus.setText(u'\u002B')
        button_plus.setStyleSheet('color: #0000FF;')
        parent.addWidget(button_plus)
        button_plus.clicked.connect(
            partial(self.create_addon, layout, type))
        spaceritem_plus = QtGui.QSpacerItem(
            516, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        parent.addItem(spaceritem_plus)

    def create_addon(self, layout, type):
        row_count = layout.rowCount()

        button_remove = QtGui.QPushButton(None)
        button_remove.setObjectName('button_remove_%s_%s' % (type, row_count))
        button_remove.setMinimumSize(QtCore.QSize(35, 25))
        button_remove.setMaximumSize(QtCore.QSize(35, 25))
        button_remove.setText(u'\u274C')
        button_remove.setStyleSheet('color: #FF0004;')
        layout.addWidget(button_remove, row_count, 0, 1, 1)
        
        lineedits = []
        for x in range(1, self.type_count[type] - 5):
            lineedit = QtGui.QLineEdit(self)
            lineedit.setObjectName('lineedit_%s_%s' % (type, row_count))
            lineedit.setReadOnly(True)
            lineedit.setStyleSheet(
                'font: %spt "Sans Serif";'%self.font_size)
            lineedit.setMaximumSize(QtCore.QSize(16777215, 30))            
            layout.addWidget(lineedit, row_count, x, 1, 1)
            lineedits.append(lineedit)
            
        next_row = self.type_count[type] - 5
        
        button_add = QtGui.QPushButton(None)
        button_add.setObjectName('button_add_%s_%s' % (type, row_count))
        button_add.setMinimumSize(QtCore.QSize(35, 25))
        button_add.setMaximumSize(QtCore.QSize(35, 25))
        button_add.setText(u'\u2B05')
        layout.addWidget(button_add, row_count, next_row, 1, 1)
        next_row += 2
        label_control = QtGui.QLabel(None)
        label_control.setObjectName('label_size_%s_%s' % (type, row_count))
        label_control.setText('  Control > ')
        label_control.setStyleSheet(
            'background-color: #393939; font: %spt "Sans Serif";'%self.font_size)
        layout.addWidget(label_control, row_count, next_row + 1, 1, 1)
        combobox = QtGui.QComboBox(None)
        combobox.setObjectName('combobox_%s_%s' % (type, row_count))
        combobox.addItems(control.controls())
                    
        layout.addWidget(combobox, row_count, next_row + 2, 1, 1)
        label_size = QtGui.QLabel(None)
        label_size.setObjectName('label_size_%s_%s' % (type, row_count))
        label_size.setText('  Size > ')
        label_size.setStyleSheet(
            'background-color: #393939; font: %spt "Sans Serif";'%self.font_size)        
        layout.addWidget(label_size, row_count, next_row + 3, 1, 1)
        spinbox_size = QtGui.QDoubleSpinBox(None)
        spinbox_size.setObjectName('spinbox_size_%s_%s' % (type, row_count))
        spinbox_size.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        spinbox_size.setValue(1.00)
        spinbox_size.setDecimals(2)
        spinbox_size.setMaximum(999999999.0)
        spinbox_size.setMaximumSize(QtCore.QSize(65, 16777215))
        layout.addWidget(spinbox_size, row_count, next_row + 4, 1, 1)

        widgets = [
            button_remove,
            button_add,
            label_control,
            combobox,
            label_size,
            spinbox_size
            ] + lineedits
        button_remove.clicked.connect(partial(self.remove_widgets, widgets))        
        button_add.clicked.connect(partial(self.add_node, lineedits))        
    
    def remove_widgets(self, widgets): 
        data = self.get_widget_value(widgets)               
        for widget in widgets:
            widget.deleteLater()            
        if 'joints' not in data:
            return            
        for each_node in data['joints']:            
            if each_node not in self.added_nodes:
                continue
            self.added_nodes.remove(each_node)
        pprint(data)

    def add_node(self, widgets):
        nodes = core.ls(sl=True)
        for node in nodes:
            if node.name() not in self.added_nodes:
                continue
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Already added node \"%s\"!...' % node.name(),
                QtGui.QMessageBox.Ok
            )
            return
        if not nodes:
            for widget in widgets:
                if widget.text() in self.added_nodes:
                    self.added_nodes.remove(widget.text())
                widget.setText('')
            return        
        if len(nodes) < len(widgets):
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Wrong selection count!...',
                QtGui.QMessageBox.Ok
            )
            return
        for x in range(len(widgets)):
            widgets[x].setText(nodes[x].name())
            self.added_nodes.append(nodes[x].name())
        logging.info('Done!...')
   
    def reset(self):        
        self.delete_widgets(self.gridlayout_ik)
        self.delete_widgets(self.gridlayout_fk)
    
    def delete_widgets(self, layout):        
        widgets = []
        for index in range (layout.count()):
            item = layout.itemAt(index)
            if not item:
                continue
            widget = item.widget()
            if not widget:
                continue
            try:
                widget.deleteLater()
            except Exception as result:
                logging.warning('widget delete : {}'.format(result))
        return widgets        
        
        

    def apply(self):
        ik_data = self.get_widget_data(self.gridlayout_ik)
        fk_data = self.get_widget_data(self.gridlayout_fk)
        if not ik_data or not fk_data:
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Wrong joints configures!...',
                QtGui.QMessageBox.Ok
            )
            return

        data = {
            'ik': ik_data,
            'fk': fk_data
        }
        json_data = json.dumps(data, indent=4)
        try:
            puppet.create_puupet_data(json_data)
            QtGui.QMessageBox.information(
                self, 'Information', 'Done!...', QtGui.QMessageBox.Ok)            
        except Exception as error:
            QtGui.QMessageBox.critical(
                self, 'Critical', str(error), QtGui.QMessageBox.Ok)
        
    def get_widget_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            node = None
            widgets = []
            for column in range(layout.columnCount()):
                if not layout.itemAtPosition(row, column):
                    continue
                widget = layout.itemAtPosition(row, column).widget()
                if not widget:
                    continue
                widgets.append(widget)                
            if not widgets:
                continue
            widget_data = self.get_widget_value(widgets)            
            if 'joints' not in widget_data:  
                return None            
            data.setdefault(row, widget_data) 
        return data

    def get_widget_value(self, widgets):
        data = {}
        for widget in widgets:
            if isinstance(widget, QtGui.QLineEdit):
                node = widget.text().encode()
                if not node:
                    continue                
                side, joint_type, other_type = generic.get_joint_type(node)                
                data.setdefault('joints', []).append(other_type)
            if isinstance(widget, QtGui.QComboBox):
                control = widget.currentText()
                data.setdefault('control', control)
            if isinstance(widget, QtGui.QDoubleSpinBox):
                radius = widget.value()
                data.setdefault('radius', radius)        
        if 'joints' in data:
            if data['joints']:
                current_node = data['joints'][0]
                if core.objExists(current_node):
                    node_parent = None
                    if core.PyNode(current_node).getParent():
                        node_parent = core.PyNode(
                            current_node).getParent().name().encode()
                    data.setdefault('parent', node_parent)
        return data
    
    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())