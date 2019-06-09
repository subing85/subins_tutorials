# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/crowd/resource/ui/old/test_ui.ui'
#
# Created: Sun Jun  9 20:35:17 2019
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
        MainWindow.resize(800, 765)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 90, 471, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 2)
        
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.widget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.widget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.widget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        
        self.gridLayout.addWidget(self.textEdit_2, 3, 1, 1, 2)
        
        self.pushButton_9 = QtGui.QPushButton(self.widget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        
        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.widget)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        
        self.gridLayout.addWidget(self.pushButton_11, 4, 1, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.widget)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        
        self.gridLayout.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.widget)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        
        self.gridLayout.addWidget(self.textEdit_3, 5, 1, 1, 2)
        
        self.pushButton_8 = QtGui.QPushButton(self.widget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        
        self.gridLayout.addWidget(self.pushButton_8, 6, 0, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.widget)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        
        self.gridLayout.addWidget(self.pushButton_10, 6, 1, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.widget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        
        self.gridLayout.addWidget(self.pushButton_7, 6, 2, 1, 1)
        self.textEdit_4 = QtGui.QTextEdit(self.widget)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        
        self.gridLayout.addWidget(self.textEdit_4, 7, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton", None))

