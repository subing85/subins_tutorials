'''
create_ui.py 0.0.1 
Date: June 14, 2019
Last modified: June 14, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''


import sys

from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.api import crowdSkeleton
from crowd.api.old import puppet

reload(platforms)
reload(crowdSkeleton)
reload(puppet)

'''
from crowd.resource.ui.old import skeleton_ui
reload(skeleton_ui)
window = skeleton_ui.Connect()
window.show()
'''
'''
publish_ui.py 0.0.1 
Date: June 10, 2019
Last modified: June 14, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys

from pymel import core
from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.api import crowdPublish
from crowd.api import crowdCreate

reload(crowdPublish)
reload(crowdCreate)


class Connect(QtGui.QWidget):

    def __init__(self, type, parent=None):
        super(Connect, self).__init__(parent)
        self.object_name = 'create_widget_%s' % type
        platforms.remove_exists_window(self.object_name)
        self.type = type
        self.heading = '[Subin CROwd]\t%s Create' % (self.type)
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
        self.tool_kit_object, self.tool_kit_name, self.version = tool_kit['publish']
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)
        self.width, self.height = [500, 125]
        self.tool_kit_titile = '{} {}'.format(self.tool_kit_name, self.version)

        self.setup_ui()
        self.modify_ui()

    def setup_ui(self):
        self.setObjectName(self.object_name)
        self.resize(490, 147)
        self.setWindowTitle(self.tool_kit_titile)
        self.setStyleSheet('font: 14pt \"Sans Serif\";')
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.label_title = QtGui.QLabel(self)
        self.label_title.setObjectName('label')
        self.label_title.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_title.setText(self.heading)
        self.verticallayout.addWidget(self.label_title)
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizepolicy.setHorizontalStretch(0)
        sizepolicy.setVerticalStretch(0)
        self.groupbox_input = QtGui.QGroupBox(self)
        self.groupbox_input.setObjectName('groupbox_input')
        self.groupbox_input.setTitle('Inputs')
        self.groupbox_input.setSizePolicy(sizepolicy)
        self.verticallayout.addWidget(self.groupbox_input)
        self.horizontallayout_input = QtGui.QHBoxLayout(self.groupbox_input)
        self.horizontallayout_input.setObjectName('horizontalLayout_input')
        self.horizontallayout_input.setSpacing(10)
        self.horizontallayout_input.setContentsMargins(10, 30, 10, 10)
        self.label_type = QtGui.QLabel(self)
        self.label_type.setObjectName('label')
        self.label_type.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_type.setText('Type')
        self.horizontallayout_input.addWidget(self.label_type)
        self.combobox_input = QtGui.QComboBox(self.groupbox_input)
        self.combobox_input.setObjectName('comboBox_layout')
        self.horizontallayout_input.addWidget(self.combobox_input)
        self.button_create = QtGui.QPushButton(self)
        self.button_create.setObjectName('button_create')
        self.button_create.setText('Create')
        self.button_create.clicked.connect(self.create)
        self.horizontallayout_input.addWidget(self.button_create)

    def modify_ui(self):
        publish = crowdPublish.Connect(type=self.type)
        tags = publish.getTags()
        self.combobox_input.addItems(tags)

    def create(self):
        current_tag = str(self.combobox_input.currentText())
        ccreate = crowdCreate.Connect(type=self.type, tag=current_tag)
        ccreate.do()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect('skeleton', parent=None)
    window.show()
    sys.exit(app.exec_())
