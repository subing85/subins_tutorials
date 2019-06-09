# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/crowd/resource/ui/old/publish_ui.ui'
#
# Created: Sun Jun  9 20:20:22 2019
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
        MainWindow.resize(426, 623)
        MainWindow.setStyleSheet(_fromUtf8("QGroupBox\n"
"{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #FFAA00;\n"
"}\n"
"\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_mainwind = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_mainwind.setSpacing(10)
        self.verticalLayout_mainwind.setMargin(10)
        self.verticalLayout_mainwind.setObjectName(_fromUtf8("verticalLayout_mainwind"))
        self.groupBox_input = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_input.sizePolicy().hasHeightForWidth())
        self.groupBox_input.setSizePolicy(sizePolicy)
        self.groupBox_input.setObjectName(_fromUtf8("groupBox_input"))
        self.horizontalLayout_input = QtGui.QHBoxLayout(self.groupBox_input)
        self.horizontalLayout_input.setSpacing(4)
        self.horizontalLayout_input.setContentsMargins(4, 30, 4, 4)
        self.horizontalLayout_input.setObjectName(_fromUtf8("horizontalLayout_input"))
        self.comboBox_layout = QtGui.QComboBox(self.groupBox_input)
        self.comboBox_layout.setStyleSheet(_fromUtf8("font: 63 italic 16pt \"Ubuntu\";"))
        self.comboBox_layout.setObjectName(_fromUtf8("comboBox_layout"))
        self.horizontalLayout_input.addWidget(self.comboBox_layout)
        self.lineEdit_bundle = QtGui.QLineEdit(self.groupBox_input)
        self.lineEdit_bundle.setStyleSheet(_fromUtf8("font: 63 italic 16pt \"Ubuntu\";"))
        self.lineEdit_bundle.setObjectName(_fromUtf8("lineEdit_bundle"))
        self.horizontalLayout_input.addWidget(self.lineEdit_bundle)
        self.verticalLayout_mainwind.addWidget(self.groupBox_input)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_validate = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_validate.setObjectName(_fromUtf8("groupBox_validate"))
        self.verticalLayout_validate = QtGui.QVBoxLayout(self.groupBox_validate)
        self.verticalLayout_validate.setSpacing(4)
        self.verticalLayout_validate.setContentsMargins(4, 30, 4, 4)
        self.verticalLayout_validate.setObjectName(_fromUtf8("verticalLayout_validate"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_validate)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 394, 86))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_validate = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_validate.setObjectName(_fromUtf8("gridLayout_validate"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_validate.addWidget(self.scrollArea)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_validate.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_validate)
        self.groupBox_extactor = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_extactor.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_extactor.setObjectName(_fromUtf8("groupBox_extactor"))
        self.verticalLayout_extactor = QtGui.QVBoxLayout(self.groupBox_extactor)
        self.verticalLayout_extactor.setSpacing(4)
        self.verticalLayout_extactor.setContentsMargins(4, 30, 4, 4)
        self.verticalLayout_extactor.setObjectName(_fromUtf8("verticalLayout_extactor"))
        self.gridLayout_extactor = QtGui.QGridLayout()
        self.gridLayout_extactor.setSpacing(2)
        self.gridLayout_extactor.setObjectName(_fromUtf8("gridLayout_extactor"))
        self.verticalLayout_extactor.addLayout(self.gridLayout_extactor)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_extactor.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox_extactor)
        self.verticalLayout_mainwind.addLayout(self.verticalLayout)
        self.groupBox_publish = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_publish.sizePolicy().hasHeightForWidth())
        self.groupBox_publish.setSizePolicy(sizePolicy)
        self.groupBox_publish.setObjectName(_fromUtf8("groupBox_publish"))
        self.verticalLayout_publish = QtGui.QVBoxLayout(self.groupBox_publish)
        self.verticalLayout_publish.setSpacing(4)
        self.verticalLayout_publish.setMargin(4)
        self.verticalLayout_publish.setObjectName(_fromUtf8("verticalLayout_publish"))
        self.horizontalLayout_publish = QtGui.QHBoxLayout()
        self.horizontalLayout_publish.setSpacing(4)
        self.horizontalLayout_publish.setObjectName(_fromUtf8("horizontalLayout_publish"))
        self.button_testRun = QtGui.QPushButton(self.groupBox_publish)
        self.button_testRun.setObjectName(_fromUtf8("button_testRun"))
        self.horizontalLayout_publish.addWidget(self.button_testRun)
        self.button_publish = QtGui.QPushButton(self.groupBox_publish)
        self.button_publish.setObjectName(_fromUtf8("button_publish"))
        self.horizontalLayout_publish.addWidget(self.button_publish)
        self.verticalLayout_publish.addLayout(self.horizontalLayout_publish)
        self.progressBar = QtGui.QProgressBar(self.groupBox_publish)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 20))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_publish.addWidget(self.progressBar)
        self.verticalLayout_mainwind.addWidget(self.groupBox_publish)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_input.setTitle(_translate("MainWindow", "Inputs", None))
        self.groupBox_validate.setTitle(_translate("MainWindow", "Validate", None))
        self.groupBox_extactor.setTitle(_translate("MainWindow", "Extactor", None))
        self.button_testRun.setText(_translate("MainWindow", "Test Run", None))
        self.button_publish.setText(_translate("MainWindow", "Publish", None))

