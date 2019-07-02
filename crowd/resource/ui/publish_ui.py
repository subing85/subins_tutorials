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
import warnings
import logging

from pymel import core
from PySide import QtCore
from PySide import QtGui
from functools import partial

from crowd import resource
from crowd.utils import platforms
from crowd.api import crowdPublish
from crowd.resource.ui import comment_ui

reload(crowdPublish)
reload(comment_ui)
reload(resource)


class Connect(QtGui.QWidget):

    def __init__(self, type, parent=None):
        super(Connect, self).__init__(parent)
        self.object_name = 'publish_widget_%s' % type
        platforms.remove_exists_window(self.object_name)
        self.type = type
        self.heading = '[Subin CROwd]\t%s Publish' % (self.type)
        self.validate_bundles = {}
        self.extract_bundles = {}
        self.global_result = []
        self.global_extract = []
        self.font_size, self.font_type = resource.getFontSize()
        valid = platforms.has_valid()
        if not valid:
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
        self.comment = comment_ui.Connect(parent=None)
        self.setup_ui()
        self.modify_ui()
        self.load_validate()
        self.load_extract()

    def setup_ui(self):
        self.setObjectName(self.object_name)
        self.resize(430, 630)
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
        self.horizontallayout_input.setSpacing(4)
        self.horizontallayout_input.setContentsMargins(4, 30, 4, 4)
        self.combobox_input = QtGui.QComboBox(self.groupbox_input)
        self.combobox_input.setObjectName('comboBox_layout')
        self.combobox_input.setStyleSheet(
            'font: %spt \"%s\";' % (self.font_size, self.font_type))
        self.horizontallayout_input.addWidget(self.combobox_input)
        self.combobox_tag = QtGui.QComboBox(self)
        self.combobox_tag.setObjectName('combobox_type')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combobox_tag.setDuplicatesEnabled(True)
        self.combobox_tag.setStyleSheet(
            'font: %spt "Sans Serif";' % self.font_size)
        self.horizontallayout_input.addWidget(self.combobox_tag)
        self.groupbox_validate = QtGui.QGroupBox(self)
        self.groupbox_validate.setObjectName('groupbox_validate')
        self.groupbox_validate.setTitle('Validate')
        self.verticallayout.addWidget(self.groupbox_validate)
        self.verticallayout_validate = QtGui.QVBoxLayout(
            self.groupbox_validate)
        self.verticallayout_validate.setObjectName('verticallayout_validate')
        self.verticallayout_validate.setSpacing(4)
        self.verticallayout_validate.setContentsMargins(10, 10, 5, 5)
        self.scrollarea_validate = QtGui.QScrollArea(self)
        self.scrollarea_validate.setObjectName('scrollarea_validate')
        self.scrollarea_validate.setWidgetResizable(True)
        self.scrollarea_validate.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollarea_validate.setStyleSheet(
            'font: %spt "Sans Serif";' % self.font_size)
        self.verticallayout_validate.addWidget(self.scrollarea_validate)
        self.scrollwidget_validate = QtGui.QWidget()
        self.scrollwidget_validate.setObjectName('scrollwidget_validate')
        self.scrollarea_validate.setWidget(self.scrollwidget_validate)
        self.gridlayout_validate = QtGui.QGridLayout(
            self.scrollwidget_validate)
        self.gridlayout_validate.setObjectName('gridlayout_validate')
        self.gridlayout_validate.setSpacing(2)
        self.gridlayout_validate.setContentsMargins(0, -1, -1, -1)
        self.groupbox_extract = QtGui.QGroupBox(self)
        self.groupbox_extract.setObjectName('groupbox_extract')
        self.groupbox_extract.setTitle('Extract')
        self.verticallayout.addWidget(self.groupbox_extract)
        self.verticallayout_extract = QtGui.QVBoxLayout(self.groupbox_extract)
        self.verticallayout_extract.setObjectName('verticallayout_extract')
        self.verticallayout_extract.setSpacing(4)
        self.verticallayout_extract.setContentsMargins(10, 10, 5, 5)
        self.scrollarea_extract = QtGui.QScrollArea(self)
        self.scrollarea_extract.setObjectName('scrollarea_validate')
        self.scrollarea_extract.setWidgetResizable(True)
        self.scrollarea_extract.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollarea_extract.setStyleSheet(
            'font: %spt "Sans Serif";' % self.font_size)
        self.verticallayout_extract.addWidget(self.scrollarea_extract)
        self.scrollwidget_extract = QtGui.QWidget()
        self.scrollwidget_extract.setObjectName('scrollwidget_validate')
        self.scrollarea_extract.setWidget(self.scrollwidget_extract)
        self.gridlayout_extract = QtGui.QGridLayout(self.scrollwidget_extract)
        self.gridlayout_extract.setSpacing(2)
        self.gridlayout_extract.setObjectName('gridlayout_extract')
        self.groupbox_publish = QtGui.QGroupBox(self)
        self.groupbox_publish.setObjectName('groupbox_publish')
        self.groupbox_publish.setSizePolicy(sizepolicy)
        self.verticallayout.addWidget(self.groupbox_publish)
        self.verticallayout_publish = QtGui.QVBoxLayout(self.groupbox_publish)
        self.verticallayout_publish.setObjectName('verticallayout_publish')
        self.verticallayout_publish.setSpacing(4)
        self.horizontallayout_publish = QtGui.QHBoxLayout()
        self.horizontallayout_publish.setObjectName('horizontalLayout_publish')
        self.horizontallayout_publish.setSpacing(4)
        self.button_testrun = QtGui.QPushButton(self.groupbox_publish)
        self.button_testrun.setObjectName('button_testrun')
        self.button_testrun.setText('Test Run')
        self.button_testrun.clicked.connect(self.test_run)
        self.horizontallayout_publish.addWidget(self.button_testrun)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')
        self.button_publish.clicked.connect(self.publish)
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.verticallayout_publish.addLayout(self.horizontallayout_publish)
        self.progressbar = QtGui.QProgressBar(self.groupbox_publish)
        self.progressbar.setMinimumSize(QtCore.QSize(0, 15))
        self.progressbar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressbar.setProperty("value", 99)
        self.progressbar.setTextVisible(True)
        self.progressbar.setObjectName('progressbar')
        self.verticallayout_publish.addWidget(self.progressbar)

    def modify_ui(self):
        data = resource.getPublishTypes()
        self.combobox_input.addItems(data)
        self.combobox_input.setCurrentIndex(data.index(self.type))
        self.combobox_input.setEnabled(False)
        crowd_publish = crowdPublish.Connect(type=self.type)
        crowd_publish.type = crowd_publish.getDependency()
        tags = crowd_publish.getTags()
        if tags:
            self.combobox_tag.addItems([''] + tags)

    def load_validate(self):
        crowd_publish = crowdPublish.Connect(type=self.type)
        validator_bundles = crowd_publish.getValidate(valid=True)
        if not validator_bundles:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any validate bundles', QtGui.QMessageBox.Ok)
            return
        self.validate_bundles = self.load_buldles(
            'validate', validator_bundles, self.gridlayout_validate)

    def load_extract(self):
        crowd_publish = crowdPublish.Connect(type=self.type)
        extract_bundles = crowd_publish.getExtract(valid=True)
        if not extract_bundles:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'Not found any extract bundles', QtGui.QMessageBox.Ok)
            return
        self.extract_bundles = self.load_buldles(
            'extract', extract_bundles, self.gridlayout_extract)

    def load_buldles(self, type, data, layout):
        sorted_data = self.sorted_order(data)
        index, ing = 0, 1
        bundle_data = {}
        for k, v in sorted_data.items():
            for each_data in v:
                button_number = QtGui.QPushButton(self)
                button_number.setObjectName(
                    'button_number%s' % each_data.LONG_NAME)
                self.decorate_widget(
                    button_number, str(index + 1), [22, 22], [22, 22], 'Fixed')
                layout.addWidget(button_number, ing - 1, 0, 1, 1)
                button_name = QtGui.QPushButton(None)
                button_name.setObjectName(
                    'button_name_%s' % each_data.LONG_NAME)
                button_name.setStyleSheet('Text-align:left;')
                self.decorate_widget(
                    button_name,
                    ' %s' % each_data.LONG_NAME, [22, 22], [16777215, 22],
                    'Preferred')
                layout.addWidget(button_name, ing - 1, 1, 1, 1)
                button_open = QtGui.QPushButton(self)
                button_open.setObjectName(
                    'button_open_%s' % each_data.LONG_NAME)
                self.decorate_widget(
                    button_open, '+', [22, 22], [22, 22], 'Fixed')
                layout.addWidget(button_open, ing - 1, 2, 1, 1)
                textedit = QtGui.QTextEdit(self)
                textedit.setObjectName('textedit_%s' % each_data.LONG_NAME)
                textedit.setStyleSheet('font: 9pt "Sans Serif";')
                textedit.hide()
                layout.addWidget(textedit, ing, 1, 1, 2)
                button_name.clicked.connect(partial(
                    self.execute_bundle, type, each_data, button_name, textedit))
                button_open.clicked.connect(
                    partial(self.execute_bundle_detail, button_open, textedit))
                bundle_data.setdefault(
                    index, [each_data, button_name, textedit])
                index += 1
                ing += 2
        return bundle_data

    def decorate_widget(self, widget, lable, min, max, policy):
        widget.setText(lable)
        widget.setMinimumSize(QtCore.QSize(min[0], min[1]))
        widget.setMaximumSize(QtCore.QSize(max[0], max[1]))
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        if policy == 'Fixed':
            sizePolicy = QtGui.QSizePolicy(
                QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        widget.setSizePolicy(sizePolicy)

    def sorted_order(self, data):
        bundles = {}
        for each_data in data:
            bundles.setdefault(each_data.ORDER, []).append(each_data)
        return bundles

    def execute_bundle_detail(self, widget, textedit):
        if textedit.isVisible():
            textedit.hide()
            widget.setText('+')
            return
        textedit.show()
        widget.setText('-')

    def execute_bundle(self, type, bundle, widget, textedit):
        crowd_publish = crowdPublish.Connect(type=self.type)
        result, value, color, data, message = crowd_publish.executeModule(
            bundle)
        if type == 'extract':
            self.global_extract.append([data, message])
        widget.setStyleSheet('Text-align:left; color: {};'.format(color))
        textedit.setText(
            '%s\n#%s\n%s\n%s' % (bundle.__file__, result, message, data))
        self.global_result.append(value)

    def test_run(self):
        print '\n%s\npublish module {' % ('#' * 100)
        self.global_result = []
        self.global_extract = []
        data = [self.validate_bundles, self.extract_bundles]
        type = ['validate', 'extract']
        for x, each_data in enumerate(data):
            for index, bundle_data in each_data.items():
                self.execute_bundle(
                    type[x],
                    bundle_data[0],
                    bundle_data[1],
                    bundle_data[2]
                )
        print '\n}\n%s' % ('#' * 100)

    def publish(self):
        self.test_run()
        if False in self.global_result:
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Can not publish,\nfix the problems and try!...',
                QtGui.QMessageBox.Ok
            )
            logging.warning('Can not publish, fix the problems and try!...')
            return
        if not self.type:
            self.type = self.combobox_input.currentText()
        if self.type not in resource.getPublishTypes():
            QtGui.QMessageBox.warning(
                self,
                'Warning',
                'Can not find publish type called <%s>!...' % self.type,
                QtGui.QMessageBox.Ok
            )
            logging.warning(
                'Can not find publish type called <%s>!...' % self.type,)
            return
        tag = str(self.combobox_tag.currentText())
        if not tag or tag == '':
            QtGui.QMessageBox.warning(
                self,
                'Warning', 'Can not find name (tag)!...',
                QtGui.QMessageBox.Ok
            )
            logging.warning('Can not find name (tag)!...')
            return

        crowd_publish = crowdPublish.Connect(type=self.type)
        crowd_publish.type = crowd_publish.getDependency()
        dependency_tags = crowd_publish.getTags()

        # to check find dependency publish
        if self.type != crowd_publish.type:
            # self.type = 'puppet'
            # crowd_publish.type = 'skeleton'
            # dependency_tags = ['biped', 'man', 'woman', 'girl'] (skeleton tags)
            # tag = 'girl' (puppet tags)
            if tag not in dependency_tags:
                replay = QtGui.QMessageBox.warning(
                    self,
                    'Warning',
                    'Not found dependency publish called type <%s> tag <%s>' % (
                        crowd_publish.type, tag),
                    QtGui.QMessageBox.Ok
                )
                return

        crowd_publish.type = self.type
        result = True
        if crowd_publish.isExists(tag):
            replay = QtGui.QMessageBox.question(
                self,
                'Question',
                'Already exist <%s> in the data base!...%s' % (
                    tag, '\nAre you sure to overwrite?...'),
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No
            )
            if replay == QtGui.QMessageBox.No:
                logging.warning('Abort!...')
                return False

        if not result:
            warnings.warn(
                'Not able to replace exists publish <%s>' % tag,
                Warning
            )
            return

        scene_name = str(core.sceneName())
        if not scene_name:
            QtGui.QMessageBox.warning(
                self,
                'Warning', 'Can not save your scene!...',
                QtGui.QMessageBox.Ok)
            logging.warning('Can not save your scene!...')
            return

        description = 'This data contain information about <%s> publish' % self.type
        self.comment.type = self.type
        self.comment.tag = tag
        self.comment.description = description
        self.comment.scene_name = scene_name
        self.comment.extract = self.global_extract
        self.comment.show()
        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect('skeleton', parent=None)
    window.show()
    sys.exit(app.exec_())
