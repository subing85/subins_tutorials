# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/smartDeform/resources/ui/geometry_ui.ui'
#
# Created: Thu Dec 20 23:01:25 2018
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.groupBox_source = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_source.setObjectName(_fromUtf8("groupBox_source"))
        self.verticalLayout_source = QtGui.QVBoxLayout(self.groupBox_source)
        self.verticalLayout_source.setSpacing(5)
        self.verticalLayout_source.setMargin(5)
        self.verticalLayout_source.setObjectName(_fromUtf8("verticalLayout_source"))
        self.horizontalLayout_source = QtGui.QHBoxLayout()
        self.horizontalLayout_source.setSpacing(1)
        self.horizontalLayout_source.setObjectName(_fromUtf8("horizontalLayout_source"))
        self.lineEdit_source = QtGui.QLineEdit(self.groupBox_source)
        self.lineEdit_source.setEnabled(True)
        self.lineEdit_source.setObjectName(_fromUtf8("lineEdit_source"))
        self.horizontalLayout_source.addWidget(self.lineEdit_source)
        self.button_source = QtGui.QPushButton(self.groupBox_source)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_source.sizePolicy().hasHeightForWidth())
        self.button_source.setSizePolicy(sizePolicy)
        self.button_source.setMinimumSize(QtCore.QSize(20, 20))
        self.button_source.setMaximumSize(QtCore.QSize(16777215, 20))
        self.button_source.setText(_fromUtf8(""))
        self.button_source.setObjectName(_fromUtf8("button_source"))
        self.horizontalLayout_source.addWidget(self.button_source)
        self.verticalLayout_source.addLayout(self.horizontalLayout_source)
        self.comboBox = QtGui.QComboBox(self.groupBox_source)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/wire.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_source.addWidget(self.comboBox)
        self.treeWidget_source = QtGui.QTreeWidget(self.groupBox_source)
        self.treeWidget_source.setAlternatingRowColors(True)
        self.treeWidget_source.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget_source.setHeaderHidden(True)
        self.treeWidget_source.setExpandsOnDoubleClick(False)
        self.treeWidget_source.setObjectName(_fromUtf8("treeWidget_source"))
        self.treeWidget_source.headerItem().setText(0, _fromUtf8("1"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_source)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_source)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_source)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_source)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_source)
        self.treeWidget_source.header().setVisible(False)
        self.verticalLayout_source.addWidget(self.treeWidget_source)
        self.horizontalLayout.addWidget(self.groupBox_source)
        self.groupBox_target = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_target.setObjectName(_fromUtf8("groupBox_target"))
        self.verticalLayout_target = QtGui.QVBoxLayout(self.groupBox_target)
        self.verticalLayout_target.setSpacing(5)
        self.verticalLayout_target.setMargin(5)
        self.verticalLayout_target.setObjectName(_fromUtf8("verticalLayout_target"))
        self.horizontalLayout_target = QtGui.QHBoxLayout()
        self.horizontalLayout_target.setSpacing(1)
        self.horizontalLayout_target.setObjectName(_fromUtf8("horizontalLayout_target"))
        self.lineEdit_target = QtGui.QLineEdit(self.groupBox_target)
        self.lineEdit_target.setEnabled(True)
        self.lineEdit_target.setObjectName(_fromUtf8("lineEdit_target"))
        self.horizontalLayout_target.addWidget(self.lineEdit_target)
        self.button_target = QtGui.QPushButton(self.groupBox_target)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_target.sizePolicy().hasHeightForWidth())
        self.button_target.setSizePolicy(sizePolicy)
        self.button_target.setMinimumSize(QtCore.QSize(20, 20))
        self.button_target.setMaximumSize(QtCore.QSize(16777215, 20))
        self.button_target.setText(_fromUtf8(""))
        self.button_target.setObjectName(_fromUtf8("button_target"))
        self.horizontalLayout_target.addWidget(self.button_target)
        self.verticalLayout_target.addLayout(self.horizontalLayout_target)
        self.listWidget_target = QtGui.QListWidget(self.groupBox_target)
        self.listWidget_target.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_target.setObjectName(_fromUtf8("listWidget_target"))
        self.verticalLayout_target.addWidget(self.listWidget_target)
        self.horizontalLayout.addWidget(self.groupBox_target)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_source.setTitle(_translate("MainWindow", "Source Mesh", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Subin", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Gopi", None))
        self.treeWidget_source.setSortingEnabled(True)
        __sortingEnabled = self.treeWidget_source.isSortingEnabled()
        self.treeWidget_source.setSortingEnabled(False)
        self.treeWidget_source.topLevelItem(0).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_source.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_source.topLevelItem(2).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_source.topLevelItem(3).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_source.topLevelItem(4).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_source.setSortingEnabled(__sortingEnabled)
        self.groupBox_target.setTitle(_translate("MainWindow", "Target Mesh", None))

import test_rc
