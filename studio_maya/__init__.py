#!/usr/bin/python

import sys
from PySide import QtGui

print 'hello'

def show_window(standalone=None):
    from studioMaya.resources.ui import main
    my_window = main.MayaWindow(parent=None)
    my_window.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = show_window()
    sys.exit(app.exec_())

