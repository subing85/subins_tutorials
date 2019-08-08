import sys

from PySide import QtGui
from PySide import QtCore

from studioMayaInterpreter import resources


reload(resources)


class Window(QtGui.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(**kwargs)
        
        self.main_window = parent

        self.label, self.name, self.version = resources.get_tool_kit()
        self.width, self.height = 670, 280

        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('maya_preference')
        self.setWindowTitle('%s %s Preference'%(self.label, self.version))
        self.resize(self.width, self.height)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(20)
        self.verticallayout.setContentsMargins(1, 1, 1, 1)
        self.groupbox_versions = QtGui.QGroupBox(self)
        self.groupbox_versions.setObjectName('groupbox_versions')
        self.groupbox_versions.setTitle('Maya Versions')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_versions.setSizePolicy(size_policy)
        self.verticallayout.addWidget(self.groupbox_versions)
        self.gridLayout_versions = QtGui.QGridLayout(self.groupbox_versions)
        self.gridLayout_versions.setObjectName('gridLayout_versions')
        self.gridLayout_versions.setSpacing(5)
        self.gridLayout_versions.setContentsMargins(5, 5, 5, 5)
        self.label_maya = QtGui.QLabel(self.groupbox_versions)
        self.label_maya.setObjectName('label_maya')
        self.label_maya.setText('Maya')
        self.label_maya.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridLayout_versions.addWidget(self.label_maya, 0, 0, 1, 1)
        self.combobox_maya = QtGui.QComboBox(self.groupbox_versions)
        self.combobox_maya.setObjectName('combobox_maya')
        self.gridLayout_versions.addWidget(self.combobox_maya, 0, 1, 1, 1)
        self.label_directory = QtGui.QLabel(self.groupbox_versions)
        self.label_directory.setObjectName('label_directory')
        self.label_directory.setText('Directory')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.label_directory.setSizePolicy(size_policy)
        self.label_directory.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridLayout_versions.addWidget(self.label_directory, 1, 0, 1, 1)
        self.lineedit_directory = QtGui.QLineEdit(self.groupbox_versions)
        self.lineedit_directory.setObjectName('lineedit_directory')
        self.gridLayout_versions.addWidget(self.lineedit_directory, 1, 1, 1, 2)
        self.button_directory = QtGui.QPushButton(self.groupbox_versions)
        self.button_directory.setObjectName('button_directory')
        self.button_directory.setText('.....')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.button_directory.setSizePolicy(size_policy)
        self.gridLayout_versions.addWidget(self.button_directory, 1, 3, 1, 1)
        self.groupbox_mode = QtGui.QGroupBox(self)
        self.groupbox_mode.setObjectName('groupbox_mode')
        self.groupbox_mode.setTitle('Settings')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_mode.setSizePolicy(size_policy)
        self.groupbox_mode.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticallayout.addWidget(self.groupbox_mode)
        self.gridLayout_settings = QtGui.QGridLayout(self.groupbox_mode)
        self.gridLayout_settings.setObjectName('gridLayout_settings')
        self.gridLayout_versions.setSpacing(10)
        self.gridLayout_versions.setContentsMargins(10, 10, 10, 10)
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.checkbox_edit = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_edit.setObjectName('checkbox_edit')
        self.checkbox_edit.setText('Edit And Query')
        self.checkbox_edit.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_edit, 0, 1, 1, 1)
        self.checkbox_query = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_query.setObjectName('checkbox_query')
        self.checkbox_query.setText('Query Only')
        self.checkbox_edit.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_query, 0, 0, 1, 1)
        self.checkbox_overwrite = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_overwrite.setObjectName('checkbox_overwrite')
        self.checkbox_overwrite.setText('Overwrite')
        self.checkbox_overwrite.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_overwrite, 1, 0, 1, 1)
        self.checkbox_version = QtGui.QCheckBox(self.groupbox_mode)
        self.checkbox_version.setObjectName('checkbox_version')
        self.checkbox_version.setText('Next version')
        self.checkbox_version.setSizePolicy(size_policy)
        self.gridLayout_settings.addWidget(self.checkbox_version, 1, 1, 1, 1)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(5)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.button_cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_apply = QtGui.QPushButton(self)
        self.button_apply.setObjectName('button_apply')
        self.button_apply.setText('Apply')
        self.button_apply.setMinimumSize(QtCore.QSize(150, 0))
        self.horizontallayout.addWidget(self.button_apply)
        vertical_spacer_item = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(vertical_spacer_item)

    def closeEvent(self, event):        
        if self.main_window:
            self.main_window.setEnabled(True)
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
