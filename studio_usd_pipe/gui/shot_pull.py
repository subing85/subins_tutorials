#!/usr/bin/python
import sys
from PySide2 import QtWidgets

from studio_usd_pipe.resource.ui import shot_pull
reload(shot_pull)


def show_window(standalone=True):    
    if not standalone:        
        from studio_usd_pipe.core import smaya
        reload(smaya)
        main_window = smaya.get_qwidget()
        smaya.remove_exists_window('widget_shot_pull')  
        window = shot_pull.Window(parent=main_window, standalone=False, application='maya')
        window.show()
    if standalone:
        app = QtWidgets.QApplication(sys.argv)
        window = shot_pull.Window(parent=None, standalone=True, application='maya')
        window.show()
        sys.exit(app.exec_())   
        
        
if __name__ == '__main__':       
    show_window()                 

