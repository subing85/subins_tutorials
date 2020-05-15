import os

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from studio_usd_pipe import resource


def get_color_code(): #**
    info_color = QtGui.QColor('darkBlue')
    error_color = QtGui.QColor('red')
    warning_color = QtGui.QColor('magenta')
    header_color = QtGui.QColor('green')
    return  header_color, info_color, warning_color, error_color


def image_to_button(button, width, height, path=None): #**
    if not path:
        path = os.path.join(resource.getIconPath(), 'unknown.png')
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap(path),
        QtGui.QIcon.Normal, QtGui.QIcon.Off
    )
    button.setIcon(icon)
    button.setIconSize(QtCore.QSize(width, height)) 
    
    
def add_treewidget_item(parent, label, icon=None, foreground=None):
    item = QtWidgets.QTreeWidgetItem (parent)
    item.setText (0, label)
    if icon:      
        icon_path = os.path.join(resource.getIconPath(), '{}.png'.format(icon))
        icon = QtGui.QIcon ()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
        item.setIcon (0, icon)
    if foreground:
        r, g, b = foreground
        brush = QtGui.QBrush(QtGui.QColor(r, g, b))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(0, brush)
    return item


def append_treewidget_item(parent, column_items):
    item = QtWidgets.QTreeWidgetItem (parent)
    if parent.columnCount()<len(column_items):   
        parent.setColumnCount(len(column_items))
    for index, column_item in enumerate(column_items):
        parent.headerItem().setText(index, column_item[0])
        item.setText (index, str(column_item[1]))
    return item
   


def update_treewidget_item_icon(item, icon_name):
    icon_path = os.path.join(resource.getIconPath(), '{}.png'.format(icon_name))
    icon = QtGui.QIcon ()
    icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
    item.setIcon (0, icon)  
      
    
def update_widget_icon(item, icon_name):
    icon_path = os.path.join(resource.getIconPath(), icon_name)
    icon = QtGui.QIcon ()
    icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
    item.setIcon (icon)  
      

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


def set_header(layout, show_icon=None): #**
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


def set_icons(mainwindow=None, widgets=None): #**
    if mainwindow:
        icon = QtGui.QIcon()
        split = mainwindow.objectName().split('_')[1:]
        name = '_'.join(split)
        
        icon.addPixmap(QtGui.QPixmap(os.path.join(resource.getIconPath(), '%s.png' % name)))
        mainwindow.setWindowIcon(icon)
    if widgets:
        # qactions = self.findChildren(QtWidgets.QAction)
        for widget in widgets :
            icon = QtGui.QIcon()         
            icon_name = widget.objectName().split('action_')[-1]
            icon_path = (os.path.join(resource.getIconPath(), '{}.png'.format(icon_name)))
            icon.addPixmap(QtGui.QPixmap (icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            widget.setIcon(icon)  


def image_resize(image_path, output_path, width=2048, height=2048): #**
    # try:
    from PySide2 import QtGui
    from PySide2 import QtCore
    #===========================================================================
    # except:   
    #     from PyQt4 import QtGui
    #     from PyQt4 import QtCore    
    #===========================================================================
    
    q_image = QtGui.QImage(image_path)
    sq_scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding) 
    if sq_scaled.width() <= sq_scaled.height():
        x = 0
        y = (sq_scaled.height() - height) / 2
    elif sq_scaled.width() >= sq_scaled.height():
        x = (sq_scaled.width() - width) / 2
        y = 0
    copy = sq_scaled.copy(x, y, width, height) 
    if not os.path.isdir(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))        
    copy.save(output_path)
    return output_path


def brows_file(label, formats): #**
    current_file = QtWidgets.QFileDialog.getOpenFileName(
        None,
        label,
        resource.getBrowsPath(),
        formats
        )
    if not current_file[0]:
        return
    os.environ['BROWS_PATH'] = os.path.dirname(current_file[0]) 
    return current_file[0]


def remove_widgets(widgets):
    for widget in widgets:
        widget.deleteLater()
    
def remove_layout_widgets(layout):
    for index in range(layout.count()):
        widget = layout.itemAt(index).widget()
        widget.deleteLater()            

    
    
    
    
