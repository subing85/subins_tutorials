# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartMayaPreference_ui.ui'
#
# Created: Sat Jul 02 23:46:57 2016
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow_preference(object):
    def setupUi(self, MainWindow_preference):
        MainWindow_preference.setObjectName(_fromUtf8("MainWindow_preference"))
        MainWindow_preference.resize(616, 248)
        MainWindow_preference.setStyleSheet(_fromUtf8("/* ==============================================\n"
"                QWidget\n"
"=============================================== */\n"
"QWidget\n"
"{\n"
"                font: 10pt \"Arial\";\n"
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
        self.centralwidget_preference = QtGui.QWidget(MainWindow_preference)
        self.centralwidget_preference.setObjectName(_fromUtf8("centralwidget_preference"))
        self.verticalLayout_preference = QtGui.QVBoxLayout(self.centralwidget_preference)
        self.verticalLayout_preference.setObjectName(_fromUtf8("verticalLayout_preference"))
        self.tabWidget_preference = QtGui.QTabWidget(self.centralwidget_preference)
        self.tabWidget_preference.setObjectName(_fromUtf8("tabWidget_preference"))
        self.tab_general = QtGui.QWidget()
        self.tab_general.setObjectName(_fromUtf8("tab_general"))
        self.verticalLayout_general = QtGui.QVBoxLayout(self.tab_general)
        self.verticalLayout_general.setObjectName(_fromUtf8("verticalLayout_general"))
        self.groupBox_versions = QtGui.QGroupBox(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_versions.sizePolicy().hasHeightForWidth())
        self.groupBox_versions.setSizePolicy(sizePolicy)
        self.groupBox_versions.setObjectName(_fromUtf8("groupBox_versions"))
        self.verticalLayout_versions = QtGui.QVBoxLayout(self.groupBox_versions)
        self.verticalLayout_versions.setSpacing(5)
        self.verticalLayout_versions.setContentsMargins(5, 15, 5, 5)
        self.verticalLayout_versions.setObjectName(_fromUtf8("verticalLayout_versions"))
        self.gridLayout_versions = QtGui.QGridLayout()
        self.gridLayout_versions.setContentsMargins(40, 10, 10, 10)
        self.gridLayout_versions.setHorizontalSpacing(10)
        self.gridLayout_versions.setVerticalSpacing(15)
        self.gridLayout_versions.setObjectName(_fromUtf8("gridLayout_versions"))
        self.radioButton_maya2009 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2009.setObjectName(_fromUtf8("radioButton_maya2009"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2009, 0, 0, 1, 1)
        self.radioButton_maya2010 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2010.setObjectName(_fromUtf8("radioButton_maya2010"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2010, 0, 1, 1, 1)
        self.radioButton_maya2011 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2011.setObjectName(_fromUtf8("radioButton_maya2011"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2011, 0, 2, 1, 1)
        self.radioButton_maya2012 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2012.setObjectName(_fromUtf8("radioButton_maya2012"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2012, 0, 3, 1, 1)
        self.radioButton_maya2013 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2013.setObjectName(_fromUtf8("radioButton_maya2013"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2013, 1, 0, 1, 1)
        self.radioButton_maya2014 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2014.setEnabled(True)
        self.radioButton_maya2014.setObjectName(_fromUtf8("radioButton_maya2014"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2014, 1, 1, 1, 1)
        self.radioButton_maya2015 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2015.setObjectName(_fromUtf8("radioButton_maya2015"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2015, 1, 2, 1, 1)
        self.radioButton_maya2016 = QtGui.QRadioButton(self.groupBox_versions)
        self.radioButton_maya2016.setObjectName(_fromUtf8("radioButton_maya2016"))
        self.gridLayout_versions.addWidget(self.radioButton_maya2016, 1, 3, 1, 1)
        self.verticalLayout_versions.addLayout(self.gridLayout_versions)
        self.verticalLayout_general.addWidget(self.groupBox_versions)
        self.groupBox_directory = QtGui.QGroupBox(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_directory.sizePolicy().hasHeightForWidth())
        self.groupBox_directory.setSizePolicy(sizePolicy)
        self.groupBox_directory.setObjectName(_fromUtf8("groupBox_directory"))
        self.horizontalLayout_directory = QtGui.QHBoxLayout(self.groupBox_directory)
        self.horizontalLayout_directory.setMargin(5)
        self.horizontalLayout_directory.setObjectName(_fromUtf8("horizontalLayout_directory"))
        self.label_directory = QtGui.QLabel(self.groupBox_directory)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directory.sizePolicy().hasHeightForWidth())
        self.label_directory.setSizePolicy(sizePolicy)
        self.label_directory.setObjectName(_fromUtf8("label_directory"))
        self.horizontalLayout_directory.addWidget(self.label_directory)
        self.lineEdit_directory = QtGui.QLineEdit(self.groupBox_directory)
        self.lineEdit_directory.setObjectName(_fromUtf8("lineEdit_directory"))
        self.horizontalLayout_directory.addWidget(self.lineEdit_directory)
        self.button_directory = QtGui.QPushButton(self.groupBox_directory)
        self.button_directory.setObjectName(_fromUtf8("button_directory"))
        self.horizontalLayout_directory.addWidget(self.button_directory)
        self.verticalLayout_general.addWidget(self.groupBox_directory)
        self.tabWidget_preference.addTab(self.tab_general, _fromUtf8(""))
        self.tab_mode = QtGui.QWidget()
        self.tab_mode.setObjectName(_fromUtf8("tab_mode"))
        self.verticalLayout_tabMode = QtGui.QVBoxLayout(self.tab_mode)
        self.verticalLayout_tabMode.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_tabMode.setObjectName(_fromUtf8("verticalLayout_tabMode"))
        self.groupBox_mode = QtGui.QGroupBox(self.tab_mode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setObjectName(_fromUtf8("groupBox_mode"))
        self.verticalLayout_mode = QtGui.QVBoxLayout(self.groupBox_mode)
        self.verticalLayout_mode.setSpacing(5)
        self.verticalLayout_mode.setContentsMargins(5, 25, 5, 5)
        self.verticalLayout_mode.setObjectName(_fromUtf8("verticalLayout_mode"))
        self.groupBox_modeType = QtGui.QGroupBox(self.groupBox_mode)
        self.groupBox_modeType.setObjectName(_fromUtf8("groupBox_modeType"))
        self.horizontalLayout_modeType = QtGui.QHBoxLayout(self.groupBox_modeType)
        self.horizontalLayout_modeType.setSpacing(0)
        self.horizontalLayout_modeType.setContentsMargins(60, 5, 15, 5)
        self.horizontalLayout_modeType.setObjectName(_fromUtf8("horizontalLayout_modeType"))
        self.radioButton_edit = QtGui.QRadioButton(self.groupBox_modeType)
        self.radioButton_edit.setObjectName(_fromUtf8("radioButton_edit"))
        self.horizontalLayout_modeType.addWidget(self.radioButton_edit)
        self.radioButton_quarry = QtGui.QRadioButton(self.groupBox_modeType)
        self.radioButton_quarry.setObjectName(_fromUtf8("radioButton_quarry"))
        self.horizontalLayout_modeType.addWidget(self.radioButton_quarry)
        self.verticalLayout_mode.addWidget(self.groupBox_modeType)
        self.groupBox_type = QtGui.QGroupBox(self.groupBox_mode)
        self.groupBox_type.setObjectName(_fromUtf8("groupBox_type"))
        self.horizontalLayout_type = QtGui.QHBoxLayout(self.groupBox_type)
        self.horizontalLayout_type.setSpacing(0)
        self.horizontalLayout_type.setContentsMargins(60, 5, 15, 5)
        self.horizontalLayout_type.setObjectName(_fromUtf8("horizontalLayout_type"))
        self.radioButton_overwrite = QtGui.QRadioButton(self.groupBox_type)
        self.radioButton_overwrite.setObjectName(_fromUtf8("radioButton_overwrite"))
        self.horizontalLayout_type.addWidget(self.radioButton_overwrite)
        self.radioButton_version = QtGui.QRadioButton(self.groupBox_type)
        self.radioButton_version.setObjectName(_fromUtf8("radioButton_version"))
        self.horizontalLayout_type.addWidget(self.radioButton_version)
        self.radioButton_none = QtGui.QRadioButton(self.groupBox_type)
        self.radioButton_none.setObjectName(_fromUtf8("radioButton_none"))
        self.horizontalLayout_type.addWidget(self.radioButton_none)
        self.verticalLayout_mode.addWidget(self.groupBox_type)
        self.verticalLayout_tabMode.addWidget(self.groupBox_mode)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_tabMode.addItem(spacerItem)
        self.tabWidget_preference.addTab(self.tab_mode, _fromUtf8(""))
        self.verticalLayout_preference.addWidget(self.tabWidget_preference)
        self.horizontalLayout_apply = QtGui.QHBoxLayout()
        self.horizontalLayout_apply.setObjectName(_fromUtf8("horizontalLayout_apply"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_apply.addItem(spacerItem1)
        self.button_cancel = QtGui.QPushButton(self.centralwidget_preference)
        self.button_cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontalLayout_apply.addWidget(self.button_cancel)
        self.button_apply = QtGui.QPushButton(self.centralwidget_preference)
        self.button_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.horizontalLayout_apply.addWidget(self.button_apply)
        self.verticalLayout_preference.addLayout(self.horizontalLayout_apply)
        MainWindow_preference.setCentralWidget(self.centralwidget_preference)

        self.retranslateUi(MainWindow_preference)
        self.tabWidget_preference.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_preference)

    def retranslateUi(self, MainWindow_preference):
        MainWindow_preference.setWindowTitle(QtGui.QApplication.translate("MainWindow_preference", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_versions.setTitle(QtGui.QApplication.translate("MainWindow_preference", "Maya Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2009.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2009", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2010.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2010", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2011.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2011", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2012.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2012", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2013.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2013", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2014.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2014", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2015.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2015", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_maya2016.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya 2016", None, QtGui.QApplication.UnicodeUTF8))
        self.label_directory.setText(QtGui.QApplication.translate("MainWindow_preference", "Maya Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.button_directory.setText(QtGui.QApplication.translate("MainWindow_preference", ".....", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_preference.setTabText(self.tabWidget_preference.indexOf(self.tab_general), QtGui.QApplication.translate("MainWindow_preference", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_mode.setTitle(QtGui.QApplication.translate("MainWindow_preference", "Maya Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_edit.setText(QtGui.QApplication.translate("MainWindow_preference", "Edit And Quary", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_quarry.setText(QtGui.QApplication.translate("MainWindow_preference", "Quarry Only", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_overwrite.setText(QtGui.QApplication.translate("MainWindow_preference", "Overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_version.setText(QtGui.QApplication.translate("MainWindow_preference", "Another version", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_none.setText(QtGui.QApplication.translate("MainWindow_preference", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_preference.setTabText(self.tabWidget_preference.indexOf(self.tab_mode), QtGui.QApplication.translate("MainWindow_preference", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("MainWindow_preference", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_apply.setText(QtGui.QApplication.translate("MainWindow_preference", "Apply", None, QtGui.QApplication.UnicodeUTF8))

