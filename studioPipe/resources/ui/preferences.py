'''
preferences.py 0.0.1 
Date: March 16, 2019
Last modified: March 16, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import sys
sys.path.append('/venture/subins_tutorials')

import warnings
from PySide import QtGui

from studioPipe import resources
from studioPipe.api import studioPreferences
#from studioPipe.core import input
import input


class Connect(input.Window):

    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)
        self.dirname = os.path.join(resources.getWorkspacePath())
        self.localhost = self.type
        self.name = self.type
        self.type = 'output_db'
        self.tag = self.type
        self.db_full_path = os.path.join(
            resources.getWorkspacePath(), self.localhost, '%s.json' % self.name)
        self.input_datas = self.get_widget_data(self.gridlayout)
        self.set_current()
        self.button_create.clicked.connect(self.create)

    def set_current(self):
        if not os.path.isfile(self.db_full_path):
            current_data = resources.getDefaultPreferences()
        else:
            studio_output = studioPreferences.Connect(
                dirname=self.dirname,
                localhost=self.localhost,
                name=self.name,
                type=self.type,
                tag=self.tag
            )
            current_data = studio_output.getOutputData()
        for k, v in self.input_datas.items():
            if k not in current_data:
                continue
            v['widget'].setText(current_data[k])

    def create(self):
        input_data = self.get_data(self.gridlayout)
        studio_preferences = studioPreferences.Connect(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag
        )
        studio_preferences.create(input_data)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None, type='preferences', value=None,
                     title='Preferences', label='Inputs', width=762, height=556)
    window.show()
    sys.exit(app.exec_())
