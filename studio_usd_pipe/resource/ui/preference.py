import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import preference
from studio_usd_pipe.resource.ui import inputs


class Connect(inputs.Window):

    def __init__(self, parent=None, **kwargs):        
        super(Connect, self).__init__(parent, **kwargs)  
        self.pref = preference.Preference()
        self.set_current()
        self.update_ui()
        
    def update_ui(self):
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_create = QtWidgets.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout.addWidget(self.button_create)
        self.button_create.clicked.connect(self.create)        
        self.button_cancel.clicked.connect(self.close)        

    def set_current(self, bundle_data=None):
        if not bundle_data:
            bundle_data = self.pref.get() 
        input_data = self.get_widget_data(self.gridlayout)
        for k, v in bundle_data.items():
            if k not in input_data:
                continue
            input_data[k]['widget'].setText(v)
        if 'icon' in input_data:
            qsize = input_data['icon']['widget'].minimumSize()            
            widgets.image_to_button(
                input_data['icon']['widget'],
                qsize.width(),
                qsize.height(),
                path=bundle_data['show_icon']
            )
    
    def create(self):
        input_data = self.get_data(self.gridlayout)
        result = self.pref.create(
            show_directory=input_data['show_directory'],
            show_icon=input_data['show_icon'],
            database_directory=input_data['database_directory'],
            mayapy_directory=input_data['mayapy_directory']
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
    window = Connect(
        parent=None,
        type='preferences',
        value=None,
        title='Preferences',
        width=570,
        height=314
    )
    window.show()
    sys.exit(app.exec_())
