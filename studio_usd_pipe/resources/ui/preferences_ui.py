import os
import sys
import json
import shutil
import getpass
import warnings

from PySide import QtGui
from PySide import QtCore
from datetime import datetime

from studio_usd_pipe import resources
from studio_usd_pipe.core import inputs
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.resources.ui import input_ui


class Connect(input_ui.Window):

    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)
        self.preferences_path = resources.getPreferencesPath()
        self.set_current()
        self.button_create.clicked.connect(self.create)

    def set_current(self):
        if not os.path.isfile(self.preferences_path):
            return
        bundle_data = None
        with (open(self.preferences_path, 'r')) as open_data:
            bundle_data = json.load(open_data)
        if not bundle_data:
            return
        if not bundle_data['enable']:
            return
        input_data = self.get_widget_data(self.gridlayout)

        for k, v in bundle_data['data'].items():
            if k not in input_data:
                continue
            input_data[k]['widget'].setText(v)

        if 'icon' in input_data:
            qsize = input_data['icon']['widget'].minimumSize()
            self.image_to_button(
                input_data['icon']['widget'],
                qsize.width(),
                qsize.height(),
                bundle_data['data']['show_icon']
            )

    def create(self):
        input_data = self.get_data(self.gridlayout)
        show_icon_path = self.update_show_icon(input_data['shows_directory'])
        input_data['show_icon'] = show_icon_path
        tool_name = platforms.get_tool_prity_name()
        bundle_data = {
            'comment': 'subin gopi tool kits',
            'created_date': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'last_modified': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'author': 'Subin Gopi',
            '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': '# WARNING! All changes made in this file will be lost!',
            'description': 'This data contain information about {} preferences'.format(tool_name),
            'type': 'preferences_inputs',
            'enable': True,
            'user': getpass.getuser(),
            'data': input_data
        }

        if not os.path.isdir(os.path.dirname(self.preferences_path)):
            os.makedirs(os.path.dirname(self.preferences_path))

        with (open(self.preferences_path, 'w')) as open_data:
            open_data.write(json.dumps(bundle_data, indent=4))
            open_data.close()
            message = '\nPreferences saved successfully!...'
            print json.dumps(bundle_data['data'], indent=4), message
            QtGui.QMessageBox.information(
                self, 'Information', message, QtGui.QMessageBox.Ok)
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
    app = QtGui.QApplication(sys.argv)
    window = Connect(
        parent=None,
        type='preferences',
        value=None,
        title='Preferences',
        width=822,
        height=376
    )
    window.show()
    sys.exit(app.exec_())
