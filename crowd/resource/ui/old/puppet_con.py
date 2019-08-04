# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/crowd/resource/ui/old/puppet_conf.ui'
#
# Created: Sun Aug  4 22:00:46 2019
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
        Form.resize(583, 509)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 569, 132))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(516, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 5)
        self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.NoEcho)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 1, 4, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMaximum(999999999.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_2.addWidget(self.doubleSpinBox, 1, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtGui.QScrollArea(Form)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 569, 131))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(516, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 2)
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(30, 10, 10, 10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "+", None))
        self.pushButton_7.setText(_translate("Form", "+", None))
        self.pushButton.setText(_translate("Form", "Add", None))
        self.pushButton_8.setText(_translate("Form", "+", None))
        self.pushButton_4.setText(_translate("Form", "+", None))
        self.pushButton_2.setText(_translate("Form", "Add", None))
        self.pushButton_6.setText(_translate("Form", "PushButton", None))
        self.pushButton_5.setText(_translate("Form", "PushButton", None))
        self.comboBox.setItemText(0, _translate("Form", "aaaa", None))
        self.comboBox.setItemText(1, _translate("Form", "aaaa", None))

