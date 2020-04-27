# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/studioPipe/test/sample_ui.ui'
#
# Created: Sat Apr  6 16:08:00 2019
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
        MainWindow.resize(595, 416)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName(_fromUtf8("verticallayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_logo = QtGui.QLabel(self.groupBox)
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.horizontalLayout.addWidget(self.label_logo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.listWidget = QtGui.QListWidget(self.splitter)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.splitter)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticallayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.action_show = QtGui.QAction(MainWindow)
        self.action_show.setObjectName(_fromUtf8("action_show"))
        self.action_discipline = QtGui.QAction(MainWindow)
        self.action_discipline.setObjectName(_fromUtf8("action_discipline"))
        self.action_preferences = QtGui.QAction(MainWindow)
        self.action_preferences.setObjectName(_fromUtf8("action_preferences"))
        self.action_tier = QtGui.QAction(MainWindow)
        self.action_tier.setObjectName(_fromUtf8("action_tier"))
        self.action_header = QtGui.QAction(MainWindow)
        self.action_header.setObjectName(_fromUtf8("action_header"))
        self.action_userpool = QtGui.QAction(MainWindow)
        self.action_userpool.setObjectName(_fromUtf8("action_userpool"))
        self.menuSettings.addAction(self.action_preferences)
        self.menuSettings.addAction(self.action_show)
        self.menuSettings.addAction(self.action_discipline)
        self.menuSettings.addAction(self.action_tier)
        self.menuSettings.addAction(self.action_header)
        self.menuSettings.addAction(self.action_userpool)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.action_show.setText(_translate("MainWindow", "Show", None))
        self.action_discipline.setText(_translate("MainWindow", "Discipline", None))
        self.action_preferences.setText(_translate("MainWindow", "Preferences", None))
        self.action_tier.setText(_translate("MainWindow", "Tier", None))
        self.action_header.setText(_translate("MainWindow", "Header", None))
        self.action_userpool.setText(_translate("MainWindow", "User Pool", None))


import qt_rc
