#!/usr/bin/python

import sys
from PySide2 import QtWidgets

def show_window(standalone=None):
    from assetLibrary_maya2018.resources.ui import main
    my_window = main.MainWindow(standalone=standalone)
    my_window.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_window(standalone=True)
    sys.exit(app.exec_())