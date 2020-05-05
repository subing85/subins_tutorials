# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/studioLauncher_ui.ui'
#
# Created: Tue May  5 18:28:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 637)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)
        self.splitter_1 = QtGui.QSplitter(self.centralwidget)
        self.splitter_1.setLineWidth(5)
        self.splitter_1.setMidLineWidth(1)
        self.splitter_1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_1.setHandleWidth(4)
        self.splitter_1.setObjectName("splitter_1")
        self.listWidget = QtGui.QListWidget(self.splitter_1)
        self.listWidget.setObjectName("listWidget")
        self.splitter_2 = QtGui.QSplitter(self.splitter_1)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_3 = QtGui.QSplitter(self.splitter_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.listWidget_2 = QtGui.QListWidget(self.splitter_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtGui.QListWidget(self.splitter_3)
        self.listWidget_3.setObjectName("listWidget_3")
        self.textEdit = QtGui.QTextEdit(self.splitter_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.splitter_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))

