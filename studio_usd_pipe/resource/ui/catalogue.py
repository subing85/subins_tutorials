import os
import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from studio_usd_pipe import resource
from studio_usd_pipe.core import swidgets

class Catalogue(QtWidgets.QGroupBox):

    def __init__(self, parent=None):  
        super(Catalogue, self).__init__(parent)
        self.setup_ui()
        self.setup_default()

    def setup_ui(self):  
        self.gridlayout_data = QtWidgets.QGridLayout(self)
        self.gridlayout_data.setObjectName('gridlayout_data')
        self.gridlayout_data.setHorizontalSpacing(5)
        self.gridlayout_data.setContentsMargins(5, 5, 5, 5)
        right_align = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        self.label_captions = QtWidgets.QLabel(self)
        self.label_captions.setObjectName('label_captions')
        self.label_captions.setText('caption: ')
        self.label_captions.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_captions, 0, 0, 1, 1)        
        self.label_caption = QtWidgets.QLabel(self)
        self.label_caption.setObjectName('label_caption')
        self.gridlayout_data.addWidget(self.label_caption, 0, 1, 1, 1)        
        self.label_tags = QtWidgets.QLabel(self)
        self.label_tags.setObjectName('label_tags')
        self.label_tags.setText('tag: ')
        self.label_tags.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_tags, 1, 0, 1, 1)        
        self.label_tag = QtWidgets.QLabel(self)
        self.label_tag.setObjectName('label_tag')
        self.gridlayout_data.addWidget(self.label_tag, 1, 1, 1, 1)     
        self.label_types = QtWidgets.QLabel(self)
        self.label_types.setObjectName('label_types')
        self.label_types.setText('type: ')
        self.label_types.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_types, 2, 0, 1, 1)        
        self.label_type = QtWidgets.QLabel(self)
        self.label_type.setObjectName('label_type')
        self.gridlayout_data.addWidget(self.label_type, 2, 1, 1, 1)  
        self.label_users = QtWidgets.QLabel(self)
        self.label_users.setObjectName('label_users')
        self.label_users.setText('owner: ')
        self.label_users.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_users, 3, 0, 1, 1)        
        self.label_user = QtWidgets.QLabel(self)
        self.label_user.setObjectName('label_user')           
        self.gridlayout_data.addWidget(self.label_user, 3, 1, 1, 1) 
        self.label_modifieds = QtWidgets.QLabel(self)
        self.label_modifieds.setObjectName('label_modifieds')
        self.label_modifieds.setText('modified: ')
        self.label_modifieds.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_modifieds, 4, 0, 1, 1)        
        self.label_modified = QtWidgets.QLabel(self)
        self.label_modified.setObjectName('label_modified')
        self.gridlayout_data.addWidget(self.label_modified, 4, 1, 1, 1)
        self.label_showpaths = QtWidgets.QLabel(self)
        self.label_showpaths.setObjectName('label_dates')
        self.label_showpaths.setText('show path: ')
        self.label_showpaths.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_showpaths, 5, 0, 1, 1)        
        self.label_showpath = QtWidgets.QLabel(self)
        self.label_showpath.setObjectName('label_showpath')
        self.gridlayout_data.addWidget(self.label_showpath, 5, 1, 1, 1)        
        self.label_locations = QtWidgets.QLabel(self)
        self.label_locations.setObjectName('label_locations')
        self.label_locations.setText('location: ')
        self.label_locations.setAlignment(right_align)
        self.gridlayout_data.addWidget(self.label_locations, 6, 0, 1, 1)        
        self.label_location = QtWidgets.QLabel(self)
        self.label_location.setObjectName('label_location')
        self.gridlayout_data.addWidget(self.label_location, 6, 1, 1, 1)
        self.label_description = QtWidgets.QLabel(self)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.gridlayout_data.addWidget(self.label_description, 7, 0, 1, 1)        
        self.textedit_description = QtWidgets.QTextEdit(self)
        self.textedit_description.setObjectName('textedit_description')
        self.textedit_description.setReadOnly(True)
        self.textedit_description.setMinimumSize(QtCore.QSize(256, 0))
        self.textedit_description.setMaximumSize(QtCore.QSize(256, 16777215))
        self.gridlayout_data.addWidget(self.textedit_description, 8, 0, 1, 2)   
        self.button_thumbnail = QtWidgets.QPushButton(self)
        self.button_thumbnail.setObjectName('button_thumbnail')
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.gridlayout_data.addWidget(self.button_thumbnail, 9, 0, 1, 2)
    
    def setup_default(self):        
        self.label_caption.clear()        
        self.label_tag.clear()       
        self.label_type.clear()      
        self.label_user.clear()       
        self.label_modified.clear()       
        self.label_showpath.clear()       
        self.label_location.clear()        
        self.textedit_description.clear()
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = os.path.join(resource.getIconPath(), 'thumbnail.png')
        swidgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)
        
    
    def set_catalogue(self, **kwargs):
        self.setup_default()
        self.label_caption.setText(kwargs['caption'])
        self.label_tag.setText(kwargs['tag'])
        self.label_type.setText(kwargs['type'])
        self.label_user.setText(kwargs['user'])
        self.label_modified.setText(kwargs['modified'])
        self.label_showpath.setText(kwargs['show_path'])
        location = '...%s' % (kwargs['location'].split(kwargs['show_path'])[-1])
        self.label_location.setText(location) 
        self.textedit_description.setText(kwargs['description'])
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = kwargs['thumbnail']
        if not os.path.isfile(thumbnail_icon):
            thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        swidgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Catalogue(parent=None)
    window.show()
    sys.exit(app.exec_())         

        
