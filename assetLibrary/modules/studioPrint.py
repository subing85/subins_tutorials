'''
studioPrint.py 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

try:
    from maya import OpenMaya
except Exception as error:
    pass


class Print(object):

    def __init__(self, type, widget):
        self.type = type
        self.widget = widget

    def display_error(self, message):
        if self.type:
            self.widget.setTextBackgroundColor('gray')
            self.widget.setTextColor('red')
            self.widget.setText('#Error {}'.format(message))
            print '#Error ', message
        else:
            OpenMaya.MGlobal.displayError(str(message))

    def display_info(self, message):
        if self.type:
            self.widget.setTextBackgroundColor('gray')
            self.widget.setTextColor('black')
            self.widget.setText('#Info {}'.format(message))
            print '#Info ', message
        else:
            OpenMaya.MGlobal.displayInfo(str(message))

    def display_warning(self, message):
        if self.type:
            self.widget.setTextBackgroundColor('gray')
            self.widget.setTextColor('yellow')
            self.widget.setText('#Warning {}'.format(message))
            print '\n#Warning ', message
        else:
            OpenMaya.MGlobal.displayWarning(str(message))
