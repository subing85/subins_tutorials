
import os
import sys


from PySide import QtCore
from PySide import QtGui
from functools import partial

from studio_usd_pipe import resources
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.core import studioImage


class Window(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.version = platforms.get_tool_version()
        self.icon_path = resources.getIconPath()        
        self.versions = ['major', 'minor', 'patch']
        self.formats = {
            '.ma': 'Maya Ascii',
            '.mb': 'Maya Binary'
        }        
        self.brows_directory = '/venture/test_show/assets/batman'
        

         
        self.setup_ui()
        # self.modify_widgets()
        

    def setup_ui(self):
        self.setObjectName('publish')
        self.resize(750, 650)
        self.setWindowTitle('Publish {}'.format(self.version))
        
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')

        self.groupbox_label = QtGui.QGroupBox(self)
        self.groupbox_label.setObjectName('groupbox_label')
        self.groupbox_label.setTitle('Input File')
        self.groupbox_label.setStyleSheet('font: 16pt;')        
        self.verticallayout.addWidget(self.groupbox_label)

        self.horizontallayout_data = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_data.setObjectName('horizontallayout_data')
        self.horizontallayout_data.setSpacing(10)
        self.horizontallayout_data.setContentsMargins(10, 10, 10, 10)

        self.button_label = QtGui.QPushButton(self.groupbox_label)
        self.button_label.setObjectName('button_label')
        self.button_label.setFlat(True)
        self.button_label.setMinimumSize(QtCore.QSize(100, 100))
        self.button_label.setMaximumSize(QtCore.QSize(100, 100))
        
        open_path = '{}/open.png'.format(self.icon_path)
        self.image_to_button(self.button_label, 100, 100, open_path)
        self.horizontallayout_data.addWidget(self.button_label)

        self.label_label = QtGui.QLabel(self.groupbox_label)
        self.label_label.setObjectName('label_label')
        # self.label_label.setStyleSheet('background-color: rgb(188, 188, 188);')
        self.label_label.setMinimumSize(QtCore.QSize(0, 100))
        self.label_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_label.setStyleSheet('font: 16pt;')        
        self.horizontallayout_data.addWidget(self.label_label)

        self.groupbox_input = QtGui.QGroupBox(self)
        self.groupbox_input.setObjectName('groupbox_input')
        self.groupbox_input.setTitle('Inputs')
        self.verticallayout.addWidget(self.groupbox_input)

        self.verticallayout_input = QtGui.QVBoxLayout(self.groupbox_input)
        self.verticallayout_input.setSpacing(10)
        self.verticallayout_input.setObjectName('verticallayout_input')
        self.verticallayout_input.setContentsMargins(10, 10, 10, 10)

        self.gridlayout_inputs = QtGui.QGridLayout()
        self.gridlayout_inputs.setObjectName('gridlayout_input')
        self.gridlayout_inputs.setContentsMargins(0, 0, 0, 0)
        self.gridlayout_inputs.setHorizontalSpacing(5)
        self.gridlayout_inputs.setVerticalSpacing(5)                
        self.verticallayout_input.addLayout(self.gridlayout_inputs)

        self.button_thumbnail = QtGui.QPushButton(self.groupbox_input)
        self.button_thumbnail.setObjectName('button_thumbnail')
        self.button_thumbnail.setFlat(True)        
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        thumbnail_path = '{}/thumbnail.png'.format(self.icon_path)
        self.image_to_button(self.button_thumbnail, 256, 180, thumbnail_path)
        self.gridlayout_inputs.addWidget(self.button_thumbnail, 1, 0, 1, 1)

        self.label_thumbnail = QtGui.QLabel(self.groupbox_input)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')

        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.label_thumbnail.setSizePolicy(size_policy)
        self.gridlayout_inputs.addWidget(self.label_thumbnail, 0, 0, 1, 1)

        self.label_description = QtGui.QLabel(self.groupbox_input)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.label_description.setSizePolicy(size_policy)
        self.gridlayout_inputs.addWidget(self.label_description, 0, 1, 1, 1)

        self.textedit_description = QtGui.QTextEdit(self.groupbox_input)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.gridlayout_inputs.addWidget(self.textedit_description, 1, 1, 1, 1)

        self.gridlayout_tags = QtGui.QGridLayout()
        self.gridlayout_tags.setObjectName('gridlayout_tags')
        self.gridlayout_tags.setContentsMargins(0, 0, 0, 0)
        self.gridlayout_tags.setHorizontalSpacing(5)
        self.gridlayout_tags.setVerticalSpacing(5)   
        self.verticallayout_input.addLayout(self.gridlayout_tags)        
        
        self.label_category = QtGui.QLabel(self.groupbox_input)
        self.label_category.setObjectName('label_category')  
        self.label_category.setText('Category')
        self.label_category.setAlignment(
            QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                     
        self.gridlayout_tags.addWidget(self.label_category, 0, 0, 1, 1)        

        self.combobox_category = QtGui.QComboBox(self.groupbox_input)
        self.combobox_category.setObjectName('combobox_category')
        self.combobox_category.setEditable(True)
        self.combobox_category.setMinimumSize(QtCore.QSize(150, 0))
        self.gridlayout_tags.addWidget(self.combobox_category, 0, 1, 1, 1)

        spacer_item_tags = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout_tags.addItem(spacer_item_tags, 0, 2, 1, 1)
                
        self.label_tag = QtGui.QLabel(self.groupbox_input)
        self.label_tag.setObjectName('label_tag')      
        self.label_tag.setText('Tag')
        self.label_tag.setAlignment(
            QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)  
        self.gridlayout_tags.addWidget(self.label_tag, 1, 0, 1, 1)
        
        self.combobox_tag = QtGui.QComboBox(self.groupbox_input)
        self.combobox_tag.setObjectName('combobox_tag')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setMinimumSize(QtCore.QSize(150, 0))                 
        self.gridlayout_tags.addWidget(self.combobox_tag, 1, 1, 1, 1)
        
        self.groupbox_publish = QtGui.QGroupBox(self)
        self.groupbox_publish.setObjectName('groupbox_publish')
        self.groupbox_publish.setTitle('Publish')
        self.verticallayout.addWidget(self.groupbox_publish)
      
        self.horizontallayout_publish = QtGui.QHBoxLayout(self.groupbox_publish)
        self.horizontallayout_publish.setObjectName('horizontallayout_publish')        
        self.horizontallayout_publish.setSpacing(10)
        self.horizontallayout_publish.setContentsMargins(10, 10, 10, 10)
        
        self.label_version = QtGui.QLabel(self.groupbox_publish)
        self.label_version.setObjectName('label_version')
        self.label_version.setText('Version Type')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.label_version.setSizePolicy(size_policy)
        self.horizontallayout_publish.addWidget(self.label_version)
        
        self.combobox_version = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_version.setObjectName('combobox_version')
        self.combobox_version.addItems(self.versions)
        self.horizontallayout_publish.addWidget(self.combobox_version)        
        
        self.label_current_version = QtGui.QLabel(self.groupbox_publish)
        self.label_current_version.setObjectName('label_current_version')
        self.label_current_version.setText('0.0.0')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.label_current_version.setSizePolicy(size_policy)
        self.label_current_version.setMinimumSize(QtCore.QSize(100, 0))
        self.label_current_version.setAlignment(QtCore.Qt.AlignCenter)
             
        self.horizontallayout_publish.addWidget(self.label_current_version)        
                
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.horizontallayout_publish.addWidget(self.button_publish)

        self.button_label.clicked.connect(
            partial(self.find_source_file, self.label_label))
        
        self.button_thumbnail.clicked.connect(
            partial(self.find_source_image, self.button_thumbnail))
        
        self.combobox_version.currentIndexChanged.connect(
            partial(self.set_version, self.label_current_version))
        
        
    def image_to_button(self, button, width, height, path=None):
        if not path:
            path = os.path.join(resources.getIconPath(), 'unknown.png')

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(path),
            QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(width - 5, height - 5))            
    
    
    def find_source_file(self, widget):
        current_format = 'image {}'.format(resources.getMayaFormats())
        current_link = QtGui.QFileDialog.getOpenFileName(
            self, 'Browse your source file', self.brows_directory, current_format)
        if not current_link[0]:
            print 'abort!...'
            return
        name, format = os.path.splitext(os.path.basename(current_link[0]))
        if format in self.formats:
            current_format = self.formats[format]
        else:
            current_format = 'unknown'        
        widget.setText('\"{}\"\n< {} >'.format(name, current_format))
        widget.setToolTip(current_link[0])        
        print os.path.splitext(current_link[0])
        
    def find_source_image(self, widget):        
        self.brows_directory = '/mnt/bkp/reference'
        current_format = 'image {}'.format(resources.getImageFormats())
        current_link = QtGui.QFileDialog.getOpenFileName(
            self, 'Browse your source file', self.brows_directory, current_format)
        if not current_link[0]:
            print 'abort!...'
            return       
        open_path = '{}/open.png'.format(self.icon_path)
        self.image_to_button(widget, 256, 180, current_link[0])
        widget.setToolTip(current_link[0])
        
    def set_version(self, widget, *args):
        if args[0]==0:
            widget.setText('1.0.0')
                    
        if args[0]==1:
            widget.setText('0.1.0')
            
        if args[0]==2:
            widget.setText('0.0.0')
            
    
    def start_publish(self, **kwargs):
        
        print kwargs
        
        
    def collect_publish_data(self):
        
        widgets = []
        
        
        
        
        
        
        
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())
