import os
import sys
import copy

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.core import sconsole  
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.resource.ui import show


class Window(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None, mode=None):  
        super(Window, self).__init__(parent)
        # self.setParent(parent)
        self.mode = mode        
        self.title = 'Studio Launcher'
        self.width = 1140
        self.height = 820        
        self.show_icon_size = [256, 128]
        self.version, self.label = self.set_tool_context()        
        self.show_data = {}
        self.current_show = None
        self.current_application = None        
        self.shows = studioShow.Show()
        self.show_window = show.Window()     
        self.setup_ui()
        self.setup_console()        
        self.setup_menu()
        self.setup_toolbar()
        self.setup_icons()
        self.set_default()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_launcher')
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
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None) 
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName("groupbox")
        self.groupbox.setTitle('.')
        self.verticallayout_item.addWidget(self.groupbox)        
        self.horizontallayout_toolbar = QtWidgets.QHBoxLayout(self.groupbox)
        self.horizontallayout_toolbar.setSpacing(0)
        self.horizontallayout_toolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_toolbar.setObjectName('horizontallayout_toolbar')
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setObjectName('horizontallayout_input')        
        self.horizontallayout_input.setSpacing(0)
        self.verticallayout_item.addLayout(self.horizontallayout_input)
        self.listwidget_shows = QtWidgets.QListWidget(self)
        self.listwidget_shows.setObjectName('listwidget_shows')    
        self.listwidget_shows.setMinimumSize(QtCore.QSize(250, 0))
        self.listwidget_shows.setMaximumSize(QtCore.QSize(250, 16777215)) 
        self.listwidget_shows.setSortingEnabled(False)
        self.listwidget_shows.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget_shows.setProperty('isWrapping', True)
        self.listwidget_shows.setResizeMode(QtWidgets.QListView.Adjust)
        self.listwidget_shows.setSpacing(0)
        self.listwidget_shows.setUniformItemSizes(True)
        self.listwidget_shows.setViewMode(QtWidgets.QListView.IconMode)
        self.listwidget_shows.setMovement(QtWidgets.QListView.Static)
        self.listwidget_shows.setSelectionRectVisible(True)
        self.listwidget_shows. setIconSize(QtCore.QSize(self.show_icon_size[0], self.show_icon_size[1]))
        self.horizontallayout_input.addWidget(self.listwidget_shows)
        self.listwidget_shows.itemClicked.connect(self.set_current_show)
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setObjectName('splitter')        
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.horizontallayout_input.addWidget(self.splitter)
        self.listwidget_tools = QtWidgets.QListWidget(self)
        self.listwidget_tools.setObjectName('listwidget_tools')   
        self.listwidget_tools.setSortingEnabled(False)
        self.listwidget_tools.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget_tools.setProperty('isWrapping', True)
        self.listwidget_tools.setResizeMode(QtWidgets.QListView.Adjust)
        self.listwidget_tools.setSpacing(10)
        self.listwidget_tools.setUniformItemSizes(True)
        self.listwidget_tools.setViewMode(QtWidgets.QListView.IconMode)
        self.listwidget_tools.setSelectionRectVisible(True)
        self.listwidget_tools.setMovement(QtWidgets.QListView.Static)
        self.listwidget_tools.setIconSize(QtCore.QSize(64, 64))  
        self.listwidget_tools.itemDoubleClicked.connect(self.set_current_tool)
        self.splitter.addWidget(self.listwidget_tools)                
        self.textedit_output = QtWidgets.QTextEdit(self)
        self.textedit_output.setObjectName('textedit_output')
        self.splitter.addWidget(self.textedit_output)
        self.splitter.setSizes([440, 136])

    def setup_menu(self):        
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')
        self.action_create_show = QtWidgets.QAction(self)
        self.action_create_show.setObjectName('action_create_show')
        self.action_create_show.setToolTip('create new show') 
        self.action_create_show.setText('Create show')                   
        self.menu.addAction(self.action_create_show)
        self.menu.addSeparator()
        self.action_create_show.triggered.connect(self.create_show)
        
    def setup_toolbar(self):             
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.addSeparator()        
        self.toolbar.addAction(self.action_create_show)
        self.toolbar.addSeparator()
        self.horizontallayout_toolbar.addWidget(self.toolbar)

    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)    
        
    def setup_console(self):
        console = sconsole.Console()    
        console.stdout(self.textedit_output).message_written.connect(
            self.textedit_output.insertPlainText)
                
    def set_tool_context(self):
        config = sheader.Header()
        config.tool()
        return config.version, config.pretty
    
    def create_show(self):
        self.show_window.show()
        
    def set_default(self):
        self.show_data = self.shows.get_preset_data()
        sorted_shows = common.sorted_show_order(self.show_data)
        self.listwidget_shows.clear()
        print '#header available shows information'        
        for each in sorted_shows:
            swidgets.add_listwidget_item(
                self.listwidget_shows,
                self.show_data [each]['current_show']['show']['long_name'],
                key=each,
                icon_path=self.show_data[each]['current_show']['show']['icon']
                )
            print 'show: '.rjust(15), self.show_data [each]['current_show']['show']['long_name']
            print 'name: '.rjust(15), self.show_data [each]['current_show']['show']['name']
            print 'usd: '.rjust(15), str(self.show_data [each]['current_show']['show']['USD'])
            print 'show path: '.rjust(15), self.show_data [each]['current_show']['show']['show_path'], '\n'

    def set_current_show(self):
        currentitem = self.listwidget_shows.currentItem()
        self.current_show = currentitem.statusTip()    
        application_contents = self.show_data[self.current_show]['applications']
        sorted_contents = common.sort_dictionary(application_contents)
        self.listwidget_tools.clear()
        show_contents = self.show_data[self.current_show]['current_show']['show']        
        print '#header current show information'
        print 'current show: '.rjust(15), show_contents['long_name']
        print 'name: '.rjust(15), show_contents['name']
        print 'usd: '.rjust(15), str(show_contents['USD'])
        print 'show path: '.rjust(15), show_contents['show_path']
        print '\n#header available applications information'
        for each in sorted_contents:            
            if each == 'show':
                continue
            contents = application_contents[each]
            swidgets.add_listwidget_item(
                self.listwidget_tools,
                contents['version'],
                key=each,
                icon_path=contents['icon']
                )
            print 'version: '.rjust(15), contents['version']
            print 'source: '.rjust(15), contents['exe']
            print 'path: '.rjust(15), contents['path'], '\n'              
            
    def set_current_tool(self, bin=True):
        currentitem = self.listwidget_tools.currentItem()
        self.current_application = currentitem.statusTip()
        show_contents = self.show_data[self.current_show]['current_show']['show']
        application_contents = self.show_data[self.current_show]['applications'][self.current_application]
        print '#header current show and applications information'
        print 'current show: '.rjust(15), show_contents['long_name']
        print 'name: '.rjust(15), show_contents['name']
        print 'usd: '.rjust(15), str(show_contents['USD']), '\n'
        print 'show path: '.rjust(15), show_contents['show_path']
        print 'version: '.rjust(15), application_contents['version']
        print 'source: '.rjust(15), application_contents['exe']
        print 'path: '.rjust(15), application_contents['path']
        self.shows.launch(
            self.current_show,
            self.current_application,
            contents=self.show_data[self.current_show],
            bin=False
            )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())         
