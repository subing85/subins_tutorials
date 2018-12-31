import os
import sys
from __builtin__ import super


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial

from maya import OpenMaya
from maya import OpenMayaAnim

from smartDeform.modules import cluster
from smartDeform.modules import skincluster
from smartDeform.modules import studioMaya

reload(studioMaya)
reload(cluster)
reload(skincluster)



class Mirror(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Mirror, self).__init__(parent=None)
        self.setupUi()
        
        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()
        self.my_maya = studioMaya.Maya()        

    def setupUi(self):
        self.setObjectName('mirror')
        self.resize(300, 100)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)
        
        mirrors= ['Cluster', 'Skincluster']
        
        for each_mirror in mirrors:

            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox')
            self.groupbox.setTitle('%s Mirror' % each_mirror)
            self.verticallayout.addWidget(self.groupbox)
    
            self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
            self.horizontallayout.setObjectName('horizontallayout_%s' % each_mirror)
            self.horizontallayout.setSpacing(10)
            self.horizontallayout.setContentsMargins(20, 10, 10, 10)
    
            self.radiobutton_x = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_x.setObjectName('radiobutton_x_%s' % each_mirror)
            self.radiobutton_x.setText('X')
            self.radiobutton_x.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_x)
    
            self.radiobutton_y = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_y.setObjectName('radiobutton_y_%s' % each_mirror)
            self.radiobutton_y.setText('Y')
            self.radiobutton_y.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_y)
    
            self.radiobutton_z = QtGui.QRadioButton(self.groupbox)
            self.radiobutton_z.setObjectName('radiobutton_z_%s' % each_mirror)
            self.radiobutton_z.setText('Z')
            self.radiobutton_z.setMinimumSize(QtCore.QSize(0, 10))
            self.horizontallayout.addWidget(self.radiobutton_z)
    
            self.button_mirror = QtGui.QPushButton(self.groupbox)
            self.button_mirror.setObjectName('button_mirror_%s' % each_mirror)
            self.button_mirror.setText('Mirror')
            self.horizontallayout.addWidget(self.button_mirror)            
            
            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox_%s' % each_mirror)
            self.groupbox.setTitle(each_mirror)
            self.verticallayout.addWidget(self.groupbox)
            
            self.horizontallayout = QtGui.QHBoxLayout(self.groupbox)
            self.horizontallayout.setObjectName('horizontallayout_%s' % each_mirror)
            self.horizontallayout.setSpacing(1)
            self.horizontallayout.setContentsMargins(1, 1, 1, 1)
    
            self.button_combine = QtGui.QPushButton(self.groupbox)
            self.button_combine.setObjectName('button_combine_%s' % each_mirror)
            self.button_combine.setText('Combine %s' % each_mirror)
            self.horizontallayout.addWidget(self.button_combine)
            
            self.button_combine.clicked.connect(partial (self.combine, each_mirror.lower()))
    
            self.button_copy = QtGui.QPushButton(self.groupbox)
            self.button_copy.setObjectName('button_copy_%s' % each_mirror)
            self.button_copy.setText('Copy %s' % each_mirror)
            self.horizontallayout.addWidget(self.button_copy)   
            
            self.button_copy.clicked.connect(partial (self.copy, each_mirror.lower()))
                     
            spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
            self.verticallayout.addItem(spacerItem)            

    def setCurrentButton(self, item):
        self.current_item = item
        return self.current_item
    
    
    def combine(self, tag):
        
        from smartDeform.modules import cluster
        from smartDeform.modules import skincluster
        from smartDeform.modules import studioMaya
        
        reload(studioMaya)
        reload(cluster)
        reload(skincluster)
        
        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()
        self.my_maya = studioMaya.Maya()        
        
        
        selections = self.my_maya.getSelectedDagPaths()

        inputs = {}        

        for index in range(selections.length()):            
            if not selections[index].isValid():
                continue            
            tag = None
            if self.my_maya.hasJoint(selections[index]):
                tag = 'skincluster'        
            elif self.my_maya.hasCluster(selections[index]):
                tag = 'cluster'                            
            inputs.setdefault(tag, []).append(selections[index])
 
        if None in inputs:
            OpenMaya.MGlobal.displayError(
                '#Unwanted nodes are found in your selection')
            return
 
        if inputs.keys().count(inputs.keys()[0]) != len(inputs.keys()):
            OpenMaya.MGlobal.displayError(
                '#You selected differ types of nodes\nselect cluster handless either joints')
            return
                
        deformer_dag_paths = inputs.values()[0]
                
        if tag=='cluster':           
            self.cluster.combine_weights(deformer_dag_paths)
        
        if tag=='skincluster':            
            self.skincluster.combine_weights(deformer_dag_paths)


    
    def copy(self, tag):
        from smartDeform.modules import cluster
        from smartDeform.modules import skincluster
        from smartDeform.modules import studioMaya
        
        reload(studioMaya)
        reload(cluster)
        reload(skincluster)
        
        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()
        self.my_maya = studioMaya.Maya()       
        
        selections = self.my_maya.getSelectedDagPaths()
        
        targets_deformer = OpenMaya.MDagPathArray()            
        for index in range (1, selections.length()):
            targets_deformer.append(selections[index])        
        
        
        if tag=='cluster':     
            self.cluster.copy_weights(selections[0], targets_deformer)

        if tag=='skincluster':
            self.skincluster.copy_weights(selections[0], targets_deformer)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Mirror(parent=None)
    window.show()
    sys.exit(app.exec_())
