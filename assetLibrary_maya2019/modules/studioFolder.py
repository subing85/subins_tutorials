'''
studioFolders.py 0.0.1 
Date: January 16, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import shutil
import warnings

from PySide2 import QtWidgets
from PySide2 import QtGui

from assetLibrary_maya2019 import resources


class Folder(object):

    def __init__(self):
        self.folder_icon = os.path.join(resources.getIconPath(), 'folder.png')

    def load_folder_structure(self, path, treewidget):
        treewidget.clear()
        data = self.get_folder_structure()
        self.set_folder_structure(path, data, parent=treewidget)

    def get_folder_structure(self, path):
        directory_list = {}
        for root, dirs, files in os.walk(path):
            replace = root.replace(path, '')
            folderList = replace.split(os.sep)
            folders = directory_list
            for eachFolder in folderList:
                folders = folders.setdefault(eachFolder, {})
        return directory_list

    def set_folder_structure(self, root, data, parent=None):
        for each_path in data:
            item = parent
            current_path = os.path.join(root, each_path)
            if each_path:
                item = QtWidgets.QTreeWidgetItem(parent)
                item.setText(0, each_path)
                item.setToolTip(0, current_path)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.folder_icon),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(0, icon)
            self.set_folder_structure(
                current_path, data[each_path], parent=item)

    def create(self, folder_path=None, force=False):
        result = True, folder_path
        if os.path.isdir(folder_path):
            return False, 'Already found the folder %s ' % folder_path
        try:
            print 'create', folder_path
            os.makedirs(folder_path)
        except Exception as error:
            warnings.warn('\n#%s' % error)
            result = False, str(error)
        return result

    def rename(self, folder_path=None, name=None, force=False):
        if not os.path.exists(folder_path):
            return False,  'Can not found the directory'
        new_path = os.path.join(os.path.dirname(folder_path), name)
        print 'new_path', new_path
        result = True, new_path
        try:
            os.chmod(folder_path, 0777)
            os.rename(folder_path, new_path)
        except Exception as error:
            warnings.warn('\n#%s' % error)
            result = False, str(error)
        return result

    def remove(self, folder_path=None, force=False):
        if not os.path.isdir(folder_path):
            return False, 'Can not found the directory'
        result = True, folder_path
        try:
            os.chmod(folder_path, 0777)
            shutil.rmtree(folder_path)
        except Exception as error:
            warnings.warn('\n#%s' % error)
            result = False, str(error)
        return result

# end ####################################################################
