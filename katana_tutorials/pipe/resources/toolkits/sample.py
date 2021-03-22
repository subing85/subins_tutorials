KEY = 'toolkit'
NAME = 'Sample'
ORDER = 0
ENABLE = True
ICON = 'sample.png'
LAST_MODIFIED = 'Jun 20, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'Sample toolkit'


def execute():
    from PyQt4 import QtGui
    message = '\n#welcome to katana python tutorials\n[https://www.subins-toolkits.com]'    
    QtGui.QMessageBox.information(
            None, 'Sample', message, QtGui.QMessageBox.Ok) 