# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/dumps/main.ui'
#
# Created: Sat Nov  2 21:27:27 2019
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 453)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.treewidget.setObjectName(_fromUtf8("treewidget"))
        self.treewidget.headerItem().setText(0, _fromUtf8("1"))
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        self.treewidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.treewidget.setSortingEnabled(True)
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, _translate("MainWindow", "abc", None))
        item_0.setWhatsThis(0, _translate("MainWindow", "hellooooooooo", None))
        self.treewidget.setSortingEnabled(__sortingEnabled)

