'''
main.py 0.0.1 
Date: January 15, 2019
Last modified: February 10, 2019
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

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial

from maya import OpenMaya
from maya import cmds

from shaderLibrary_maya2017.modules import readWrite
from shaderLibrary_maya2017.modules import studioFolder
from shaderLibrary_maya2017.modules import studioMaya
from shaderLibrary_maya2017.modules import studioShader
from shaderLibrary_maya2017.resources.ui import preferences
from shaderLibrary_maya2017.resources.ui import catalogue
from shaderLibrary_maya2017.resources.ui import model
from shaderLibrary_maya2017.utils import platforms
from shaderLibrary_maya2017 import resources


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=platforms.get_qwidget()):
        super(MainWindow, self).__init__(parent)
        self.image_object = None
        self.width, self.height = [500, 500]
        self.publish_format = 'shader'
        self.image_format = 'png'
        self.tool_mode = 'publish'
        self.currnet_publish = None

        self.preference = preferences.Preference(parent=None)
        self.folder = studioFolder.Folder()
        self.studio_maya = studioMaya.Maya()
        self.catalogue = catalogue.Catalogue(parent=None)
        self.model = model.Model(parent=None)
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        # to check the preferencees
        resource_path = resources.getResourceTypes()['preference'].encode()
        self.rw = readWrite.ReadWrite(
            t='preference',
            path=resource_path,
            format='json',
            name='library_preferences',
            tag='shader_library')
        self.library_paths = self.rw.get_library_paths()
        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)

        self.setup_ui()
        self.set_icons()
        self.load_library_folders(self.treewidget)
        self.parent_maya_layout()

    def setup_ui(self):
        self.resize(self.width, self.height)
        self.setStyleSheet('font: 12pt \"MS Shell Dlg 2\";')
        self.setObjectName('mainwindow_%s' % self.tool_kit_object)
        self.setWindowTitle(self.tool_kit_titile)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.addWidget(self.catalogue.splitter)
        self.catalogue.splitter.addWidget(self.model.groupbox_model)
        self.catalogue.splitter.setSizes([175, 201, 200])
        self.treewidget = self.catalogue.treewidget_folder
        self.treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget))
        self.treewidget.itemClicked.connect(
            partial(self.load_current_folder, self.treewidget))  # Load Pose to UI
        self.listwidget = self.catalogue.listWidget_catalogue
        self.listwidget.itemClicked.connect(
            partial(self.builds, 'load', self.listwidget))  # Load Pose to UI
        self.listwidget.itemDoubleClicked.connect(
            partial(self.builds, 'build', self.listwidget))  # Load Pose to UI
        self.checkbox_build = self.model.checkbox_build
        self.checkbox_assign = self.model.checkbox_assign
        self.button_build = self.model.button_build
        self.button_build.clicked.connect(
            partial(self.builds, 'build', self.listwidget))
        self.lineEdit_label = self.model.lineEdit_label
        self.textedit_history = self.model.textedit_history
        self.button_publish = self.model.button_publish
        self.lineEdit_label.returnPressed.connect(
            partial(self.rename_model, self.lineEdit_label))
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
        self.menu_file.addAction(self.action_rename)
        self.menu_file.addAction(self.action_remove)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_refresh)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_preferences)
        self.menu_help.addAction(self.action_aboutool)
        self.menu_help.addAction(self.action_abouttoolkits)
        self.contex_menu = QtWidgets.QMenu(self)
        self.contex_menu.addAction(self.action_create)
        self.contex_menu.addAction(self.action_rename)
        self.contex_menu.addAction(self.action_remove)
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.action_refresh)
        self.contex_menu.addSeparator()
        self.contex_menu.addAction(self.action_expand)
        self.contex_menu.addAction(self.action_collapse)
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
        self.model.button_snapshot.clicked.connect(
            partial(self.snapshot, self.model.button_snapshot))
        self.model.button_publish.clicked.connect(self.publish)
        self.preference.button_apply.clicked.connect(self.set_preference)
        self.preference.button_cancel.clicked.connect(self.cancel_preference)
        self.action_aboutool.triggered.connect(self.toolkit_help_link)
        self.action_abouttoolkits.triggered.connect(self.toolkit_link)

    def set_icons(self):
        actions = self.findChildren(QtWidgets.QAction)
        for each_action in actions:
            objectName = each_action.objectName()
            if not objectName:
                continue
            current_icon = '{}.png'.format(objectName.split('_')[-1])
            icon_path = os.path.join(resources.getIconPath(), current_icon)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            each_action.setIcon(icon)

    def toolkit_link(self):
        webbrowser.BaseBrowser(resources.getToolKitLink())
        OpenMaya.MGlobal.displayInfo(resources.getToolKitLink())

    def toolkit_help_link(self):
        webbrowser.open(resources.getToolKitHelpLink())
        OpenMaya.MGlobal.displayInfo(resources.getToolKitHelpLink())

    def parent_maya_layout(self):
        object_name = str(self.objectName())
        self.floating_layout = cmds.paneLayout(
            cn='single', w=self.width, p=platforms.get_main_window())
        cmds.dockControl(
            self.tool_kit_object,
            l=self.tool_kit_titile,
            area='right',
            content=self.floating_layout,
            allowedArea=['right', 'left'])
        cmds.control(object_name, e=1, p=self.floating_layout)

    def show_preference(self):
        self.preference.show()

    def set_preference(self):
        self.preference.apply()
        self.library_paths = self.rw.get_library_paths()
        self.load_library_folders(self.treewidget)

    def cancel_preference(self):
        self.setEnabled(True)

    def close_library(self):
        if cmds.dockControl(self.tool_kit_object, q=1, ex=1):
            cmds.deleteUI(self.tool_kit_object, ctl=1)
        self.close()

    def on_context_menu(self, treewidget, paint):
        self.contex_menu.exec_(treewidget.mapToGlobal(paint))

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

    def create(self):
        folder_name, ok = QtWidgets.QInputDialog.getText(
            self, 'Input', 'Enter the folder name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            OpenMaya.MGlobal.displayWarning('abort the folder creation!...')
            return
        if not self.library_paths:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Not found Publish directory', QtWidgets.QMessageBox.Ok)
            return
        current_path = os.path.join(self.library_paths[0], folder_name)
        if self.treewidget.selectedItems():
            current_item = self.treewidget.selectedItems()[-1]
            tool_tip = str(current_item.toolTip(0))
            current_path = os.path.join(tool_tip, folder_name)
        if os.path.isdir(current_path):
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Already found the folder.\n%s' % current_path,
                QtWidgets.QMessageBox.Ok)
            return
        result, message = self.folder.create(folder_path=current_path)
        if not result:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', message, QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Create folder  - faild!...')
            return
        self.load_library_folders(self.treewidget)
        OpenMaya.MGlobal.displayInfo(
            '\"%s\" Folder create - success!...' % message)

    def rename(self):
        folder_name, ok = QtWidgets.QInputDialog.getText(
            self, 'Input', 'Enter the new name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            print '\n#warnings abort the rename'
            return
        if not self.treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not found any selection\nSelect the folder and try',
                QtWidgets.QMessageBox.Ok)
            return
        current_item = self.treewidget.selectedItems()[-1]
        current_path = str(current_item.toolTip(0))
        result, message = self.folder.rename(
            folder_path=current_path, name=folder_name)
        if not result:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', message, QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Rename folder - faild!...')
            return
        self.load_library_folders(self.treewidget)
        OpenMaya.MGlobal.displayInfo(
            '\"%s\" Rename folder - success!...' % message)

    def remove(self):
        if not self.treewidget.selectedItems():
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not found any selection\nSelect the folder and try',
                QtWidgets.QMessageBox.Ok)
            return
        replay = QtWidgets.QMessageBox.question(
            self,
            'Question',
            'Are you sure, you want to remove folder',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if replay == QtWidgets.QMessageBox.No:
            OpenMaya.MGlobal.displayWarning('abort the remove folder!...')
            return
        for each_item in self.treewidget.selectedItems():
            current_path = str(each_item.toolTip(0))
            result, message = self.folder.remove(folder_path=current_path)
            if not result:
                QtWidgets.QMessageBox.warning(
                    self,
                    'Warning', '%s\n%s' % (current_path, message),
                    QtWidgets.QMessageBox.Ok)
                OpenMaya.MGlobal.displayWarning('Remove folder - faild!...')
        self.load_library_folders(self.treewidget)
        self.listwidget.clear()
        OpenMaya.MGlobal.displayInfo(
            '\"%s\" Remove folder - success!...' % message)

    def refresh(self):
        self.load_library_folders(self.treewidget)
        self.listwidget.clear()

    def load_library_folders(self, treewidget):
        if not self.library_paths:
            return
        treewidget.clear()
        for each_library in self.library_paths:
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
            icon.addPixmap(
                QtGui.QPixmap(icon_path),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setTextAlignment(QtCore.Qt.AlignHCenter |
                                  QtCore.Qt.AlignBottom)
            thread.start_new_thread(
                self.validte_model_publish, (each_file, item,))

    def validte_model_publish(self, file, item):
        studio_shader = studioShader.Shader()
        valid = studio_shader.had_valid(file)
        if valid:
            return
        item.setFlags(
            QtCore.Qt.ItemIsSelectable |
            QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)

    def collect_child_items(self, parent):
        for index in range(parent.childCount()):
            current_child = parent.child(index)
            self.dependent_list.append(current_child)
            self.collect_child_items(current_child)

    def publish(self):
        current_items = self.treewidget.selectedItems()
        if not current_items:
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not found any folder selection.\nSelect the folder and try!...',
                QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning('Not found any folder selection.')
            return
        current_path = str(current_items[-1].toolTip(0))
        if not os.path.isdir(current_path):
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not found such Publish directory!...%s' % current_path,
                QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning(
                'Not found such Publish directory!...%s' % current_path)
            return
        geometry_dag_paths = self.studio_maya.getSelectedObjectShapeNode(
            OpenMaya.MFn.kMesh)
        if not geometry_dag_paths.length():
            QtWidgets.QMessageBox.warning(
                self, 
                'Warning',
                'Not found any Polygon Geometry in your selection!...',
                QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning(
                'Not found any Polygon Geometry in your selection!...')
            return
        label = self.model.lineEdit_label.text()
        if not label:
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not found the Name of the the Publish!...',
                QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning(
                'Not found the Name of the the Publish!...')
            return        # add condition for mutlipe object
        studio_shader = studioShader.Shader(
            geometry_dag_path=geometry_dag_paths[0])
        if studio_shader.had_file(current_path, label):
            replay = QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Already a file with the same name in the publish\n\"%s\"\nIf you want to overwrite press Yes' % label,
                QtWidgets.QMessageBox.Yes,
                QtWidgets.QMessageBox.No)
            OpenMaya.MGlobal.displayWarning(
                'Already a file with the same name in the publish')
            if replay != QtWidgets.QMessageBox.Yes:
                return
        user_comment = self.model.textedit_history.toPlainText()
        result = studio_shader.save(
            current_path, label, self.image_object, user_comment=user_comment)
        self.load_current_folder(self.treewidget)
        self.clear_publish()
        message = 'Publish success!...'
        if False in result:
            message = 'Publish Failed!...\n%s\n%s' % (
                result[False], '[more details and debugging subing85@gmail.com]')
            QtWidgets.QMessageBox.critical(
                self, 'Failed', message, QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayInfo(message)
            return
        QtWidgets.QMessageBox.information(
            self, 'Information', message, QtWidgets.QMessageBox.Ok)
        OpenMaya.MGlobal.displayInfo(message)

    def snapshot(self, button):
        self.clear_publish()
        self.image_object, image_path = self.model.snapshot(button)

    def clear_publish(self):
        self.currnet_publish = None
        self.model.image_to_button()
        self.lineEdit_label.clear()
        self.button_publish.show()
        self.button_build.hide()
        self.checkbox_build.hide()
        # self.checkbox_build.setChecked(False)
        self.checkbox_assign.hide()
        # self.checkbox_assign.setChecked(False)
        self.textedit_history.clear()
        self.textedit_history.setReadOnly(False)

    def builds(self, tag, listwidge, *args):
        current_items = listwidge.selectedItems()
        if not current_items:
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not selected any shader or shader not valid!...',
                QtWidgets.QMessageBox.Ok)
            OpenMaya.MGlobal.displayWarning(
                'Not select any shader or shader not valid.')
            return
        self.button_publish.hide()
        self.button_build.show()
        self.checkbox_build.show()
        self.checkbox_assign.show()
        publish_path = current_items[-1].toolTip()
        self.currnet_publish = publish_path
        studio_shader = studioShader.Shader(
            path=publish_path, geometry_dag_path=None)
        data = studio_shader.create(False, False, fake=True)
        comment = [
            data['comment'],
            'author : %s' % data['author'],
            data['tag'],
            data['#copyright'],
            'user : %s' % data['user'],
            data['created_date']
        ]
        self.textedit_history.setText('\n'.join(comment))
        self.textedit_history.setReadOnly(True)
        self.lineEdit_label.setText(os.path.basename(
            os.path.splitext(publish_path)[0]))
        self.model.image_to_button(path=studio_shader.get_image(publish_path))
        if tag == 'build':
            result = studio_shader.create(
                self.checkbox_build.isChecked(),
                self.checkbox_assign.isChecked(),
            )
            if False in result:
                OpenMaya.MGlobal.displayWarning(
                    'Build Failed!... %s' % result[False])
            else:
                OpenMaya.MGlobal.displayInfo('Build Success!...')

    def rename_model(self, lineedit):
        studio_shader = studioShader.Shader()
        if not self.currnet_publish:
            OpenMaya.MGlobal.displayWarning(
                'Not selected any shader or shader not valid.')
            return
        current_image = studio_shader.get_image(self.currnet_publish)
        new_name = '%s' % lineedit.text()
        model_format = os.path.splitext(self.currnet_publish)[-1]
        self.folder.rename(
            folder_path=self.currnet_publish,
            name='%s%s' % (new_name, model_format))
        image_format = os.path.splitext(current_image)[-1]
        self.folder.rename(
            folder_path=current_image,
            name='%s%s' % (new_name, image_format))
        self.load_current_folder(self.treewidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
