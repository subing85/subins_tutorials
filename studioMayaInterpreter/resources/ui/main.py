import os
import sys

from PySide import QtGui
from PySide import QtCore

from studioMayaInterpreter import resources

reload(resources)


class MayaWindow(QtGui.QMainWindow):

    def __init__(self, parent=None, **kwargs):
        super(MayaWindow, self).__init__(**kwargs)

        self.label, self.name, self.version = resources.get_tool_kit()
        self.width, self.height = 600, 500
        
        self.setup_ui()
        self.modify_widgets()
        self.set_toolbar(self.horizontallayout_bar)
        print self.splitter.sizes()

    def setup_ui(self):
        self.setObjectName('maya_window')
        self.setWindowTitle('{} {}'.format(self.label, self.version))
        self.resize(self.width, self.height)

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        # self.verticallayout.setSpacing(10)
        #self.verticallayout.setContentsMargins(10, 10, 10, 10)

        self.groupbox_bar = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_bar.setObjectName('groupbox_bar')
        sizepolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        self.groupbox_bar.setSizePolicy(sizepolicy)
        self.verticallayout.addWidget(self.groupbox_bar)

        self.horizontallayout_bar = QtGui.QHBoxLayout(self.groupbox_bar)
        self.horizontallayout_bar.setObjectName('horizontallayout_toolbar')
        self.horizontallayout_bar.setSpacing(10)
        self.horizontallayout_bar.setContentsMargins(10, 10, 10, 10)

        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setObjectName('splitter')
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.verticallayout.addWidget(self.splitter)

        self.groupbox_input = QtGui.QGroupBox(self.splitter)
        self.groupbox_input.setObjectName('groupbox_input')

        self.horizontallayout_input = QtGui.QHBoxLayout(self.groupbox_input)
        self.horizontallayout_input.setObjectName('horizontallayout_input')
        # self.horizontallayout_input.setSpacing(10)
        #self.horizontallayout_input.setContentsMargins(10, 10, 10, 10)

        self.splitter_input = QtGui.QSplitter(self.groupbox_input)
        self.splitter_input.setObjectName('splitter_input')
        self.splitter_input.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_input.setHandleWidth(5)
        self.horizontallayout_input.addWidget(self.splitter_input)

        # trail
        self.textEdit_result = QtGui.QTextEdit(self.splitter_input)
        self.textEdit_result.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_result = QtGui.QTextEdit(self.splitter_input)
        self.textEdit_result.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)

        self.textedit_output = QtGui.QTextEdit(self.splitter)
        self.textedit_output.setObjectName('textedit_output')
        self.textedit_output.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textedit_output.setReadOnly(True)
        self.textedit_output.setOverwriteMode(False)

        self.progressbar = QtGui.QProgressBar(self.centralwidget)
        self.progressbar.setObjectName('progressbar')
        self.progressbar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressbar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressbar.setValue(0)
        self.progressbar.setFormat('')
        self.verticallayout.addWidget(self.progressbar)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName('label')
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticallayout.addWidget(self.label)

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
        self.action_import_file = QtGui.QAction(self)
        self.action_import_file.setObjectName('action_import_file')
        self.action_import_file.setText('Import Maya File')         
        self.action_import_code = QtGui.QAction(self)
        self.action_import_code.setObjectName('action_import_code')
        self.action_import_code.setText('Import Mel/Python')
        self.action_preference = QtGui.QAction(self)
        self.action_preference.setObjectName('action_preference')
        self.action_preference.setText('Preference')
        self.action_execute = QtGui.QAction(self)
        self.action_execute.setObjectName('action_execute')
        self.action_execute.setText('Start To Execute')           
        self.action_about = QtGui.QAction(self)
        self.action_about.setObjectName('action_about')
        self.action_about.setText('About Application')        
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_saveAs)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_edit.addAction(self.action_import_file)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_import_code)
        self.menu_settings.addAction(self.action_preference)
        self.menu_help.addAction(self.action_about)
        self.menu_run.addAction(self.action_execute)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_run.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        
        self.splitter.setSizes([500, 350])

    def modify_widgets(self):
        icon_path = resources.getIconPath()        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(icon_path, 'logo.png')))
        self.setWindowIcon(icon)
        qactions = self.findChildren(QtGui.QAction)
        for qaction in qactions :
            icon = QtGui.QIcon()            
            label =  str(qaction.objectName()).split ('action_')[-1]
            print label
            if not label:
                continue
            icon.addPixmap(
                QtGui.QPixmap(os.path.join(icon_path, '%s.png'%label)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
            )
            qaction.setIcon(icon)  
            # qaction.setIconSize(QtCore.QSize(140, 140))
            
    def set_toolbar (self, layout) :
        self.toolBar = QtGui.QToolBar()
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        # self.toolBar.addAction(self.action_saveAs)        
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_import_file)
        self.toolBar.addAction(self.action_import_code)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_preference)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_execute)       
        layout.addWidget (self.toolBar)    
                
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MayaWindow()
    window.show()
    sys.exit(app.exec_())
