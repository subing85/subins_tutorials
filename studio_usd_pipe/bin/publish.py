#!/usr/bin/python

import sys
from PySide import QtGui


def show_window(standalone=False):
    from studio_usd_pipe.core import publish
    my_window = publish.Connect(parent=None, standalone=standalone)
    my_window.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    show_window(standalone=True)
    sys.exit(app.exec_())
