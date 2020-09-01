# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/template.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(232, 186)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_type = QtGui.QLabel(Form)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 0, 0, 1, 1)
        self.combobox_type = QtGui.QComboBox(Form)
        self.combobox_type.setObjectName("combobox_type")
        self.gridLayout.addWidget(self.combobox_type, 0, 1, 1, 1)
        self.label_versions = QtGui.QLabel(Form)
        self.label_versions.setObjectName("label_versions")
        self.gridLayout.addWidget(self.label_versions, 1, 0, 1, 1)
        self.combobox_versions = QtGui.QComboBox(Form)
        self.combobox_versions.setObjectName("combobox_versions")
        self.gridLayout.addWidget(self.combobox_versions, 1, 1, 1, 1)
        self.label_latest = QtGui.QLabel(Form)
        self.label_latest.setObjectName("label_latest")
        self.gridLayout.addWidget(self.label_latest, 2, 0, 1, 1)
        self.combobox_latest = QtGui.QComboBox(Form)
        self.combobox_latest.setObjectName("combobox_latest")
        self.gridLayout.addWidget(self.combobox_latest, 2, 1, 1, 1)
        self.label_next = QtGui.QLabel(Form)
        self.label_next.setObjectName("label_next")
        self.gridLayout.addWidget(self.label_next, 3, 0, 1, 1)
        self.button_publish = QtGui.QPushButton(Form)
        self.button_publish.setObjectName("button_publish")
        self.gridLayout.addWidget(self.button_publish, 4, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_type.setText(QtGui.QApplication.translate("Form", "type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_versions.setText(QtGui.QApplication.translate("Form", "versions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_latest.setText(QtGui.QApplication.translate("Form", "latest versions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_next.setText(QtGui.QApplication.translate("Form", "next versions", None, QtGui.QApplication.UnicodeUTF8))
        self.button_publish.setText(QtGui.QApplication.translate("Form", "publish", None, QtGui.QApplication.UnicodeUTF8))

