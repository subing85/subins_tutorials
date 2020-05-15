#!/usr/bin/python

import sys

from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import launcher


def show_window():    
    app = QtWidgets.QApplication(sys.argv)
    window = launcher.Window(parent=None)
    window.show()
    sys.exit(app.exec_())    


