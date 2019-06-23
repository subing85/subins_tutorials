'''
main.py 0.0.1 
Date: January 15, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import sys
import webbrowser
import thread
import platform

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial

from assetLibrary_maya2018.modules import readWrite
from assetLibrary_maya2018.modules import studioFolder
from assetLibrary_maya2018.modules import studioAsset
from assetLibrary_maya2018.modules import studioPrint
from assetLibrary_maya2018.resources.ui import preferences
from assetLibrary_maya2018.resources.ui import catalogue
from assetLibrary_maya2018.resources.ui import asset
from assetLibrary_maya2018.utils import platforms
from assetLibrary_maya2018.core import inputs
from assetLibrary_maya2018 import resources


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None, standalone=False):
        super(MainWindow, self).__init__(parent)
        self.standalone = standalone
        self.image_object = None
        self.width, self.height = [500, 500]
        self.publish_format = 'asset'
        self.image_format = 'png'
        self.tool_mode = 'publish'
        self.currnet_publish = None
        self.q_image, self.q_image_path = None, None
        self.source_file, self.source_file_path = None, None
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.preference = preferences.Preference(parent=None)
        self.catalogue = catalogue.Catalogue(parent=None)
        self.asset = asset.Asset(parent=None)
        self.folder = studioFolder.Folder()
        # to check the preferencees
        resource_path = resources.getResourceTypes()['preference'].encode()
        self.rw = readWrite.ReadWrite(t='preference', path=resource_path,
                                      format='json', name='library_preferences', tag='asset_library')
        inputs = self.rw.get_inputs()
        self.create_type_values = ['None', 'import', 'reference']
        self.maya_type_values = ['None', 'mayaAscii', 'mayaBinary']
        self.maya_path = inputs[0]
        self.library_path = inputs[1]
        self.create_type = self.create_type_values[inputs[2]]
        self.maya_type = self.maya_type_values[inputs[3]]
        self.output_path = inputs[4]
        self.setup_ui()
        self.set_icons()
        self.load_library_folders(self.treewidget)
        if not self.standalone:
            self.parent_maya_layout()
        self.set_contex_menu()
        self.studio_print = studioPrint.Print(
            self.standalone, self.textedit_console)

    def setup_ui(self):
        self.resize(self.width, self.height)
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')
        self.setObjectName('mainwindow_%s' % self.tool_kit_object)
        self.setWindowTitle(self.tool_kit_titile)
        title_icon = os.path.join(resources.getIconPath(), 'title.png')
        self.setWindowIcon(QtGui.QIcon(title_icon))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.addWidget(self.catalogue.splitter)
        self.catalogue.splitter.addWidget(self.asset.groupbox_asset)
        self.treewidget = self.catalogue.treewidget_folder
        self.listwidget = self.catalogue.listwidget_catalogue
        self.label_filepath = self.asset.label_filepath
        self.lineedit_filepath = self.asset.lineedit_filepath
        self.pushbutton_filepath = self.asset.pushbutton_filepath
        self.label_imagepath = self.asset.label_imagepath
        self.lineedit_imagepath = self.asset.lineedit_imagepath
        self.pushbutton_imagepath = self.asset.pushbutton_imagepath
        self.lineedit_label = self.asset.lineedit_label
        self.button_publish = self.asset.button_publish
        self.button_build = self.asset.button_build
        self.textedit_history = self.asset.textedit_history
        self.button_snapshot = self.asset.button_snapshot
        self.textedit_console = self.asset.textedit_console
        self.pushbutton_filepath = self.asset.pushbutton_filepath
        self.groupbox_path = self.asset.groupbox_path
        if not self.standalone:
            self.textedit_console.hide()
            self.pushbutton_filepath.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.pushbutton_filepath.customContextMenuRequested.connect(
                partial(self.on_context_path, self.pushbutton_filepath))
            self.path_menu = QtWidgets.QMenu(self)
            self.action_scene = QtWidgets.QAction(self)
            self.action_scene.setObjectName('action_scene')
            self.action_scene.setText('Current Scene')
            self.path_menu.addAction(self.action_scene)
            self.action_scene.triggered.connect(
                partial(self.set_current_scene, self.lineedit_filepath))
        self.treewidget.itemClicked.connect(
            partial(self.load_current_folder, self.treewidget))
        self.button_snapshot.clicked.connect(
            partial(self.snapshot, self.button_snapshot))
        self.lineedit_label.returnPressed.connect(
            partial(self.rename_model, self.lineedit_label))        
        self.listwidget.itemClicked.connect(
            partial(self.builds, 'load', self.listwidget))
        self.listwidget.itemSelectionChanged.connect(
            partial(self.builds, 'load', self.listwidget))
        self.button_build.clicked.connect(
            partial(self.builds, 'build', self.listwidget))
        # self.listwidget.itemDoubleClicked.connect(
        #     partial(self.builds, 'build', self.listwidget))               
        self.pushbutton_filepath.clicked.connect(
            partial(self.set_source_file_path, self.lineedit_filepath))
        self.pushbutton_imagepath.clicked.connect(
            partial(self.set_source_image_path, self.lineedit_imagepath))
        self.treewidget.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget))
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 960, 25))
        self.menu_bar.setObjectName('menu_bar')
        self.setMenuBar(self.menu_bar)
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName('menu_file')
        self.menu_file.setTitle('File')
        self.menu_settings = QtWidgets.QMenu(self.menu_bar)
        self.menu_settings.setObjectName('menu_settings')
        self.menu_settings.setTitle('Settings')
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName('menu_help')
        self.menu_help.setTitle('Help')
        self.action_create = QtWidgets.QAction(self)
        self.action_create.setObjectName('action_create')
        self.action_create.setText('Create Folder')
        self.menu_default = QtWidgets.QMenu(self.menu_file)
        self.menu_default.setObjectName('menu_default')
        self.menu_default.setTitle('Default Folders')
        self.default_menu(self.menu_default)
        self.action_remove = QtWidgets.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove Folder')
        self.action_rename = QtWidgets.QAction(self)
        self.action_rename.setObjectName('action_rename')
        self.action_rename.setText('Rename Folder')
        self.action_refresh = QtWidgets.QAction(self)
        self.action_refresh.setObjectName('action_refresh')
        self.action_refresh.setText('Refresh')
        self.action_expand = QtWidgets.QAction(self)
        self.action_expand.setObjectName('action_expand')
        self.action_expand.setText('Expand')
        self.action_collapse = QtWidgets.QAction(self)
        self.action_collapse.setObjectName('action_collapse')
        self.action_collapse.setText('Collapse')
        self.action_quit = QtWidgets.QAction(self)
        self.action_quit.setObjectName('action_quit')
        self.action_quit.setText('Quit')
        self.action_preferences = QtWidgets.QAction(self)
        self.action_preferences.setObjectName('action_preferences')
        self.action_preferences.setText('Preferences')
        self.action_aboutool = QtWidgets.QAction(self)
        self.action_aboutool.setObjectName('action_aboutool')
        self.action_aboutool.setText('About Tool')
        self.action_abouttoolkits = QtWidgets.QAction(self)
        self.action_abouttoolkits.setObjectName('action_abouttoolkits')
        self.action_abouttoolkits.setText('About Tool Kits')
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_create)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_default.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_rename)
        self.menu_file.addAction(self.action_remove)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_refresh)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_preferences)
        self.menu_help.addAction(self.action_aboutool)
        self.menu_help.addAction(self.action_abouttoolkits)
        self.action_preferences.triggered.connect(self.show_preference)
        self.action_create.triggered.connect(self.create)
        self.action_rename.triggered.connect(self.rename)
        self.action_remove.triggered.connect(self.remove)
        self.action_refresh.triggered.connect(self.refresh)
        self.action_quit.triggered.connect(self.close_library)
        self.action_expand.triggered.connect(
            partial(self.expand, self.treewidget))
        self.action_collapse.triggered.connect(
            partial(self.collapse, self.treewidget))
        self.asset.button_publish.clicked.connect(self.publish)
        self.preference.button_apply.clicked.connect(self.set_preference)
        self.preference.button_cancel.clicked.connect(self.cancel_preference)
        self.action_aboutool.triggered.connect(self.toolkit_help_link)
        self.action_abouttoolkits.triggered.connect(self.toolkit_link)

    def toolkit_link(self):
        webbrowser.BaseBrowser(resources.getToolKitLink())
        self.studio_print.display_info(resources.getToolKitLink())

    def toolkit_help_link(self):
        webbrowser.open(resources.getToolKitHelpLink())
        self.studio_print.display_info(resources.getToolKitHelpLink())

    def set_icons(self):
        actions = self.findChildren(QtWidgets.QAction)
        qmenus = self.findChildren(QtWidgets.QMenu)
        for each_action in actions + qmenus:
            objectName = each_action.objectName()
            if not objectName:
                continue
            current_icon = '{}.png'.format(objectName.split('_')[-1])
            icon_path = os.path.join(resources.getIconPath(), current_icon)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            each_action.setIcon(icon)

    def on_context_menu(self, treewidget, paint):
        self.contex_menu.exec_(treewidget.mapToGlobal(paint))

    def on_context_path(self, button, paint):
        self.path_menu.exec_(button.mapToGlobal(paint))

    def default_menu(self, parent):
        data, order_data = inputs.get_input_data()
        for index in range(len(order_data)):
            if not data[order_data[index]]['enable']:
                continue
            action_default = QtWidgets.QAction(self)
            action_default.setObjectName('action_{}'.format(order_data[index]))
            action_default.setText(data[order_data[index]]['long_name'])
            action_default.setToolTip(data[order_data[index]]['tooltip'])
            action_default.triggered.connect(
                partial(self.create_default, order_data[index]))
            parent.addAction(action_default)

    def set_contex_menu(self):
        self.contex_menu = QtWidgets.QMenu(self)
        self.contex_menu.addAction(self.action_create)
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.menu_default.menuAction())
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.action_rename)
        self.contex_menu.addAction(self.action_remove)
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.action_refresh)
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.action_expand)
        self.contex_menu.addAction(self.action_collapse)

    def set_current_scene(self, linedeit):
        from pymel import core
        current_scene = core.sceneName()
        if not current_scene:
            self.source_file, self.source_file_path = False, None
        linedeit.setText(current_scene)
        self.source_file, self.source_file_path = True, str(current_scene)

    def show_preference(self):
        self.preference.show()

    def set_preference(self):
        self.preference.apply()
        inputs = self.rw.get_inputs()
        self.maya_path = inputs[0]
        self.library_path = inputs[1]
        self.create_type = self.create_type_values[inputs[2]]
        self.maya_type = self.maya_type_values[inputs[3]]
        self.output_path = inputs[4]
        self.load_library_folders(self.treewidget)

    def cancel_preference(self):
        self.setEnabled(True)

    def close_library(self):
        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)
        self.close()

    def expand(self, treewidget):  # expand the qtreeWidget
        if treewidget.selectedItems():
            current_item = treewidget.selectedItems()[-1]
            self.dependent_list = [current_item]
            self.collect_child_items(current_item)
            for each_dependency in self.dependent_list:
                treewidget.setItemExpanded(each_dependency, 1)
        else:
            treewidget.expandAll()

    def collapse(self, treewidget):  # collapse the qtreeWidget
        current_item = treewidget.invisibleRootItem()
        if treewidget.selectedItems():
            current_item = treewidget.selectedItems()[-1]
        self.dependent_list = [current_item]
        self.collect_child_items(current_item)
        for each_dependency in self.dependent_list:
            treewidget.collapseItem(each_dependency)

    def create_default(self, default):
        self.create(input=default)

    def create(self, input=None):
        folder_name = input
        if not input:
            folder_name, ok = QtWidgets.QInputDialog.getText(
                self, 'Input', 'Enter the folder name:', QtWidgets.QLineEdit.Normal)
            if not ok:
                self.studio_print.display_warning(
                    'abort the folder creation!...')
                return
        if not self.library_path:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found Publish directory', QtWidgets.QMessageBox.Ok)
            return
        current_path = os.path.join(self.library_path, folder_name)
        if self.treewidget.selectedItems():
            current_item = self.treewidget.selectedItems()[-1]
            tool_tip = str(current_item.toolTip(0))
            current_path = os.path.join(tool_tip, folder_name)
        if os.path.isdir(current_path):
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Already found the folder.\n%s' % current_path, QtWidgets.QMessageBox.Ok)
            return
        result, message = self.folder.create(folder_path=current_path)
        if not result:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', message, QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning('Create folder  - faild!...')
            return
        self.load_library_folders(self.treewidget)
        self.studio_print.display_info(
            '\"%s\" Folder create - success!...' % message)

    def rename(self):
        folder_name, ok = QtWidgets.QInputDialog.getText(
            self, 'Input', 'Enter the new name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        if not self.treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any selection\nSelect the folder and try', QtWidgets.QMessageBox.Ok)
            return
        current_item = self.treewidget.selectedItems()[-1]
        current_path = str(current_item.toolTip(0))
        result, message = self.folder.rename(
            folder_path=current_path, name=folder_name)
        if not result:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', message, QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning('Rename folder - faild!...')
            return
        self.load_library_folders(self.treewidget)
        self.studio_print.display_info(
            '\"%s\" Rename folder - success!...' % message)

    def remove(self):
        if not self.treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any selection\nSelect the folder and try', QtWidgets.QMessageBox.Ok)
            return
        replay = QtWidgets.QMessageBox.question(
            self, 'Question', 'Are you sure, you want to remove folder', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if replay == QtWidgets.QMessageBox.No:
            self.studio_print.display_warning('abort the remove folder!...')
            return
        for each_item in self.treewidget.selectedItems():
            current_path = str(each_item.toolTip(0))
            result, message = self.folder.remove(folder_path=current_path)
            if not result:
                QtWidgets.QMessageBox.warning(self, 'Warning', '%s\n%s' % (
                    current_path, message), QtWidgets.QMessageBox.Ok)
                self.studio_print.display_warning('Remove folder - faild!...')
        self.load_library_folders(self.treewidget)
        self.listwidget.clear()
        self.studio_print.display_info(
            '\"%s\" Remove folder - success!...' % message)

    def refresh(self):
        self.load_library_folders(self.treewidget)
        self.listwidget.clear()

    def load_library_folders(self, treewidget):
        if not self.library_path:
            return
        treewidget.clear()
        all_library_path = [self.library_path]
        for each_library in all_library_path:
            data = self.folder.get_folder_structure(each_library)
            self.folder.set_folder_structure(
                each_library, data, parent=treewidget)

    def load_current_folder(self, treewidget, *args):
        self.clear_publish()
        self.image_object = None
        current_items = treewidget.selectedItems()
        self.dependent_list = []
        for each_item in current_items:
            self.dependent_list.append(each_item)
            self.collect_child_items(each_item)
        self.load_publish_to_layout(self.listwidget, self.dependent_list)
        self.tool_mode = 'publish'

    def load_publish_to_layout(self, listwidget, items):
        publish_files = []
        for each_item in items:
            curren_path = each_item.toolTip(0)
            if not os.path.isdir(curren_path):
                continue
            publish_datas = os.listdir(curren_path)
            for each_publish in publish_datas:
                if not os.path.isfile(os.path.join(curren_path, each_publish)):
                    continue
                if not each_publish.endswith('.%s' % self.publish_format):
                    continue
                publish_files.append(os.path.join(curren_path, each_publish))
        listwidget.clear()
        for each_file in publish_files:
            item = QtWidgets.QListWidgetItem()
            listwidget.addItem(item)
            label = os.path.basename(os.path.splitext(each_file)[0])
            item.setText(label)
            item.setToolTip(each_file)
            icon = QtGui.QIcon()
            icon_path = each_file.replace(
                '.%s' % self.publish_format, '.%s' % self.image_format)
            if not os.path.isfile(icon_path):
                icon_path = os.path.join(
                    resources.getIconPath(), 'unknown.png')
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setTextAlignment(QtCore.Qt.AlignHCenter |
                                  QtCore.Qt.AlignBottom)
            thread.start_new_thread(
                self.validte_asset_publish, (each_file, item,))

    def validte_asset_publish(self, file, item):
        studio_asset = studioAsset.Asset()
        valid = studio_asset.had_valid(file)
        if valid:
            return
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)

    def collect_child_items(self, parent):
        for index in range(parent.childCount()):
            current_child = parent.child(index)
            self.dependent_list.append(current_child)
            self.collect_child_items(current_child)

    def set_source_file_path(self, widget):
        self.source_file, self.source_file_path = self.asset.set_source_path(
            widget, 'file')
        print self.source_file, self.source_file_path

    def set_source_image_path(self, widget):
        self.q_image, self.q_image_path = self.asset.set_source_path(
            widget, 'image')

    def publish(self):
        current_items = self.treewidget.selectedItems()
        if not current_items:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any folder selection.\nSelect the folder and try!...',
                QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning(
                'Not found any folder selection.')
            return
        current_path = str(current_items[-1].toolTip(0))
        if not os.path.isdir(current_path):
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found such Publish directory!...%s' % current_path,
                QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning(
                'Not found such Publish directory!...%s' % current_path)
            return
        if not self.source_file:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any source file!...', QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning('Not found any source file!...')
            return
        label = self.asset.lineedit_label.text()
        if not label:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found the Name of the the Publish!...',
                QtWidgets.QMessageBox.Ok)
            self.studio_print.display_warning(
                'Not found the Name of the the Publish!...')
            return  # add condition for mutlipe object

        self.source_file_path = os.path.abspath(
            str(self.lineedit_filepath.text())).replace('\\', '/')
        studio_asset = studioAsset.Asset(
            path=self.source_file_path, image=self.q_image)
        if studio_asset.had_file(current_path, label):
            replay = QtWidgets.QMessageBox.warning(
                self, 'Warning', 
                'Already a file with the same name in the publish\n\"%s\"\nIf you want to overwrite press Yes' % label,
                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            self.studio_print.display_warning(
                'Already a file with the same name in the publish')
            if replay != QtWidgets.QMessageBox.Yes:
                return
        user_comment = self.asset.textedit_history.toPlainText()
        result = studio_asset.save(
            current_path, label, user_comment=user_comment)
        self.load_current_folder(self.treewidget)
        self.clear_publish()
        self.source_file, self.source_file_path = False, None

        message = 'Publish success!...'
        if False in result:
            message = 'Publish Failed!...\n%s\n%s' % (
                result[False], '[more details and debugging subing85@gmail.com]')
            QtWidgets.QMessageBox.critical(
                self, 'Failed', message, QtWidgets.QMessageBox.Ok)
            self.studio_print.display_info(message)
            return
        QtWidgets.QMessageBox.information(
            self, 'Information', message, QtWidgets.QMessageBox.Ok)
        self.studio_print.display_info(message)

    def snapshot(self, button):
        if not self.treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found any selection\nSelect the folder and try',
                QtWidgets.QMessageBox.Ok)
            return
        self.clear_publish()
        self.q_image, self.q_image_path = self.asset.snapshot(button)

    def clear_publish(self):
        self.currnet_publish = None
        self.asset.image_to_button()
        self.lineedit_label.clear()
        self.button_publish.show()
        self.button_build.hide()
        self.textedit_history.clear()
        self.textedit_history.setReadOnly(False)
        self.groupbox_path.show()
        self.lineedit_filepath.show()
        self.lineedit_filepath.clear()
        self.lineedit_imagepath.show()
        self.lineedit_imagepath.clear()
        self.pushbutton_filepath.show()
        self.pushbutton_imagepath.show()

    def builds(self, tag, listwidge, *args):
        current_items = listwidge.selectedItems()
        if not current_items:
            self.clear_publish()
            return
        self.button_publish.hide()
        self.button_build.show()
        self.groupbox_path.hide()
        self.label_filepath.hide()
        self.lineedit_filepath.hide()
        self.pushbutton_filepath.hide()
        self.label_imagepath.hide()
        self.lineedit_imagepath.hide()
        self.pushbutton_imagepath.hide()
        publish_paths = []
        for each_item in current_items:
            publish_paths.append(str(each_item.toolTip()))
        self.currnet_publish = publish_paths[-1]
        studio_asset = studioAsset.Asset(paths=publish_paths)
        data = studio_asset.create(False, 'reference', fake=True)
        data = data[data.keys()[0]]
        comment = [data['comment'], 'author : %s' % data['author'], data['tag'],
                   data['#copyright'], 'user : %s' % data['user'], data['created_date']]
        self.textedit_history.setText('\n'.join(comment))
        self.textedit_history.setReadOnly(True)
        self.lineedit_label.setText(os.path.basename(
            os.path.splitext(publish_paths[-1])[0]))
        self.asset.image_to_button(
            path=studio_asset.get_image(publish_paths[-1]))

        if tag == 'build':
            if self.standalone:
                if not self.maya_path:
                    QtWidgets.QMessageBox.warning(
                        self, 'Warning', 'Please set the maya path!...',
                        QtWidgets.QMessageBox.Ok)
                    self.studio_print.display_warning(
                        'Please set the maya path!...')
                    return
                if not os.path.isdir(self.maya_path):
                    QtWidgets.QMessageBox.warning(
                        self, 'Warning', 'Not such maya path!...\n%s' % self.maya_path,
                        QtWidgets.QMessageBox.Ok)
                    self.studio_print.display_warning(
                        'Not such maya path!...\n%s' % self.maya_path)
                    return
            if not self.create_type or self.create_type == 'None':
                QtWidgets.QMessageBox.warning(
                    self, 'Warning', 'Please set the create type [import or reference]!...',
                    QtWidgets.QMessageBox.Ok)
                self.studio_print.display_warning(
                    'Please set the create type [import or reference]!...')
                return

            if not self.maya_type or self.maya_type == 'None':
                QtWidgets.QMessageBox.warning(
                    self, 'Warning', 'Please set the maya file type [mayaAscii or mayaBinary]!...',
                    QtWidgets.QMessageBox.Ok)
                self.studio_print.display_warning(
                    'Please set the maya file type [mayaAscii or mayaBinary]!...')
                return

            if self.standalone:
                QtWidgets.QApplication.setOverrideCursor(
                    QtCore.Qt.CustomCursor.WaitCursor)
                result = studio_asset.create(
                    'standalone', self.create_type, maya_type=self.maya_type,
                    maya_path=self.maya_path, output_path=self.output_path)
                message = 'maya file created in - {}'.format(result)
                self.studio_print.display_info(message)
                QtWidgets.QApplication.restoreOverrideCursor()
                if result:
                    QtWidgets.QMessageBox.information(
                        self, 'Information', message, QtWidgets.QMessageBox.Ok)
                    if platform.system() == 'Windows':
                        try:
                            os.startfile(os.path.dirname(result))
                        except:
                            pass
                    if platform.system() == 'Linux':
                        try:
                            os.system('xdg-open \"%s\"' %
                                      os.path.dirname(result))
                        except:
                            pass
                else:
                    QtWidgets.QMessageBox.warning(
                        self, 'Warning', 'maya file creation faild!...',
                        QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QApplication.setOverrideCursor(
                    QtCore.Qt.CustomCursor.WaitCursor)
                result = studio_asset.create(
                    'maya', self.create_type)
                QtWidgets.QApplication.restoreOverrideCursor()

    def rename_model(self, lineedit):
        studio_asset = studioAsset.Asset()
        if not self.currnet_publish:
            self.studio_print.display_warning(
                'Not selected any shader or shader not valid.')
            return
        current_image = studio_asset.get_image(self.currnet_publish)
        new_name = '%s' % lineedit.text()
        model_format = os.path.splitext(self.currnet_publish)[-1]
        self.folder.rename(folder_path=self.currnet_publish,
                           name='%s%s' % (new_name, model_format))
        image_format = os.path.splitext(current_image)[-1]
        self.folder.rename(folder_path=current_image,
                           name='%s%s' % (new_name, image_format))
        self.load_current_folder(self.treewidget)

    def parent_maya_layout(self):
        from maya import cmds
        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)
        object_name = str(self.objectName())
        self.floating_layout = cmds.paneLayout(
            cn='single', w=self.width, p=platforms.get_main_window())
        cmds.dockControl(self.tool_kit_object, l=self.tool_kit_titile, area='right',
                         content=self.floating_layout, allowedArea=['right', 'left'])
        cmds.control(object_name, e=1, p=self.floating_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_())
