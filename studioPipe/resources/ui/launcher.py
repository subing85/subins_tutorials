'''
studioLauncher.py 0.0.1 
Date: April 06, 2019
Last modified: April 06, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os

import sys
sys.path.append('/venture/subins_tutorials')

from PySide import QtGui
from PySide import QtCore

from pprint import pprint
from studioPipe import resources
from studioPipe.utils import platforms


class Launcher(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)
        self.module, self.lable, self.version = platforms.get_tool_kit()
        
        self.setup_ui()
        self.load_menu_bar()
    
    def setup_ui(self):
        self.setObjectName('main_window')
        self.setWindowTitle(
            'Studio Launcher ({} {})'.format(self.lable, self.version))
        self.resize(300, 200)
              
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticallayout_main = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout_main.setObjectName('verticallayout')
        
        self.groupbox = QtGui.QGroupBox(self.centralwidget)
        self.groupbox.setTitle('Studio Launcher')
        self.groupbox.setObjectName('groupbox')
        self.verticallayout_main.addWidget(self.groupbox)
        
        self.verticallayout = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout.setObjectName('verticallayout')        

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.verticallayout.addLayout(self.horizontalLayout)
        self.label_logo = QtGui.QLabel(self)
        self.label_logo.setObjectName('label_subins_toolkits')
        self.label_logo.setPixmap(QtGui.QPixmap(
            os.path.join(resources.getIconPath(), 'subins_toolkits_1.png')))
        self.label_logo.setScaledContents(True)
        self.label_logo.setMinimumSize(QtCore.QSize(128, 128))
        self.label_logo.setMaximumSize(QtCore.QSize(128, 128))
        self.horizontalLayout.addWidget(self.label_logo)    
        
        self.button_launcher = QtGui.QPushButton(self)
        self.button_launcher.setFlat(True)
        self.button_launcher.setSizePolicy(
            QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred))
        self.button_launcher.setObjectName('button_launcher')
        self.button_launcher.setMinimumSize(QtCore.QSize(470, 100))
        self.button_launcher.setMaximumSize(QtCore.QSize(470, 100))
        launcher_icon = os.path.join(resources.getIconPath(), 'studio_launcher.png')
        self.image_to_button(
            self.button_launcher, path=launcher_icon, width=470, height=100)
        self.horizontalLayout.addWidget(self.button_launcher)
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)
        
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName('splitter') 
        self.verticallayout.addWidget(self.splitter)
                
        # self.listwidget_shows = QtGui.QListWidget(self.splitter)
        # self.listwidget_shows.setObjectName('listwidget_shows')
         
        # self.listwidget_tools = QtGui.QListWidget(self.splitter)
        # self.listwidget_tools.setObjectName('listwidget_tools')

    def load_menu_bar(self):    
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 23))
        self.menubar.setObjectName('menubar')
        self.setMenuBar(self.menubar)                
        
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setTitle('File')        
        self.menu_file.setObjectName('menu_file')
        self.menubar.addAction(self.menu_file.menuAction())
        
        self.menu_settings = QtGui.QMenu(self.menubar)
        self.menu_settings.setTitle('Settings')
        self.menu_settings.setObjectName('menu_settings')
        self.menubar.addAction(self.menu_settings.menuAction())
        
        self.action_konsole = QtGui.QAction(self)
        self.action_konsole.setObjectName('action_konsole')
        self.action_konsole.setText('Konsole')        
        
        self.action_preferences = QtGui.QAction(self)
        self.action_preferences.setObjectName('action_preferences')
        self.action_preferences.setText('Preferences')
                
        self.action_show = QtGui.QAction(self)
        self.action_show.setObjectName('action_show')
        self.action_show.setText('Show')   
             
        self.action_discipline = QtGui.QAction(self)
        self.action_discipline.setObjectName('action_discipline')
        self.action_discipline.setText('Discipline')
        
        self.action_tier = QtGui.QAction(self)
        self.action_tier.setObjectName('action_tier')
        self.action_tier.setText('Tier')
        
        self.action_header = QtGui.QAction(self)
        self.action_header.setObjectName('action_header')
        self.action_header.setText('Header')
        
        self.action_userpool = QtGui.QAction(self)
        self.action_userpool.setObjectName('action_userpool')
        self.action_userpool.setText('User Pool')    
              
        self.menu_file.addAction(self.action_konsole)
        
        self.menu_settings.addAction(self.action_preferences)
        self.menu_settings.addAction(self.action_show)
        self.menu_settings.addAction(self.action_discipline)
        self.menu_settings.addAction(self.action_tier)
        self.menu_settings.addAction(self.action_header)
        self.menu_settings.addAction(self.action_userpool)

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
        button.setIconSize(QtCore.QSize(width - 5, height - 5))

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Launcher(parent=None)
    window.show()
    sys.exit(app.exec_())        
        
