# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/main.ui'
#
# Created: Sat Apr 25 15:06:06 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 453)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.treewidget.setObjectName("treewidget")
        self.treewidget.headerItem().setText(0, "1")
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        self.treewidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.setSortingEnabled(True)
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "abc", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.setSortingEnabled(__sortingEnabled)

