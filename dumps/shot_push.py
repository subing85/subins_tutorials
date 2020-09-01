# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/shot_push.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 233)
        self.label_top = QtGui.QLabel(Form)
        self.label_top.setGeometry(QtCore.QRect(4, 34, 65, 17))
        self.label_top.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top.setObjectName("label_top")
        self.combobox_top = QtGui.QComboBox(Form)
        self.combobox_top.setGeometry(QtCore.QRect(75, 34, 92, 26))
        self.combobox_top.setObjectName("combobox_top")
        self.label_sub = QtGui.QLabel(Form)
        self.label_sub.setGeometry(QtCore.QRect(4, 64, 67, 17))
        self.label_sub.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sub.setObjectName("label_sub")
        self.comboBox_sub = QtGui.QComboBox(Form)
        self.comboBox_sub.setGeometry(QtCore.QRect(75, 64, 92, 26))
        self.comboBox_sub.setObjectName("comboBox_sub")
        self.label_assets = QtGui.QLabel(Form)
        self.label_assets.setGeometry(QtCore.QRect(4, 94, 43, 17))
        self.label_assets.setObjectName("label_assets")
        self.treewidget = QtGui.QTreeWidget(Form)
        self.treewidget.setGeometry(QtCore.QRect(75, 94, 222, 135))
        self.treewidget.setHeaderHidden(True)
        self.treewidget.setObjectName("treewidget")
        self.treewidget.headerItem().setText(0, "1")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(301, 148, 103, 26))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(4, 4, 63, 17))
        self.label.setObjectName("label")
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(75, 4, 92, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_top.setText(QtGui.QApplication.translate("Form", "top levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sub.setText(QtGui.QApplication.translate("Form", "sub levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_assets.setText(QtGui.QApplication.translate("Form", "assets", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "pipe type", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "layout", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "animation", None, QtGui.QApplication.UnicodeUTF8))

