import os
import sys
import copy

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.core import sconsole  
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.resource.ui import show


class Window(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None, mode=None):  
        super(Window, self).__init__(parent)
        self.mode = mode        
        self.title = 'Studio Launcher'
        self.width = 720
        self.height = 750
        self.show_icon_size = [256, 128]
        self.show_data = {}
        self.current_show = None
        self.shows = studioShow.Show()
        self.setup_ui()
        # self.setup_console()        
        self.setup_menu()
        self.setup_toolbar()
        self.setup_icons()
        self.setup_default()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_launcher')
        self.resize(self.width, self.height)        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')        
        self.setCentralWidget(self.centralwidget)        
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(5, 5, 5, 5) 
        self.verticallayout_item, self.button_show = swidgets.set_header(
            self, self.title, self.verticallayout, show_icon=None)           
        self.groupbox_toolbar = QtWidgets.QGroupBox(self)
        self.groupbox_toolbar.setObjectName('groupbox_toolbar')
        self.groupbox_toolbar.setTitle('.')
        sizepolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.groupbox_toolbar.setSizePolicy(sizepolicy)        
        self.verticallayout_item.addWidget(self.groupbox_toolbar)
        self.horizontallayout_toolbar = QtWidgets.QHBoxLayout(self.groupbox_toolbar)
        self.horizontallayout_toolbar.setSpacing(0)
        self.horizontallayout_toolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_toolbar.setObjectName('horizontallayout_toolbar')
        self.splitter_main = QtWidgets.QSplitter(self)
        self.splitter_main.setObjectName('splitter_main')
        self.splitter_main.setLineWidth(0)
        self.splitter_main.setHandleWidth(0)
        self.splitter_main.setMidLineWidth(0)            
        self.splitter_main.setOrientation(QtCore.Qt.Horizontal)
        self.verticallayout_item.addWidget(self.splitter_main)  
        self.listwidget_shows = QtWidgets.QListWidget(self)
        self.listwidget_shows.setObjectName('listwidget_shows')    
        self.listwidget_shows.setMinimumSize(QtCore.QSize(235, 0))
        self.listwidget_shows.setMaximumSize(QtCore.QSize(235, 16777215)) 
        self.listwidget_shows.setSortingEnabled(False)
        self.listwidget_shows.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget_shows.setProperty('isWrapping', True)
        self.listwidget_shows.setResizeMode(QtWidgets.QListView.Adjust)
        self.listwidget_shows.setSpacing(0)
        self.listwidget_shows.setUniformItemSizes(True)
        self.listwidget_shows.setViewMode(QtWidgets.QListView.IconMode)
        self.listwidget_shows.setMovement(QtWidgets.QListView.Static)
        self.listwidget_shows.setSelectionRectVisible(True)
        self.listwidget_shows.setIconSize(
            QtCore.QSize(self.show_icon_size[0], self.show_icon_size[1]))
        self.splitter_main.addWidget(self.listwidget_shows)
        self.listwidget_shows.itemClicked.connect(self.set_current_show)
        self.splitter_applications = QtWidgets.QSplitter(self)
        self.splitter_applications.setObjectName('splitter_applications')
        self.splitter_applications.setLineWidth(0)
        self.splitter_applications.setHandleWidth(0)  
        self.splitter_applications.setMidLineWidth(0)
        self.splitter_applications.setOrientation(QtCore.Qt.Vertical)        
        self.splitter_main.addWidget(self.splitter_applications)
        self.splitter_outputs = QtWidgets.QSplitter(self)
        self.splitter_outputs.setObjectName('splitter_outputs')
        self.splitter_outputs.setLineWidth(0)
        self.splitter_outputs.setHandleWidth(0)   
        self.splitter_outputs.setMidLineWidth(0)
        self.splitter_outputs.setOrientation(QtCore.Qt.Horizontal)        
        self.splitter_applications.addWidget(self.splitter_outputs)
        self.listwidget_show_applications = QtWidgets.QListWidget(self)
        self.listwidget_show_applications.setObjectName('listwidget_show_applications')   
        self.listwidget_show_applications.setSortingEnabled(False)
        self.listwidget_show_applications.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget_show_applications.setProperty('isWrapping', True)
        self.listwidget_show_applications.setResizeMode(QtWidgets.QListView.Adjust)
        self.listwidget_show_applications.setSpacing(10)
        self.listwidget_show_applications.setUniformItemSizes(True)
        self.listwidget_show_applications.setViewMode(QtWidgets.QListView.IconMode)
        self.listwidget_show_applications.setSelectionRectVisible(True)
        self.listwidget_show_applications.setMovement(QtWidgets.QListView.Static)
        self.listwidget_show_applications.setIconSize(QtCore.QSize(64, 64))  
        self.splitter_outputs.addWidget(self.listwidget_show_applications)             
        self.listwidget_show_applications.itemDoubleClicked.connect(self.set_current_show_application)
        self.listwidget_build_in_applications = QtWidgets.QListWidget(self)
        self.listwidget_build_in_applications.setObjectName('listwidget_applications')   
        self.listwidget_build_in_applications.setSortingEnabled(False)
        self.listwidget_build_in_applications.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwidget_build_in_applications.setProperty('isWrapping', True)
        self.listwidget_build_in_applications.setResizeMode(QtWidgets.QListView.Adjust)
        self.listwidget_build_in_applications.setSpacing(10)
        self.listwidget_build_in_applications.setUniformItemSizes(True)
        self.listwidget_build_in_applications.setViewMode(QtWidgets.QListView.IconMode)
        self.listwidget_build_in_applications.setSelectionRectVisible(True)
        self.listwidget_build_in_applications.setMovement(QtWidgets.QListView.Static)
        self.listwidget_build_in_applications.setIconSize(QtCore.QSize(64, 64))  
        self.splitter_outputs.addWidget(self.listwidget_build_in_applications)     
        self.listwidget_build_in_applications.itemDoubleClicked.connect(self.set_current_show_application)
        self.textedit_output = QtWidgets.QTextEdit(self)
        self.textedit_output.setObjectName('textedit_output')
        self.splitter_applications.addWidget(self.textedit_output)
        self.splitter_main.setSizes([235, 459])                  
        self.splitter_applications.setSizes([390, 120])                  
        self.splitter_outputs.setSizes([328, 131])                   
        
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
    
    def create_show(self):
        print self.splitter_main.sizes()                  
        print self.splitter_applications.sizes()                  
        print self.splitter_outputs.sizes()   
        show_window = show.Window(launcher=self)             
        show_window.show()
        
    def setup_default(self):
        self.show_data = self.shows.get_preset_data()
        sorted_shows = common.sorted_show_order(self.show_data)
        self.listwidget_shows.clear()
        print '#header available shows information'
        for each in sorted_shows:
            swidgets.add_listwidget_item(
                self.listwidget_shows,
                self.show_data [each]['current_show']['show']['long_name'][1],
                key=each,
                icon_path=self.show_data[each]['current_show']['show']['icon'][1]
                )
            print 'show: '.rjust(15), self.show_data [each]['current_show']['show']['long_name'][1]
            print 'name: '.rjust(15), self.show_data [each]['current_show']['show']['show_name'][1]
            print 'usd: '.rjust(15), str(self.show_data [each]['current_show']['show']['USD'][1])
            print 'show path: '.rjust(15), self.show_data [each]['current_show']['show']['show_path'][1], '\n'

    def set_current_show(self):
        currentitem = self.listwidget_shows.currentItem()
        self.current_show = currentitem.statusTip()    
        show_contents = self.show_data[self.current_show]['current_show']['show']
        print '#header current show information'
        print 'current show: '.rjust(15), show_contents['long_name'][1]
        print 'name: '.rjust(15), show_contents['show_name'][1]
        print 'usd: '.rjust(15), str(show_contents['USD'][1])
        print 'show path: '.rjust(15), show_contents['show_path'][1]
        print '\n#header available show applications information'
        self.listwidget_show_applications.clear()
        show_application_contents = self.show_data[self.current_show]['show_applications']
        common_application_contents = self.show_data[self.current_show]['common_applications']
        build_in_application_contents = self.show_data[self.current_show]['build-in_applications']
        
        self.setup_applications('show_applications', show_application_contents, self.listwidget_show_applications)
        self.setup_applications('common_applications', common_application_contents, self.listwidget_show_applications)
        self.setup_applications('build-in_applications', build_in_application_contents, self.listwidget_build_in_applications)
        
    def setup_applications(self, application_type, application_contents, listwidget):
        if not application_contents:
            return
        sorted_contents = common.sort_dictionary(application_contents)
        for each in sorted_contents:            
            if each == 'show':
                continue
            contents = application_contents[each]
            print '%s|%s' % (application_type, each)
            swidgets.add_listwidget_item(
                listwidget,
                contents['version'][1],
                key='%s|%s' % (application_type, each),
                icon_path=contents['icon'][1]
                )
            print 'version: '.rjust(15), contents['version'][1]
            print 'source: '.rjust(15), contents['exe'][1]
            print 'path: '.rjust(15), contents['path'][1], '\n'
                      
            
    def set_current_show_application(self, *args):
        currentitem = args[0]
        application_type, current_application = currentitem.statusTip().split('|')
        show_contents = self.show_data[self.current_show]['current_show']['show']
        show_application_contents = self.show_data[self.current_show][application_type][current_application]
        print '#header current show and show applications information'
        print 'current show: '.rjust(15), show_contents['long_name'][1]
        print 'name: '.rjust(15), show_contents['show_name'][1]
        print 'usd: '.rjust(15), str(show_contents['USD'][1]), '\n'
        print 'show path: '.rjust(15), show_contents['show_path'][1]
        print 'version: '.rjust(15), show_application_contents['version'][1]
        print 'source: '.rjust(15), show_application_contents['exe'][1]
        print 'path: '.rjust(15), show_application_contents['path'][1]
        self.shows.launch(
            self.current_show,
            application_type,
            current_application,
            contents=self.show_data[self.current_show],
            thread=True
            )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())         
