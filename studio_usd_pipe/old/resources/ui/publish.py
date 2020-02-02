
import os
import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import widgets
# from studio_usd_pipe.utils import platforms
#from studio_usd_pipe.api import studioImage
from studio_usd_pipe.resource.ui.old import logo


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, standalone=False):
        super(Window, self).__init__(parent)
        self.standalone = standalone
        #=======================================================================
        # self.prity_name = platforms.get_child('asset_publish')
        # self.tool_prity_name = platforms.get_tool_prity_name()
        # self.version = platforms.get_tool_version()
        #=======================================================================
        self.sem_versions = ['major', 'minor', 'patch']
        self.width, self.height = 623, 669
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('main_window')
        self.resize(self.width, self.height)
        #self.setWindowTitle('{} <{}> {}'.format(
        #    self.tool_prity_name, self.prity_name, self.version))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setContentsMargins(5, 5, 5, 5)

        #self.input_dirname = resource.getInputDirname()

        #logo.Connect(
        #   self.verticallayout, show_icon=self.input_dirname['show_icon'])

        self.groupbox_source = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_source.setObjectName('groupbox_source')
        self.groupbox_source.setTitle('Source File')
        self.verticallayout.addWidget(self.groupbox_source)

        self.horizontallayout_source = QtWidgets.QHBoxLayout(self.groupbox_source)
        self.horizontallayout_source.setObjectName('horizontallayout_source')
        self.horizontallayout_source.setSpacing(10)
        self.horizontallayout_source.setContentsMargins(5, 5, 5, 5)

        self.button_open = QtWidgets.QPushButton(self.groupbox_source)
        self.button_open.setObjectName('button_open')
        self.button_open.setFlat(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_open.setSizePolicy(sizePolicy)
        open_path = os.path.join(resource.getIconPath(), 'open.png')
        widgets.image_to_button(self.button_open, 100, 100, path=open_path)

        self.horizontallayout_source.addWidget(self.button_open)

        self.label_source = QtWidgets.QLabel(self.groupbox_source)
        self.label_source.setObjectName('label_source')
        self.label_source.setStyleSheet('font: 16pt;')
        self.horizontallayout_source.addWidget(self.label_source)

        self.groupbox_inputs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_inputs.setObjectName('groupbox_inputs')
        self.groupbox_inputs.setTitle('Inputs')
        self.verticallayout.addWidget(self.groupbox_inputs)

        self.gridlayout_inputs = QtWidgets.QGridLayout(self.groupbox_inputs)
        self.gridlayout_inputs.setObjectName('gridlayout_inputs')
        self.gridlayout_inputs.setHorizontalSpacing(10)
        self.gridlayout_inputs.setContentsMargins(5, 5, 5, 5)

        self.label_dagpath = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_dagpath.setObjectName('label_dagpath')
        self.label_dagpath.setText('Source file transform nodes')
        self.label_dagpath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_dagpath, 0, 0, 1, 1)

        self.combobox_dagpath = QtWidgets.QComboBox(self.groupbox_inputs)
        self.combobox_dagpath.setObjectName('combobox_dagpath')
        self.combobox_dagpath.setEditable(True)
        self.combobox_dagpath.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_dagpath, 0, 1, 1, 1)

        self.label_caption = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_caption.setObjectName('label_caption')
        self.label_caption.setText('Caption')
        self.label_caption.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_caption, 1, 0, 1, 1)

        self.combobox_caption = QtWidgets.QComboBox(self.groupbox_inputs)
        self.combobox_caption.setObjectName('combobox_caption')
        self.combobox_caption.setEditable(True)
        self.combobox_caption.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_caption, 1, 1, 1, 1)

        self.label_subfield = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_subfield.setObjectName('label_subfield')
        self.label_subfield.setText('Subfield')
        self.label_subfield.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_subfield, 2, 0, 1, 1)

        self.combobox_subfield = QtWidgets.QComboBox(self.groupbox_inputs)
        self.combobox_subfield.setObjectName('combobox_subfield')
        self.combobox_subfield.setEditable(True)
        self.combobox_subfield.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_subfield, 2, 1, 1, 1)

        self.label_type = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('Type')
        self.label_type.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_type, 3, 0, 1, 1)

        self.combobox_type = QtWidgets.QComboBox(self.groupbox_inputs)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.setEditable(True)
        self.combobox_type.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_type, 3, 1, 1, 1)

        self.label_tag = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_tag.setObjectName('label_tag')
        self.label_tag.setText('Tag')
        self.label_tag.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_tag, 4, 0, 1, 1)

        self.combobox_tag = QtWidgets.QComboBox(self.groupbox_inputs)
        self.combobox_tag.setObjectName('combobox_tag')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_tag, 4, 1, 1, 1)

        self.line_thumbnail = QtWidgets.QFrame(self.groupbox_inputs)
        self.line_thumbnail.setObjectName('line_thumbnail')
        self.gridlayout_inputs.addWidget(self.line_thumbnail, 5, 0, 1, 1)

        self.line_description = QtWidgets.QFrame(self.groupbox_inputs)
        self.line_description.setObjectName('line_description')
        self.gridlayout_inputs.addWidget(self.line_description, 5, 1, 1, 1)

        self.label_thumbnail = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.gridlayout_inputs.addWidget(self.label_thumbnail, 6, 0, 1, 1)

        self.label_description = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.gridlayout_inputs.addWidget(self.label_description, 6, 1, 1, 1)

        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox_inputs)
        self.button_thumbnail.setObjectName('button_thumbnail')
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        thumbnail_icon = os.path.join(resource.getIconPath(), 'thumbnail.png')
        unknown_image = os.path.join(resource.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.button_thumbnail, 256, 180, path=thumbnail_icon)
        self.button_thumbnail.setStatusTip(unknown_image)
        self.gridlayout_inputs.addWidget(self.button_thumbnail, 6, 0, 1, 1)

        self.textedit_description = QtWidgets.QTextEdit(self.groupbox_inputs)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.gridlayout_inputs.addWidget(self.textedit_description, 6, 1, 1, 1)

        self.groupbox_publish = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_publish.setObjectName('groupbox_publish')
        self.groupbox_publish.setTitle('Publish')
        self.verticallayout.addWidget(self.groupbox_publish)

        self.gridlayout_publish = QtWidgets.QGridLayout(self.groupbox_publish)
        self.gridlayout_publish.setObjectName('gridlayout_publish')
        self.gridlayout_publish.setHorizontalSpacing(10)
        self.gridlayout_publish.setContentsMargins(5, 5, 5, 5)

        self.label_versions = QtWidgets.QLabel(self.groupbox_publish)
        self.label_versions.setObjectName('label_versions')
        self.label_versions.setText('Versions')
        self.label_versions.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_versions, 0, 0, 1, 1)

        self.combobox_versions = QtWidgets.QComboBox(self.groupbox_publish)
        self.combobox_versions.setObjectName('combobox_versions')
        self.combobox_versions.setEditable(True)
        self.combobox_versions.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combobox_versions.addItems(self.sem_versions)
        self.gridlayout_publish.addWidget(self.combobox_versions, 0, 1, 1, 1)

        self.label_latestversion = QtWidgets.QLabel(self.groupbox_publish)
        self.label_latestversion.setObjectName('label_latestversion')
        self.label_latestversion.setText('Latest Versions')
        self.label_latestversion.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_latestversion, 1, 0, 1, 1)

        self.combobox_latestversion = QtWidgets.QComboBox(self.groupbox_publish)
        self.combobox_latestversion.setObjectName('combobox_latestversion')
        self.combobox_latestversion.setEditable(True)
        self.combobox_latestversion.setEnabled(False)
        self.combobox_latestversion.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_publish.addWidget(
            self.combobox_latestversion, 1, 1, 1, 1)

        self.label_nextversion = QtWidgets.QLabel(self.groupbox_publish)
        self.label_nextversion.setObjectName('label_nextversion')
        self.label_nextversion.setText('Avilable Publish versions')
        self.label_nextversion.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_nextversion, 2, 0, 1, 1)

        self.combobox_nextversion = QtWidgets.QComboBox(self.groupbox_publish)
        self.combobox_nextversion.setObjectName('combobox_nextversion')
        self.combobox_nextversion.setEditable(True)
        self.combobox_nextversion.setEnabled(False)
        self.combobox_nextversion.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout_publish.addWidget(
            self.combobox_nextversion, 2, 1, 1, 1)

        self.button_publish = QtWidgets.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.gridlayout_publish.addWidget(self.button_publish, 4, 1, 1, 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())
