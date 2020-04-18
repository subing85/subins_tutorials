#!/usr/bin/python

import sys
from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import push
        
# if __name__ == '__main__':
app = QtWidgets.QApplication(sys.argv)
my_window = push.Window(parent=None)
my_window.show()
sys.exit(app.exec_())
        

