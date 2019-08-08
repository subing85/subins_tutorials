# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/studioMayaInterpreter/samples/sourceCode/ui/preference_ui.ui'
#
# Created: Wed Aug  7 23:25:08 2019
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
        Form.resize(664, 276)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupbox_versions = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_versions.sizePolicy().hasHeightForWidth())
        self.groupbox_versions.setSizePolicy(sizePolicy)
        self.groupbox_versions.setObjectName(_fromUtf8("groupbox_versions"))
        self.gridLayout_versions = QtGui.QGridLayout(self.groupbox_versions)
        self.gridLayout_versions.setObjectName(_fromUtf8("gridLayout_versions"))
        self.label_maya = QtGui.QLabel(self.groupbox_versions)
        self.label_maya.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_maya.setObjectName(_fromUtf8("label_maya"))
        self.gridLayout_versions.addWidget(self.label_maya, 0, 0, 1, 1)
        self.combobox_maya = QtGui.QComboBox(self.groupbox_versions)
        self.combobox_maya.setObjectName(_fromUtf8("combobox_maya"))
        self.gridLayout_versions.addWidget(self.combobox_maya, 0, 1, 1, 1)
        self.label_directory = QtGui.QLabel(self.groupbox_versions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directory.sizePolicy().hasHeightForWidth())
        self.label_directory.setSizePolicy(sizePolicy)
        self.label_directory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_directory.setObjectName(_fromUtf8("label_directory"))
        self.gridLayout_versions.addWidget(self.label_directory, 1, 0, 1, 1)
        self.lineEdit_directory = QtGui.QLineEdit(self.groupbox_versions)
        self.lineEdit_directory.setObjectName(_fromUtf8("lineEdit_directory"))
        self.gridLayout_versions.addWidget(self.lineEdit_directory, 1, 1, 1, 2)
        self.button_directory = QtGui.QPushButton(self.groupbox_versions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_directory.sizePolicy().hasHeightForWidth())
        self.button_directory.setSizePolicy(sizePolicy)
        self.button_directory.setObjectName(_fromUtf8("button_directory"))
        self.gridLayout_versions.addWidget(self.button_directory, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupbox_versions)
        self.groupBox_mode = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mode.sizePolicy().hasHeightForWidth())
        self.groupBox_mode.setSizePolicy(sizePolicy)
        self.groupBox_mode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_mode.setObjectName(_fromUtf8("groupBox_mode"))
        self.gridLayout_settings = QtGui.QGridLayout(self.groupBox_mode)
        self.gridLayout_settings.setMargin(20)
        self.gridLayout_settings.setSpacing(20)
        self.gridLayout_settings.setObjectName(_fromUtf8("gridLayout_settings"))
        self.checkBox_edit = QtGui.QCheckBox(self.groupBox_mode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_edit.sizePolicy().hasHeightForWidth())
        self.checkBox_edit.setSizePolicy(sizePolicy)
        self.checkBox_edit.setObjectName(_fromUtf8("checkBox_edit"))
        self.gridLayout_settings.addWidget(self.checkBox_edit, 0, 1, 1, 1)
        self.checkBox_quarry = QtGui.QCheckBox(self.groupBox_mode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_quarry.sizePolicy().hasHeightForWidth())
        self.checkBox_quarry.setSizePolicy(sizePolicy)
        self.checkBox_quarry.setObjectName(_fromUtf8("checkBox_quarry"))
        self.gridLayout_settings.addWidget(self.checkBox_quarry, 0, 0, 1, 1)
        self.checkBox_overwrite = QtGui.QCheckBox(self.groupBox_mode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_overwrite.sizePolicy().hasHeightForWidth())
        self.checkBox_overwrite.setSizePolicy(sizePolicy)
        self.checkBox_overwrite.setObjectName(_fromUtf8("checkBox_overwrite"))
        self.gridLayout_settings.addWidget(self.checkBox_overwrite, 1, 0, 1, 1)
        self.checkBox_version = QtGui.QCheckBox(self.groupBox_mode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_version.sizePolicy().hasHeightForWidth())
        self.checkBox_version.setSizePolicy(sizePolicy)
        self.checkBox_version.setObjectName(_fromUtf8("checkBox_version"))
        self.gridLayout_settings.addWidget(self.checkBox_version, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_mode)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName(_fromUtf8("horizontallayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacerItem)
        self.button_cancel = QtGui.QPushButton(Form)
        self.button_cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_apply = QtGui.QPushButton(Form)
        self.button_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.horizontallayout.addWidget(self.button_apply)
        self.verticalLayout.addLayout(self.horizontallayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupbox_versions.setTitle(_translate("Form", "Maya Versions", None))
        self.label_maya.setText(_translate("Form", "Maya", None))
        self.label_directory.setText(_translate("Form", "Directory", None))
        self.button_directory.setText(_translate("Form", ".....", None))
        self.groupBox_mode.setTitle(_translate("Form", "Settings", None))
        self.checkBox_edit.setText(_translate("Form", "Edit And Query", None))
        self.checkBox_quarry.setText(_translate("Form", "Query Only", None))
        self.checkBox_overwrite.setText(_translate("Form", "Overwrite", None))
        self.checkBox_version.setText(_translate("Form", "Next version", None))
        self.button_cancel.setText(_translate("Form", "Cancel", None))
        self.button_apply.setText(_translate("Form", "Apply", None))

