#!/usr/bin/python
import sys
from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import castingsheet

reload(castingsheet)


def show_window(standalone=False):    
    if not standalone:        
        from studio_usd_pipe.core import smaya
        main_window = smaya.get_qwidget()
        smaya.remove_exists_window('mainwindow_castingsheet')        
        window = castingsheet.Window(parent=main_window, standalone=False)
        window.show()
    if standalone:
        app = QtWidgets.QApplication(sys.argv)
        window = castingsheet.Window(parent=None, standalone=True)
        window.show()
        sys.exit(app.exec_())   
        
        
if __name__ == '__main__':       
    show_window()                 

