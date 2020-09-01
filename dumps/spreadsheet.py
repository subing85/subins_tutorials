# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/spreadsheet.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combobox_pipe = QtGui.QComboBox(self.centralwidget)
        self.combobox_pipe.setObjectName("combobox_pipe")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/batman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combobox_pipe.addItem(icon, "")
        self.horizontalLayout.addWidget(self.combobox_pipe)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treewidget = QtGui.QTreeWidget(self.centralwidget)
        self.treewidget.setObjectName("treewidget")
        self.verticalLayout.addWidget(self.treewidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_pipe.setItemText(0, QtGui.QApplication.translate("MainWindow", "New Item", "gopi", QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "number", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Subin", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Sachin", None, QtGui.QApplication.UnicodeUTF8))

import icon_rc
