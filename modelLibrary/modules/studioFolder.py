import os

from pprint import pprint

class Folder(object):
    
    def __init__(self, path=None):        
        self.path = None        
        if path:
            self.path = path

    
    def get_folder_structure(self):        
        directory_list = {}
        for root, dirs, files in os.walk(self.path):
            replace = root.replace(self.path, '')
            folderList = replace.split(os.sep)
            folders = directory_list
            for eachFolder in folderList:
                folders = folders.setdefault(eachFolder, {})         
        return directory_list
    
    
    def create_folder(self, path):
        pass
    
    def remove_folder(self, path):
        pass
    
    def rename_folder(self, path):
        pass
    
    

folder = Folder(path='/venture/packages')

a = folder.get_folder_structure()
pprint(a)   

