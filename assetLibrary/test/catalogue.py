# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/assetLibrary/test/catalogue.ui'
#
# Created: Sat Feb 23 15:20:50 2019
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.treeWidget_folder = QtGui.QTreeWidget(self.splitter_2)
        self.treeWidget_folder.setObjectName(_fromUtf8("treeWidget_folder"))
        self.treeWidget_folder.headerItem().setText(0, _fromUtf8("1"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.group = QtGui.QGroupBox(self.splitter)
        self.group.setObjectName(_fromUtf8("group"))
        self.verticalLayout = QtGui.QVBoxLayout(self.group)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.group)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.group)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.group)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget_search = QtGui.QTreeWidget(self.group)
        self.treeWidget_search.setObjectName(_fromUtf8("treeWidget_search"))
        self.treeWidget_search.headerItem().setText(0, _fromUtf8("No"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_search)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_search)
        self.verticalLayout.addWidget(self.treeWidget_search)
        self.progressBar = QtGui.QProgressBar(self.group)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    border: 1px solid grey;\n"
"    text-align: right;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"}"))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.listWidget_icons = QtGui.QListWidget(self.splitter)
        self.listWidget_icons.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_icons.setFlow(QtGui.QListView.LeftToRight)
        self.listWidget_icons.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget_icons.setUniformItemSizes(True)
        self.listWidget_icons.setObjectName(_fromUtf8("listWidget_icons"))
        item = QtGui.QListWidgetItem()
        self.listWidget_icons.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_icons.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_icons.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_icons.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_icons.addItem(item)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        self.menuDefault = QtGui.QMenu(self.menuFIle)
        self.menuDefault.setObjectName(_fromUtf8("menuDefault"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuCategory = QtGui.QMenu(self.menubar)
        self.menuCategory.setObjectName(_fromUtf8("menuCategory"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate = QtGui.QAction(MainWindow)
        self.actionCreate.setObjectName(_fromUtf8("actionCreate"))
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionChracter = QtGui.QAction(MainWindow)
        self.actionChracter.setObjectName(_fromUtf8("actionChracter"))
        self.actionProp = QtGui.QAction(MainWindow)
        self.actionProp.setObjectName(_fromUtf8("actionProp"))
        self.menuDefault.addAction(self.actionChracter)
        self.menuDefault.addAction(self.actionProp)
        self.menuFIle.addAction(self.actionCreate)
        self.menuFIle.addAction(self.actionRemove)
        self.menuFIle.addAction(self.menuDefault.menuAction())
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuCategory.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.group.setTitle(_translate("MainWindow", "Search Assets", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.treeWidget_search.headerItem().setText(1, _translate("MainWindow", "Path", None))
        self.treeWidget_search.headerItem().setText(2, _translate("MainWindow", "Add", None))
        __sortingEnabled = self.treeWidget_search.isSortingEnabled()
        self.treeWidget_search.setSortingEnabled(False)
        self.treeWidget_search.topLevelItem(0).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_search.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_search.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_icons.isSortingEnabled()
        self.listWidget_icons.setSortingEnabled(False)
        item = self.listWidget_icons.item(0)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget_icons.item(1)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget_icons.item(2)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget_icons.item(3)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget_icons.item(4)
        item.setText(_translate("MainWindow", "New Item", None))
        self.listWidget_icons.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle", None))
        self.menuDefault.setTitle(_translate("MainWindow", "default", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuCategory.setTitle(_translate("MainWindow", "Category", None))
        self.actionCreate.setText(_translate("MainWindow", "Create", None))
        self.actionRemove.setText(_translate("MainWindow", "Remove", None))
        self.actionChracter.setText(_translate("MainWindow", "chracter", None))
        self.actionProp.setText(_translate("MainWindow", "prop", None))

