import os
import sys
import json
import shutil
import getpass
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import inputs
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import preference
from studio_usd_pipe.resource.ui import inputs
reload(inputs)


class Connect(inputs.Window):

    def __init__(self, parent=None, **kwargs):        
        super(Connect, self).__init__(parent, **kwargs)  
        self.setObjectName('preference_widget')
        self.pref = preference.Preference()       
        bundle_data = self.pref.get() 
        self.set_current(bundle_data)
        self.button_create.clicked.connect(self.create)        
        _pref = preference.Preference()
        print 'release\t', _pref.config.name, '\t', _pref.config.version               

    def set_current(self, bundle_data):
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
            show_directory = input_data['show_directory'],
            show_icon = input_data['show_icon'],
            database_directory = input_data['database_directory'],
            mayapy_directory = input_data['mayapy_directory']
            )        
        if not result:
            QtWidgets.QMessageBox.critical(
                self, 'Critical', 'Failed!...', QtWidgets.QMessageBox.Ok)
            return
        message = '\nPreferences saved successfully!...'
        QtWidgets.QMessageBox.information(
            self, 'Information', message, QtWidgets.QMessageBox.Ok)        
        self.close()        

    def update_show_icon(self, destination):
        temp_path = self.button_show.statusTip()
        destination_path = os.path.join(
            destination,
            'icons',
            'show_icon{}'.format(os.path.splitext(temp_path)[-1])
        )
        if not os.path.isdir(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))
        try:
            shutil.copy2(temp_path, destination_path)
        except Exception as error:
            warnings.warn(str(error))
        return destination_path


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Connect(
        parent=None,
        type='preferences',
        value=None,
        title='Preferences',
        width=662,
        height=380
    )
    window.show()
    sys.exit(app.exec_())

