# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/walkCycle/module/controls_ui.ui'
#
# Created: Sun Dec  2 01:13:01 2018
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
        MainWindow.resize(480, 391)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_leg = QtGui.QHBoxLayout()
        self.horizontalLayout_leg.setObjectName(_fromUtf8("horizontalLayout_leg"))
        self.label_leg = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_leg.sizePolicy().hasHeightForWidth())
        self.label_leg.setSizePolicy(sizePolicy)
        self.label_leg.setObjectName(_fromUtf8("label_leg"))
        self.horizontalLayout_leg.addWidget(self.label_leg)
        self.lineEdit_leg = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_leg.setObjectName(_fromUtf8("lineEdit_leg"))
        self.horizontalLayout_leg.addWidget(self.lineEdit_leg)
        self.pushButton_leg = QtGui.QPushButton(self.groupBox)
        self.pushButton_leg.setObjectName(_fromUtf8("pushButton_leg"))
        self.horizontalLayout_leg.addWidget(self.pushButton_leg)
        self.verticalLayout.addLayout(self.horizontalLayout_leg)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 0, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.gridLayout.addWidget(self.spinBox_4, 1, 4, 1, 1)
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout.addWidget(self.spinBox_3, 0, 4, 1, 1)
        self.spinBox_6 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.gridLayout.addWidget(self.spinBox_6, 1, 3, 1, 1)
        self.spinBox_5 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.gridLayout.addWidget(self.spinBox_5, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.label_image = QtGui.QLabel(self.groupBox)
        self.label_image.setObjectName(_fromUtf8("label_image"))
        self.horizontalLayout.addWidget(self.label_image)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_leg.setText(_translate("MainWindow", "Leg", None))
        self.pushButton_leg.setText(_translate("MainWindow", "PushButton", None))
        self.label_3.setText(_translate("MainWindow", "Leg", None))
        self.label_2.setText(_translate("MainWindow", "Leg", None))
        self.label_image.setText(_translate("MainWindow", "TextLabel", None))