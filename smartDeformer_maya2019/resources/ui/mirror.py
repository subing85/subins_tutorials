'''
mirror.py 0.0.1 
Date: January 01, 2019
Last modified: April 23, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.  
'''


import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial

from maya import OpenMaya

from smartDeformer_maya2019.modules import cluster
from smartDeformer_maya2019.modules import skincluster
from smartDeformer_maya2019.modules import studioMaya


class Mirror(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Mirror, self).__init__(parent=None)
        self.setup_ui()
        self.my_maya = studioMaya.Maya()
        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()

    def setup_ui(self):
        self.setObjectName('mirror')
        self.resize(300, 100)
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)
        mirrors = ['Cluster', 'Skincluster']
        for each_mirror in mirrors:
            self.groupbox = QtWidgets.QGroupBox(self)
            self.groupbox.setObjectName('groupbox')
            self.groupbox.setTitle('%s Mirror' % each_mirror)
            self.verticallayout.addWidget(self.groupbox)
            self.horizontallayout_mirror = QtWidgets.QHBoxLayout(self.groupbox)
            self.horizontallayout_mirror.setObjectName(
                'horizontallayout_mirror_%s' % each_mirror)
            self.horizontallayout_mirror.setSpacing(10)
            self.horizontallayout_mirror.setContentsMargins(20, 20, 20, 20)
            self.radiobutton_x = QtWidgets.QRadioButton(self.groupbox)
            self.radiobutton_x.setObjectName('radiobutton_x_%s' % each_mirror)
            self.radiobutton_x.setText('X')
            self.radiobutton_x.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout_mirror.addWidget(self.radiobutton_x)
            self.radiobutton_y = QtWidgets.QRadioButton(self.groupbox)
            self.radiobutton_y.setObjectName('radiobutton_y_%s' % each_mirror)
            self.radiobutton_y.setText('Y')
            self.radiobutton_y.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout_mirror.addWidget(self.radiobutton_y)
            self.radiobutton_z = QtWidgets.QRadioButton(self.groupbox)
            self.radiobutton_z.setObjectName('radiobutton_z_%s' % each_mirror)
            self.radiobutton_z.setText('Z')
            self.radiobutton_z.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout_mirror.addWidget(self.radiobutton_z)
            self.button_mirror = QtWidgets.QPushButton(self.groupbox)
            self.button_mirror.setObjectName('button_mirror_%s' % each_mirror)
            self.button_mirror.setText('Mirror')
            self.horizontallayout_mirror.addWidget(self.button_mirror)
            self.button_flip = QtWidgets.QPushButton(self.groupbox)
            self.button_flip.setObjectName('button_flip_%s' % each_mirror)
            self.button_flip.setText('Flip')
            self.horizontallayout_mirror.addWidget(self.button_flip)
            radiobuttons = [self.radiobutton_x,
                            self.radiobutton_y, self.radiobutton_z]
            self.button_mirror.clicked.connect(
                partial(self.set_mirror_flip, each_mirror.lower(), 'mirror', radiobuttons))
            self.button_flip.clicked.connect(
                partial(self.set_mirror_flip, each_mirror.lower(), 'flip', radiobuttons))
            self.radiobutton_x.setChecked(True)
            self.groupbox = QtWidgets.QGroupBox(self)
            self.groupbox.setObjectName('groupbox_%s' % each_mirror)
            self.groupbox.setTitle(each_mirror)
            self.verticallayout.addWidget(self.groupbox)
            self.horizontallayout_copy = QtWidgets.QHBoxLayout(self.groupbox)
            self.horizontallayout_copy.setObjectName(
                'horizontallayout_copy_%s' % each_mirror)
            self.horizontallayout_copy.setSpacing(10)
            self.horizontallayout_copy.setContentsMargins(20, 20, 20, 20)
            self.button_combine = QtWidgets.QPushButton(self.groupbox)
            self.button_combine.setObjectName(
                'button_combine_%s' % each_mirror)
            self.button_combine.setText('Combine %s' % each_mirror)
            self.horizontallayout_copy.addWidget(self.button_combine)
            self.button_combine.clicked.connect(
                partial(self.combine, each_mirror.lower()))
            self.button_copy = QtWidgets.QPushButton(self.groupbox)
            self.button_copy.setObjectName('button_copy_%s' % each_mirror)
            self.button_copy.setText('Copy %s' % each_mirror)
            self.horizontallayout_copy.addWidget(self.button_copy)
            self.button_copy.clicked.connect(
                partial(self.copy, each_mirror.lower()))
            spacerItem = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticallayout.addItem(spacerItem)

    def set_current_button(self, item):
        self.current_item = item
        return self.current_item

    def set_mirror_flip(self, tag, type, radiobuttons):
        selections = self.my_maya.getSelectedDagPaths()
        # to check your selection
        selection_array = OpenMaya.MDagPathArray()
        for index in range(selections.length()):
            if tag == 'cluster':
                if not self.my_maya.hasCluster(selections[index]):
                    continue
                selection_array.append(selections[index])
            if tag == 'skincluster':
                if not self.my_maya.hasJoint(selections[index]):
                    continue
                selection_array.append(selections[index])
        if not selection_array.length():
            OpenMaya.MGlobal.displayWarning(
                'Your select not contain %s!...' % tag)
            return
        axis = [1, 1, 1]
        if radiobuttons[0].isChecked():
            axis = [-1, 1, 1]
        if radiobuttons[1].isChecked():
            axis = [1, -1, 1]
        if radiobuttons[2].isChecked():
            axis = [1, 1, -1]
        if tag == 'cluster':
            self.cluster.create_mirror_flip(selection_array, axis, type)
        if tag == 'skincluster':
            self.skincluster.create_mirror_flip(selection_array, axis, type)
        OpenMaya.MGlobal.displayInfo('%s %s Done!...' % (tag, type))

    def combine(self, tag):
        selections = self.my_maya.getSelectedDagPaths()
        # to check your selection
        selection_array = OpenMaya.MDagPathArray()
        for index in range(selections.length()):
            if tag == 'cluster':
                if not self.my_maya.hasCluster(selections[index]):
                    continue
                selection_array.append(selections[index])
            if tag == 'skincluster':
                if not self.my_maya.hasJoint(selections[index]):
                    continue
                selection_array.append(selections[index])
        if not selection_array.length():
            OpenMaya.MGlobal.displayWarning(
                'Your select not contain %s!...' % tag)
            return

        if tag == 'cluster':
            self.cluster.combine_weights(selection_array)
        if tag == 'skincluster':
            self.skincluster.combine_weights(selection_array)
        OpenMaya.MGlobal.displayInfo('%s combine Done!...' % (tag))

    def copy(self, tag):
        selections = self.my_maya.getSelectedDagPaths()
        # to check your selection
        selection_array = OpenMaya.MDagPathArray()
        for index in range(selections.length()):
            if tag == 'cluster':
                if not self.my_maya.hasCluster(selections[index]):
                    continue
                selection_array.append(selections[index])
            if tag == 'skincluster':
                if not self.my_maya.hasJoint(selections[index]):
                    continue
                selection_array.append(selections[index])

        tag_result = {'cluster': 'Cluster Handle', 'skincluster': 'Joint'}
        if not selection_array.length():
            OpenMaya.MGlobal.displayWarning(
                'Your select not contain %s!...' % tag_result[tag])
            return
        if selection_array.length() < 2:
            OpenMaya.MGlobal.displayWarning(
                'You need to select minimum two %s!...' % tag_result[tag])
            return

        if tag == 'cluster':
            targets_deformer = OpenMaya.MDagPathArray()
            for index in range(1, selection_array.length()):
                targets_deformer.append(selection_array
                                        [index])
            self.cluster.copy_weights(selection_array[0], targets_deformer)
        if tag == 'skincluster':
            if selection_array.length() != 2:
                OpenMaya.MGlobal.displayWarning(
                    'You need to select only two %s!...' % tag_result[tag])
            self.skincluster.copy_weights(
                selections[0], selections[selections.length() - 1])
        OpenMaya.MGlobal.displayInfo('%s copy Done!...' % (tag))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mirror(parent=None)
    window.show()
    sys.exit(app.exec_())
