# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/shot_pull.ui'
#
# Created: Mon May 18 01:08:54 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 233)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_top = QtGui.QLabel(Form)
        self.label_top.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top.setObjectName("label_top")
        self.gridLayout.addWidget(self.label_top, 0, 0, 1, 1)
        self.combobox_top = QtGui.QComboBox(Form)
        self.combobox_top.setObjectName("combobox_top")
        self.gridLayout.addWidget(self.combobox_top, 0, 1, 1, 2)
        self.label_sub = QtGui.QLabel(Form)
        self.label_sub.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sub.setObjectName("label_sub")
        self.gridLayout.addWidget(self.label_sub, 1, 0, 1, 1)
        self.comboBox_sub = QtGui.QComboBox(Form)
        self.comboBox_sub.setObjectName("comboBox_sub")
        self.gridLayout.addWidget(self.comboBox_sub, 1, 1, 1, 2)
        self.label_assets = QtGui.QLabel(Form)
        self.label_assets.setObjectName("label_assets")
        self.gridLayout.addWidget(self.label_assets, 2, 0, 1, 1)
        self.treewidget = QtGui.QTreeWidget(Form)
        self.treewidget.setHeaderHidden(True)
        self.treewidget.setObjectName("treewidget")
        self.treewidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treewidget, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_top.setText(QtGui.QApplication.translate("Form", "top levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sub.setText(QtGui.QApplication.translate("Form", "sub levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_assets.setText(QtGui.QApplication.translate("Form", "assets", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

