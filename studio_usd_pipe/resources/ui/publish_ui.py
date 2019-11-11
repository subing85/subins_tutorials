
import os
import sys


from PySide import QtCore
from PySide import QtGui
from functools import partial

from studio_usd_pipe import resources
from studio_usd_pipe.core import widgets
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.api import studioImage
from studio_usd_pipe.resources.ui import logo_ui


class Window(QtGui.QMainWindow):

    def __init__(self, parent=None, standalone=False):
        super(Window, self).__init__(parent)
        self.standalone = standalone
        self.prity_name = platforms.get_child('asset_publish')
        self.tool_prity_name = platforms.get_tool_prity_name()
        self.version = platforms.get_tool_version()
        self.sem_versions = ['major', 'minor', 'patch']
        self.publish_types = ['versions', 'variations']
        self.width, self.height = 623, 669
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('main_window')
        self.resize(self.width, self.height)
        self.setWindowTitle('{} <{}> {}'.format(
            self.tool_prity_name, self.prity_name, self.version))

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setContentsMargins(5, 5, 5, 5)

        self.input_dirname = resources.getInputDirname()

        logo = logo_ui.Connect(
            self.verticallayout, show_icon=self.input_dirname['show_icon'])

        self.groupbox_source = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_source.setObjectName('groupbox_source')
        self.groupbox_source.setTitle('Source File')
        self.verticallayout.addWidget(self.groupbox_source)

        self.horizontallayout_source = QtGui.QHBoxLayout(self.groupbox_source)
        self.horizontallayout_source.setObjectName('horizontallayout_source')
        self.horizontallayout_source.setSpacing(10)
        self.horizontallayout_source.setContentsMargins(5, 5, 5, 5)

        self.button_open = QtGui.QPushButton(self.groupbox_source)
        self.button_open.setObjectName('button_open')
        self.button_open.setFlat(True)        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.button_open.setSizePolicy(sizePolicy)       
        open_path = os.path.join(resources.getIconPath(), 'open.png')
        widgets.image_to_button(self.button_open, 100, 100, path=open_path)
                
        self.horizontallayout_source.addWidget(self.button_open)

        self.label_source = QtGui.QLabel(self.groupbox_source)
        self.label_source.setObjectName('label_source')
        self.label_source.setStyleSheet('font: 16pt;') 
        self.horizontallayout_source.addWidget(self.label_source)

        self.groupbox_inputs = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_inputs.setObjectName('groupbox_inputs')
        self.groupbox_inputs.setTitle('Inputs')
        self.verticallayout.addWidget(self.groupbox_inputs)

        self.gridlayout_inputs = QtGui.QGridLayout(self.groupbox_inputs)
        self.gridlayout_inputs.setObjectName('gridlayout_inputs')
        self.gridlayout_inputs.setHorizontalSpacing(10)
        self.gridlayout_inputs.setContentsMargins(5, 5, 5, 5)

        self.label_caption = QtGui.QLabel(self.groupbox_inputs)
        self.label_caption.setObjectName('label_caption')
        self.label_caption.setText('Caption')
        self.label_caption.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_caption, 0, 0, 1, 1)

        self.combobox_caption = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_caption.setObjectName('combobox_caption')
        self.combobox_caption.setEditable(True)
        self.combobox_caption.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_caption, 0, 1, 1, 1)

        self.label_subfield = QtGui.QLabel(self.groupbox_inputs)
        self.label_subfield.setObjectName('label_subfield')
        self.label_subfield.setText('Subfield')
        self.label_subfield.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_subfield, 1, 0, 1, 1)

        self.combobox_subfield = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_subfield.setObjectName('combobox_subfield')
        self.combobox_subfield.setEditable(True)
        self.combobox_subfield.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_subfield, 1, 1, 1, 1)

        self.label_type = QtGui.QLabel(self.groupbox_inputs)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('Type')
        self.label_type.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_type, 2, 0, 1, 1)

        self.combobox_type = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.setEditable(True)
        self.combobox_type.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_type, 2, 1, 1, 1)

        self.label_tag = QtGui.QLabel(self.groupbox_inputs)
        self.label_tag.setObjectName('label_tag')
        self.label_tag.setText('Tag')
        self.label_tag.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_inputs.addWidget(self.label_tag, 3, 0, 1, 1)

        self.combobox_tag = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_tag.setObjectName('combobox_tag')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_inputs.addWidget(self.combobox_tag, 3, 1, 1, 1)

        self.line_thumbnail = QtGui.QFrame(self.groupbox_inputs)
        self.line_thumbnail.setObjectName('line_thumbnail')
        self.gridlayout_inputs.addWidget(self.line_thumbnail, 4, 0, 1, 1)

        self.line_description = QtGui.QFrame(self.groupbox_inputs)
        self.line_description.setObjectName('line_description')
        self.gridlayout_inputs.addWidget(self.line_description, 4, 1, 1, 1)

        self.label_thumbnail = QtGui.QLabel(self.groupbox_inputs)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.gridlayout_inputs.addWidget(self.label_thumbnail, 5, 0, 1, 1)

        self.label_description = QtGui.QLabel(self.groupbox_inputs)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.gridlayout_inputs.addWidget(self.label_description, 5, 1, 1, 1)

        self.button_thumbnail = QtGui.QPushButton(self.groupbox_inputs)
        self.button_thumbnail.setObjectName('button_thumbnail')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        thumbnail_icon = os.path.join(resources.getIconPath(), 'thumbnail.png')
        unknown_image = os.path.join(resources.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.button_thumbnail, 256, 180, path=thumbnail_icon)
        self.button_thumbnail.setStatusTip(unknown_image)      
        self.gridlayout_inputs.addWidget(self.button_thumbnail, 6, 0, 1, 1)

        self.textedit_description = QtGui.QTextEdit(self.groupbox_inputs)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.gridlayout_inputs.addWidget(self.textedit_description, 6, 1, 1, 1)

        self.groupbox_publish = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_publish.setObjectName('groupbox_publish')
        self.groupbox_publish.setTitle('Publish')
        self.verticallayout.addWidget(self.groupbox_publish)

        self.gridlayout_publish = QtGui.QGridLayout(self.groupbox_publish)
        self.gridlayout_publish.setObjectName('gridlayout_publish')
        self.gridlayout_publish.setHorizontalSpacing(10)
        self.gridlayout_publish.setContentsMargins(5, 5, 5, 5)

        self.label_publishtype = QtGui.QLabel(self.groupbox_publish)
        self.label_publishtype.setObjectName('label_publishtype')
        self.label_publishtype.setText('Publish Type')
        self.label_publishtype.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_publishtype, 0, 0, 1, 1)

        self.combobox_publishtype = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_publishtype.setObjectName('combobox_publishtype')
        self.combobox_publishtype.setEditable(True)
        self.combobox_publishtype.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.combobox_publishtype.addItems(self.publish_types)
        self.gridlayout_publish.addWidget(
            self.combobox_publishtype, 0, 1, 1, 1)

        self.label_versions = QtGui.QLabel(self.groupbox_publish)
        self.label_versions.setObjectName('label_versions')
        self.label_versions.setText('Versions')
        self.label_versions.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_versions, 1, 0, 1, 1)

        self.combobox_versions = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_versions.setObjectName('combobox_versions')
        self.combobox_versions.setEditable(True)
        self.combobox_versions.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.combobox_versions.addItems(self.sem_versions)
        self.gridlayout_publish.addWidget(self.combobox_versions, 1, 1, 1, 1)

        self.label_latestversion = QtGui.QLabel(self.groupbox_publish)
        self.label_latestversion.setObjectName('label_latestversion')
        self.label_latestversion.setText('Latest Versions')
        self.label_latestversion.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_latestversion, 2, 0, 1, 1)

        self.combobox_latestversion = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_latestversion.setObjectName('combobox_latestversion')
        self.combobox_latestversion.setEditable(True)
        self.combobox_latestversion.setEnabled(False)        
        self.combobox_latestversion.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_publish.addWidget(self.combobox_latestversion, 2, 1, 1, 1)


        self.label_nextversion = QtGui.QLabel(self.groupbox_publish)
        self.label_nextversion.setObjectName('label_nextversion')
        self.label_nextversion.setText('Avilable Publish versions')
        self.label_nextversion.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gridlayout_publish.addWidget(self.label_nextversion, 3, 0, 1, 1)

        self.combobox_nextversion = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_nextversion.setObjectName('combobox_nextversion')
        self.combobox_nextversion.setEditable(True)
        self.combobox_nextversion.setEnabled(False)      
        self.combobox_nextversion.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.gridlayout_publish.addWidget(
            self.combobox_nextversion, 3, 1, 1, 1)

        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.gridlayout_publish.addWidget(self.button_publish, 4, 1, 1, 1)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window(parent=None)
    window.show()
    sys.exit(app.exec_())
