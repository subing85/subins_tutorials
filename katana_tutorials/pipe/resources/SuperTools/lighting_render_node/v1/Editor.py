# Editor.py - the Qt4 UI (this is only imported in the interactive GUI,
# not in batch or scripting modes).

import UI4

from PyQt4 import QtGui


class LightingRenderEditor(QtGui.QWidget):
    
    def __init__(self, parent, node):
        QtGui.QWidget.__init__(self, parent)
        self.knode = node
        self.parameter_policy = UI4.FormMaster.CreateParameterPolicy
        self.widget_factory = UI4.FormMaster.KatanaFactory.ParameterWidgetFactory
        self.main_layout = QtGui.QVBoxLayout()
        self.setLayout(self.main_layout)        
        parameter = self.knode.getParameter('studio_pipe') 
        policy = self.parameter_policy(None, parameter)
        widget = self.widget_factory.buildWidget(self, policy)
        self.main_layout.addWidget(widget)

    def add_widget(self):
        parameter = self.knode.getParameter('studio_pipe') 
        policy = self.parameter_policy(None, parameter)
        widget = self.widget_factory.buildWidget(self, policy)
        self.main_layout.addWidget(widget)
          
