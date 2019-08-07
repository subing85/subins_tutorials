# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/studioMayaInterpreter/samples/sourceCode/ui/smartMaya_ui.ui'
#
# Created: Tue Aug  6 23:19:53 2019
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
        self.splitter = QtGui.QSplitter(self.centralwidget_smartMaya)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter_2 = QtGui.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(5)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.textEdit_result_2 = QtGui.QTextEdit(self.splitter_2)
        self.textEdit_result_2.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_result_2.setReadOnly(True)
        self.textEdit_result_2.setOverwriteMode(False)
        self.textEdit_result_2.setObjectName(_fromUtf8("textEdit_result_2"))
        self.treeWidget = QtGui.QTreeWidget(self.splitter_2)
        self.treeWidget.setLineWidth(10)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("NO"))
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setText(2, _fromUtf8("3"))
        self.horizontalLayout.addWidget(self.splitter_2)
        self.textEdit_result = QtGui.QTextEdit(self.splitter)
        self.textEdit_result.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setOverwriteMode(False)
        self.textEdit_result.setObjectName(_fromUtf8("textEdit_result"))
        self.verticalLayout.addWidget(self.splitter)
        self.progressBar = QtGui.QProgressBar(self.centralwidget_smartMaya)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtGui.QLabel(self.centralwidget_smartMaya)
        self.label.setEnabled(True)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
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
        MainWindow_smartMaya.setWindowTitle(_translate("MainWindow_smartMaya", "MainWindow", None))
        self.textEdit_result_2.setHtml(_translate("MainWindow_smartMaya", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.setProperty("type", _translate("MainWindow_smartMaya", "maya", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow_smartMaya", "New Column", None))
        self.textEdit_result.setHtml(_translate("MainWindow_smartMaya", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow_smartMaya", "subing85@gmail.com", None))
        self.menuFile.setTitle(_translate("MainWindow_smartMaya", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow_smartMaya", "Edit", None))
        self.menuSettings.setTitle(_translate("MainWindow_smartMaya", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow_smartMaya", "Help", None))
        self.menuRun.setTitle(_translate("MainWindow_smartMaya", "Run", None))
        self.action_new.setText(_translate("MainWindow_smartMaya", "New", None))
        self.action_open.setText(_translate("MainWindow_smartMaya", "Open", None))
        self.action_save.setText(_translate("MainWindow_smartMaya", "Save", None))
        self.action_saveAs.setText(_translate("MainWindow_smartMaya", "Save As", None))
        self.action_quit.setText(_translate("MainWindow_smartMaya", "Quit", None))
        self.action_importMayaFile.setText(_translate("MainWindow_smartMaya", "Import Maya File", None))
        self.action_importMelPython.setText(_translate("MainWindow_smartMaya", "Import Mel/Python", None))
        self.action_aboutApplication.setText(_translate("MainWindow_smartMaya", "About Application", None))
        self.action_preference.setText(_translate("MainWindow_smartMaya", "Preference", None))
        self.action_startToExecute.setText(_translate("MainWindow_smartMaya", "Start To Execute", None))

