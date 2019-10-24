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
import warnings

from functools import partial
from PySide import QtGui
#from studioPipe.core import input
import input

from pprint import pprint
from studioPipe import resources
from studioPipe.api import studioDiscipline
from studioPipe.api import studioShows

reload(studioDiscipline)


class Connect(input.Window):

    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)

        self.localhost = 'root'
        self.name = self.type
        self.type = 'output_db'
        self.tag = self.type
        self.current_show = None
        
        self.button_create.clicked.connect(self.create)
        self.set_current_show()

    def set_current_show(self):
        studio_shows = studioShows.Connect()
        current_data = studio_shows.getShows()
        self.input_datas = self.get_widget_data(self.gridlayout)
        self.show_widget = None
        self.description_widget = None
        for k, v in self.input_datas.items():
            if k=='current_show':
                self.show_widget = v['widget']
            if k=='description':
                self.description_widget = v['widget']

        self.show_widget.addItems(['None'] + current_data)        
        self.show_widget.currentIndexChanged.connect(partial(self.set_show, self.show_widget))
        self.show_widget.setCurrentIndex(1)
        

    def set_show(self, current_widget, *args):
        self.current_show = str(current_widget.currentText())
        studio_shows = studioShows.Connect()        
        show_iocn = studio_shows.getSpecificValue(self.current_show, 'show_icon')        
        self.image_to_button(self.button_show, show_iocn, 256, 144)

    def create(self):
        if not self.current_show:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any show!..', QtGui.QMessageBox.Ok)
        if not self.description_widget:
            warnings.warn('Not found type widget')
            return
        if self.description_widget.currentText()=='None':
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any discipline type(description)!..', QtGui.QMessageBox.Ok)
            return
        
        input_data = self.get_data(self.gridlayout)
        
        pprint(input_data)
        
        studio_discipline = studioDiscipline.Connect()        
        studio_discipline.create(self.current_show, input_data)
        
        QtGui.QMessageBox.information(
            self, 'Information', 'Success - create the discipline!..', QtGui.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None, type='discipline', value=None,
                     title='Disciplines Inputs', label='Create your Show Disciplines', width=500, height=407)
    window.show()
    sys.exit(app.exec_())
