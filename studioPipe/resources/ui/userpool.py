'''
tier.py 0.0.1 
Date: March 28, 2019
Last modified: March 28, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os

import sys
sys.path.append('/venture/subins_tutorials')

from functools import partial
from PySide import QtGui
from PySide import QtCore
#from studioPipe.core import input
import input

from pprint import pprint
from studioPipe import resources
from studioPipe.api import studioUserpool
from studioPipe.api import studioShows
from studioPipe.api import studioDiscipline

reload(studioUserpool)


class Connect(input.Window):

    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)

        self.localhost = 'root'
        self.name = self.type
        self.type = 'output_db'
        self.tag = self.type
        self.current_show = None
        self.button_data = {}
        self.button_create.clicked.connect(self.create)
        self.set_current_show()
        self.default_tier()

    def set_current_show(self):
        studio_shows = studioShows.Connect()
        current_data = studio_shows.getShows()
        self.input_datas = self.get_widget_data(self.gridlayout)
       
        self.show_widget = None
        self.description_widget = None
        self.add_widget = None
        for k, v in self.input_datas.items():
            if k=='current_show':
                self.show_widget = v['widget']
            if k=='description':
                self.description_widget = v['widget']
             
        # print self.description_widget.geometry()
    
        self.show_widget.addItems(['None'] + current_data)        
        self.show_widget.currentIndexChanged.connect(partial(self.set_show, self.show_widget))
        
        ################################
        self.show_widget.setCurrentIndex(1)
        
    def set_show(self, current_widget, *args):
        self.current_show = str(current_widget.currentText())
        studio_shows = studioShows.Connect()        
        show_iocn = studio_shows.getSpecificValue(self.current_show, 'show_icon')        
        self.image_to_button(self.button_show, show_iocn, 256, 144)

    def default_tier(self):
        row_count = self.gridlayout.rowCount()
        button_add = QtGui.QPushButton(None)
        button_add.setObjectName('button_add')
        button_add.setMinimumSize(QtCore.QSize(35, 25))
        button_add.setMaximumSize(QtCore.QSize(35, 25))
        button_add.setText(u'\u002B')
        button_add.setStyleSheet('color: #0000FF;')       
        self.gridlayout.addWidget(button_add, row_count-1, 1, 1, 1)
        button_add.clicked.connect(partial(self.add_tier, button_add, self.gridlayout, row_count))
                
    def add_tier(self, preivous_button, gridlayout, row):
        if preivous_button in self.button_data:
            self.button_data[preivous_button]['combobox'].deleteLater()            
            self.button_data[preivous_button]['button'].deleteLater()
            preivous_button.setText(u'\u002B')
            preivous_button.setStyleSheet('color: #0000FF;')
            self.button_data.pop(preivous_button)        
            return            
        combobox = QtGui.QComboBox(None)
        combobox.setObjectName('combobox_%s' % row)
        combobox.setEditable(True)
        combobox.setStatusTip(str(row-3))
        items = ['', 'character',
                 'prop',
                 'environment',
                 'dress',
                 'camera',
                 'light']
        combobox.addItems(items)
        self.gridlayout.addWidget(combobox, row-1, 2, 1, 1)
        button_add = QtGui.QPushButton(None)
        button_add.setObjectName('button_add')
        button_add.setMinimumSize(QtCore.QSize(35, 25))
        button_add.setMaximumSize(QtCore.QSize(35, 25))
        button_add.setText(u'\u002B')
        button_add.setStyleSheet('color: #0000FF;')       
        self.gridlayout.addWidget(button_add, row, 1, 1, 1)
        button_add.clicked.connect(partial(self.add_tier, button_add, self.gridlayout, row+1))
        preivous_button.setText(u'\u274C')
        preivous_button.setStyleSheet('color: #FF0004;')      
        data = {
            'combobox': combobox,
            'button': button_add,
            'row': row-1
            }       
        self.button_data.setdefault(preivous_button, data)


    def create(self):
        if not self.current_show:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any show!..', QtGui.QMessageBox.Ok)
        if not self.description_widget:
            warnings.warn('Not found type widget')
            return
        if self.description_widget.currentText()=='None':
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any show discipline description!..', QtGui.QMessageBox.Ok)
            return
        input_data = self.get_data(self.gridlayout)

        studio_discipline = studioUserpool.Connect()        
        studio_discipline.create(self.current_show, input_data['description'], input_data)
        
        QtGui.QMessageBox.information(
            self, 'Information', 'Success - create the show discipline description!..', QtGui.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None, type='userpool', value=None,
        title='User Pool', label='Create your Description Users', width=450, height=379)
    window.show()
    sys.exit(app.exec_())
