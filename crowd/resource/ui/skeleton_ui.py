import sys

from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.api import skeleton
from crowd.api import puppet

reload(platforms)
reload(skeleton)
reload(puppet)

'''
from crowd.resource.ui import skeleton_ui
reload(skeleton_ui)
window = skeleton_ui.Connect()
window.show()
'''


class Connect(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Connect, self).__init__(parent=None)

        self.input_skeleton_data = {}
        self.order = None
        self.input_skeletons = None
        self.input_puppet_skeleton = {}
        self.input_puppets = None
        self.input_widgets = {}
        self.comboboxs = []
        self.widget_type = ['Skeleton', 'Puppet']

        valid = platforms.has_valid()
        if not valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resource.getDownloadLink())
            QtGui.QMessageBox.critical(
                self, 'Critical', message, QtGui.QMessageBox.Ok)
            return
        if False in valid:
            message = '{}\n\nPlease download the proper version from\n{}'.format(
                valid[False], resource.getDownloadLink())
            QtGui.QMessageBox.critical(
                self, 'Critical', message, QtGui.QMessageBox.Ok)
            return
        tool_kit = platforms.get_tool_kit()
        self.tool_kit_object, self.tool_kit_name, self.version = tool_kit['skeleton']
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [500, 125]
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.get_input_data()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('Skeleton')
        self.resize(500, 125)
        self.setWindowTitle(self.tool_kit_titile)
        self.setStyleSheet('font: 14pt \"Sans Serif\";')
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.label_title = QtGui.QLabel(self)
        self.label_title.setObjectName('label')
        self.label_title.setStyleSheet('font: 20pt \"Sans Serif\";')
        self.label_title.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_title.setText('Subin CROwd')
        self.verticallayout.addWidget(self.label_title)
        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.verticallayout.addWidget(self.groupbox)
        self.gridlayout = QtGui.QGridLayout(self.groupbox)
        self.gridlayout.setObjectName('gridLayout')
        self.verticallayout.addLayout(self.gridlayout)
        for x, widget in enumerate(self.widget_type):
            self.label = QtGui.QLabel(self)
            self.label.setObjectName('label_{}'.format(widget.lower()))
            self.label.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.label.setText('{} Type'.format(widget))
            self.gridlayout.addWidget(self.label, x, 0, 1, 1)
            self.combobox = QtGui.QComboBox(self)
            self.combobox.setObjectName('combobox_{}'.format(widget.lower()))
            self.combobox.addItems(self.input_widgets[widget])
            self.gridlayout.addWidget(self.combobox, x, 1, 1, 1)
            self.button = QtGui.QPushButton(self)
            self.button.setObjectName('button_{}'.format(widget.lower()))
            self.button.setText('Create')
            self.gridlayout.addWidget(self.button, x, 2, 1, 1)
            self.button.clicked.connect(
                partial(self.create, self.combobox, widget.lower()))
            self.comboboxs.append(self.combobox)

    def get_input_data(self):
        crowd_skeleton = skeleton.Connect()
        self.input_skeleton_data, self.order = crowd_skeleton.findInputs()
        self.input_skeletons = sum(self.order.values(), [])
        self.input_puppet_skeleton = crowd_skeleton.findSkeletons()
        self.input_puppets = [each.name() for each in sorted(
            self.input_puppet_skeleton.keys())]
        self.input_widgets['Skeleton'] = self.input_skeletons
        self.input_widgets['Puppet'] = self.input_puppets

    def update_puppet_inputs(self):
        self.get_input_data()
        for x, widget in enumerate(self.widget_type):
            self.comboboxs[x].clear()
            self.comboboxs[x].addItems(self.input_widgets[widget])

    def create(self, widget, type):
        current = widget.currentText()
        if type == 'skeleton':
            crowd_skeleton = skeleton.Connect()
            crowd_skeleton.create(current)
            self.update_puppet_inputs()
        if type == 'puppet':
            crowd_puppet = puppet.Connect()
            crowd_puppet.create(current)

    def create_puppet(self):
        pass
        from crowd.api import skeleton
        reload(skeleton)
        ske = skeleton.Connect()
        ske.create('biped')

        from crowd.api import puppet
        reload(puppet)
        ske = puppet.Connect()
        ske.create('biped')

        from crowd.api import animation
        reload(animation)
        ske = animation.Connect('biped')
        ske.write_puppet()

        from pymel import core
        from crowd.api import crowdMaya
        reload(crowdMaya)
        node = core.ls(sl=1)
        crowd_maya = crowdMaya.Connect()
        print crowd_maya.read_ainmations(node)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None)
    window.show()
    sys.exit(app.exec_())
