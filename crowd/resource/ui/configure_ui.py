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
import logging

from pprint import pprint
from pymel import core

from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.core import control



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

        self.button_data = {}
        self.type_count = {'ik': 3, 'fk': 1}
        self.added_nodes = []
        self.input_data = {}
        
        tool_kit = platforms.get_tool_kit()
        self.tool_kit_object, self.tool_kit_name, self.version = tool_kit['create']
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [500, 125]
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.setup_ui()
        self.default_addon('ik', self.gridlayout_ik)
        self.default_addon('fk', self.gridlayout_fk)

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
        self.button_apply.clicked.connect(self.apply)  
        self.horizontallayout.addWidget(self.button_apply)
        self.verticallayout.addLayout(self.horizontallayout)                

    def default_addon(self, type, layout):
        row_count = layout.rowCount()
        button_plus = QtGui.QPushButton(None)
        button_plus.setObjectName('button_plus_%s' % type)
        button_plus.setMinimumSize(QtCore.QSize(35, 25))
        button_plus.setMaximumSize(QtCore.QSize(35, 25))
        button_plus.setText(u'\u002B')
        button_plus.setStyleSheet('color: #0000FF;')
        layout.addWidget(button_plus, row_count - 1, 1, 1, 1)
        button_plus.clicked.connect(
            partial(self.create_addon, button_plus, layout, row_count, type))

    def create_addon(self, preivous_button, layout, row, type):
        if preivous_button in self.button_data:
            for widget in self.button_data[preivous_button]['widgets']:
                widget.deleteLater()
            preivous_button.setText(u'\u002B')
            preivous_button.setStyleSheet('color: #0000FF;')
            pprint (self.button_data)
            
            self.button_data.pop(preivous_button)
            
            return
        widget_data = {}
        lineedits = []
        for x in range(self.type_count[type]):
            lineedit = QtGui.QLineEdit(self)
            lineedit.setObjectName('lineedit_%s' % row)
            lineedit.setStatusTip(str(row - 3))
            lineedit.setReadOnly(True)
            layout.addWidget(lineedit, row - 1, x + 2, 1, 1)
            lineedits.append(lineedit)
            widget_data.setdefault('widgets', []).append(lineedit)
        button_add = QtGui.QPushButton(None)
        button_add.setObjectName('button_plus_%s_%s' % (row, type))
        button_add.setMinimumSize(QtCore.QSize(35, 25))
        button_add.setMaximumSize(QtCore.QSize(35, 25))
        button_add.setText(u'\u2B05')
        button_add.clicked.connect(partial(self.add_node, lineedits, button_add))
        layout.addWidget(button_add, row - 1, x + 3, 1, 1)
        widget_data.setdefault('widgets', []).append(button_add)        
        
        combobox = QtGui.QComboBox(None)
        combobox.setObjectName('combobox_%s_%s' % (row, type))
        combobox.addItems(control.controls())
        layout.addWidget(combobox, row - 1, x + 4, 1, 1)
        widget_data.setdefault('widgets', []).append(combobox)        
        
        label_size = QtGui.QLabel(self)
        label_size.setObjectName('label_size_%s_%s' % (row, type))
        label_size.setText(' Size')        
        layout.addWidget(label_size, row - 1, x + 5, 1, 1)
        widget_data.setdefault('widgets', []).append(label_size)        
            
        spinbox_size = QtGui.QDoubleSpinBox(self)
        spinbox_size.setObjectName('spinbox_size_%s_%s' % (row, type))        
        spinbox_size.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        spinbox_size.setValue(1.00)
        spinbox_size.setDecimals(2)
        spinbox_size.setMaximum(999999999.0)
        spinbox_size.setMaximumSize(QtCore.QSize(100, 16777215))
        layout.addWidget(spinbox_size, row - 1, x + 6, 1, 1)
        widget_data.setdefault('widgets', []).append(spinbox_size)        
        button_plus = QtGui.QPushButton(None)
        button_plus.setObjectName('button_plus_%s_%s' % (row, type))
        button_plus.setMinimumSize(QtCore.QSize(35, 25))
        button_plus.setMaximumSize(QtCore.QSize(35, 25))
        button_plus.setText(u'\u002B')
        button_plus.setStyleSheet('color: #0000FF;')
        layout.addWidget(button_plus, row, 1, 1, 1)
        button_plus.clicked.connect(
            partial(self.create_addon, button_plus, layout, row + 1, type))
        preivous_button.setText(u'\u274C')
        preivous_button.setStyleSheet('color: #FF0004;')
        widget_data.setdefault('widgets', []).append(button_plus)
        self.button_data.setdefault(preivous_button, widget_data)        
    
    def add_node(self, widgets, button):
        nodes = core.ls(sl=True)        
        for node in nodes:
            if node.name() not in self.added_nodes:
                continue
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Already added node \"%s\"!...'%node.name(),
                QtGui.QMessageBox.Ok
            )            
            return
        if not nodes: 
            for x in range(len(widgets)):
                if widgets[x].text() in self.added_nodes:
                    self.added_nodes.remove(widgets[x].text())                    
                widgets[x].setText('')
            return       
        if len(nodes)<len(widgets):
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Wrong selection count!...',
                QtGui.QMessageBox.Ok
            )            
        for x in range(len(widgets)):
            widgets[x].setText(nodes[x].name())
            self.added_nodes.append(nodes[x].name())
        logging.info('Done!...')
        
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
        
        from pprint import pprint
        pprint (data)

    def get_widget_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            node = None
            for column in range(layout.columnCount()):
                if not layout.itemAtPosition(row, column):
                    continue                    
                widget = layout.itemAtPosition(row, column).widget()                
                if isinstance(widget, QtGui.QLineEdit):                    
                    node = widget.text().encode()
                    if not node:
                        continue
                    data.setdefault(row, {})               
                    data[row].setdefault('joints', []).append(node)
                    
                if isinstance(widget, QtGui.QComboBox):
                    if not node:
                        continue
                    control = widget.currentText()                         
                    data[row].setdefault('control', control.encode())
                                  
                if isinstance(widget, QtGui.QDoubleSpinBox):
                    if not node:
                        continue
                    radius = widget.value()                    
                    data[row].setdefault('radius', radius)
            if row in data:
                pynode = core.PyNode(data[row]['joints'][0])
                parent_node = None
                if pynode.getParent():
                    parent_node = pynode.getParent().name()
                print  '\t',  parent_node, data[row]['joints']
                if parent_node in data[row]['joints']:
                    return None                   
                data[row].setdefault('parent', parent_node.encode())
        return data 
    
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
