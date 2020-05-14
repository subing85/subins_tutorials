'''
main.py 0.0.1 
Date: March 09, 2019
Last modified: March 09, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys
import os
import tempfile
import thread
import copy
from pprint import  pprint

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime

from studioPipe import resources
from studioPipe.utils import platforms
from studioPipe.api import studioShows
from studioPipe.api import studioDiscipline
from studioPipe.api import studioHeader
from studioPipe.api import studioTier
from studioPipe.api import studioUserpool
import catalogue


class Main(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.brows_directory = resources.getWorkspacePath()
        self.brows_directory = '/mnt/bkp/Icons gallery/icons_04'
        self.studio_pipe_path = '/home/shreya/Documents/studio_pipe'
        self.module, self.lable, self.version = platforms.get_tool_kit()
                
        self.icon_format = 'png'
        self.width, self.height = 256, 144
        self.show_data = {}
        self.description_type = {
            1: 'assets',
            2: 'shots'
        }           
        self.current_show = None
        self.current_discipline = None
        self.current_description = None

        # studio_header = studioHeader.Connect()
        # self.input_data, self.input_sort_data, self.input_key_data = studio_header.getInputData()
        self.setup_ui()
        self.load_tool_bar()
        self.set_icons()
        # self.load_shows_to_layout(self.listWidget_shows)

    def setup_ui(self):
        self.setObjectName('asset')
        self.setWindowTitle(
            'Show Inputs ({} {})'.format(self.lable, self.version))
        self.resize(1000, 600)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        
        self.label_logo = QtGui.QLabel(self)
        self.label_logo.setObjectName('label_subins_toolkits')
        self.label_logo.setPixmap(QtGui.QPixmap(
            os.path.join(resources.getIconPath(), 'subins_toolkits_2.png')))
        self.label_logo.setScaledContents(True)
        self.label_logo.setMinimumSize(QtCore.QSize(500, 142))
        self.label_logo.setMaximumSize(QtCore.QSize(500, 142))        
        self.verticallayout.addWidget(self.label_logo)       
       
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout.addLayout(self.horizontallayout)
        
        self.verticalLayout_shows_a = QtGui.QVBoxLayout()
        self.verticalLayout_shows_a.setObjectName('verticalLayout_show_a')
        self.horizontallayout.addLayout(self.verticalLayout_shows_a)
        
        self.verticalLayout_pipe = QtGui.QVBoxLayout()
        self.verticalLayout_pipe.setObjectName('verticalLayout_pipe')        
        self.horizontallayout.addLayout(self.verticalLayout_pipe)
               
        self.groupbox_shows = QtGui.QGroupBox(self)
        self.groupbox_shows.setObjectName('groupbox_shows')
        self.groupbox_shows.setTitle('Shows')
        self.verticalLayout_pipe.addWidget(self.groupbox_shows)
        
        self.verticalLayout_shows_b = QtGui.QVBoxLayout(self.groupbox_shows)
        self.verticalLayout_shows_b.setObjectName('verticalLayout_show_b')
        
        self.listWidget_shows = catalogue.Catalogue(
            parent=self.groupbox_shows, width=self.width, height=self.height)
        self.listWidget_shows.itemClicked.connect(
            partial(self.set_my_show, self.listWidget_shows))  # Load Pose to UI
        self.verticalLayout_shows_b.addWidget(self.listWidget_shows)
        
        self.groupbox_toolbar = QtGui.QGroupBox(self)
        self.groupbox_toolbar.setObjectName('groupbox_toolbar')
        # self.groupbox_toolbar.setTitle('groupbox_toolbar')
        self.groupbox_toolbar.setMinimumSize(QtCore.QSize(0, 35))
        self.groupbox_toolbar.setMaximumSize(QtCore.QSize(16777215, 35))         
        self.groupbox_toolbar.hide()
        self.verticalLayout_pipe.addWidget(self.groupbox_toolbar)  
                 
        self.horizontallayout_toolbar = QtGui.QHBoxLayout(self.groupbox_toolbar)
        self.horizontallayout_toolbar.setObjectName('horizontallayout_toolbar')
                
        self.groupbox_show = QtGui.QGroupBox(self)
        self.groupbox_show.setObjectName('groupbox_show')
        # self.groupbox_show.setTitle('Show')
        self.groupbox_show.hide()
        self.verticalLayout_pipe.addWidget(self.groupbox_show)
        
        self.verticalLayout_show = QtGui.QVBoxLayout(self.groupbox_show)
        self.verticalLayout_show.setObjectName('verticalLayout_show')        

        self.splitter = QtGui.QSplitter(self.groupbox_show)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName('splitter')
        
        self.verticalLayout_show.addWidget(self.splitter)
        
        self.treewidget_discipline = QtGui.QTreeWidget(self.splitter)
        self.treewidget_discipline.setObjectName('treewidget_discipline') 
        # self.treewidget_discipline.setStyleSheet('font: 14pt \"Sans Serif\";')        
        self.treewidget_discipline.headerItem().setText(0, 'Deciplines')
        self.treewidget_discipline.setAlternatingRowColors(True)
               
        self.splitter.addWidget(self.treewidget_discipline)
        
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setObjectName('treewidget')   
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSortingEnabled(True)        
        self.treewidget.setColumnCount(0)        
        self.splitter.addWidget(self.treewidget) 
        
        self.groupbox_details = QtGui.QGroupBox(self.splitter)
        self.groupbox_details.setObjectName('groupbox_details')
        self.groupbox_details.setTitle('Details')
        self.splitter.addWidget(self.groupbox_details)
        self.splitter.setSizes([171, 381, 108])
        
        self.treewidget_discipline.itemClicked.connect(
            partial(self.set_my_discipline, self.treewidget_discipline, self.treewidget))
    
    def load_tool_bar(self):    
        self.toolBar = QtGui.QToolBar()        
        self.horizontallayout_toolbar.addWidget(self.toolBar)
        
        self.action_add_discipline = QtGui.QAction(self)
        self.action_add_discipline.setObjectName('action_add_discipline')
        self.action_add_discipline.setText('Add Discipline')
        self.action_add_discipline.setToolTip('Add Discipline')
        
        self.action_remove_discipline = QtGui.QAction(self)
        self.action_remove_discipline.setObjectName('action_remove_discipline')
        self.action_remove_discipline.setText('Remove Discipline')
        self.action_remove_discipline.setToolTip('Add Discipline')
        
        self.action_add_item = QtGui.QAction(self)
        self.action_add_item.setObjectName('action_add_item')
        self.action_add_item.setText('Add Item')
        self.action_add_item.setToolTip('Add Item')
        
        self.action_remove_item = QtGui.QAction(self)
        self.action_remove_item.setObjectName('action_remove_item')      
        self.action_remove_item.setText('Remove Tag')
        self.action_remove_item.setToolTip('Remove Item')
        
        self.action_submit = QtGui.QAction(self)
        self.action_submit.setObjectName('action_submit')      
        self.action_submit.setText('Submit')
        self.action_submit.setToolTip('Submit')        
        
        self.toolBar.addAction(self.action_add_discipline)
        self.toolBar.addAction(self.action_remove_discipline)
        self.toolBar.addSeparator ()        
        self.toolBar.addAction(self.action_add_item)
        self.toolBar.addAction(self.action_remove_item)
        self.toolBar.addSeparator ()        
        self.toolBar.addAction(self.action_submit)
       
        self.action_add_discipline.triggered.connect(self.add_discipline)
        self.action_add_item.triggered.connect(partial(self.add_item, self.treewidget))
        self.action_submit.triggered.connect(partial(self.submit, self.treewidget))
        
    def set_icons(self):
        actions = self.findChildren(QtGui.QAction)
        for each_action in actions:
            objectName = each_action.objectName()
            if not objectName:
                continue
            current_icon = '{}.png'.format(objectName.split('action_')[-1])
            icon_path = os.path.join(resources.getIconPath(), current_icon)
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            each_action.setIcon(icon)
    
    # 689x195    
    def load_shows_to_layout(self, listwidget):
        studio_shows = studioShows.Connect()
        data, rollback_data, sort_data = studio_shows.getShowAllData()

        listwidget.clear()
        for each_show in sort_data:
            current_icon = data[rollback_data[each_show]][each_show]['show_icon']
            display_name = data[rollback_data[each_show]][each_show]['display_name']
            tooltip = data[rollback_data[each_show]][each_show]['tooltip']           
            self.show_data.setdefault(each_show, data[rollback_data[each_show]][each_show])
            
            item = QtGui.QListWidgetItem()
            listwidget.addItem(item)
            item.setText(display_name)
            item.setToolTip(tooltip)
            item.setStatusTip(each_show)
            icon = QtGui.QIcon()

            icon.addPixmap(
                QtGui.QPixmap(current_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            item.setIcon(icon)
            item.setTextAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

    def set_my_show(self, listwidget, *args):        
        current_items = listwidget.selectedItems()
        if not current_items:
            return        
        self.current_show = current_items[-1].statusTip()        
        if self.current_show not in self.show_data:
            print 'Value error, not found your show %s' % current_show
            return
        
        self.verticalLayout_shows_a.addWidget(self.listWidget_shows)

        self.listWidget_shows.setMinimumSize(QtCore.QSize(290, 0))
        self.listWidget_shows.setMaximumSize(QtCore.QSize(290, 16777215))             
        self.groupbox_shows.hide()
        
        self.groupbox_show.show()
        self.groupbox_toolbar.show()
        
        self.load_discipline(self.treewidget_discipline, self.current_show)   
        self.load_discipline_header(self.treewidget)
        
    def load_discipline(self, treewidget, current_show):
        treewidget.clear()
        studio_discipline = studioDiscipline.Connect()
        disciplines, discipline_content = studio_discipline.getDisciplines(current_show)

        for each_discipline in disciplines:
            content = discipline_content[each_discipline]
            display_name = content['display_name']
            tooltip = content['tooltip']
            icon_path = content['discipline_icon']
            
            item = QtGui.QTreeWidgetItem(treewidget)
            item.setText(0, display_name)
            item.setToolTip(0, '%s/%s' % (self.description_type[content['type']], tooltip))
            item.setStatusTip(0, str(content['type']))
            item.setWhatsThis(0, each_discipline)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(0, icon)            
        
        treewidget.setIconSize(QtCore.QSize(50, 50))

    def add_discipline(self):
        discipline_window = discipline.Connect(parent=None, type='discipline', value=None,
                         title='Disciplines Inputs', label='Create your Show Disciplines', width=500, height=407)
        discipline_window.show()
    
    def load_discipline_header(self, treewidget, *args):
        treewidget.header().setDefaultSectionSize(100)       
        index = 0
        for each in self.input_sort_data:
            header = self.input_data[each]
            treewidget.headerItem().setText(index, header['display_name'])
            treewidget.header ().resizeSection (index, header['size'])
            index += 1 
        treewidget.header ().resizeSection (0, 50)
        
    def set_my_discipline(self, source, target, *args):
        target.clear()
        selected_items = source.selectedItems()
        if not selected_items:
            return
        self.current_description_type = int(selected_items[-1].statusTip(0))
        self.current_description = self.description_type[self.current_description_type]
        self.current_discipline = selected_items[-1].whatsThis(0)
        
        studio_header = studioHeader.Connect(name=self.current_description)
        output_data = studio_header.getOutputData(show_name=self.current_show)
        
        output_sort = output_data.keys()
        output_sort.sort()

        discipline_data = None
        
        for index in output_sort:
        
            # for index, content in output_data.items():
            content = output_data[index]
            
            if self.current_discipline not in content:
                continue
            discipline_output_data = content[self.current_discipline]
            
            input_instance = copy.deepcopy(self.input_data)
            for header, data_content in self.input_data.items():
                input_instance[header]['value'] = discipline_output_data[header]['value']
            
            item = QtGui.QTreeWidgetItem(target)
            for each in self.input_sort_data:
                self.add_description_item(
                    item, each, input_instance, self.current_description, target)
         
    def add_item(self, treewidget):
        if not self.current_description:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Please select any discipline and try!..', QtGui.QMessageBox.Ok)
            return
        widget_item = treewidget.invisibleRootItem()
        index = widget_item.childCount() + 1      
        item = QtGui.QTreeWidgetItem(treewidget)  
              
        default_data = copy.deepcopy(self.input_data)
        default_data['number']['value'] = str(index)
        for each in self.input_sort_data:
            self.add_description_item(
                item, each, default_data, self.current_description, treewidget)
            
    def add_description_item(self, item, each, input_data, description, treewidget):
        enable = input_data[each]['enable']
        editable = input_data[each]['editable']
        type = input_data[each]['type']
        order = input_data[each]['order']
        tooltip = input_data[each]['tooltip']
        value = input_data[each]['value']
        values = input_data[each]['values']
        r, g, b = input_data[each]['color']
        add = input_data[each]['add']
        
        if type == 'str':
            item.setText(order, value)
            item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
        if type == 'enum':
            combobox = QtGui.QComboBox(treewidget)
            combobox.setObjectName('comboBox_%s' % each)
            combobox.setToolTip(tooltip)
            combobox.setEditable(True)
            comb_values = None
            
            if add:
                comb_values = self.add_values(add, description)
            elif values:
                comb_values = values

            if comb_values:                                
                combobox.addItems(comb_values)                
                if value:
                    current_index = 0
                    if isinstance(value, int):
                        current_index = int(value)
                    if isinstance(value, str) or isinstance(value, unicode):
                        current_index = comb_values.index(value)
                    combobox.setCurrentIndex(current_index)             

            combobox.setStyleSheet('color: rgb({}, {}, {});'.format(r, g, b))
            treewidget.setItemWidget(item, order, combobox)

    def add_values(self, type, description):        
        if type == 'tier': 
            studio_tier = studioTier.Connect()
            descriptions = studio_tier.getSpecificTypes(self.current_show, description)
            if description not in descriptions:
                print 'not found any tier under descriptions called\"%s\"!...' % description
                return 
            return descriptions[description]
        
        if type == 'user':
            studio_userpool = studioUserpool.Connect()
            descriptions = studio_userpool.getSpecificTypes(self.current_show, description)   
            if description not in descriptions:
                print 'not found any user under descriptions called\"%s\"!...' % description
                return 
            return descriptions[description]
                    
    def submit(self, treewidget):       
        widget_data = self.get_widget_data(treewidget)
        input_data = widget_data
        
        reload(studioHeader)
        
        studio_header = studioHeader.Connect(name=self.current_description)
        studio_header.create(
            self.current_show, self.current_description_type, self.current_discipline, input_data)
    
    def get_widget_data(self, treewidget):
        '''
            self.input_data
            self.input_sort_data
            self.input_key_data
        '''
        
        input_data = {}
        
        widget_item = treewidget.invisibleRootItem()
        for index in range (widget_item.childCount()):
            current_item = widget_item.child(index)
            keys = current_item.text(0)
            
            each_data = {}
            for each in self.input_sort_data:
                header = self.input_data[each]
                
                if header['type'] == 'str':
                    current_value = current_item.text(header['order']).encode() 
                if header['type'] == 'enum':
                    combobox = treewidget.itemWidget(current_item, header['order'])
                    current_value = combobox.currentText().encode()
                                        
                each_data.setdefault(each.encode(), current_value)
            input_data.setdefault(keys.encode(), each_data)
               
        return input_data
 
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
        icon.addPixmap(
            QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(self.width - 5, self.height - 5))
        # button.setMinimumSize(QtCore.QSize(self.width, self.height))
        # button.setMaximumSize(QtCore.QSize(self.width, self.height))

                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main(parent=None)
    window.show()
    sys.exit(app.exec_())
