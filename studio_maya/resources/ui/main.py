'''
main.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import sys
import json
import warnings
import threading
import subprocess
import webbrowser

from PySide import QtGui
from PySide import QtCore
from pprint import pprint
from functools import partial

from studio_maya import resources
from studio_maya.core import drag
from studio_maya.core import generic
from studio_maya.core import console
from studio_maya.core import widgets
from studio_maya.core import stylesheet
from studio_maya.resources.ui import preference


class MayaWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MayaWindow, self).__init__(parent)
        self.label, self.name, self.version = resources.getToolKit()
        self.width, self.height = 1000, 900
        self.browse_path = resources.getWorkspacePath()
        self.preference_path = resources.getPreferenceFile()
        self.current_file = None
        self.current_treewidget = None
        self.pause = False
        self.stop = False
        self.operating_system = resources.getOperatingSystem()
        self.thread_status = []
        self.style = stylesheet.connect()
        self.setup_ui()
        self.modify_widgets()
        self.preference = preference.Window(
            parent=self, lables=[self.label_mayalogo, self.label_maya])
        self.preference.setStyleSheet(self.style)
        self.set_toolbar(self.horizontallayout_bar)
        self.set_maya_version()
        self.custom_console = console.Connect()
        self.custom_console.stdout().message_written.connect(
            self.textedit_output.insertPlainText)

    def setup_ui(self):
        self.setObjectName('maya_mainwindow')
        self.setStyleSheet(self.style)
        self.setWindowTitle('{} {}'.format(self.label, self.version))
        self.resize(self.width, self.height)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)
        self.groupbox_bar = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_bar.setObjectName('groupbox_bar')
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_bar.setSizePolicy(sizepolicy)
        self.verticallayout.addWidget(self.groupbox_bar)
        self.horizontallayout_bar = QtGui.QHBoxLayout(self.groupbox_bar)
        self.horizontallayout_bar.setObjectName('horizontallayout_toolbar')
        self.horizontallayout_bar.setSpacing(10)
        self.horizontallayout_bar.setContentsMargins(2, 2, 2, 2)
        self.label_mayalogo = QtGui.QLabel(self.centralwidget)
        self.label_mayalogo.setObjectName('label_mayalogo')
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        self.label_mayalogo.setSizePolicy(sizepolicy)
        self.label_maya = QtGui.QLabel(self.centralwidget)
        self.label_maya.setObjectName('label_maya')
        self.label_maya.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_maya.setSizePolicy(sizepolicy)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setObjectName('splitter')
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.verticallayout.addWidget(self.splitter)
        self.groupbox_input = QtGui.QGroupBox(self.splitter)
        self.groupbox_input.setObjectName('groupbox_input')
        self.horizontallayout_input = QtGui.QHBoxLayout(self.groupbox_input)
        self.horizontallayout_input.setObjectName('horizontallayout_input')
        self.horizontallayout_input.setSpacing(10)
        self.horizontallayout_input.setContentsMargins(2, 2, 2, 2)
        self.splitter_input = QtGui.QSplitter(self.groupbox_input)
        self.splitter_input.setObjectName('splitter_input')
        self.splitter_input.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_input.setHandleWidth(5)
        self.horizontallayout_input.addWidget(self.splitter_input)
        self.textedit_output = QtGui.QTextEdit(self.splitter)
        self.textedit_output.setObjectName('textedit_output')
        self.textedit_output.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textedit_output.setStyleSheet('font: 11pt')
        self.textedit_output.setReadOnly(True)
        self.progressbar = QtGui.QProgressBar(self.centralwidget)
        self.progressbar.setObjectName('progressbar')
        self.progressbar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressbar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressbar.setValue(0)
        self.progressbar.setFormat('%p%')
        self.progressbar.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.progressbar.hide()
        self.verticallayout.addWidget(self.progressbar)
        self.horizontallayout_credit = QtGui.QHBoxLayout(None)
        self.horizontallayout_credit.setObjectName('horizontallayout_credit')
        self.horizontallayout_credit.setSpacing(10)
        self.horizontallayout_credit.setContentsMargins(5, 5, 5, 5)
        self.verticallayout.addLayout(self.horizontallayout_credit)
        spacer_item = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontallayout_credit.addItem(spacer_item)
        self.button_logo = QtGui.QPushButton(self.centralwidget)
        self.button_logo.setObjectName('button_logo')
        self.button_logo.setFlat(True)
        log_path = os.path.join(
            resources.getIconPath(), 'studio_maya_logo.png')
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(log_path),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.button_logo.setIcon(icon)
        self.button_logo.setIconSize(QtCore.QSize(341, 90))
        self.button_logo.setMinimumSize(QtCore.QSize(341, 90))
        self.button_logo.setMaximumSize(QtCore.QSize(341, 90))
        self.horizontallayout_credit.addWidget(self.button_logo)
        self.label_sign = QtGui.QLabel(self.centralwidget)
        self.label_sign.setObjectName('label_sign')
        self.label_sign.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_sign.setText('www.subin-toolkits.com\nsubing85@gmail.com')
        self.label_sign.setStyleSheet('font: 10pt;')
        self.verticallayout.addWidget(self.label_sign)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setObjectName('menubar')
        self.setMenuBar(self.menubar)
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName('menu_file')
        self.menu_file.setTitle('File')
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName('menu_edit')
        self.menu_edit.setTitle('Edit')
        self.menu_settings = QtGui.QMenu(self.menubar)
        self.menu_settings.setObjectName('menu_settings')
        self.menu_settings.setTitle('Settings')
        self.menu_run = QtGui.QMenu(self.menubar)
        self.menu_run.setObjectName('menu_run')
        self.menu_run.setTitle('Run')
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName('menu_help')
        self.menu_help.setTitle('Help')
        self.action_new = QtGui.QAction(self)
        self.action_new.setObjectName('action_new')
        self.action_new.setText('New')
        self.action_open = QtGui.QAction(self)
        self.action_open.setObjectName('action_open')
        self.action_open.setText('Open')
        self.action_save = QtGui.QAction(self)
        self.action_save.setObjectName('action_save')
        self.action_save.setText('Save')
        self.action_saveAs = QtGui.QAction(self)
        self.action_saveAs.setObjectName('action_saveAs')
        self.action_saveAs.setText('Save As...')
        self.action_quit = QtGui.QAction(self)
        self.action_quit.setObjectName('action_quit')
        self.action_quit.setText('Quit')
        self.action_import_maya = QtGui.QAction(self)
        self.action_import_maya.setObjectName('action_import_maya')
        self.action_import_maya.setText('Import Maya File')
        self.action_import_code = QtGui.QAction(self)
        self.action_import_code.setObjectName('action_import_code')
        self.action_import_code.setText('Import Mel/Python')
        self.action_import_sample = QtGui.QAction(self)
        self.action_import_sample.setObjectName('action_import_sample')
        self.action_import_sample.setText('Import Sample Scripts')
        self.action_preference = QtGui.QAction(self)
        self.action_preference.setObjectName('action_preference')
        self.action_preference.setText('Preference')
        self.action_execute = QtGui.QAction(self)
        self.action_execute.setObjectName('action_execute')
        self.action_execute.setText('Start To Execute')
        self.action_pause = QtGui.QAction(self)
        self.action_pause.setObjectName('action_pause')
        self.action_pause.setText('Pause')
        self.action_pause.setVisible(False)
        self.action_stop = QtGui.QAction(self)
        self.action_stop.setObjectName('action_stop')
        self.action_stop.setText('Stop')
        self.action_stop.setVisible(False)
        self.action_about = QtGui.QAction(self)
        self.action_about.setObjectName('action_about')
        self.action_about.setText('About Application')
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_saveAs)
        self.menu_file.addSeparator()
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_edit.addAction(self.action_import_maya)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_import_code)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_import_sample)
        self.menu_settings.addAction(self.action_preference)
        self.menu_help.addAction(self.action_about)
        self.menu_run.addAction(self.action_execute)
        self.menu_run.addAction(self.action_pause)
        self.menu_run.addAction(self.action_stop)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_run.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.action_remove = QtGui.QAction(self)
        self.action_remove.setObjectName('action_remove')
        self.action_remove.setText('Remove')
        self.action_clear = QtGui.QAction(self)
        self.action_clear.setObjectName('action_clear')
        self.action_clear.setText('Clear')
        self.action_edit = QtGui.QAction(self)
        self.action_edit.setObjectName('action_edit')
        self.action_edit.setText('Edit')
        self.treewidget_maya = drag.DropArea(type='maya')
        self.treewidget_maya.setObjectName('treewidget_maya')
        self.treewidget_maya.headerItem().setText(0, 'No')
        self.treewidget_maya.headerItem().setText(1, 'Maya Files')
        self.treewidget_maya.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.treewidget_maya.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget_maya.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget_maya, 'maya'))
        self.splitter_input.addWidget(self.treewidget_maya)
        self.treewidget_code = drag.DropArea(type='code')
        self.treewidget_code.setObjectName('treewidget_code')
        self.treewidget_code.headerItem().setText(0, 'No')
        self.treewidget_code.headerItem().setText(1, 'Scripts')
        self.treewidget_code.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.treewidget_code.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treewidget_code.customContextMenuRequested.connect(
            partial(self.on_context_menu, self.treewidget_code, 'code'))
        self.splitter_input.addWidget(self.treewidget_code)
        self.treewidget_maya.header().resizeSection(0, 80)
        self.treewidget_maya.header().resizeSection(1, 80)
        self.treewidget_code.header().resizeSection(0, 80)
        self.treewidget_code.header().resizeSection(1, 80)
        self.splitter.setSizes([468, 175])
        self.action_new.triggered.connect(self.new)
        self.action_open.triggered.connect(self.open)
        self.action_save.triggered.connect(self.save)
        self.action_saveAs.triggered.connect(self.save_as)
        self.action_quit.triggered.connect(self.quit)
        self.action_execute.triggered.connect(self.execute)
        self.action_pause.triggered.connect(self.set_pause)
        self.action_stop.triggered.connect(self.set_stop)
        self.action_about.triggered.connect(self.about)
        self.action_import_maya.triggered.connect(
            partial(self.import_source, 'maya'))
        self.action_import_code.triggered.connect(
            partial(self.import_source, 'code'))
        self.action_import_sample.triggered.connect(
            partial(self.import_samples, self.treewidget_code))
        self.action_preference.triggered.connect(self.show_preference)
        self.action_remove.triggered.connect(partial(self.remove, 'selected'))
        self.action_clear.triggered.connect(partial(self.remove, 'all'))
        self.action_edit.triggered.connect(
            partial(self.edit_code, self.treewidget_code))
        self.button_logo.clicked.connect(self.subin_toolkit)

    def modify_widgets(self):
        icon_path = resources.getIconPath()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(icon_path, 'title.png')))
        self.setWindowIcon(icon)
        qactions = self.findChildren(QtGui.QAction)
        for qaction in qactions:
            icon = QtGui.QIcon()
            label = str(qaction.objectName()).split('action_')[-1]
            if not label:
                continue
            icon.addPixmap(
                QtGui.QPixmap(os.path.join(icon_path, '%s.png' % label)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
            )
            qaction.setIcon(icon)

    def set_toolbar(self, layout):
        self.toolBar = QtGui.QToolBar()
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_import_maya)
        self.toolBar.addAction(self.action_import_code)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_preference)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_execute)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_pause)
        self.toolBar.addAction(self.action_stop)
        self.toolBar.addSeparator()
        layout.addWidget(self.toolBar)
        layout.addWidget(self.label_mayalogo)
        layout.addWidget(self.label_maya)

    def on_context_menu(self, treewidget, type, point):
        self.current_treewidget = treewidget
        self.contex_menu = QtGui.QMenu(self)
        index = treewidget.indexAt(point)
        if not index.isValid():
            import_type = self.action_import_maya
            if type == 'code':
                import_type = self.action_import_code
            self.contex_menu.addAction(import_type)
        if index.isValid():
            if type == 'code':
                self.contex_menu.addAction(self.action_edit)
            self.contex_menu.addSeparator()
            self.contex_menu.addAction(self.action_remove)
            self.contex_menu.addAction(self.action_clear)
        self.contex_menu.exec_(treewidget.mapToGlobal(point))

    def set_maya_version(self):
        widgets.set_maya_version(
            self.preference_path, self.label_mayalogo, self.label_maya)

    def new(self):
        self.treewidget_maya.clear()
        self.treewidget_code.clear()
        self.textedit_output.clear()
        self.current_file = None
        self.setWindowTitle('{} {}'.format(self.label, self.version))

    def open(self):
        if self.current_file:
            replay = QtGui.QMessageBox.question(
                self,
                'Question',
                'Are you sure, you want to open?!..',
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No,
            )
            if replay == QtGui.QMessageBox.No:
                return
        self.new()
        self.current_file, extension = QtGui.QFileDialog.getOpenFileName(
            self, 'Open Form', self.browse_path, 'Studio Maya (*.smi)')
        data = generic.read_data(self.current_file)
        if not data:
            print 'not valid data'
            return
        if 'code' in data:
            widgets.set_item_contents(
                'code', data['code'], self.treewidget_code)
        if 'maya' in data:
            widgets.set_item_contents(
                'maya', data['maya'], self.treewidget_maya)
        self.setWindowTitle(self.current_file)

    def save(self):
        if not self.current_file:
            self.save_as()
            return
        self.save_to()

    def save_as(self):
        self.current_file, extension = QtGui.QFileDialog.getSaveFileName(
            self, 'Save Form As', self.browse_path, 'Studio Maya (*.smi)')
        if not self.current_file:
            return
        self.save_to()

    def save_to(self):
        label, name, version = resources.getToolKit()
        maya_data = widgets.get_item_contents(self.treewidget_maya, 1)
        code_data = widgets.get_item_contents(self.treewidget_code, 1)
        data = {
            'parent': {
                'studio_maya': {
                    'label': label,
                    'version': version,
                    'type': 'studio_maya_data',
                }
            },
            'child': {
                'maya': maya_data,
                'code': code_data
            }
        }
        generic.write_data(data, self.current_file)
        self.setWindowTitle(self.current_file)
        print 'Successfully saved to %s' % self.current_file

    def quit(self):
        self.close()

    def import_source(self, type):
        formats = resources.getFormats()
        files, extension = QtGui.QFileDialog.getOpenFileNames(
            self,
            'Import %s files' % type,
            self.browse_path,
            '%s file (%s)' % (type, '*%s' % ' *'.join(formats[type]))
            # example 'Maya file (*.ma *.mb)'
        )
        if not files:
            return
        treewidget = self.treewidget_maya
        if type == 'code':
            treewidget = self.treewidget_code
        exist_codes = widgets.get_exists_items(treewidget)
        for file in files:
            if file in exist_codes:
                continue
            widgets.create_item(treewidget, type, file)
        self.browse_path = os.path.basename(files[-1])

    def import_samples(self, treewidget):
        exist_codes = widgets.get_exists_items(treewidget)
        script_path = resources.getScriptPath()
        source_codes = generic.get_codes(script_path)
        for code in source_codes:
            if code in exist_codes:
                continue
            widgets.create_item(treewidget, 'code', code)

    def show_preference(self):
        self.preference.show()
        self.setEnabled(False)

    def remove(self, type):
        if not self.current_treewidget:
            return
        if type == 'all':
            self.current_treewidget.clear()
            return
        items = self.current_treewidget.selectedItems()
        for each in items:
            each.removeChild(each)

    def edit_code(self, treewidget):
        items = treewidget.selectedItems()
        if not items:
            warnings.warn('Not selected any items', Warning)
            return
        code_path = items[-1].toolTip(1).encode()
        print 'source code :', code_path
        generic.open_editer(code_path)

    def set_stop(self):
        self.stop = True

    def set_pause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True

    def execute(self):
        self.textedit_output.clear()
        input_data = generic.read_preset(self.preference_path)
        mayapy = input_data['current_version']['path'].replace('\\', '/')
        maya_version = input_data['current_version']['name']
        query = input_data['mode']['query_only']
        overwrite = input_data['mode']['overwrite']
        maya_files = self.treewidget_maya.selectedItems()
        if not maya_files:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'select the maya files', QtGui.QMessageBox.Ok)
            return
        codes = self.treewidget_code.selectedItems()
        if not codes:
            QtGui.QMessageBox.warning(
                self, 'Warning', 'select the source code file', QtGui.QMessageBox.Ok)
            return
        code_file = codes[-1].toolTip(1).encode().replace('\\', '/')
        ing = len(maya_files) - 1
        if len(maya_files) < 1:
            ing = 1
        progress = QtGui.QProgressDialog(self)
        progress.setWindowTitle('Progress')
        progress.setLabelText('Executing \tplease wait .....')
        progress.setMaximum(ing)
        progress.setAutoClose(True)
        progress.setValue(10)
        progress.show()
        for index, each in enumerate(maya_files):
            maya_file = each.toolTip(1).encode().replace('\\', '/')
            progress.setLabelText(
                'Executing \tplease wait!...\n%s' % each.text(1))
            progress.setValue(index)
            if progress.wasCanceled():
                break
            save = None
            if not query and overwrite:
                save = maya_file
            elif not query:
                next_maya = generic.next_version(maya_file)
                save = next_maya
            if self.stop:
                self.stop = False
                break
            if self.pause:
                with self.state:
                    self.state.wait()
            if not self.stop and not self.pause:
                self.state = threading.Condition()
                self.paly_thread = threading.Thread(
                    target=self.sub_process,
                    args=(
                        mayapy,
                        maya_file,
                        code_file,
                        save,
                    )
                )
                self.paly_thread.daemon = True
                self.paly_thread.start()
                self.paly_thread.join()
                print index + 1
                print '\tmaya file :'.expandtabs(5), maya_file
                print '\tmayapy :'.expandtabs(5), mayapy
                print '\tsource code file :'.expandtabs(5), code_file
                print '\tsaved file :'.expandtabs(5), save

        progress.setValue(100)
        progress.close()

        QtGui.QMessageBox.information(
            self,
            'Information',
            'Done!...\nMore details, please check < Konsole >',
            QtGui.QMessageBox.Ok)
        print '\nDone!...\nMore details, please check < Konsole >'

    def os_process(self, mayapy, maya, code, save):
        commands = [
            'import sys',
            'sys.path.append(\'%s\')' % resources.getInputPath(),
            'import initialize',
            'initialize.start(\'%s\', \'%s\', \'%s\')' % (
                maya, code, save)
        ]
        command = None
        if self.operating_system == 'Linux':
            command = "\"" + mayapy + '\"' + \
                ' -c \"' + '; '.join(commands) + '\"'
        if self.operating_system == 'Windows':
            if 'Program Files' in mayapy:
                mayapy = mayapy.replace('Program Files', '\"Program Files\"')
            command = mayapy + ' -c ' + '\"' + '; '.join(commands) + '\"'
        os.system(command)

    def sub_process(self, mayapy, maya, code, save):
        commands = [
            'import sys',
            'sys.path.append(\'%s\')' % resources.getInputPath(),
            'import initialize',
            'initialize.start(\'%s\', \'%s\', \'%s\')' % (maya, code, save)
        ]
        process = None
        if self.operating_system == 'Linux':
            command = mayapy + ' -c \"' + '; '.join(commands) + '\"'
            process = subprocess.Popen([command], shell=True)
        if self.operating_system == 'Windows':
            process = subprocess.Popen(
                [mayapy, '-c', '; '.join(commands)], shell=True)
        if process:
            process.wait()
            communicate = process.communicate()
        # result = process.returncode

    def about(self):
        webbrowser.open(resources.getToolKitHelpLink())

    def subin_toolkit(self):
        webbrowser.open(resources.getToolKitLink())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MayaWindow()
    window.show()
    sys.exit(app.exec_())
