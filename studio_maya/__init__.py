#!/usr/bin/python

import sys
from PySide import QtGui


def show_window(standalone=None):
    from studio_maya.resources.ui import main
    my_window = main.MayaWindow(parent=None)
    my_window.show()
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    show_window(standalone=True)
    sys.exit(app.exec_())
