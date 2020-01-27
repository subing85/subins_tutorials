#!/usr/bin/python

import sys
from PySide2 import QtWidgets
from studio_usd_pipe.resource.ui import preference

from studio_usd_pipe.utils import maya_utils


def show_window(standalone=False):    
    if not standalone:        
        # main_window = maya_utils.get_qwidget()
        main_window = None
        maya_utils.remove_exists_window('preference_widget')        
        my_window = preference.Connect(
            parent=main_window,
            type='preferences',
            value=None,
            title='Preferences',
            width=662,
            height=380)
        my_window.show()
    if standalone:
        # if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = preference.Connect(
            parent=None,
            type='preferences',
            value=None,
            title='Preferences',
            width=662,
            height=380
            )
        window.show()
        sys.exit(app.exec_())
    
