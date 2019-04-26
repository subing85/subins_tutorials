'''
weights.py 0.0.1 
Date: January 01, 2019
Last modified: April 23, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.  
'''


import os
import sys
import warnings

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from datetime import datetime
from functools import partial

from maya import OpenMaya

from smartDeformer_maya2017 import resources
from smartDeformer_maya2017.modules import cluster
from smartDeformer_maya2017.modules import readWrite
from smartDeformer_maya2017.modules import skincluster
from smartDeformer_maya2017.modules import studioMaya


class Weights(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Weights, self).__init__(parent=None)
        self.setup_ui()
        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()
        self.my_maya = studioMaya.Maya()

    def setup_ui(self):
        self.setObjectName('weights')
        self.resize(300, 400)
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle('Weights')
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_weight = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_weight.setObjectName('verticallayout_weight')
        self.verticallayout_weight.setSpacing(10)
        self.verticallayout_weight.setContentsMargins(1, 1, 1, 1)
        self.listwidget = QtWidgets.QListWidget(self.groupbox)
        self.listwidget.setObjectName('listwidget')
        self.listwidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listwidget.setAlternatingRowColors(True)
        self.verticallayout_weight.addWidget(self.listwidget)
        self.horizontallayout_weight = QtWidgets.QHBoxLayout()
        self.horizontallayout_weight.setObjectName('horizontallayout_weight')
        self.horizontallayout_weight.setSpacing(1)
        self.horizontallayout_weight.setContentsMargins(1, 1, 1, 1)
        self.verticallayout_weight.addLayout(self.horizontallayout_weight)
        self.button_export = QtWidgets.QPushButton(self.groupbox)
        self.button_export.setObjectName('button_export')
        self.button_export.setText('Export')
        self.horizontallayout_weight.addWidget(self.button_export)
        self.button_import = QtWidgets.QPushButton(self.groupbox)
        self.button_import.setObjectName('button_import')
        self.button_import.setText('Import')
        self.horizontallayout_weight.addWidget(self.button_import)
        self.button_export.clicked.connect(self.exports)
        self.button_import.clicked.connect(self.imports)
        self.load_weigts()
        self.pop_menu(self.listwidget)

    def pop_menu(self, listwidget):
        # custom Context Menu
        listwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        listwidget.customContextMenuRequested.connect(
            partial(self.context_menu, listwidget))
        self.pop_menu = QtWidgets.QMenu(self)
        self.action_rename = QtWidgets.QAction(self)
        self.action_rename.setObjectName('action_rename')
        self.action_rename.setText('Rename')
        self.pop_menu.addAction(self.action_rename)
        self.action_remove = QtWidgets.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove')
        self.pop_menu.addAction(self.action_remove)
        self.action_rename.triggered.connect(self.rename_item)
        self.action_remove.triggered.connect(self.remove_items)
        for each_actions in [self.action_rename, self.action_remove]:
            icon_name = str(each_actions.objectName()).split('_')[-1]
            current_icon = os.path.join(resources.getIconPath(),
                                        '{}.png'.format(icon_name))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(current_icon),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            each_actions.setIcon(icon)

    def context_menu(self, listwidget, point):  # Right click menu
        index = listwidget.indexAt(point)
        if not index.isValid():
            return
        self.pop_menu.exec_(QtWidgets.QCursor.pos())

    def load_weigts(self):
        self.listwidget.clear()
        rw = readWrite.ReadWrite(t='weights')
        self.bundles = rw.getBundles()
        for each_bundle, bundle_data in self.bundles.items():
            item = QtWidgets.QListWidgetItem()
            item.setText(each_bundle)
            current_icon = os.path.join(resources.getIconPath(),
                                        '{}.png'.format(bundle_data['tag']))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(current_icon),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setToolTip('\n'.join(bundle_data['data'].keys()))
            self.listwidget.addItem(item)

    def exports(self):
        selections = self.my_maya.getSelectedDagPaths()
        drivers = {}
        for index in range(selections.length()):
            if not selections[index].isValid():
                continue
            tag = None
            if self.my_maya.hasJoint(selections[index]):
                tag = 'skincluster'
            elif self.my_maya.hasCluster(selections[index]):
                tag = 'cluster'
            drivers.setdefault(tag, []).append(selections[index])

        if None in drivers:
            OpenMaya.MGlobal.displayError(
                '#Unwanted nodes are found in your selection')
            return
        if drivers.keys().count(drivers.keys()[0]) != len(drivers.keys()):
            OpenMaya.MGlobal.displayError(
                '#You selected differ types of nodes\nselect cluster handless either joints')
            return

        file_name, ok = QtWidgets.QInputDialog.getText(self, 'Weight Export',
                                                       'Enter the weight name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            OpenMaya.MGlobal.displayWarning('#Abrot your export!...')
            return

        weights = {}
        if drivers.keys()[0] == 'cluster':
            weights = self.cluster.get_weights(drivers['cluster'])
        if drivers.keys()[0] == 'skincluster':
            weights = self.skincluster.get_weights(drivers['skincluster'])

        comment = 'smart tool 0.0.1 - weights container'
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about maya 2016 deformers weights'
        type = 'weights'
        valid = True
        data = weights
        tag = drivers.keys()[0]
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                                 d=description, t=type, v=valid, data=data, tag=tag)
        rw.create(name=str(file_name))
        print rw.file_path
        self.load_weigts()
        OpenMaya.MGlobal.displayInfo(
            'Export {} weights Done!...'.format(drivers.keys()[0]))

    def imports(self):
        if not self.bundles:
            OpenMaya.MGlobal.displayError('No export data')
            return
        if not self.listwidget.selectedItems():
            OpenMaya.MGlobal.displayWarning('\nNo selection')
            return
        OpenMaya.MGlobal.displayInfo('\nImport weights')

        for each_item in self.listwidget.selectedItems():
            if str(each_item.text()) not in self.bundles:
                OpenMaya.MGlobal.displayWarning(
                    '\nCorresponding weight not found %s' % each_item.text())
                continue
            current_weights = self.bundles[str(each_item.text())]
            if current_weights['tag'] == 'cluster':
                print type(current_weights['data'])
                self.cluster.set_weights(current_weights['data'])
            if current_weights['tag'] == 'skincluster':
                self.skincluster.set_weights(current_weights['data'])
            OpenMaya.MGlobal.displayInfo('\t{}'.format(each_item.text()))
        OpenMaya.MGlobal.displayInfo(
            'Import {} Done!...'.format(current_weights['tag']))

    def rename_item(self):
        file_name, ok = QtWidgets.QInputDialog.getText(self, 'Rename',
                                                       'Enter the new name:', QtWidgets.QLineEdit.Normal)
        if not ok:
            OpenMaya.MGlobal.displayWarning('#Abrot your rename!...')
            return
        if not self.listwidget.selectedItems():
            OpenMaya.MGlobal.displayWarning('\nNo selection')
            return

        current_item = self.listwidget.selectedItems()[-1]
        if str(current_item.text()) not in self.bundles:
            OpenMaya.MGlobal.displayWarning(
                '\nCorresponding weight not found %s' % current_item.text())
            return
        rw = readWrite.ReadWrite(t='weights')
        weight_path = self.bundles[str(current_item.text())]['path']
        new_weight_path = os.path.join(os.path.dirname(
            weight_path), '%s.%s' % (file_name, rw.extention))
        try:
            os.chmod(weight_path, 0777)
            os.rename(weight_path, new_weight_path)
            replay = 1
        except Exception as error:
            warnings.warn('\n%s' % str(error), Warning)
        self.load_weigts()
        OpenMaya.MGlobal.displayInfo('Rename Done!...')

    def remove_items(self):
        if not self.listwidget.selectedItems():
            OpenMaya.MGlobal.displayWarning('\nNo selection')
            return
        replay = QtWidgets.QMessageBox.question(self, 'Question',
                                                'Are you sure, you want to remove the weights?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if replay == QtWidgets.QMessageBox.No:
            OpenMaya.MGlobal.displayWarning('#Abrot your remove!...')
            return
        for each_item in self.listwidget.selectedItems():
            if str(each_item.text()) not in self.bundles:
                OpenMaya.MGlobal.displayWarning(
                    '\nCorresponding weight not found %s' % each_item.text())
                continue
            weight_path = self.bundles[str(each_item.text())]['path']
            try:
                os.chmod(weight_path, 0777)
                os.remove(weight_path)
            except Exception as error:
                warnings.warn('\n%s' % str(error), Warning)
        self.load_weigts()
        OpenMaya.MGlobal.displayInfo('Removed Done!...')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Weights(parent=None)
    window.show()
    sys.exit(app.exec_())
