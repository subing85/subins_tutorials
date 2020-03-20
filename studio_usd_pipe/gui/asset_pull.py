#!/usr/bin/python

import sys
from PySide2 import QtWidgets

from studio_usd_pipe.utils import smaya
from studio_usd_pipe.api import studioMaya
from studio_usd_pipe.resource.ui import pull
reload(pull)


def show_window(standalone=False):    
    studio_maya = studioMaya.Maya()
    #===========================================================================
    # cfile, ctype = studio_maya.get_current_file()
    # if not cfile:    
    #     message = 'Empty scene\nOpen the maya scene and try!...'
    #     QtWidgets.QMessageBox.critical(
    #         None, 'warning', message, QtWidgets.QMessageBox.Ok)
    #     return
    #===========================================================================
      
    if not standalone:        
        main_window = smaya.get_qwidget()
        # main_window = None
        smaya.remove_exists_window('widget_asset')        
        my_window = pull.Window(
            parent=main_window,
            mode='asset_pull',
            value=None,
            title='Asset Pull',
            width=570,
            height=314)
        my_window.show()
            
    if standalone:
        # if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        my_window = pull.Window(
            parent=None,
            mode='asset_pull',
            value=None,
            title='Asset Pull',
            width=570,
            height=314
            )
        my_window.show()
        sys.exit(app.exec_())
    
