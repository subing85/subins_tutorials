'''
widgets.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import warnings

from PySide import QtGui
from PySide import QtCore

from studio_maya import resources
from studio_maya.core import generic


def get_exists_items(parent):
    exist_items = []
    treewidget= parent.invisibleRootItem()
    for index in range (treewidget.childCount()):
        path = treewidget.child(index).toolTip(1)
        exist_items.append(path.encode())
    return exist_items


def create_item(parent, type, path):
    padding_size = 3
    icon_path = resources.getIconPath()
    formats = resources.getFormats()
    images = resources.getImages()
    format = os.path.splitext(path)[-1]
    if format not in formats[type]:
        warnings.warn(
            'wrong file, please check the file extension',
            Warning
        )
        return
    item = QtGui.QTreeWidgetItem(parent)
    item.setText(1, os.path.basename(path))
    item.setToolTip(1, path)
    current_icon = os.path.join(
        icon_path, '%s.png' % images[format])
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(current_icon),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off
    )
    item.setIcon(1, icon)
    if not os.path.isfile(path):
        item.setFlags(QtCore.Qt.ItemIsDragEnabled)
    item_count = parent.topLevelItemCount()
    zeros = padding(item_count, padding_size)
    current_number = '%s%s' % (zeros, item_count)
    item.setText(0, current_number)


def get_item_contents(treewidget, row):
    widget_item = treewidget.invisibleRootItem()
    contents = {}
    for index in range(widget_item.childCount()):
        current_item = widget_item.child(index)
        text = current_item.text(row)
        full_path = current_item.toolTip(row)
        current_index = int(current_item.text(0))
        data = {
            'label': text.encode(),
            'path': full_path.encode()
        }
        contents.setdefault(current_index, data)
    return contents


def set_item_contents(type, data, treewidget):
    for index, contents in data.items():
        create_item(treewidget, type, contents['path'])


def set_maya_version(path, *args):
    input_data = generic.read_preset(path)
    if not input_data:
        return
    maya_version = input_data['current_version']['name']
    args[0].setPixmap(QtGui.QPixmap(
        os.path.join(resources.getIconPath(), 'maya%s.png' % maya_version)))
    args[0].setScaledContents(True)
    args[0].setMinimumSize(QtCore.QSize(32, 32))
    args[0].setMaximumSize(QtCore.QSize(32, 32))
    args[1].setText('Autodesk Maya %s' % maya_version)


def padding(value=0, size=0):
    vaue_len = len(str(value))
    zero = size - vaue_len
    zero = (abs(zero) * '0')
    return zero
