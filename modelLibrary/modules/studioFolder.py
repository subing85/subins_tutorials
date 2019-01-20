import os
import shutil
import warnings

from pprint import pprint
from PySide import QtCore
from PySide import QtGui

from modelLibrary import resources

class Folder(object):
    
    def __init__(self, path=None):        
        self.path = None        
        if path:
            self.path = path            
        self.folder_icon = os.path.join(resources.getIconPath(), 'folder.png')
        
        
    def load_folder_structure(self, treewidget):
        treewidget.clear()
        data = self.get_folder_structure()
        self.set_folder_structure(data, parent=treewidget)
        
                    
    def get_folder_structure(self):        
        directory_list = {}
        for root, dirs, files in os.walk(self.path):
            replace = root.replace(self.path, '')
            folderList = replace.split(os.sep)
            folders = directory_list
            for eachFolder in folderList:
                folders = folders.setdefault(eachFolder, {})         
        return directory_list   

    def set_folder_structure(self, data, parent=None, path=None):
        if not path:
            path = self.path        
        for each_path in data:            
            item = parent
            current_path = os.path.join(path, each_path)        
            if each_path:      
                item = QtGui.QTreeWidgetItem(parent)
                item.setText(0, each_path)
                base_path = current_path.replace('%s/' % self.path, '')
                item.setToolTip(0, base_path)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.folder_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)                
                item.setIcon(0, icon)
            self.set_folder_structure(data[each_path], parent=item, path=current_path)

    def create(self, basename=None, force=False):        
        if not basename:            
            return        
        folder_path = os.path.join(self.path, basename)
        result = True, folder_path
        if os.path.isdir(folder_path):
            return False, 'Already found the folder %s ' % folder_path
        try:        
            os.makedirs(folder_path)
        except Exception as error:
            warnings.warn('\n#%s' % error)
            result = False, str(error)            
        return result
  
    
    def rename(self, basename=None, name=None, force=False):
        folder_path = self.path
        if basename:        
            folder_path = os.path.join(self.path, basename)           
        if not os.path.isdir(folder_path):
            return False,  'Can not found directory'

        new_path = os.path.join(os.path.dirname(folder_path), name)
        result = True, new_path        
        try:
            os.chmod(folder_path, 0777)
            os.rename(folder_path, new_path)    
        except Exception as error:
            warnings.warn('\n#%s' % error)
            result = False, str(error)           
        return result
   
    
    def remove(self, basename=None, force=False):
        folder_path = self.path
        if basename:        
            folder_path = os.path.join(self.path, basename)

        if not os.path.isdir(folder_path):
            return False, 'Can not found directory'
            
        result = True, folder_path   
                     
        try:
            os.chmod(folder_path, 0777)
            shutil.rmtree(folder_path)
        except Exception as error:
            warnings.warn('\n#%s' % error)  
            result = False, str(error)                 
        return result  

