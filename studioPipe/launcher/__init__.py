import sys
from PySide import QtGui

from studioPipe.resources.ui import launcher

class SLauncher(launcher.Launcher):
    
    def __init__(self, parent=None, **kwargs):
        super(SLauncher, self).__init__(**kwargs)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = SLauncher(parent=None)
    window.show()
    sys.exit(app.exec_())       