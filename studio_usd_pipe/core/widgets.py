import os

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from studio_usd_pipe import resource


def image_to_button(button, width, height, path=None):
    if not path:
        path = os.path.join(resource.getIconPath(), 'unknown.png')
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(path),
        QtGui.QIcon.Normal, QtGui.QIcon.Off
    )
    button.setIcon(icon)
    button.setIconSize(QtCore.QSize(width, height)) 
    

def add_treewidget(parent, input_data):
    item = QtWidgets.QTreeWidgetItem(parent)
    item.setText(0, input_data['display'])
    item.setStatusTip(0, input_data['statustip'])
    item.setToolTip(0, input_data['tooltip'])
    item.setWhatsThis(0, input_data['whatsthis'])
    current_icon = input_data['icon']
    if not os.path.isfile(current_icon):
        current_icon = os.path.join(resource.getIconPath(), 'unknown.png')
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(current_icon),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off
        )
    item.setIcon(0, icon)    
    return item


def get_treeitem_hierarchy(items):
    stack = items
    hierarchy = []
    while stack:
        item = stack.pop()
        parent = item.parent()
        if parent:
            stack.append(parent)
            hierarchy.append(parent)
        else:
            hierarchy.append(item)
    return hierarchy
    
