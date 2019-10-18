'''
shows.py 0.0.1 
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


from PySide import QtGui
#from studioPipe.core import input
import input

from pprint import pprint
from studioPipe import resources
from studioPipe.api import studioShows
reload(studioShows)


class Connect(input.Window):

    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)

        self.localhost = 'root'
        self.name = self.type
        self.type = 'output_db'
        self.tag = self.type
        self.db_full_path = os.path.join(
            resources.getWorkspacePath(), self.localhost, '%s.json' % self.name)
        self.button_create.clicked.connect(self.create)

    def create(self):
        input_data = self.get_data(self.gridlayout)
        studio_shows = studioShows.Connect()
        studio_shows.create(input_data)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None, type='shows', value=None,
                     title='Show Inputs', label='Create your Show', width=625, height=436)
    window.show()
    sys.exit(app.exec_())
