#!/usr/bin/python

import sys
from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import preferences
reload(preferences)


def show_window(standalone=True):    
    if not standalone:
        from studio_usd_pipe.utils import smaya        
        main_window = smaya.get_qwidget()
        smaya.remove_exists_window('widget_preferences')        
        my_window = preferences.Window(parent=main_window)
        my_window.show()
    if standalone:
        app = QtWidgets.QApplication(sys.argv)
        my_window = preferences.Window(parent=None)
        my_window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':       
    show_window()                 
        
