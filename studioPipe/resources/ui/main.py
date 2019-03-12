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

sys.path.append('/venture/subins_tutorials')

from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime

from studioPipe import resources
from studioPipe.utils import platforms
from studioPipe.api import studioShows
from studioPipe.api import studioInput



import catalogue
import input

reload(input)


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

        self.setup_ui()
        # self.load_widgets()
        self.load_tool_bar()
        self.set_icons()
        self.load_shows_to_layout(self.listWidget_shows)
        self.load_discipline(self.treewidget_discipline)   
        

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
        self.treewidget_discipline.headerItem().setText(0,'Deciplines')
               
        self.splitter.addWidget(self.treewidget_discipline)
        
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setObjectName('treewidget')        
        self.splitter.addWidget(self.treewidget) 
        
        self.groupbox_details = QtGui.QGroupBox(self.splitter)
        self.groupbox_details.setObjectName('groupbox_details')
        self.groupbox_details.setTitle('Details')
        self.splitter.addWidget(self.groupbox_details)
        self.splitter.setSizes([171, 381, 108])
        

               
    
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
        
        self.action_add_tag = QtGui.QAction(self)
        self.action_add_tag.setObjectName('action_add_tag')
        self.action_add_tag.setText('Add Tag')
        self.action_add_tag.setToolTip('Add Discipline')
        
        self.action_remove_tag = QtGui.QAction(self)
        self.action_remove_tag.setObjectName('action_remove_tag')      
        self.action_remove_tag.setText('Remove Tag')
        self.action_remove_tag.setToolTip('Add Discipline')
        
        self.toolBar.addAction(self.action_add_discipline)
        self.toolBar.addAction(self.action_remove_discipline)
        self.toolBar.addSeparator ()        
        self.toolBar.addAction(self.action_add_tag)
        self.toolBar.addAction(self.action_remove_tag)
        self.action_add_discipline.triggered.connect(self.add_discipline)
        
        
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
                QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
            

    def set_my_show(self, listwidget, *args):        
        current_items = listwidget.selectedItems()
        if not current_items:
            return        
        current_show = current_items[-1].statusTip()        
        if current_show not in self.show_data:
            print 'Value error, not found your show %s'%current_show
            return
        
        self.verticalLayout_shows_a.addWidget(self.listWidget_shows)

        self.listWidget_shows.setMinimumSize(QtCore.QSize(290, 0))
        self.listWidget_shows.setMaximumSize(QtCore.QSize(290, 16777215))             
        self.groupbox_shows.hide()
        
        self.groupbox_show.show()
        self.groupbox_toolbar.show()
        print current_show
        
    
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
        
    def load_discipline (self, treewidget):
        cursor = studioInput.Connect('discipline', value='disciplines')
        disciplines, sort_disciplines = cursor.getInputData()
        
        for each_discipline in sort_disciplines:            
            display_name = disciplines[each_discipline]['display_name']
            tooltip = disciplines[each_discipline]['tooltip']
            
            icon_path = os.path.join(
                resources.getIconPath(), '%s.png'%each_discipline)
            
            item = QtGui.QTreeWidgetItem(treewidget)
            item.setText(0, display_name)
            item.setToolTip(0, tooltip)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(0, icon)            
        
        treewidget.setIconSize(QtCore.QSize(50, 50))
      
    
    def add_discipline(self):
        print self.splitter.sizes ()
               
        self.input_window = input.Window(
            parent=None, type='discipline', value='discipline_child_inputs')
        self.input_window.show()

                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main(parent=None)
    window.show()
    sys.exit(app.exec_())
