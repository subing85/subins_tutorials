#!/usr/bin/python

import sys

from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import preferences


def show_window():    
    app = QtWidgets.QApplication(sys.argv)
    window = preferences.Window(parent=None)
    window.show()
    sys.exit(app.exec_())
   