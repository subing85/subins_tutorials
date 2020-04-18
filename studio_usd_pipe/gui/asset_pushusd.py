#!/usr/bin/python

import sys
from PySide2 import QtWidgets

from studio_usd_pipe.utils import smaya
from studio_usd_pipe.resource.ui import pushusd
reload(pushusd)


def show_window(standalone=False):    
      
    if not standalone:        
        main_window = smaya.get_qwidget()
        # main_window = None
        smaya.remove_exists_window('mainwindow_pullusd')        
        my_window = pushusd.Window(parent=main_window, mode='assets')
        my_window.show()
            
    if standalone:
        # if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        my_window = pushusd.Window(parent=None, mode='assets')
        my_window.show()
        sys.exit(app.exec_())
        
        
    