import os
import UI4
import pkgutil
import resources

from PyQt4 import QtGui
from Katana import Shelves
from functools import partial
from resources import console


class Menu(object):
        
    def __init__(self, title):        
        self.title = title 
        self.main_window = self.get_main_window()
        self.main_menu = self.get_mainmenu(parent=self.main_window)
        self.main_layout = self.get_mainlayout(parent=self.main_window)        
        self.shelves_path = resources.get_shelves_path()
        self.toolkit_path = resources.get_toolkit_path()
        self.icon_path = resources.get_icon_path()
        
    def show_pipe_menu(self):
        '''
        :example
            from resources import menu
            pipe_menu = menu.Menu('studio_toolkts')
            pipe_menu.show_pipe_menu()
        '''
        self.remove_menu()
        self.remove_toolbar()
        self.remove_console()
        self.setup_ui()
        self.create_from_shelf()
        self.create_from_toolkit()
        self.create_reload()      
        self.set_studio_console(bypass=True)
        
    def setup_ui(self):
        self.studio_menu = QtGui.QMenu(parent=self.main_menu)
        self.studio_menu.setObjectName('menu_%s' % self.title)
        self.studio_menu.setTitle(self.title)
        self.studio_menu.setTearOffEnabled(True)
        self.main_menu.addMenu(self.studio_menu)        
        self.studio_toolbar = QtGui.QToolBar(parent=self.main_window)
        self.studio_toolbar.setObjectName('toolbar_%s' % self.title)
        # self.studio_toolbar.setWindowTitle('Stuido PIPE Tools')
        # main_layout.addWidget(studio_toolbar)
        self.main_layout.insertWidget(1, self.studio_toolbar)       
        self.horizontallayout_console = QtGui.QHBoxLayout()
        self.horizontallayout_console.setObjectName('horizontallayout_console')
        self.main_layout.addLayout(self.horizontallayout_console)
        # self.main_layout.insertLayout(2, self.horizontallayout_console)
        self.button_clear = QtGui.QPushButton(self.main_window)     
        self.button_clear.setObjectName('button_clear')
        self.button_clear.setFlat(True)
        self.set_icon(self.button_clear, os.path.join(self.icon_path, 'clear.png'))
        self.horizontallayout_console.addWidget(self.button_clear)
        self.lindeedit_console = QtGui.QLineEdit(self.main_window)
        self.lindeedit_console.setObjectName('lindeedit_console')
        self.lindeedit_console.setReadOnly(False)
        self.clear_console(self.lindeedit_console)
        self.horizontallayout_console.addWidget(self.lindeedit_console)
        self.button_clear.clicked.connect(
            partial(self.clear_console, self.lindeedit_console))
                       
    def set_studio_console(self, bypass=True):  
        if bypass:
            return
        studio_console = console.Connect()
        studio_console.stdout().message_written.connect(self.show_console)
        print '\n#welcome to katana python tutorials [https://www.subins-toolkits.com]'
       
    def show_console(self, message):
        self.set_text_color(self.lindeedit_console, message)
        self.lindeedit_console.setText(message)
        
    def set_text_color(self, widget, message):
        info_color = QtGui.QColor('green')
        error_color = QtGui.QColor('red')
        warning_color = QtGui.QColor('magenta')
        header_color = QtGui.QColor('blue')
        normal_color = QtGui.QColor('yellow')       
        if '#header' in message:
            clolor_code = header_color
        elif '#info' in message:
            clolor_code = info_color   
        elif '#warning' in message:
            clolor_code = warning_color
        elif '#error' in message:
            clolor_code = error_color
        elif '#failed' in message:
            clolor_code = error_color   
        else:
            clolor_code = normal_color
        widget.setStyleSheet('color: %s' % clolor_code.name())        

    def clear_console(self, widget):
        widget.clear()
        widget.setStyleSheet('color: yellow')
        widget.setText('#welcome to katana python tutorials [https://www.subins-toolkits.com]')

    def get_main_window(self):
        return UI4.App.Layouts._PrimaryWindow    
    
    def _get_main_window(self):
        main_window = None
        for widget in QtGui.qApp.topLevelWidgets():
            if widget.objectName() != 'mainWindow':
                continue
            main_window = widget
            break
        return main_window
    
    def get_mainmenu(self, parent=None):
        if not  parent:
            parent = self.get_main_window()
        main_menu = parent.findChild(UI4.App.MainMenu.MainMenu)
        return main_menu
    
    def get_mainlayout(self, parent=None):
        if not  parent:
            parent = self.get_main_window()
        main_layout = parent.findChild(QtGui.QVBoxLayout)
        return main_layout
    
    def _get_mainlayout(self, parent=None):
        if not  parent:
            parent = self.get_main_window()
        main_layout = None    
        for each in parent.children():
            if each.objectName() != 'mainLayout':
                continue
            main_layout = each
            break
        return main_layout
    
    def remove_menu(self):
        for each in self.main_menu.findChildren(QtGui.QMenu):
            if each.objectName() != 'menu_%s' % self.title:
                continue
            each.deleteLater()
    
    def remove_toolbar(self):
        for index in range(self.main_layout.count()):
            item = self.main_layout.itemAt(index)
            widget = item.widget()
            if not widget:
                continue            
            if not isinstance(widget, QtGui.QToolBar):
                continue
            if widget.objectName() != 'toolbar_%s' % self.title:
                continue
            widget.deleteLater()
            
    def remove_console(self):
        for index in range(self.main_layout.count()):
            item = self.main_layout.itemAt(index)
            layout = item.layout()
            if not layout:
                continue
            if layout.objectName() != 'horizontallayout_console':
                continue
            for x in range(layout.count()):
                sub_item = layout.itemAt(x)
                sub_widget = sub_item.widget()
                sub_widget.deleteLater()
            layout.deleteLater()        

    def find_shelfs(self):        
        shelfs = []
        for each in os.listdir(self.shelves_path):
            path = os.path.join(self.shelves_path, each)
            if not os.path.isdir(path):
                continue
            shelfs.append(each)
        return shelfs
    
    def get_shelf_items(self):        
        shelfs = self.find_shelfs()
        shelf_items = {} 
        for shelf in shelfs:
            shelf_path = os.path.join(self.shelves_path, shelf)
            pipe_shelf = Shelves.Shelf(shelf, shelf_path, Shelves.SHELF_TYPE_USER)    
            shelf_items.setdefault(shelf, pipe_shelf)          
        return shelf_items    
    
    def get_toolkit_items(self):
        index = 0
        toolkit_items = {}        
        for importer, name, ispkg in pkgutil.iter_modules([self.toolkit_path]):
            loader = importer.find_module(name)
            module = loader.load_module(name)     
            if not hasattr(module, 'KEY'):
                continue
            if module.KEY != 'toolkit':
                continue    
            if hasattr(module, 'ORDER'):
                order = module.ORDER
            else:
                order = index
            toolkit_items.setdefault(order, []).append(module)            
            index += 1 
        return toolkit_items       
    
    def create_from_shelf(self):
        shelf_items = self.get_shelf_items()        
        for name, pipe_shelf in shelf_items.items():            
            shelf_menu = self.add_sub_menu(self.studio_menu, name, 'shelf')             
            #===================================================================
            # toolbar_menu = QtGui.QMenu(parent=self.studio_toolbar)
            # toolbar_menu.setObjectName('toolbar_menu_%s'%name)
            # toolbar_menu.setTitle(name)
            # self.studio_toolbar.addAction(shelf_menu.menuAction())            
            #===================================================================            
            for item in pipe_shelf.getItems():                
                name = item.getName()
                description = item.getDescription().replace('description: ', '')
                icon_name = item.getIconName()                
                action = self.add_actions(shelf_menu, name, description, icon_name)
                action.triggered.connect(partial(self.shelf_action, item))

    def create_from_toolkit(self):
        toolkit_items = self.get_toolkit_items()        
        for index, modules in toolkit_items.items():
            for module in modules: 
                if hasattr(module, 'ENABLE'):
                    if not module.ENABLE:
                        continue
                name = module.__name__                
                if hasattr(module, 'NAME'):
                    name = module.NAME
                description = 'not available'
                if hasattr(module, 'DESCRIPTION'):
                    description = module.DESCRIPTION
                icon = 'unknown.png'
                if hasattr(module, 'ICON'):
                    icon = module.ICON
                icon_file = os.path.join(self.icon_path, icon)                 
                action = self.add_actions(
                    self.studio_menu, name, description, icon_file)
                action.triggered.connect(partial(self.toolkit_action, module))     
    
    def create_reload(self):
        icon_file = os.path.join(self.icon_path, 'reload.png')  
        action = self.add_actions(self.studio_menu, 'reload', 'reload studio toolkit', icon_file)        
        action.triggered.connect(self.reload)                
    
    def add_sub_menu(self, parent, name, typed):
        sub_menu = QtGui.QMenu(parent=parent)        
        sub_menu.setObjectName('sub_menu_%s_%s' % (name, typed))
        sub_menu.setTitle(name)
        parent.addAction(sub_menu.menuAction())
        return sub_menu
    
    def add_actions(self, parent, name, description, icon):
        action = QtGui.QAction(parent)
        action.setText(name)
        action.setToolTip(description)
        self.set_icon(action, icon=icon)
        parent.addAction(action)
        self.studio_toolbar.addAction(action)
        return action    
    
    def set_icon(self, widget, icon=None):
        if not icon:
            icon = os.path.join(self.icon_path, 'unknown.png')            
        if not os.path.isfile(icon):
            icon = os.path.join(self.icon_path, 'unknown.png')
        qicon = QtGui.QIcon()
        qicon.addPixmap(QtGui.QPixmap(icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setIcon(qicon)
                
    def shelf_action(self, item):
        item.run(True, additionalEnvironment=None, checkScope=False)
        
    def toolkit_action(self, module):
        module.execute()
        
    def reload(self):
        self.show_pipe_menu()

