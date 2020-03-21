import os
import sys
import ast
import copy
import json
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial
from distutils import version

from studio_usd_pipe import resource
from studio_usd_pipe.core import widgets
from studio_usd_pipe.core import configure
from studio_usd_pipe.core import preferences
from studio_usd_pipe.api import studioPublish

reload(studioPublish)


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None, mode=None):  
        super(Window, self).__init__(parent)
        # self.setParent(parent)
        self.mode = mode        
        self.title = 'Asset Publish/Push'
        self.width = 1000
        self.height = 570
        self.version, self.label = self.set_tool_context()
        self.pub = studioPublish.Publish(self.mode)             
        self.pref = preferences.Preferences()        
        self.setup_ui()
        self.set_current()
        self.load_date()
        
    def setup_ui(self):
        self.setObjectName('mainwindow_pull')
        self.setWindowTitle('{} ({} {})'.format(self.title, self.label, self.version)) 
        self.resize(self.width, self.height)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        
        self.verticallayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        # self.verticallayout.setSpacing(10)
        # self.verticallayout.setContentsMargins(5, 5, 5, 5)  
        
        self.horizontallayout = QtWidgets.QHBoxLayout()
        # self.horizontallayout.setSpacing(10)
        # self.horizontallayout.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout.setObjectName('horizontallayout')
        self.verticallayout.addLayout(self.horizontallayout)
        
        self.button_logo, self.button_show = widgets.set_header(
            self.horizontallayout, show_icon=None) 
        
        #=======================================================================
        # self.groupbox_bar = QtWidgets.QGroupBox(self)
        # self.groupbox_bar.setObjectName('groupbox_bar')
        # self.groupbox_bar.setMinimumSize(QtCore.QSize(0, 40))
        # self.groupbox_bar.setMaximumSize(QtCore.QSize(16777215, 40))        
        # self.verticallayout.addWidget(self.groupbox_bar)
        # self.horizontallayout_bar = QtWidgets.QHBoxLayout(self.groupbox_bar)
        # self.horizontallayout_bar.setObjectName('horizontallayout_bar')        
        # self.horizontallayout_bar.setSpacing(0)
        # self.horizontallayout_bar.setContentsMargins(0, 0, 0, 0)
        # self.pushButton_2 = QtWidgets.QPushButton(self)
        # self.pushButton_2.setObjectName('pushButton_2')
        # self.pushButton_2.setMinimumSize(QtCore.QSize(100, 35))
        # self.pushButton_2.setMaximumSize(QtCore.QSize(100, 35))        
        # self.horizontallayout_bar.addWidget(self.pushButton_2)
        #=======================================================================
        
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setObjectName('horizontallayout_input')        
        self.horizontallayout_input.setSpacing(10)
        self.horizontallayout_input.setContentsMargins(5, 5, 5, 5)   
        self.verticallayout.addLayout(self.horizontallayout_input)
             
        self.treewidget = QtWidgets.QTreeWidget(self)
        self.treewidget.setObjectName('treewidget')
        # self.treewidget.headerItem().setText(0, "No")
        self.treewidget.headerItem().setText(0, "Name")
        self.treewidget.headerItem().setText(1, "Location")
        self.treewidget.header().resizeSection (0, 250)
        self.treewidget.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.itemClicked.connect (self.current_item_select)
                
        self.horizontallayout_input.addWidget(self.treewidget)
        
        self.groupbox_data = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_data.setObjectName('groupbox_data')
        self.horizontallayout_input.addWidget(self.groupbox_data)
        
        self.gridlayout_data = QtWidgets.QGridLayout(self.groupbox_data)
        self.gridlayout_data.setObjectName('gridlayout_data')
        self.gridlayout_data.setHorizontalSpacing(10)
        self.gridlayout_data.setContentsMargins(10, 20, 10, 10)
        
        self.label_captions = QtWidgets.QLabel(self.groupbox_data)
        self.label_captions.setObjectName('label_captions')
        self.label_captions.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_captions.setText('Caption')
        self.gridlayout_data.addWidget(self.label_captions, 0, 0, 1, 1)        
        
        self.label_caption = QtWidgets.QLabel(self.groupbox_data)
        self.label_caption.setObjectName('label_caption')
        self.gridlayout_data.addWidget(self.label_caption, 0, 1, 1, 1)        
        
        self.label_tags = QtWidgets.QLabel(self.groupbox_data)
        self.label_tags.setObjectName('label_tags')
        self.label_tags.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_tags.setText('Tag')
        self.gridlayout_data.addWidget(self.label_tags, 1, 0, 1, 1)        
        
        self.label_tag = QtWidgets.QLabel(self.groupbox_data)
        self.label_tag.setObjectName('label_tag')
        self.gridlayout_data.addWidget(self.label_tag, 1, 1, 1, 1)     
                
        self.label_types = QtWidgets.QLabel(self.groupbox_data)
        self.label_types.setObjectName('label_types')
        self.label_types.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_types.setText('Type')
        self.gridlayout_data.addWidget(self.label_types, 2, 0, 1, 1)        
        
        self.label_type = QtWidgets.QLabel(self.groupbox_data)
        self.label_type.setObjectName('label_type')
        self.gridlayout_data.addWidget(self.label_type, 2, 1, 1, 1)  
        
        self.label_users = QtWidgets.QLabel(self.groupbox_data)
        self.label_users.setObjectName('label_users')
        self.label_users.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_users.setText('Owner')
        self.gridlayout_data.addWidget(self.label_users, 3, 0, 1, 1)        
        
        self.label_user = QtWidgets.QLabel(self.groupbox_data)
        self.label_user.setObjectName('label_user')           
        self.gridlayout_data.addWidget(self.label_user, 3, 1, 1, 1) 
        
        self.label_dates = QtWidgets.QLabel(self.groupbox_data)
        self.label_dates.setObjectName('label_dates')
        self.label_dates.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_dates.setText('Date')
        self.gridlayout_data.addWidget(self.label_dates, 4, 0, 1, 1)        
        
        self.label_date = QtWidgets.QLabel(self.groupbox_data)
        self.label_date.setObjectName('label_date')
        self.gridlayout_data.addWidget(self.label_date, 4, 1, 1, 1)                                    
        
        self.label_description = QtWidgets.QLabel(self.groupbox_data)
        self.label_description.setObjectName("label_description")
        self.label_description.setText('Description')
        self.gridlayout_data.addWidget(self.label_description, 5, 0, 1, 1)        

        self.textedit_description = QtWidgets.QTextEdit(self.groupbox_data)
        self.textedit_description.setObjectName("textedit_description")
        self.textedit_description.setReadOnly(True)
        self.textedit_description.setMinimumSize(QtCore.QSize(256, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(256, 90))
        self.gridlayout_data.addWidget(self.textedit_description, 6, 0, 1, 2)   
   
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox_data)
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.gridlayout_data.addWidget(self.button_thumbnail, 7, 0, 1, 2)  

        thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
         
        widgets.image_to_button(
            self.button_thumbnail, 256, 180, path=thumbnail_icon)
                
        spaceritem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout_data.addItem(spaceritem, 8, 0, 1, 1)        

    def set_tool_context(self):
        config = configure.Configure()
        config.tool()
        return config.version, config.pretty          
        
    def set_current(self):
        bundle_data = self.pref.get()   
        if not bundle_data:
            warnings.warn('not found show icon', Warning)
            return        
        size = self.button_show.minimumSize()
        widgets.image_to_button(
            self.button_show, size.width(), size.height(), path=bundle_data['show_icon'])
    
    def load_date(self):
        pub_data = self.pub.get()
        valid_subfields = self.pub.valid_modes[self.mode]['subfield']
        for caption, contents in pub_data.items():
            version_contents = contents[contents.keys()[0]]
            tag = version_contents[version_contents.keys()[0]]['tag']
            caption_item = self.add_treewidget_item(
                self.treewidget, caption, icon=tag, path=None)
            for subfield in valid_subfields:                
                if subfield not in contents:
                    continue
                subfield_item = self.add_treewidget_item(caption_item, subfield, icon=subfield)
                versions = sorted(contents[subfield].keys(), key=version.StrictVersion)
                versions.reverse()
                for each in versions:
                    version_item = self.add_treewidget_item(
                        subfield_item, each, icon='version', path=contents[subfield][each]['path'])
                    # item_data.setdefault(version_item, contents[subfield][each])
                    ver_contents = copy.deepcopy(contents[subfield][each])
                    ver_contents['hierarchy'] = '{}|{}|{}'.format(caption, subfield, each)
                    version_item.setStatusTip(0, str(ver_contents))
    
    def add_treewidget_item(self, parent, label, icon=None, path=None):
        item = QtWidgets.QTreeWidgetItem (parent)
        item.setText (0, label)

        if path:
            item.setText (1, path)  
        
        if icon:      
            icon_path = os.path.join(resource.getIconPath(), '{}.png'.format(icon))
            icon = QtGui.QIcon ()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
            item.setIcon (0, icon)
        return item        

    def current_item_select(self, *args):
        self.clear_display() 
        current_item = args[0]        
        
        contents = current_item.statusTip(0)
        if not contents:
            return
        contents = ast.literal_eval(contents)
        
        self.label_caption.setText(contents['caption'])
        self.label_tag.setText(contents['tag'])
        self.label_type.setText(contents['type'])
        self.label_user.setText(contents['user'])
        self.label_date.setText(contents['date'])
        
        caption, subfield, version = contents['hierarchy'].split('|')
        more_contents = self.pub.get_more_data(caption, subfield, version)
        self.textedit_description.setText(more_contents['description'])
        size = self.button_thumbnail.minimumSize()
        
        thumbnail_icon = more_contents['thumbnail'][0]
        if not os.path.isfile(thumbnail_icon):
            thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        
        widgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)
    
    def clear_display(self):
        self.label_caption.clear()
        self.label_tag.clear()
        self.label_type.clear()
        self.label_user.clear()
        self.label_date.clear()
        self.textedit_description.clear()
        size = self.button_thumbnail.minimumSize()
        thumbnail_icon = os.path.join(resource.getIconPath(), 'unknown.png')
        widgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=thumbnail_icon)        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, mode='assets')
    window.show()
    sys.exit(app.exec_())        
