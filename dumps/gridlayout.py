# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/gridlayout.ui'
#
# Created: Sat Apr 25 15:06:07 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 425)
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 30, 301, 261))
        self.toolBox.setStyleSheet("color: rgb(255, 128, 0);")
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 291, 193))
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtGui.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 291, 193))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Form", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "Page 2", None, QtGui.QApplication.UnicodeUTF8))

