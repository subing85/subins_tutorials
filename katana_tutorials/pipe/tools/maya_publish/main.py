import os
import sys
import json
import resources

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from functools import partial

from core import versions
from tools.maya_publish import publish
reload(publish)
reload(versions)


class MayaPublish(QtWidgets.QWidget):
    
    def __init__(self, parent=None, **kwargs):
        '''
        :example
            from tools.template_publishs import main
            window = main.TemplatePublish(parent=None)
            window.show()
        '''        
        super(MayaPublish, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self.template_path = resources.get_template_path()
        self.align_right = QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter  
        self.setup_ui()
        self.set_current_pipe(0)        
        self.set_current_type(0)
        self.set_default()
   
    def setup_ui(self):
        self.setObjectName('maya_publishs')
        self.resize(380, 280)
        self.setStyleSheet('font: 14pt')
        self.setWindowTitle('Maya Publishs')          
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName("verticalLayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.verticallayout.addLayout(self.gridlayout) 
        self.label_pipe = QtWidgets.QLabel(self)
        self.label_pipe.setObjectName('label_pipe')
        self.label_pipe.setText('pipe')      
        self.label_pipe.setAlignment(self.align_right) 
        self.gridlayout.addWidget(self.label_pipe, 0, 0, 1, 1)
        self.combobox_pipe = QtWidgets.QComboBox(self)
        self.combobox_pipe.setObjectName('combobox_pipe')
        self.combobox_pipe.addItems(['asset', 'scene'])          
        self.combobox_pipe.currentIndexChanged.connect(self.set_current_pipe)
        self.gridlayout.addWidget(self.combobox_pipe, 0, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setObjectName('label_name')
        self.label_name.setText('name') 
        self.label_name.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_name, 1, 0, 1, 1)
        self.lineedit_name = QtWidgets.QLineEdit(self)
        self.lineedit_name.setObjectName('combobox_versions')
        self.lineedit_name.textEdited.connect(self.set_name_change)
        self.gridlayout.addWidget(self.lineedit_name, 1, 1, 1, 1)
        self.label_category = QtWidgets.QLabel(self)
        self.label_category.setObjectName('label_category')
        self.label_category.setText('category') 
        self.label_category.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_category, 2, 0, 1, 1)
        self.combobox_category = QtWidgets.QComboBox(self)
        self.combobox_category.setObjectName('combobox_category')
        self.combobox_category.addItems(['character', 'prop', 'set', 'camera'])
        self.gridlayout.addWidget(self.combobox_category, 2, 1, 1, 1) 
        self.label_type = QtWidgets.QLabel(self)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('type') 
        self.label_type.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_type, 3, 0, 1, 1)
        self.combobox_type = QtWidgets.QComboBox(self)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.addItems(['model', 'puppet'])
        self.combobox_type.currentIndexChanged.connect(self.set_current_type)
        self.gridlayout.addWidget(self.combobox_type, 3, 1, 1, 1)   
        self.label_scene = QtWidgets.QLabel(self)
        self.label_scene.setObjectName('label_scene')
        self.label_scene.setText('scene') 
        self.label_scene.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_scene, 4, 0, 1, 1)
        self.combobox_scene = QtWidgets.QComboBox(self)
        self.combobox_scene.setObjectName('combobox_scene')
        self.combobox_scene.addItems(['layout', 'animation'])        
        self.gridlayout.addWidget(self.combobox_scene, 4, 1, 1, 1) 
        self.label_sequence = QtWidgets.QLabel(self)
        self.label_sequence.setObjectName('label_sequence')
        self.label_sequence.setText('sequence') 
        self.label_sequence.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_sequence, 5, 0, 1, 1)
        self.lineedit_sequence = QtWidgets.QLineEdit(self)
        self.lineedit_sequence.setObjectName('lineedit_sequence')
        self.lineedit_sequence.textEdited.connect(self.set_name_change)        
        self.gridlayout.addWidget(self.lineedit_sequence, 5, 1, 1, 1)
        self.label_shot = QtWidgets.QLabel(self)
        self.label_shot.setObjectName('label_shot')
        self.label_shot.setText('shot') 
        self.label_shot.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_shot, 6, 0, 1, 1)
        self.label_shot.setText('shot_1001')
        self.lineedit_shot = QtWidgets.QLineEdit(self)
        self.lineedit_shot.setObjectName('lineedit_shot')
        self.lineedit_sequence.textEdited.connect(self.set_name_change)        
        self.gridlayout.addWidget(self.lineedit_shot, 6, 1, 1, 1)                   
        self.label_version = QtWidgets.QLabel(self)
        self.label_version.setObjectName('label_version')
        self.label_version.setText('version') 
        self.label_version.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_version, 7, 0, 1, 1)
        self.combobox_version = QtWidgets.QComboBox(self)
        self.combobox_version.setObjectName('combobox_version')
        self.combobox_version.addItems(['major', 'minor', 'patch'])
        self.combobox_version.currentIndexChanged.connect(self.set_current_versions)
        self.gridlayout.addWidget(self.combobox_version, 7, 1, 1, 1) 
        self.label_latestversion = QtWidgets.QLabel(self)
        self.label_latestversion.setObjectName('label_latestversion')
        self.label_latestversion.setText('latest_version') 
        self.label_latestversion.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_latestversion, 8, 0, 1, 1)
        self.lineedit_latestversion = QtWidgets.QLineEdit(self)
        self.lineedit_latestversion.setObjectName('lineedit_latestversion')
        self.lineedit_latestversion.setText('0.0.0')
        self.lineedit_latestversion.setEnabled(False)
        self.gridlayout.addWidget(self.lineedit_latestversion, 8, 1, 1, 1) 
        self.label_nextversion = QtWidgets.QLabel(self)
        self.label_nextversion.setObjectName('label_nextversion')
        self.label_nextversion.setText('next_version') 
        self.label_nextversion.setAlignment(self.align_right)
        self.label_nextversion.setStyleSheet('color: rgb(255, 128, 0)')
        self.gridlayout.addWidget(self.label_nextversion, 9, 0, 1, 1)
        self.lineedit_nextversion = QtWidgets.QLineEdit(self)
        self.lineedit_nextversion.setObjectName('lineedit_nextversion')
        self.lineedit_nextversion.setText('0.0.0')
        self.lineedit_nextversion.setEnabled(False)
        self.lineedit_nextversion.setStyleSheet('color: rgb(255, 128, 0)')        
        self.gridlayout.addWidget(self.lineedit_nextversion, 9, 1, 1, 1) 
        self.label_model = QtWidgets.QLabel(self)
        self.label_model.setObjectName('label_model')
        self.label_model.setText('model') 
        self.label_model.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_model, 10, 0, 1, 1)
        self.lineedit_model = QtWidgets.QLineEdit(self)
        self.lineedit_model.setObjectName('lineedit_model')
        self.lineedit_model.setText('0.0.0')
        self.gridlayout.addWidget(self.lineedit_model, 10, 1, 1, 1)
        self.label_lookdev = QtWidgets.QLabel(self)
        self.label_lookdev.setObjectName('label_lookdev')
        self.label_lookdev.setText('lookdev') 
        self.label_lookdev.setAlignment(self.align_right)  
        self.gridlayout.addWidget(self.label_lookdev, 11, 0, 1, 1)
        self.lineedit_lookdev = QtWidgets.QLineEdit(self)
        self.lineedit_lookdev.setObjectName('lineedit_lookdev')
        self.lineedit_lookdev.setText('0.0.0')
        self.gridlayout.addWidget(self.lineedit_lookdev, 11, 1, 1, 1)        
        self.button_asset = QtWidgets.QPushButton(self)
        self.button_asset.setObjectName('button_asset')
        self.button_asset.setText('publish')
        self.button_asset.clicked.connect(partial(self.set_publish, None))
        self.gridlayout.addWidget(self.button_asset, 12, 1, 1, 1)
    
    def set_default(self):
        self.lineedit_name.setText('batman')       
        self.lineedit_sequence.setText('101')
        self.lineedit_shot.setText('1001')        
        
    def set_current_pipe(self, index):
        asset_widgets = [
            self.label_name,
            self.lineedit_name,
            self.label_category,
            self.combobox_category,
            self.label_type,
            self.combobox_type,
            self.label_model,
            self.lineedit_model,
            self.label_lookdev,
            self.lineedit_lookdev
            ]
        scene_widgets = [           
            self.label_scene,
            self.combobox_scene,
            self.label_sequence,
            self.lineedit_sequence,
            self.label_shot,
            self.lineedit_shot
            ]
        common_widget = [  
            self.label_version,
            self.combobox_version,
            self.label_latestversion,
            self.lineedit_latestversion,
            self.label_nextversion,
            self.lineedit_nextversion,
            ]
        all_widgets = asset_widgets + scene_widgets
        for asset_widget in all_widgets:
            asset_widget.hide()        
        if index == 0:
            for asset_widget in asset_widgets:
                asset_widget.show()
        if index == 1:
            for scene_widget in scene_widgets:
                scene_widget.show()                
        self.set_current_versions()
                
    def set_current_type(self, index):        
        if index == 0:
            self.lineedit_lookdev.setText('None')
            self.lineedit_lookdev.setEnabled(False)
        if index == 1:
            self.set_puppet_depnendency()
        self.set_current_versions()
        
    def set_puppet_depnendency(self):
        category = str(self.combobox_category.currentText())
        name = str(self.lineedit_name.text())
        model = publish.get_current_version(name)
        message = None
        if not model:
            message = 'model dependency missing'
        model_depnendency = publish.get_lookdev_model_depnendency(category, name)
        if model not in model_depnendency:
            message = 'current model lookdev does not published'
        if message:
            self.lineedit_lookdev.setEnabled(True)
            QtWidgets.QMessageBox.warning(
                self, 'warning', message, QtWidgets.QMessageBox.Ok)
            return        
        self.lineedit_model.setText(model)
        self.lineedit_model.setEnabled(False)
        self.lineedit_lookdev.setText(model_depnendency[model][0])
        self.lineedit_lookdev.setEnabled(False)
        
    def set_name_change(self):
        index = self.combobox_type.currentIndex()
        self.set_current_type(index)
        
    def set_current_versions(self):
        publish_path, pipe = self.get_publish_path()
        version_type = str(self.combobox_version.currentText())
        temp_version = versions.get_latest_version(publish_path, pipe)
        current_versions = str(self.combobox_version.currentText())
        version_index = versions.PATTERN[current_versions]
        latest_version = 'None'        
        if temp_version:
            latest_version = temp_version    
        next_version = versions.get_next_version(version_index, temp_version)
        self.lineedit_latestversion.setText(latest_version)
        self.lineedit_nextversion.setText(next_version)
        
    def get_inputs(self):
        pipe = str(self.combobox_pipe.currentText())
        show_path = resources.get_show_path()
        next_version = str(self.lineedit_nextversion.text())
        model = str(self.lineedit_model.text())
        lookdev = str(self.lineedit_lookdev.text())
        inputs = {
            'version': next_version,
            'model': model,
            'lookdev': lookdev            
            }
        if pipe == 'asset':
            inputs['category'] = str(self.combobox_category.currentText())
            inputs['type'] = str(self.combobox_type.currentText())
            inputs['name'] = str(self.lineedit_name.text())

        elif pipe == 'scene':
            inputs['scene'] = str(self.combobox_scene.currentText())
            inputs['sequence'] = str(self.lineedit_sequence.text())
            inputs['shot'] = str(self.lineedit_shot.text())
        return pipe, inputs
    
    def get_publish_path(self):
        pipe, inputs = self.get_inputs()
        show_path = resources.get_show_path()
        if pipe == 'asset':
            publish_path = os.path.join(
                show_path,
                'asset',
                inputs['category'],
                inputs['name']
                )
            return publish_path, inputs['type']
        if pipe == 'scene':
            category = str(self.combobox_category.currentText())
            sequence = str(self.lineedit_sequence.text())
            shot = str(self.lineedit_shot.text())
            scene = str(self.combobox_scene.currentText())
            publish_path = os.path.join(
                show_path,
                'scene',
                inputs['sequence'],
                inputs['shot']
                )
            return publish_path, inputs['scene']
        return None, None
    
    def set_publish(self, *args):
        pipe, inputs = self.get_inputs()
        messages = None
        if pipe == 'asset':            
            publish.asset_publish(
                inputs['name'],
                inputs['category'],
                inputs['type'],
                inputs['version'],
                inputs['model'],
                inputs['lookdev'],
                )
            messages = [
                pipe,
                inputs['name'],
                inputs['category'],
                inputs['type'],
                inputs['version'],
                ]
        if pipe == 'scene':
            publish.scene_publish(
                inputs['sequence'],
                inputs['shot'],
                inputs['scene'],
                inputs['version']
                )
            messages = [
                pipe,
                inputs['sequence'],
                inputs['shot'],
                inputs['scene'],
                inputs['version']                
                ]            
        QtWidgets.QMessageBox.information(
            self, 'success', '\n'.join(messages), QtWidgets.QMessageBox.Ok)          
        self.set_current_versions()        
        print json.dumps(inputs, indent=4)
        print 'done!...'   
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MayaPublish(parent=None)
    window.show()
    sys.exit(app.exec_()) 
