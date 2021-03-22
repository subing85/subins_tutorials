# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/tx_maker.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 470)
        self.gridlayout = QtGui.QGridLayout(Form)
        self.gridlayout.setObjectName("gridlayout")
        self.label_txmaker = QtGui.QLabel(Form)
        self.label_txmaker.setObjectName("label_txmaker")
        self.gridlayout.addWidget(self.label_txmaker, 0, 0, 1, 1)
        self.lineedit_txmaker = QtGui.QLineEdit(Form)
        self.lineedit_txmaker.setObjectName("lineedit_txmaker")
        self.gridlayout.addWidget(self.lineedit_txmaker, 0, 1, 1, 1)
        self.button_txmaker = QtGui.QPushButton(Form)
        self.button_txmaker.setObjectName("button_txmaker")
        self.gridlayout.addWidget(self.button_txmaker, 0, 2, 1, 1)
        self.label_source = QtGui.QLabel(Form)
        self.label_source.setObjectName("label_source")
        self.gridlayout.addWidget(self.label_source, 1, 0, 1, 1)
        self.lineedit_source = QtGui.QLineEdit(Form)
        self.lineedit_source.setObjectName("lineedit_source")
        self.gridlayout.addWidget(self.lineedit_source, 1, 1, 1, 1)
        self.button_source = QtGui.QPushButton(Form)
        self.button_source.setObjectName("button_source")
        self.gridlayout.addWidget(self.button_source, 1, 2, 1, 1)
        self.treewidget = QtGui.QTreeWidget(Form)
        self.treewidget.setObjectName("treewidget")
        self.gridlayout.addWidget(self.treewidget, 2, 1, 1, 1)
        self.label_out = QtGui.QLabel(Form)
        self.label_out.setObjectName("label_out")
        self.gridlayout.addWidget(self.label_out, 3, 0, 1, 1)
        self.lineedit_out = QtGui.QLineEdit(Form)
        self.lineedit_out.setObjectName("lineedit_out")
        self.gridlayout.addWidget(self.lineedit_out, 3, 1, 1, 1)
        self.button_out = QtGui.QPushButton(Form)
        self.button_out.setObjectName("button_out")
        self.gridlayout.addWidget(self.button_out, 3, 2, 1, 1)
        self.button_create = QtGui.QPushButton(Form)
        self.button_create.setObjectName("button_create")
        self.gridlayout.addWidget(self.button_create, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_txmaker.setText(QtGui.QApplication.translate("Form", "tx_maker", None, QtGui.QApplication.UnicodeUTF8))
        self.button_txmaker.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_source.setText(QtGui.QApplication.translate("Form", "source", None, QtGui.QApplication.UnicodeUTF8))
        self.button_source.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "index", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(1, QtGui.QApplication.translate("Form", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_out.setText(QtGui.QApplication.translate("Form", "out", None, QtGui.QApplication.UnicodeUTF8))
        self.button_out.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_create.setText(QtGui.QApplication.translate("Form", "create", None, QtGui.QApplication.UnicodeUTF8))

