# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/modelLibrary/resources/ui/pre.ui'
#
# Created: Fri Jan 18 00:25:46 2019
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(534, 194)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.g = QtGui.QGroupBox(Form)
        self.g.setObjectName(_fromUtf8("g"))
        self.gridLayout = QtGui.QGridLayout(self.g)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.g)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.g)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.g)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.g)
        self.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.g)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_cancel = QtGui.QPushButton(Form)
        self.button_cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontalLayout.addWidget(self.button_cancel)
        self.button_apply = QtGui.QPushButton(Form)
        self.button_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.horizontalLayout.addWidget(self.button_apply)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.g.setTitle(_translate("Form", "Path", None))
        self.pushButton.setText(_translate("Form", "-", None))
        self.pushButton_2.setText(_translate("Form", "...", None))
        self.pushButton_3.setText(_translate("Form", "+", None))
        self.button_cancel.setText(_translate("Form", "Cancel", None))
        self.button_apply.setText(_translate("Form", "Apply", None))

