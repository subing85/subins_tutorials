# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/publish.ui'
#
# Created: Fri Jun 19 12:16:29 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 487)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setObjectName("treewidget")
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.treewidget.header().setVisible(False)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticallayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)
        self.verticallayout.setObjectName("verticallayout")
        self.groupbox_label = QtGui.QGroupBox(self.layoutWidget)
        self.groupbox_label.setObjectName("groupbox_label")
        self.horizontallayout_data = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_data.setSpacing(10)
        self.horizontallayout_data.setContentsMargins(10, 10, 10, 10)
        self.horizontallayout_data.setObjectName("horizontallayout_data")
        self.button_label = QtGui.QPushButton(self.groupbox_label)
        self.button_label.setObjectName("button_label")
        self.horizontallayout_data.addWidget(self.button_label)
        self.lineedit_label = QtGui.QLineEdit(self.groupbox_label)
        self.lineedit_label.setObjectName("lineedit_label")
        self.horizontallayout_data.addWidget(self.lineedit_label)
        self.button_open = QtGui.QPushButton(self.groupbox_label)
        self.button_open.setObjectName("button_open")
        self.horizontallayout_data.addWidget(self.button_open)
        self.verticallayout.addWidget(self.groupbox_label)
        self.groupbox_input = QtGui.QGroupBox(self.layoutWidget)
        self.groupbox_input.setObjectName("groupbox_input")
        self.verticallayout_input = QtGui.QVBoxLayout(self.groupbox_input)
        self.verticallayout_input.setSpacing(10)
        self.verticallayout_input.setContentsMargins(10, 10, 10, 10)
        self.verticallayout_input.setObjectName("verticallayout_input")
        self.gridlayout_input = QtGui.QGridLayout()
        self.gridlayout_input.setObjectName("gridlayout_input")
        self.button_thumbnail = QtGui.QPushButton(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridlayout_input.addWidget(self.button_thumbnail, 1, 0, 1, 1)
        self.label_thumbnail = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.gridlayout_input.addWidget(self.label_thumbnail, 0, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName("label_description")
        self.gridlayout_input.addWidget(self.label_description, 0, 1, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName("textedit_description")
        self.gridlayout_input.addWidget(self.textedit_description, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_input)
        self.horizontallayout_input = QtGui.QHBoxLayout()
        self.horizontallayout_input.setObjectName("horizontallayout_input")
        self.label_tag = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tag.sizePolicy().hasHeightForWidth())
        self.label_tag.setSizePolicy(sizePolicy)
        self.label_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tag.setObjectName("label_tag")
        self.horizontallayout_input.addWidget(self.label_tag)
        self.combobox_tag = QtGui.QComboBox(self.groupbox_input)
        self.combobox_tag.setEditable(False)
        self.combobox_tag.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.combobox_tag.setObjectName("combobox_tag")
        self.horizontallayout_input.addWidget(self.combobox_tag)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout_input.addItem(spacerItem)
        self.verticallayout_input.addLayout(self.horizontallayout_input)
        self.verticallayout.addWidget(self.groupbox_input)
        self.groupbox_publish = QtGui.QGroupBox(self.layoutWidget)
        self.groupbox_publish.setObjectName("groupbox_publish")
        self.horizontallayout_publish = QtGui.QHBoxLayout(self.groupbox_publish)
        self.horizontallayout_publish.setSpacing(10)
        self.horizontallayout_publish.setContentsMargins(10, 10, 10, 10)
        self.horizontallayout_publish.setObjectName("horizontallayout_publish")
        self.label_publish = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publish.sizePolicy().hasHeightForWidth())
        self.label_publish.setSizePolicy(sizePolicy)
        self.label_publish.setObjectName("label_publish")
        self.horizontallayout_publish.addWidget(self.label_publish)
        self.combobox_publish = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_publish.setObjectName("combobox_publish")
        self.horizontallayout_publish.addWidget(self.combobox_publish)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName("button_publish")
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.verticallayout.addWidget(self.groupbox_publish)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action_add = QtGui.QAction(MainWindow)
        self.action_add.setObjectName("action_add")
        self.action_remove = QtGui.QAction(MainWindow)
        self.action_remove.setObjectName("action_remove")
        self.action_reload = QtGui.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Hero", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Demon", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Girl", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Shot_001", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Shot_002", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.setSortingEnabled(__sortingEnabled)
        self.groupbox_label.setTitle(QtGui.QApplication.translate("MainWindow", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.button_label.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_input.setTitle(QtGui.QApplication.translate("MainWindow", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.button_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tag.setText(QtGui.QApplication.translate("MainWindow", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_publish.setTitle(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_publish.setText(QtGui.QApplication.translate("MainWindow", "Next Avilable Publish versions", None, QtGui.QApplication.UnicodeUTF8))
        self.button_publish.setText(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setToolTip(QtGui.QApplication.translate("MainWindow", "Add Items", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setToolTip(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))

