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


def set_header(layout, show_icon=None):
    button_logo = QtWidgets.QPushButton(None)
    button_logo.setFlat(True)
    button_logo.setObjectName('button_logo')
    button_logo.setMinimumSize(QtCore.QSize(350, 99))
    button_logo.setMaximumSize(QtCore.QSize(350, 99))                
    logo_path = os.path.join(resource.getIconPath(), 'logo.png')        
    image_to_button(button_logo, 350, 99, path=logo_path)
    layout.addWidget(button_logo)       
    spacer_item = QtWidgets.QSpacerItem(
        40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    layout.addItem(spacer_item)    
    button_show = QtWidgets.QPushButton(None)
    button_show.setFlat(True)
    button_show.setObjectName('button_show')
    button_show.setMinimumSize(QtCore.QSize(176, 99))
    button_show.setMaximumSize(QtCore.QSize(176, 99))
    if show_icon:
        image_to_button(button_show, 176, 99, path=show_icon)            
    layout.addWidget(button_show)
    return button_logo, button_show
        
    
