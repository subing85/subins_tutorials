# Editor.py - the Qt4 UI (this is only imported in the interactive GUI,
# not in batch or scripting modes).

from PyQt4 import QtGui


class TemplateEditor(QtGui.QWidget):
    
    def __init__(self, parent, node):
        QtGui.QWidget.__init__(self, parent)
        
        print 'node', node
