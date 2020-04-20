#!/usr/bin/python
import sys
from PySide2 import QtWidgets

from studio_usd_pipe.utils import smaya
from studio_usd_pipe.resource.ui import push
reload(push)


def show_window(standalone=True):    
    if not standalone:        
        from studio_usd_pipe.api import studioMaya 
        studio_maya = studioMaya.Maya()
        cfile, ctype = studio_maya.get_current_file()
        if not cfile:    
            message = 'Empty scene\nOpen the maya scene and try!...'
            QtWidgets.QMessageBox.critical(
                None, 'warning', message, QtWidgets.QMessageBox.Ok)
            return
        main_window = smaya.get_qwidget()
        smaya.remove_exists_window('widget_asset')        
        my_window = push.Window(parent=main_window)
        my_window.show()
    if standalone:
        app = QtWidgets.QApplication(sys.argv)
        my_window = push.Window(parent=None, standalone=True)
        my_window.show()
        sys.exit(app.exec_())   
        
        
if __name__ == '__main__':       
    show_window()                 

