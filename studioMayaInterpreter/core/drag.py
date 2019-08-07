import os
import sys
import warnings

from PySide import QtCore
from PySide import QtGui

from studioMayaInterpreter import resources
from studioMayaInterpreter.core import widgets


# path = '/venture/subins_tutorials/studioMayaInterpreter/samples/sourceCode/ui/convert'
# print os.path.splitext(path)

class DropArea (QtGui.QTreeWidget):
    # changed = QtCore.pyqtSignal(QtCore.QMimeData)
    changed = QtCore.Signal()

    def __init__(self, parent=None, **kwargs):
        super(DropArea, self).__init__(parent=None)

        #======================================================================
        # try:
        #     __file__
        # except NameError:
        #     __file__ = sys.argv[0]
        #======================================================================
        self.type = None

        if 'type' in kwargs:
            self.type = kwargs['type']
        
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.sortByColumn(1, QtCore.Qt.AscendingOrder)
        self.setColumnCount(1)
        self.setLineWidth(10)
        self.headerItem().setTextAlignment(
            0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.setIconSize(QtCore.QSize(30, 30))

        self.clear()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        # self.column
        mimeData = event.mimeData()
        for each_url in mimeData.urls():
            widgets.create_item(self, self.type, each_url.path())

        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        # self.clear()
        event.accept()


