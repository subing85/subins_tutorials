import os
import sys
import ast

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import swidgets

from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPipe

import json


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, standalone=None):  
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.title = 'Studio Spread Sheet'
        self.width = 800
        self.height = 600
        self.version, self.label = self.set_tool_context() 
        self.setup_ui()
        self.setup_menu()
        self.setup_icons()        
        self.set_default()

    def setup_ui(self):
        self.setObjectName('mainwindow_spreadsheet')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version)) 
        self.resize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
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
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout_output')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None) 
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.combobox_show = QtWidgets.QComboBox(self)
        self.combobox_show.setObjectName('combobox_show')
        self.horizontallayout.addWidget(self.combobox_show)        
        self.combobox_pipe = QtWidgets.QComboBox(self)
        self.combobox_pipe.setObjectName('combobox_pipe')
        self.horizontallayout.addWidget(self.combobox_pipe)
        spaceritem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spaceritem)
        self.treewidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treewidget.setObjectName('treewidget')
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.treewidget.customContextMenuRequested.connect(partial(self.on_context_menu, self.treewidget))   
        self.verticallayout_item.addWidget(self.treewidget)
        self.combobox_show.currentIndexChanged.connect(self.set_current_show)
        self.combobox_pipe.currentIndexChanged.connect(self.set_current_pipe)

    def setup_menu(self):        
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')
        self.action_remove = QtWidgets.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setToolTip('Remove from composition') 
        self.action_remove.setText('Remove')   
        self.menu.addAction(self.action_remove)
        self.action_remove.triggered.connect(partial(self.remove_items, self.treewidget))
        
    def on_context_menu(self, widget, point):
        index = widget.indexAt(point)
        if not index.isValid():
            return      
        if not widget.selectedItems():
            return
        self.menu.exec_(widget.mapToGlobal(point))

    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)
        
    def set_tool_context(self):
        config = sheader.Header()
        config.tool()
        return config.version, config.pretty
    
    def set_default(self):
        sshow = studioShow.Show()
        preset_data = sshow.get_preset_data()
        shows = sshow.get_shows(preset_data=preset_data, verbose=False)
        self.combobox_show.addItem('None')      
        for each in shows:
            icon_path = preset_data[shows[each][1]]['current_show']['show']['icon'][1]
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.combobox_show.addItem(icon, shows[each][1])

    def set_current_show(self):
        self.combobox_pipe.clear()
        if self.combobox_show.currentText() == 'None':
            return
        pipes = sorted(resource.getPipeData()['pipe'].keys())
        self.combobox_pipe.addItem('None')
        for pipe in pipes:
            icon_path = os.path.join(resource.getIconPath(), '%s.png' % pipe)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.combobox_pipe.addItem(icon, pipe)
            
    def set_current_pipe(self):
        self.treewidget.clear()       
        current_show = self.combobox_show.currentText().encode()
        current_pipe = self.combobox_pipe.currentText().encode()
        if current_show == 'None':
            return
        if current_pipe == 'None':
            return        
        spipe = studioPipe.Pipe(current_show, current_pipe)
        subfileds = spipe.pipe_inputs['subfield']['values']
        publish_data = spipe.get()
        self.treewidget.setColumnCount(10)
        index = 1
        for caption in publish_data:
            for subfiled in subfileds:
                if subfiled not in publish_data[caption]:
                    continue
                versions = publish_data[caption][subfiled].keys()
                versions = common.set_version_order(versions)                
                for version in versions:
                    column_items = [
                        ['No', index],
                        ['caption', caption],
                        ['subfield', subfiled],
                        ['version', version]
                        ]                    
                    publish_data[caption][subfiled][version].pop('version')
                    version_contents = sorted(publish_data[caption][subfiled][version].keys())
                    for each in version_contents:
                        column_items.append([each, publish_data[caption][subfiled][version][each]])
                    version_item = swidgets.append_treewidget_item(
                        self.treewidget, column_items)
                    table_data = [
                        publish_data[caption][subfiled][version]['table'],
                        publish_data[caption][subfiled][version]['location'],
                        version,
                        publish_data[caption][subfiled][version]['subfield'],
                        publish_data[caption][subfiled][version]['caption'],
                        ]
                    version_item.setStatusTip(0, str(table_data))
                    index+=1
   
    def remove_items(self, treewidget):
        selecteditems = treewidget.selectedItems()
        if not selecteditems:
            return
        current_show = self.combobox_show.currentText().encode()
        current_pipe = self.combobox_pipe.currentText().encode()
        print '# remove'        
        for item in selecteditems:
            contents = item.statusTip(0)
            if not contents:
                continue
            table, location, version, subfiled, caption = ast.literal_eval(contents)
            spipe = studioPipe.Pipe(current_show, current_pipe)
            spipe.remove(table, location)
            print '%s: %s' % ('show'.rjust(15), current_show)
            print '%s: %s' % ('pipe'.rjust(15), current_pipe)
            print '%s: %s' % ('version'.rjust(15), version)
            print '%s: %s' % ('subfield'.rjust(15), subfiled)
            print '%s: %s' % ('caption'.rjust(15), caption)
        self.set_current_pipe()
        print '# remove success!...'
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_()) 
