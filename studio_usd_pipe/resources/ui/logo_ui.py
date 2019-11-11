import os

from PySide import QtCore
from PySide import QtGui

from studio_usd_pipe import resources
from studio_usd_pipe.core import widgets


class Connect(QtGui.QWidget):

    def __init__(self, layout, show_icon=None, width=256, height=144):
        super(Connect, self).__init__()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        layout.addLayout(self.horizontalLayout)
        self.button_logo = QtGui.QPushButton(self)
        self.button_logo.setFlat(True)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setMinimumSize(QtCore.QSize(350, 99))
        self.button_logo.setMaximumSize(QtCore.QSize(350, 99))                
        logo_path = os.path.join(resources.getIconPath(), 'logo.png')        
        widgets.image_to_button(self.button_logo, 350, 99, path=logo_path)     
        self.horizontalLayout.addWidget(self.button_logo)       
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)
        self.button_show = QtGui.QPushButton(self)
        self.button_show.setFlat(True)
        self.button_show.setObjectName('button_show')
        # width=176, height=99
        self.button_show.setMinimumSize(QtCore.QSize(width, height))
        self.button_show.setMaximumSize(QtCore.QSize(width, height))
        if show_icon:
            widgets.image_to_button(self.button_show, width, height, path=show_icon)            
        self.horizontalLayout.addWidget(self.button_show)
        
