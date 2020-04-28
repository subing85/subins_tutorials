import os

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from studio_usd_pipe import resource


def get_color_code():
    info_color = QtGui.QColor('darkBlue')
    error_color = QtGui.QColor('red')
    warning_color = QtGui.QColor('magenta')
    header_color = QtGui.QColor('green')
    return  header_color, info_color, warning_color, error_color


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
    
    
def add_treewidget_item(parent, label, icon_path=None, foreground=None):
    item = QtWidgets.QTreeWidgetItem (parent)
    item.setText (0, label)
    if icon_path:      
        icon_path = os.path.join(resource.getIconPath(), '{}.png'.format(icon_path))
        icon = QtGui.QIcon ()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
        item.setIcon (0, icon)
    if foreground:
        r, g, b = foreground
        brush = QtGui.QBrush(QtGui.QColor(r, g, b))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(0, brush)
    return item


def add_listwidget_item(parent, label, key=None, icon_path=None):
    item = QtWidgets.QListWidgetItem()
    parent.addItem(item)
    item.setText(label)
    if key:
        item.setStatusTip(key)            
    icon = QtGui.QIcon()
    
    if not icon_path:
        icon_path = os.path.join(resource.getIconPath(), 'unknown.png')
    if not os.path.isfile(icon_path) and os.path.isabs(icon_path):
        icon_path = os.path.join(resource.getIconPath(), 'unknown.png')
    
    icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon)
    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)       


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


def set_icons(mainwindow=None, widgets=None):
    
    if mainwindow:
        icon = QtGui.QIcon()
        name = mainwindow.objectName().split('_')[-1]
        icon.addPixmap(QtGui.QPixmap(os.path.join(resource.getIconPath(), '%s.png' % name)))
        mainwindow.setWindowIcon(icon)
    
    if widgets:
        # qactions = self.findChildren(QtWidgets.QAction)
        for widget in widgets :
            icon = QtGui.QIcon()         
            icon_name = widget.objectName().split('action_')[-1]
            icon_path = (os.path.join(resource.getIconPath(), '{}.png'.format(icon_name)))
            icon.addPixmap(QtGui.QPixmap (icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            widget.setIcon (icon)  

