import os
import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.api import studioShow


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.setParent(parent)
        self.title = 'Show configure'
        self.width = 729
        self.height = 663
        self.version, self.label = self.set_tool_context()
        self.shows = studioShow.Show()
        self.setup_ui()
        self.set_default()

    def setup_ui(self):
        self.setObjectName('widget_show')
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
        self.verticallayout_item.setObjectName('verticallayout_item')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)                
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None)
        self.toolbox = QtWidgets.QToolBox(self)
        self.toolbox.setObjectName("toolbox")
        self.verticallayout_item.addWidget(self.toolbox)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout_item.addItem(spacer_item)
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.verticallayout_item.addLayout(self.horizontallayout) 
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)              
        self.horizontallayout.addItem(spacer_item)
        self.button_close = QtWidgets.QPushButton(self)
        self.button_close.setObjectName('button_close')
        self.button_close.setText('Close')
        self.horizontallayout.addWidget(self.button_close)
        self.button_create = QtWidgets.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout.addWidget(self.button_create)
        self.button_close.clicked.connect(self.close)
        self.button_create.clicked.connect(self.create)
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)                          
        
    def set_tool_context(self):
        config = sheader.Header()
        config.tool()
        return config.version, config.pretty
    
    def set_default(self):
        inputs = self.shows.get_show_configure_data()
        order = self.shows.get_next_order()
        inputs['show_name']['order']['value'] = order
        self.set_widgets('current_show', 'show', inputs['show_name'])        
        sorted_application = common.sorted_order(inputs['applications'])
        for application in sorted_application:
            self.set_widgets(
                'applications', application, inputs['applications'][application])        
        
    def set_widgets(self, header, key, inputs):
        '''
            :param header <str> 'current_show', 'applications'
            :param key <str>  'show', maya, katana, nuke, natron
        '''
        page = QtWidgets.QWidget()
        page.setObjectName('%s_%s' % (page, header))
        page.setStatusTip(key)
        page.setToolTip(header)
        self.toolbox.addItem(page, '%s configure' % key)
        gridlayout = QtWidgets.QGridLayout(page)
        gridlayout.setObjectName('gridlayout_%s' % key)
        gridlayout.setSpacing(5)
        gridlayout.setContentsMargins(10, 10, 10, 10)
        self.set_context_widgets(inputs, gridlayout)
    
    def set_context_widgets(self, inputs, layout):
        sizepolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)        
        sorted_date = common.sorted_order(inputs)
        for index, each in enumerate(sorted_date):
            contents = inputs[each]
            label = QtWidgets.QLabel(self)
            label.setObjectName('label_%s' % each)
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            label.setText(contents['label'])
            label.setSizePolicy(sizepolicy)                
            layout.addWidget(label, index, 0, 1, 1)
            if contents['type'] in ['str', 'path', 'dirname', 'list']:
                lineedit = QtWidgets.QLineEdit(self)
                lineedit.setObjectName('lineedit_%s' % each)
                value = contents['value']
                if contents['type'] == 'list':
                    value = ', '.join(contents['value'])
                lineedit.setText(value)
                lineedit.setStatusTip(
                    '%s,%s,%s' % (each, contents['type'], contents['order']))
                layout.addWidget(lineedit, index, 1, 1, 1)
            if contents['type'] in ['path', 'dirname']:                
                button = QtWidgets.QPushButton(self)
                button.setObjectName('button_%s' % each)  
                button.setText('...') 
                button.setMinimumSize(QtCore.QSize(30, 0))
                button.setMaximumSize(QtCore.QSize(30, 16777215))                                        
                layout.addWidget(button, index, 2, 1, 1)
                button.clicked.connect(partial(self.find_directory, lineedit, contents))
            if contents['type'] in ['int']:
                spinbox = QtWidgets.QSpinBox(self)
                spinbox.setObjectName('spinbox_%s' % each)  
                spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                spinbox.setMinimum(0)
                value = 999999999
                if contents['type'] == 'bool':
                    value = 1
                spinbox.setMaximum(value)
                spinbox.setValue(contents['value'])
                spinbox.setStatusTip(
                    '%s,%s,%s' % (each, contents['type'], contents['order']))
                layout.addWidget(spinbox, index, 1, 1, 1)
            if contents['type'] in ['bool']:
                combobox = QtWidgets.QComboBox(self)
                combobox.setObjectName('combobox_%s' % each)
                combobox.addItems(['False', 'True'])
                combobox.setCurrentIndex(contents['value'])
                combobox.setStatusTip(
                    '%s,%s,%s' % (each, contents['type'], contents['order']))
                layout.addWidget(combobox, index, 1, 1, 1)                

    def find_directory(self, widget, contents):
        if contents['type'] == 'path':
            directory, format = QtWidgets.QFileDialog.getOpenFileName(
                self, contents['description'], resource.getBrowsPath(), contents['format'])
            os.environ['BROWS_PATH'] = os.path.dirname(directory)
        if contents['type'] == 'dirname':
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self, contents['description'], resource.getBrowsPath())
            os.environ['BROWS_PATH'] = directory
        widget.setText(directory)                

    def get_widget_data(self, toolbox):
        widget_data = {}        
        for index in range(toolbox.count()):
            widget = toolbox.widget (index)
            header = widget.toolTip()
            key = widget.statusTip()
            girdlayout = widget.findChild(QtWidgets.QGridLayout)
            layout_data = self.get_layout_data(girdlayout)
            if header not in widget_data:
                widget_data.setdefault(header, {})
            widget_data[header].setdefault(key, layout_data)
        return widget_data
 
    def get_layout_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):            
            widget = self.get_widget(layout, row, 1)
            if not widget:
                continue
            if isinstance(widget, QtWidgets.QLineEdit):
                value = widget.text()
            elif isinstance(widget, QtWidgets.QSpinBox):
                value = widget.value()
            elif isinstance(widget, QtWidgets.QComboBox):
                value = bool(widget.currentIndex())
            name, types, order = widget.statusTip().split(',')
            if types == 'list':
                value = value.replace(' ', '').split(',')
            data.setdefault(name, value)
            data.setdefault('order', order)
        return data
    
    def get_widget(self, layout, row, column):    
        widgetitem = layout.itemAtPosition(row, column)
        if not widgetitem:
            return None
        widget = widgetitem.widget()        
        if not widget:
            return None
        return widget
                    
    def create(self):     
        widget_data = self.get_widget_data(self.toolbox)
        if not widget_data:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty inputs!...', QtWidgets.QMessageBox.Ok)
            return           
        label, ok = QtWidgets.QInputDialog.getText(
            self, 'Input', 'Enter the preset name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '#warning: abrot your process!...'
            return
        valid, value, message = self.shows.create_show_preset(label, widget_data)
        if not valid:        
            QtWidgets.QMessageBox.critical(
                self, 'critical', '%s\n%s' % (message, value), QtWidgets.QMessageBox.Ok)
            print '#warning: ', message, value
            return         
        QtWidgets.QMessageBox.information(
            self, 'information', '%s\ncreated %s show' % (message, label), QtWidgets.QMessageBox.Ok)
        self.close()            
        print '#successfully registered show preset!...'
        return

          
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_()) 
        
