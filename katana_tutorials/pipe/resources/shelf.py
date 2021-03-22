# Studio Pipe Additional Shelves

# more details
# https://learn.foundry.com/katana/Content/tg/shelf_item_scripts/shelf_item_scripts.html

import os
import shutil
import resources  # pipe module

from Katana import Shelves


class Shelf(object):
    
    def __init__(self, name, icon, commands, **kwargs):
        self.name = name
        self.icon = icon
        self.commands = commands
        self.shelf_name = 'studio_toolkit'
        self.description = 'description: '
        self.shortcut = None
        self.scope = None        
        if 'shelf_name' in kwargs:
            self.shelf_name = kwargs['shelf_name']        
        if 'description' in kwargs:
            self.description = kwargs['description']   
        if 'shortcut' in kwargs:
            self.shortcut = kwargs['shortcut']                        
        if 'scope' in kwargs:
            self.scope = kwargs['scope']
        self.shelf_path = os.path.join(resources.get_shelves_path(), self.shelf_name)
        self.icon_path = os.path.join(resources.get_icon_path(), self.icon)
        self.shelf_type = Shelves.SHELF_TYPE_USER
        self.make_pipe_shelf()
    
    def make_pipe_shelf(self):
        if self.shelf_name != 'studio_toolkit':
            self.shelf_path = os.path.join(resources.get_shelves_path(), self.shelf_name)
        print self.shelf_path
        if os.path.isdir(self.shelf_path):
            return
        os.makedirs(self.shelf_path)
        
    def has_item(self):
        if self.shelf_name != 'studio_toolkit':
            self.shelf_path = os.path.join(resources.get_shelves_path(), self.shelf_name)
        pipe_shelf = Shelves.Shelf(
            self.name, self.shelf_path, Shelves.SHELF_TYPE_USER)
        item = pipe_shelf.find(self.name) 
        if item:
            return True, item, pipe_shelf
        return False, None, pipe_shelf
    
    def create(self):        
        '''
        :example
            from resources import shelf
            reload(shelf)
            name = 'disable_nodes'
            icon = 'disable.png'
            
            commands = [
                'from core import nodegraph',
                'nodegraph.set_knode_disable()'
                ]
            
            pipe_shelf = shelf.Shelf(name, icon, commands)
            pipe_shelf.create()  
        '''        
        valid, item, shelf = self.has_item()
        if valid:
            # source_file = item.getSourceFile()
            # os.remove(source_file)
            item.deleteSourceFile()
        item = shelf.createItem(
            self.name,
            self.description,
            # keyboardShortcut=self.shortcut,
            icon=self.icon_path
            )
        item.setScope(self.scope)
        self.add_commands(item, self.commands)
        
    def add_commands(self, item, commands):
        code = item.getCode()        
        default_code = code.rsplit('print(\"hello, world\")', 1)[0]
        command_code = default_code + '\n'.join(commands)
        with (open(item.getSourceFile(), 'w')) as code_open:
            code_open.write(command_code)
            return True
        return False
    
    def clear(self):
        try:
            shutil.rmtree(self.shelf_path)
        except Exception as error:
            print error
            
    def find_shelfs(self):
        shelfs = []       
        for each in os.listdir(self.shelves_path):
            path = os.path.join(self.shelves_path, each)
            if not os.path.isdir(path):
                continue
            shelfs.append(each)
        return shelfs
        
