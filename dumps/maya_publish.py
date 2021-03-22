# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/maya_publish.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 239)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridGroupBox = QtGui.QGroupBox(Form)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.gridGroupBox_2 = QtGui.QGroupBox(Form)
        self.gridGroupBox_2.setObjectName("gridGroupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout.addWidget(self.gridGroupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

