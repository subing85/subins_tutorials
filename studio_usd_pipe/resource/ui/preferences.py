import os
import sys
import tempfile

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import image
from studio_usd_pipe.core import sheader
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.core import preferences

print os.environ['PACKAGE_PATH']


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)        
        # self.setParent(parent)
        self.setWindowFlags(QtCore.Qt.Window)        
        self.mode = 'preferences'        
        self.title = 'Preferences'
        self.width = 572
        self.height = 314
        self.version, self.label = self.set_tool_context()
        self.brows_directory = resource.getWorkspacePath()        
        self.pref = preferences.Preferences()          
        self.setup_ui()
        self.set_current()
        
    def setup_ui(self):
        self.setObjectName('widget_preferences')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version))        
        self.resize(self.width, self.height) 
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.groupbox = QtWidgets.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle('{} <{}>'.format(self.label, self.title))  
        self.verticallayout.addWidget(self.groupbox)             
        self.verticallayout_item = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)                     
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout_item.addLayout(self.horizontallayout)        
        self.button_logo, self.button_show = swidgets.set_header(
            self.horizontallayout, show_icon=None)  
        # space
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout_input.setObjectName('horizontallayout_input') 
        self.verticallayout_item.addLayout(self.horizontallayout_input)
        self.gridlayout = QtWidgets.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)        
        self.label_icon = QtWidgets.QLabel(self.groupbox)
        self.label_icon.setObjectName('label_icon')
        self.label_icon.setText('Show Icon/Image')
        self.label_icon.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_icon, 0, 0, 1, 1)
        self.lineedit_icon = QtWidgets.QLineEdit(self.groupbox)
        self.lineedit_icon.setObjectName('lineedit_icon')
        self.gridlayout.addWidget(self.lineedit_icon, 0, 1, 1, 1)
        self.button_icon = QtWidgets.QPushButton(self.groupbox)
        self.button_icon.setObjectName('button_icon')
        self.button_icon.setText('...')
        self.button_icon.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        self.button_icon.setMinimumSize(QtCore.QSize(25, 25))
        self.button_icon.setMaximumSize(QtCore.QSize(25, 25))      
        self.gridlayout.addWidget(self.button_icon, 0, 2, 1, 1)
        self.label_directory = QtWidgets.QLabel(self.groupbox)
        self.label_directory.setObjectName('label_directory')
        self.label_directory.setText('Show Directory')
        self.label_directory.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_directory, 1, 0, 1, 1)
        self.lineedit_directory = QtWidgets.QLineEdit(self.groupbox)
        self.lineedit_directory.setObjectName('lineedit_directory')
        self.gridlayout.addWidget(self.lineedit_directory, 1, 1, 1, 1)
        self.button_directory = QtWidgets.QPushButton(self.groupbox)
        self.button_directory.setObjectName('button_directory')
        self.button_directory.setText('...')
        self.button_directory.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        self.button_directory.setMinimumSize(QtCore.QSize(25, 25))
        self.button_directory.setMaximumSize(QtCore.QSize(25, 25))      
        self.gridlayout.addWidget(self.button_directory, 1, 2, 1, 1)        
        self.label_database = QtWidgets.QLabel(self.groupbox)
        self.label_database.setObjectName('label_database')
        self.label_database.setText('Data Base Directory')
        self.label_database.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_database, 2, 0, 1, 1)
        self.lineedit_database = QtWidgets.QLineEdit(self.groupbox)
        self.lineedit_database.setObjectName('lineedit_database')
        self.gridlayout.addWidget(self.lineedit_database, 2, 1, 1, 1)
        self.button_database = QtWidgets.QPushButton(self.groupbox)
        self.button_database.setObjectName('button_database')
        self.button_database.setText('...')
        self.button_database.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        self.button_database.setMinimumSize(QtCore.QSize(25, 25))
        self.button_database.setMaximumSize(QtCore.QSize(25, 25))      
        self.gridlayout.addWidget(self.button_database, 2, 2, 1, 1)        
        self.label_maya = QtWidgets.QLabel(self.groupbox)
        self.label_maya.setObjectName('label_maya')
        self.label_maya.setText('Mayapy Directory')
        self.label_maya.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_maya, 3, 0, 1, 1)
        self.lineedit_maya = QtWidgets.QLineEdit(self.groupbox)
        self.lineedit_maya.setObjectName('lineedit_maya')
        self.gridlayout.addWidget(self.lineedit_maya, 3, 1, 1, 1)
        self.button_maya = QtWidgets.QPushButton(self.groupbox)
        self.button_maya.setObjectName('button_maya')
        self.button_maya.setText('...')
        self.button_maya.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        self.button_maya.setMinimumSize(QtCore.QSize(25, 25))
        self.button_maya.setMaximumSize(QtCore.QSize(25, 25))      
        self.gridlayout.addWidget(self.button_maya, 3, 2, 1, 1)  
        
        self.label_python = QtWidgets.QLabel(self.groupbox)
        self.label_python.setObjectName('label_python')
        self.label_python.setText('Python Directory')
        self.label_python.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_python, 4, 0, 1, 1)
        self.lineedit_python = QtWidgets.QLineEdit(self.groupbox)
        self.lineedit_python.setObjectName('lineedit_python')
        self.gridlayout.addWidget(self.lineedit_python, 4, 1, 1, 1)
        self.button_python = QtWidgets.QPushButton(self.groupbox)
        self.button_python.setObjectName('button_python')
        self.button_python.setText('...')
        self.button_python.setStyleSheet(
            'color: #ff007f; border: 1px solid #000000; border-radius: 12px')
        self.button_python.setMinimumSize(QtCore.QSize(25, 25))
        self.button_python.setMaximumSize(QtCore.QSize(25, 25))      
        self.gridlayout.addWidget(self.button_python, 4, 2, 1, 1)  
              
        self.horizontallayout_button = QtWidgets.QHBoxLayout()
        self.horizontallayout_button.setObjectName('horizontallayout_button')
        self.horizontallayout_button.setSpacing(10)
        self.horizontallayout_button.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout_button)
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_button.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout_button.addWidget(self.button_cancel)
        self.button_create = QtWidgets.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout_button.addWidget(self.button_create)
        self.button_create.clicked.connect(self.create)        
        self.button_cancel.clicked.connect(self.close)        
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        contents = {
            'show_icon': {
                'description': 'Browse your show icon/image file',
                'format': '(*.bmp *.jpg *.jpeg *.png *.ppm *.tiff *.xbn *.xpm)',
                'resolution': [640, 400]
                },
            'show_directory': {
                'description': 'Browse your Show Directory'
                },
            'database_directory': {
                'description': 'Browse your database Directory'
                },
            'mayapy_directory': {
                'description': 'Browse your mayapy Directory',
                'format': '(*mayapy*)'
                },
            'python_path': {
                'description': 'Browse your Python Path'
                }         
            }            
        self.button_icon.clicked.connect(partial(self.find_file, self.lineedit_icon, contents['show_icon'], display=True))
        self.button_directory.clicked.connect(partial(self.find_directory, self.lineedit_directory, contents['show_directory']))
        self.button_database.clicked.connect(partial(self.find_directory, self.lineedit_database, contents['database_directory']))
        self.button_maya.clicked.connect(partial(self.find_file, self.lineedit_maya, contents['mayapy_directory']))
        self.button_python.clicked.connect(partial(self.find_directory, self.lineedit_python, contents['python_path']))
        
    def set_tool_context(self):
        config = sheader.Configure()
        config.tool()
        return config.version, config.pretty   

    def set_current(self):
        bundle_data = self.pref.get()        
        if not bundle_data:
            return        
        self.lineedit_icon.setText(bundle_data['show_icon'])
        self.lineedit_directory.setText(bundle_data['show_directory'])
        self.lineedit_database.setText(bundle_data['database_directory'])
        self.lineedit_maya.setText(bundle_data['mayapy_directory'])
        self.lineedit_python.setText(bundle_data['python_path'])
        size = self.button_show.minimumSize()
        self.snapshot(self.button_show, bundle_data['show_icon'], [size.width(), size.height()])

    def find_file(self, widget, content, display=False):    
        current_link = QtWidgets.QFileDialog.getOpenFileName(
            self, content['description'], self.brows_directory, content['format'])
        self.brows_directory = os.path.dirname(current_link[0])
        widget.setText(current_link[0])
        if display:
            qsize = self.button_show.minimumSize()
            resolution = [qsize.width(), qsize.height()]
            self.snapshot(self.button_show, current_link[0], resolution)  
            
    def find_directory(self, widget, content):    
        current_link = QtWidgets.QFileDialog.getExistingDirectory(
            self, content['description'], self.brows_directory)
        self.brows_directory = current_link
        widget.setText(current_link)              
            
    def snapshot(self, button, image_file, resolution):
        output_path = os.path.join(
            tempfile.gettempdir(), 'studio_image_snapshot.png')
        q_image_path = image.image_resize(
            image_file,
            output_path,
            resolution[0],
            resolution[1],
            )  
        if not q_image_path:
            QtWidgets.QMessageBox.warning(
                self,
                'Warning',
                'Not able to process image!..',
                QtWidgets.QMessageBox.Ok
                )
            return
        swidgets.image_to_button(
            button, resolution[0], resolution[1], path=q_image_path)
        button.setStatusTip(q_image_path)
        return q_image_path
    
    def get_widget_data(self):        
        widgets = {
            'show_icon': self.lineedit_icon,
            'show_directory': self.lineedit_directory,
            'database_directory': self.lineedit_database,
            'mayapy_directory': self.lineedit_maya,
            'python_path': self.lineedit_python
            }        
        widget_data = {}        
        for key, widget in widgets.items():
            widget_value = widget.text().encode()            
            if not widget_value:
                widget_value = None
            widget_data.setdefault(key, widget_value)        
        show_icon = self.button_show.statusTip().encode()        
        if show_icon:
            widget_data['show_icon'] = show_icon
        return widget_data

    def create(self):
        widget_data = self.get_widget_data()
        if None in widget_data.values():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty input!...', QtWidgets.QMessageBox.Ok)
            return                       
        result = self.pref.create(
            show_directory=widget_data['show_directory'],
            show_icon=widget_data['show_icon'],
            database_directory=widget_data['database_directory'],
            mayapy_directory=widget_data['mayapy_directory'],
            python_path=widget_data['python_path']
            )
        if not result:
            QtWidgets.QMessageBox.critical(
                self, 'Critical', 'Failed!...', QtWidgets.QMessageBox.Ok)
            return        
        message = '\nPreferences saved successfully!...'
        QtWidgets.QMessageBox.information(
            self, 'Information', message, QtWidgets.QMessageBox.Ok)        
        self.close()

            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())            
                  
