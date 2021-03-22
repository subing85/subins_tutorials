#!/usr/bin/python

import sys
from PySide2 import QtGui


def show_window(standalone=False): 
    '''
    :example
        from tools import texture_manager
        reload(texture_manager)   
        texture_manager.show_window(standalone=False)
    '''    
    if standalone:
        from tools.maya_publish import main
        app = QtGui.QApplication(sys.argv)
        window = main.MayaPublish()        
        window.show()
        sys.exit(app.exec_())
    if not standalone:
        from tools.maya_publish import main
        window = main.MayaPublish(parent=None)
        window.show()
