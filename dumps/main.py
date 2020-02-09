# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/dumps/main.ui',
# licensing of '/venture/subins_tutorials/dumps/main.ui' applies.
#
# Created: Mon Feb  3 02:27:11 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treewidget = QtWidgets.QTreeWidget(self.splitter)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treewidget.setObjectName("treewidget")
        self.treewidget.headerItem().setText(0, "1")
        item_0 = QtWidgets.QTreeWidgetItem(self.treewidget)
        self.treewidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treewidget.setSortingEnabled(True)
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "abc", None, -1))
        self.treewidget.setSortingEnabled(__sortingEnabled)

