import os
import warnings

from PySide import QtGui
from PySide import QtCore

from studioMayaInterpreter import resources


def create_item(parent, type, path):
    padding_size = 3
    icon_path = resources.getIconPath()
    formats = resources.getFormats()
    images = resources.getImages()    
    
    format = os.path.splitext(path)[-1]
    
    if format not in formats[type]:
        warnings.warn(
            'wrong file, please check the file extension', Warning)
        return  

    item = QtGui.QTreeWidgetItem(parent)
    item.setText(1, os.path.basename(path))
    item.setToolTip(1, path)
    item.setFlags(
        QtCore.Qt.ItemIsEnabled |
        QtCore.Qt.ItemIsEditable |
        QtCore.Qt.ItemIsSelectable |
        QtCore.Qt.ItemIsDropEnabled |
        QtCore.Qt.ItemIsDragEnabled
    )
    current_icon = os.path.join(
        icon_path, '%s.png' % images[format])
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(current_icon),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off
    )
    item.setIcon(1, icon)

    item_count = parent.topLevelItemCount()
    zeros = padding(item_count, padding_size)
    current_number = '%s%s' % (zeros, item_count)
    item.setText(0, current_number)


def padding(value=0, size=0):
    vaue_len = len(str(value))
    zero = size - vaue_len
    zero = (abs(zero) * '0')
    return zero
