#!/usr/bin/python
import sys
from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import asset_composition

reload(asset_composition)


def show_window(standalone=False):    
    if not standalone:        
        from studio_usd_pipe.core import smaya
        main_window = smaya.get_qwidget()
        smaya.remove_exists_window('mainwindow_asset_composition')        
        window = asset_composition.Window(parent=main_window, standalone=False, application='pixar')
        window.show()
    if standalone:
        app = QtWidgets.QApplication(sys.argv)
        window = asset_composition.Window(parent=None, standalone=True, application='pixar')
        window.show()
        sys.exit(app.exec_())   
        
        
        
if __name__ == '__main__':       
    show_window()                 

