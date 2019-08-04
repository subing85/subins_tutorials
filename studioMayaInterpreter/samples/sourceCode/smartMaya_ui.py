# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartMaya_ui.ui'
#
# Created: Sun Jul 31 19:41:51 2016
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow_smartMaya(object):
    def setupUi(self, MainWindow_smartMaya):
        MainWindow_smartMaya.setObjectName(_fromUtf8("MainWindow_smartMaya"))
        MainWindow_smartMaya.setEnabled(True)
        MainWindow_smartMaya.resize(593, 517)
        MainWindow_smartMaya.setStyleSheet(_fromUtf8("/* ==============================================\n"
"                QWidget\n"
"=============================================== */\n"
"QWidget\n"
"{\n"
"                font:10pt \"Arial\";\n"
"}\n"
"/* ==============================================\n"
"                QLineEdit\n"
"=============================================== */\n"
"QLineEdit\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;\n"
"}\n"
" \n"
"QLineEdit::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
" \n"
"/* ==============================================\n"
"                QPushButton\n"
"=============================================== */\n"
"QPushButton\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;        \n"
" \n"
"}\n"
" \n"
"QPushButton::menu-indicator:open\n"
"{\n"
"                position: relative;          \n"
"                top: 2px; left: 2px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
"/* ==============================================\n"
"                QLabel\n"
"=============================================== */\n"
"QLabel\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;\n"
"}\n"
" \n"
"QLabel::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
"/* ==============================================\n"
"                QTreeWidget\n"
"=============================================== */\n"
"QTreeWidget\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;\n"
"}\n"
" \n"
"QTreeWidget::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
"/* ==============================================\n"
"                QGroupBox\n"
"=============================================== */\n"
"QGroupBox\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;\n"
"}\n"
" \n"
"QGroupBox::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
"/* ==============================================\n"
"                QProgressBar\n"
"=============================================== */\n"
"QProgressBar::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}\n"
"/* ==============================================\n"
"                QTextEdit\n"
"=============================================== */\n"
"QTextEdit\n"
"{\n"
"                padding: 1px;\n"
"                border: 1px solid #ffaa00;\n"
"                border-radius: 2px;\n"
"}\n"
" \n"
"QLabel::hover\n"
"{\n"
"                border: 1px solid #55aaff;\n"
"}"))
        self.centralwidget_smartMaya = QtGui.QWidget(MainWindow_smartMaya)
        self.centralwidget_smartMaya.setObjectName(_fromUtf8("centralwidget_smartMaya"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget_smartMaya)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_toolBar = QtGui.QGroupBox(self.centralwidget_smartMaya)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_toolBar.sizePolicy().hasHeightForWidth())
        self.groupBox_toolBar.setSizePolicy(sizePolicy)
        self.groupBox_toolBar.setObjectName(_fromUtf8("groupBox_toolBar"))
        self.horizontalLayout_toolBar = QtGui.QHBoxLayout(self.groupBox_toolBar)
        self.horizontalLayout_toolBar.setSpacing(2)
        self.horizontalLayout_toolBar.setMargin(0)
        self.horizontalLayout_toolBar.setObjectName(_fromUtf8("horizontalLayout_toolBar"))
        self.verticalLayout.addWidget(self.groupBox_toolBar)
        self.groupBox = QtGui.QGroupBox(self.centralwidget_smartMaya)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.groupBox)
        self.textEdit_result = QtGui.QTextEdit(self.centralwidget_smartMaya)
        self.textEdit_result.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setOverwriteMode(False)
        self.textEdit_result.setObjectName(_fromUtf8("textEdit_result"))
        self.verticalLayout.addWidget(self.textEdit_result)
        self.progressBar = QtGui.QProgressBar(self.centralwidget_smartMaya)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtGui.QLabel(self.centralwidget_smartMaya)
        self.label.setEnabled(True)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 100)
        self.verticalLayout.setStretch(2, 50)
        self.verticalLayout.setStretch(3, 10)
        MainWindow_smartMaya.setCentralWidget(self.centralwidget_smartMaya)
        self.menubar = QtGui.QMenuBar(MainWindow_smartMaya)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        MainWindow_smartMaya.setMenuBar(self.menubar)
        self.action_new = QtGui.QAction(MainWindow_smartMaya)
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_open = QtGui.QAction(MainWindow_smartMaya)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_save = QtGui.QAction(MainWindow_smartMaya)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_saveAs = QtGui.QAction(MainWindow_smartMaya)
        self.action_saveAs.setObjectName(_fromUtf8("action_saveAs"))
        self.action_quit = QtGui.QAction(MainWindow_smartMaya)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_importMayaFile = QtGui.QAction(MainWindow_smartMaya)
        self.action_importMayaFile.setObjectName(_fromUtf8("action_importMayaFile"))
        self.action_importMelPython = QtGui.QAction(MainWindow_smartMaya)
        self.action_importMelPython.setObjectName(_fromUtf8("action_importMelPython"))
        self.action_aboutApplication = QtGui.QAction(MainWindow_smartMaya)
        self.action_aboutApplication.setObjectName(_fromUtf8("action_aboutApplication"))
        self.action_preference = QtGui.QAction(MainWindow_smartMaya)
        self.action_preference.setObjectName(_fromUtf8("action_preference"))
        self.action_startToExecute = QtGui.QAction(MainWindow_smartMaya)
        self.action_startToExecute.setObjectName(_fromUtf8("action_startToExecute"))
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_saveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuEdit.addAction(self.action_importMayaFile)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_importMelPython)
        self.menuSettings.addAction(self.action_preference)
        self.menuHelp.addAction(self.action_aboutApplication)
        self.menuRun.addAction(self.action_startToExecute)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow_smartMaya)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_smartMaya)

    def retranslateUi(self, MainWindow_smartMaya):
        MainWindow_smartMaya.setWindowTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_result.setHtml(QtGui.QApplication.translate("MainWindow_smartMaya", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "subing85@gmail.com", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRun.setTitle(QtGui.QApplication.translate("MainWindow_smartMaya", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_saveAs.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_importMayaFile.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Import Maya File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_importMelPython.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Import Mel/Python", None, QtGui.QApplication.UnicodeUTF8))
        self.action_aboutApplication.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "About Application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_preference.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.action_startToExecute.setText(QtGui.QApplication.translate("MainWindow_smartMaya", "Start To Execute", None, QtGui.QApplication.UnicodeUTF8))

