'''
import main
reload(main)
a = main.Main()
a.show()
'''

import resource

from PySide import QtGui
from PySide import QtCore

from util import pyside

UI_FILE = resource.getGuiPath()


FROM, BASE = pyside.loadUi(UI_FILE)


class Main(FROM, BASE):
         
    def __init__(self, *args):
        # uic.loadUi(UI_FILE, self)
        
        super(Main, self).__init__(parent=None) #QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)        
        
        
        # self.show()  

