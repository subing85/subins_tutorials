import os
import sys

from pprint import pprint


from PySide import QtCore
from PySide import QtGui
from functools import partial
from datetime import datetime


from studio_usd_pipe import resources
from studio_usd_pipe.core import inputs
from studio_usd_pipe.core import widgets
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.api import studioImage
from studio_usd_pipe.resources.ui import logo_ui


class Window(QtGui.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Window, self).__init__(parent)

        self.current_show = None
        if 'show' in kwargs:
            self.current_show = kwargs['show']
        self.type = kwargs['type']
        self.value = kwargs['value']
        self.title = kwargs['title']
        self.width = kwargs['width']
        self.height = kwargs['height']

        self.version = platforms.get_tool_version()
        self.label = platforms.get_tool_prity_name()

        self.brows_directory = resources.getWorkspacePath()
        self.brows_directory = '/mnt/bkp/reference'

        self.setup_ui()
        self.modify_widgets()

    def setup_ui(self):
        self.setObjectName('input_widget')
        self.setWindowTitle(
            '{} ({} {})'.format(self.title, self.label, self.version))
        self.resize(self.width, self.height)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox_asset')
        self.groupbox.setTitle(self.label)
        self.verticallayout.addWidget(self.groupbox)
        self.verticallayout_item = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_item.setObjectName('verticallayout')
        self.verticallayout_item.setSpacing(10)
        self.verticallayout_item.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.verticallayout_item.addLayout(self.horizontalLayout)
        logo = logo_ui.Connect(self.horizontalLayout)
        self.button_show = logo.button_show
        self.gridlayout = QtGui.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)
        spacer_item = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        self.horizontallayout = QtGui.QHBoxLayout()
        self.horizontallayout.setObjectName('horizontallayout')
        self.horizontallayout.setSpacing(10)
        self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout.addItem(spacer_item)
        self.button_cancel = QtGui.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout.addWidget(self.button_cancel)
        self.button_create = QtGui.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.horizontallayout.addWidget(self.button_create)
        self.button_cancel.clicked.connect(self.close)

    def modify_widgets(self):
        input = inputs.Connect(self.type)
        str_bundle = ['str', 'path', 'directory']
        for index, each in enumerate(input.keys):
            current_item = input.data[each]
            label = QtGui.QLabel(self.groupbox)
            label.setObjectName('label_%s' % each)
            label.setText(current_item['display'])
            label.setStatusTip(current_item['tooltip'])
            label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.gridlayout.addWidget(label, index, 0, 1, 1)
            widget = None
            button_find = None
            if current_item['type'] in str_bundle:
                widget = QtGui.QLineEdit(self.groupbox)
                widget.setObjectName('lineedit_%s' % each)
                widget.setText(current_item['value'])
                widget.setEnabled(current_item['enable'])
                button_find = QtGui.QPushButton(self.groupbox)
                button_find.setObjectName('button_find_%s' % each)
                button_find.setText('...')
                button_find.setStyleSheet('color: #0000FF;')
                button_find.setMinimumSize(QtCore.QSize(35, 25))
                button_find.setMaximumSize(QtCore.QSize(35, 25))
            elif current_item['type'] == 'enum':
                widget = QtGui.QComboBox(self.groupbox)
                widget.setObjectName('combobox_%s' % each)
                if current_item['values']:
                    widget.addItems(current_item['values'])
                    widget.setCurrentIndex(current_item['value'])
            elif current_item['type'] == 'add':
                widget = QtGui.QPushButton(self.groupbox)
                widget.setObjectName('button_add_%s' % each)
                widget.setText(u'\u002B')
                widget.setStyleSheet('color: #0000FF;')
                widget.setMinimumSize(QtCore.QSize(20, 20))
                widget.setMaximumSize(QtCore.QSize(20, 20))
            if widget:
                widget.setStatusTip(each)
                self.gridlayout.addWidget(widget, index, 1, 1, 1)
            if current_item['example']:
                widget.setToolTip('\n'.join(current_item['example']))
            if button_find:
                description = None
                if 'description' in current_item:
                    description = current_item['description']
                resolution = None
                if 'resolution' in current_item:
                    resolution = current_item['resolution']
                format = current_item['format']
                button_find.clicked.connect(
                    partial(
                        self.find_paths,
                        widget,
                        current_item['type'],
                        description,
                        resolution,
                        format
                        )
                    )
                self.gridlayout.addWidget(button_find, index, 2, 1, 1)

    def find_paths(self, widget, types, title=None, resolution=None, format=None):
        if types == 'path':
            current_link = QtGui.QFileDialog.getOpenFileName(
                self, title, self.brows_directory, format)
            self.brows_directory = os.path.dirname(current_link[0])
        if types == 'directory':
            current_link = [QtGui.QFileDialog.getExistingDirectory(
                self, 'Browser', self.brows_directory)]
            self.brows_directory = current_link[0]
        if not os.path.exists(current_link[0]):
            return False, None
        widget.setText(current_link[0])
        if types == 'path' and resolution:
            self.snapshot(self.button_show, current_link[0], resolution)

    def snapshot(self, button, image_file, resolution):
        studio_image = studioImage.ImageCalibration(imgae_file=image_file)
        q_image, q_image_path = studio_image.set_studio_size(
            width=resolution[0], height=resolution[1])
        if not q_image:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not able to process image!..', QtGui.QMessageBox.Ok)
            return
        widgets.image_to_button(
            button, resolution[0], resolution[1], path=q_image_path)
        button.setStatusTip(q_image_path)
        return q_image, q_image_path

    def get_widget_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            widget = layout.itemAtPosition(row, 1).widget()
            if not widget:
                continue
            if isinstance(widget, QtGui.QComboBox):
                if not widget.isEditable():
                    value = widget.currentIndex()
                else:
                    value = widget.currentText().encode()
            else:
                value = widget.text().encode()
            values = {
                'widget': widget,
                'value': value
                }
            data.setdefault(widget.statusTip().encode(), values)
        data.setdefault('icon', {'widget': self.button_show, 'value': None})
        return data

    def get_data(self, layout):
        data = {}
        for row in range(layout.rowCount()):
            widget = layout.itemAtPosition(row, 1).widget()
            if not widget:
                continue
            if isinstance(widget, QtGui.QPushButton):
                continue
            if isinstance(widget, QtGui.QComboBox):
                if not widget.isEditable():
                    value = widget.currentIndex()
                else:
                    value = widget.currentText().encode()
            else:
                value = widget.text().encode()
            data.setdefault(widget.statusTip().encode(), value)
        return data


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window(
        parent=None,
        type='preferences',
        value=None,
        title='Show Inputs',
        width=822,
        height=376
    )
    window.show()
    sys.exit(app.exec_())
