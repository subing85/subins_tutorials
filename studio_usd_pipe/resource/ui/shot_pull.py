import os
import sys
import ast
import copy
import json
import getpass
import tempfile
import warnings


from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets

from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioPull
from studio_usd_pipe.api import studioInputs
from studio_usd_pipe.api import studioEnviron
from studio_usd_pipe.resource.ui import catalogue
reload(studioPull)

class Window(QtWidgets.QWidget):
 
    def __init__(self, parent=None, standalone=None, application=None):
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.application = application        
        self.pipe = 'shots'
        self.upstrem_pipe = 'assets'
        self.subfield = 'layout'
        self.title = 'shot pull'
        self.width = 572
        self.height = 318
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.upstrem_pipe) 
        self.comp_catalogue = catalogue.Catalogue()        
        self.show_icon = self.environ.get_show_icon()
        
        self.setup_ui()
        self.setup_icons()
        self.set_default()
        
    def setup_ui(self):  
        self.setObjectName('widget_shot_pull')
        self.resize(self.width, self.height)         
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)

        self.verticallayout_item, self.button_show = swidgets.set_header(
            self, self.title, self.verticallayout, show_icon=self.show_icon)    

        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName('gridlayout')
        self.verticallayout_item.addLayout(self.gridlayout)
        
        self.label_subfield = QtWidgets.QLabel(self)
        self.label_subfield.setObjectName('label_subfield')
        self.label_subfield.setText('subfield')
        self.label_subfield.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_subfield, 0, 0, 1, 1)
        self.combobox_subfield = QtWidgets.QComboBox(self)
        self.combobox_subfield.setObjectName('combobox_subfield')
        self.combobox_subfield.setEditable(True)
        self.combobox_subfield.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_subfield, 0, 1, 1, 1)  
                
        
        self.label_type = QtWidgets.QLabel(self)
        self.label_type.setObjectName('label_type')        
        self.label_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_type.setText('type')   
        self.gridlayout.addWidget(self.label_type, 1, 0, 1, 1)

        self.combobox_type = QtWidgets.QComboBox(self)
        self.combobox_type.setObjectName('combobox_type')
        self.gridlayout.addWidget(self.combobox_type, 1, 1, 1, 1)
        self.combobox_type.currentIndexChanged.connect(self.set_current_type)

        self.label_tag = QtWidgets.QLabel(self)
        self.label_tag.setObjectName('label_tag')
        self.label_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tag.setText('tag')
        self.gridlayout.addWidget(self.label_tag, 2, 0, 1, 1)
        
        self.combobox_tag = QtWidgets.QComboBox(self)
        self.combobox_tag.setObjectName('comboBox_tag')
        self.gridlayout.addWidget(self.combobox_tag, 2, 1, 1, 1)
        self.combobox_tag.currentIndexChanged.connect(self.set_current_tag)
        
                
       
        # self.gridlayout.addWidget(self.comp_catalogue, 2, 2, 1, 1)

        self.horizontallayout_button = QtWidgets.QHBoxLayout()
        self.horizontallayout_button.setObjectName('horizontallayout_button')
        self.horizontallayout_button.setSpacing(10)
        self.horizontallayout_button.setContentsMargins(5, 5, 5, 5)        
        self.verticallayout.addLayout(self.horizontallayout_button)  
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_button.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('cancel')
        self.horizontallayout_button.addWidget(self.button_cancel)
        
        self.button_open = QtWidgets.QPushButton(self)
        self.button_open.setObjectName('button_open')
        self.button_open.setText('open')
                
        self.horizontallayout_button.addWidget(self.button_open)
        self.button_cancel.clicked.connect(self.close)     
        self.button_open.clicked.connect(self.open)

    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)
    
    def set_default(self):
        castingsheet_path = self.get_castingsheet_path()
        if not castingsheet_path:
            return
        self.casting_data = resource.getInputData(castingsheet_path)
        self.combobox_type.clear()
        types = sorted(self.casting_data.keys())
        self.combobox_type.addItems(types)
    
    def set_current_type(self):
        current_type = self.combobox_type.currentText()
        tags = sorted(self.casting_data[current_type].keys())
        self.combobox_tag.clear()
        self.combobox_tag.addItems(tags)
        
    def set_current_tag(self):
        current_type = self.combobox_type.currentText()
        current_tag = self.combobox_tag.currentText()

        if current_tag not in self.casting_data[current_type]:
            return
        for asset in self.casting_data[current_type][current_tag]:        
            current_item = swidgets.add_treewidget_item(
                self.treewidget, asset, icon='asset', foreground=None)
            caption, subfield, version = asset.split('|')          
            version_data = self.spipe.get_version_data(caption, subfield, version)
            current_item.setStatusTip(0, str(version_data))
            
    def current_asset_select(self, *args):
        if not args[0]:
            return
        contents = args[0].statusTip(0)
        if not contents:
            self.comp_catalogue.setup_default()
            return
        contents = ast.literal_eval(contents)
        self.comp_catalogue.set_catalogue(**contents)
    
    def get_castingsheet_path(self):
        show_path = self.environ.get_show_path() 
        castingsheet_path = resource.getSpecificPreset(show_path, 'castingsheet')
        if not os.path.isfile(castingsheet_path):
            return None
        return castingsheet_path

    def has_casting_preset(self):
        castingsheet_path = self.get_castingsheet_path()        
        if os.path.isfile(castingsheet_path):
            return True
        return False    
        
    def open(self):
        print self.size()
        

    def get_widget_data(self):
        casting_data = {}        
        current_type = self.combobox_type.currentText()
        current_tag = self.combobox_tag.currentText()        
        widget_item = self.treewidget.invisibleRootItem()
        for x in range(widget_item.childCount()):
            contents = widget_item.child(x).statusTip(0)
            if not contents:
                continue
            contents = ast.literal_eval(contents) 
            name = widget_item.child(x).text(0)
            current_source = self.find_extactor_inputs(contents)
            casting_data.setdefault(contents['subfield'], {})
            casting_data[contents['subfield']].setdefault(name, current_source)
        input_data = {
            'pipe': self.pipe,
            'caption': '%s|%s'%(current_type, current_tag), 
            'subfield': self.subfield, 
            'type': current_type, 
            'tag': current_tag, 
            'dependency': None, 
            'version': None,             
            'modified': None,
            'location': None,
            'description': None, 
            'user': getpass.getuser()
            }
        input_data['casting_data'] = casting_data
        return input_data  
    
    def find_extactor_inputs(self, input_data):  
        inputs = studioInputs.Inputs(self.upstrem_pipe)
        extractor_keys = inputs.get_puppet_extractor_keys()
        subfield = input_data['subfield']
        if subfield not in extractor_keys:
            return None
        if extractor_keys[subfield] not in input_data:
            return None
        current_source = input_data[extractor_keys[subfield]]
        if not current_source:
            return None
        return current_source[0]
          

    def build(self):        
        widget_data = self.get_widget_data()
        if not widget_data:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty inputs!...', QtWidgets.QMessageBox.Ok)
            return
        print '\n#header: inputs'
        print json.dumps(widget_data, indent=4)      
        pull = studioPull.Pull(application=self.application, subfield=self.subfield)
        modules = pull.get_creators()
        valids = {}
        if not modules:            
            valids = {False: ['not found any creators']}
        for index in modules:
            valid, message = pull.do_pull(modules[index], **widget_data)
            valids.setdefault(valid, []).append(message)
        if False in valids:
            QtWidgets.QMessageBox.critical(
                self, 'critical', '\n'.join(valids[False]), QtWidgets.QMessageBox.Ok)
            return
        QtWidgets.QMessageBox.information(
            self, 'Success', 'Done!...', QtWidgets.QMessageBox.Ok)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True, application='maya')
    window.show()
    sys.exit(app.exec_())         
