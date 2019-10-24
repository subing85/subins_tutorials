import os
import sys
import json
import warnings

from PySide import QtCore
from PySide import QtGui
from functools import partial

from studio_usd_pipe import resources
from studio_usd_pipe.core import inputs
from studio_usd_pipe.utils import platforms
from studio_usd_pipe.resources.ui import main_ui
from studio_usd_pipe.resources.ui import _publish_ui


class Connect(main_ui.Window):
    
    def __init__(self, parent=None, **kwargs):
        super(Connect, self).__init__(**kwargs)
        self.publish = _publish_ui.Window(parent=self.splitter)
        self.resize(750, 450)
        
        # self.setWindowState(QtCore.Qt.WindowMaximized)
        # self.setWindowState(QtCore.Qt.WindowMinimized)

        self.splitter.setSizes([200, 30])
        print self.splitter.size()
        
        self.treewidget.itemClicked.connect(
             partial(self.load_current_category, self.treewidget)) 
        
        self.publish.button_publish.clicked.connect(self.start_publish)        
        
        
    def load_current_category(self, treewidget, *args):
        if not treewidget.selectedItems():
            warnings.warn(
                'Not found any selection\nSelect the item and try',
                Warning
            )
            return
        
        parent_item = treewidget.selectedItems()[-1]    
        if treewidget.selectedItems()[-1].parent():
            parent_item = treewidget.selectedItems()[-1].parent()

            self.publish.groupbox_label.setTitle(
                self.treewidget.selectedItems()[-1].text(0))
            
                    
        self.publish.combobox_category.clear()
        self.publish.combobox_tag.clear()

        parent = parent_item.statusTip(0).encode()
        input = inputs.Connect('subfield')
        input.get(parent)            
        self.publish.combobox_category.addItems(input.keys)
        self.publish.combobox_category.setToolTip(parent)
        
        input = inputs.Connect('tag')
        input.get(parent)            
        self.publish.combobox_tag.addItems(input.keys)        
        self.publish.combobox_tag.setToolTip(parent)
                
            
    
    def start_publish(self, **kwargs):        
        input_data = self.collect_publish_data()       

        
    def collect_publish_data(self):
        input_data = {
            'parent': self.publish.combobox_category.toolTip(),
            'name': self.treewidget.selectedItems()[-1].text(0),
            'path': self.publish.label_label.toolTip(),
            'thumbnail': self.publish.button_thumbnail.toolTip(),            
            'description': self.publish.textedit_description.toPlainText(),
            'category': self.publish.combobox_category.currentText(),
            'tag': self.publish.combobox_tag.currentText(),
            'version': self.publish.label_current_version.text()
            }
        print json.dumps(input_data, indent=4)
        return input_data
        
        #=======================================================================
        # self._data['parent'] =  ''     
        # self.label_label
        # self.button_thumbnail
        # self.textedit_description
        # self.combobox_category
        # self.combobox_tag
        # self.label_current_version
        #=======================================================================
        
  
                  
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Connect(parent=None, child='publish')
    window.show()
    sys.exit(app.exec_())

