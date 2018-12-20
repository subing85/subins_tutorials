import os
import sys
import warnings

from pprint import pprint

path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from maya import OpenMaya
from functools import partial
from smartDeform import resources
from smartDeform.utils import read
from smartDeform.utils import generic
from smartDeform.modules import studioMaya
reload(studioMaya)


class Geometry(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Geometry, self).__init__(parent=None)
        self.current_item = None
        self.icon_path = resources.getIconPath() 
        
        self.source_path = resources.getInputPath('source_geometry')
        self.target_path = resources.getInputPath('target_geometry')
        
        read_source_data = read.Data(file=self.source_path)
        self.source_data = read_source_data.getData()
        
        read_target_data = read.Data(file=self.target_path)
        self.target_data = read_target_data.getData()
                
        self.my_maya = studioMaya.Maya()
        self.deformer_index = {}       
        self.setupUi()

    def setupUi(self):
        self.setObjectName('geometry')
        self.resize(300, 400)
        
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout_')
        self.verticallayout.setSpacing(5)
        self.verticallayout.setContentsMargins(5, 10, 5, 5)       
        
        self.horizontallayout = QtGui.QHBoxLayout(None)
        self.horizontallayout.setObjectName('horizontalLayout')
        self.horizontallayout.setSpacing(5)
        self.horizontallayout.setContentsMargins(0, 0, 0, 0)
        self.verticallayout.addLayout(self.horizontallayout) 
              
        titles = ['Source', 'Target']
        index = 0
        
        for each_data in [self.source_data, self.target_data]:            
            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox_%s' % titles[index])
            self.groupbox.setTitle(titles[index])
            self.horizontallayout.addWidget(self.groupbox) 
            
            self.verticallayout_geometry = QtGui.QVBoxLayout(self.groupbox)
            self.verticallayout_geometry.setObjectName('verticallayout_%s' % titles[index])
            self.verticallayout_geometry.setSpacing(5)
            self.verticallayout_geometry.setContentsMargins(0, 0, 0, 0)
                 
            self.horizontallayout_inputs = QtGui.QHBoxLayout(None)
            self.horizontallayout_inputs.setObjectName('horizontallayout_inputs_%s' % titles[index])
            self.horizontallayout_inputs.setSpacing(1)
            self.horizontallayout_inputs.setContentsMargins(0, 0, 0, 0)
            self.verticallayout_geometry.addLayout(self.horizontallayout_inputs)                 
                 
            self.lineedit = QtGui.QLineEdit(self.groupbox)
            self.lineedit.setObjectName('lineedit_%s' % titles[index])
            self.lineedit.setReadOnly(True)
            self.lineedit.setToolTip('%s Geometry' % titles[index])            
            self.horizontallayout_inputs.addWidget(self.lineedit)
     
            self.button = QtGui.QPushButton(self.groupbox)
            self.button.setObjectName('button_%s' % titles[index])
            self.button.setMinimumSize(QtCore.QSize(25, 25))
            self.button.setMaximumSize(QtCore.QSize(25, 25))
            self.button.setText('+')
            self.button.setToolTip('Add %s Geometry' % titles[index])          
            self.horizontallayout_inputs.addWidget(self.button)
            self.button.clicked.connect(self.add_object)        
             
            self.combobox = QtGui.QComboBox(self.groupbox)
            self.combobox.setObjectName('combobox_%s' % titles[index])       
            self.combobox.setToolTip('%s Deformers' % titles[index])     
            self.verticallayout_geometry.addWidget(self.combobox)                 
                 
            none_icon_path = os.path.join(self.icon_path, 'none.png')
            none_icon = QtGui.QIcon()
            none_icon.addPixmap(QtGui.QPixmap(none_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.combobox.addItem(none_icon, 'None')           
            sort_data = generic.sortDictionary(each_data['data'])
            print each_data
            self.deformer_index = {}
            
            ing = 1    
            for x, items in sort_data.items():
                for each in items:                
                    current_icon_path = os.path.join(self.icon_path, '%s.png' % each)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(current_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)                        
                    self.combobox.addItem(icon, each_data['data'][each]['label'])
                    self.deformer_index.setdefault(index, each)
                    ing += 1
                    
            self.treewidget = QtGui.QTreeWidget(self.groupbox)
            self.treewidget.setObjectName('treeWidget_%s' % titles[index])
            self.treewidget.setAlternatingRowColors(True)
            self.treewidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
            self.treewidget.setHeaderHidden(True)
            self.treewidget.setSortingEnabled(True)
            self.treewidget.setToolTip('%s defomer list' % titles[index])
                 
            self.verticallayout_geometry.addWidget(self.treewidget)
            self.combobox.currentIndexChanged.connect(self.setCurrentDeformer)                 
            index += 1       
            
        self.button = QtGui.QPushButton(self.groupbox)
        self.button.setObjectName('button_convert')
        self.button.setText('Convert')
        self.button.setToolTip('Convert to target deformer')
        self.verticallayout.addWidget(self.button)
        self.button.clicked.connect(self.convert)    
    
    def create_items(self, parent, text, icon_name):        
        current_item = QtGui.QTreeWidgetItem(parent, icon_name)            
        iconPath = ''                        
        icon  = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)                    
        current_item.setIcon(0, icon)
        current_item.setText(0, text)
        return current_item       

    def add_object(self):               
                
        self.lineedit.clear()        
        shapes = self.my_maya.getSelectedObjectShapeNode(OpenMaya.MFn.kMesh)        
        if not shapes:
            OpenMaya.MGlobal.displayWarning('not found mesh in your selection!...')   
            return         
        self.lineedit.setText(shapes[-1].partialPathName())
        self.my_maya.nodee = shapes[-1].partialPathName()
        
        current_deform = str(self.combobox.currentText())
        
        # self.my_maya.getShapeNode(OpenMaya.MFn.kMesh)
        
    def setCurrentDeformer(self, current_index):
        
        current_mesh = str(self.lineedit.text())
        self.treewidget.clear()  
              
        if not current_mesh:
            return             
        if current_index not in self.deformer_index:
            return        
        if self.deformer_index[current_index] not in self.my_maya.object_types:
            return
         
        current_type = self.my_maya.object_types[self.deformer_index[current_index]]        
        deformers = self.my_maya.getDeformerNodes(current_mesh, current_type)
        
        print self.deformer_index[current_index]
        
        deformer_data = {}
        
        if self.deformer_index[current_index]=='blendShape':
            deformers = self.my_maya.getBlenshapeAttributes(deformers)      
        
        if self.deformer_index[current_index]=='skinCluster':
            deformers = self.my_maya.getSkinclusterJoints(deformers[0])
           
        if self.deformer_index[current_index]=='wire':
            deformer_data = {}
            for index in range (deformers.length()):
                curve_object = self.my_maya.getDeformerNodes(deformers[index], OpenMaya.MFn.kCurve)
                joint_data = self.my_maya.getDeformerJoints(curve_object)
                cluster_data = self.my_maya.getClusterHandle(curve_object)
                                
                for k, v in joint_data.items():            
                    curve_node = OpenMaya.MFnDependencyNode(k)
                    for index in range (v.length()):
                        deformer_data.setdefault(curve_node.name(), []).append(v[index].fullPathName())               
                
                for k, v in cluster_data.items():
                    curve_node = OpenMaya.MFnDependencyNode(k)
                    for index in range (v.length()):
                        cluster_node = OpenMaya.MFnDependencyNode(v[index])
                        deformer_data.setdefault(curve_node.name(), []).append(cluster_node.name())

        if self.deformer_index[current_index]=='lattice':
            deformer_data = {}
            joint_data = self.my_maya.getDeformerJoints(deformers)            
            cluster_data = self.my_maya.getClusterHandle(deformers)
            
            for k, v in joint_data.items():
                parent_node = OpenMaya.MFnDependencyNode(k)
                for index in range (v.length()):
                    deformer_data.setdefault(parent_node.name(), []).append(v[index].fullPathName())
                    
            for k, v in cluster_data.items():
                parent_node = OpenMaya.MFnDependencyNode(k)
                for index in range (v.length()):
                    child_node = OpenMaya.MFnDependencyNode(v[index])
                    deformer_data.setdefault(parent_node.name(), []).append(child_node.name())
                    
            
        if self.deformer_index[current_index]=='cluster':
            
            for index in range (deformers.length()):  
                mfn_dag_cluster = OpenMaya.MFnDagNode(deformers[index])
                cluster_mobject = mfn_dag_cluster.parent(0)
                cluster_handle = OpenMaya.MFnDependencyNode(cluster_mobject)
                deformer_data.setdefault(cluster_handle.name(), [])
                    
        if not deformer_data:
            for index in range (deformers.length()):
                if isinstance(deformers[index] , OpenMaya.MPlug):
                    deformer_data.setdefault(deformers[index].name(), [])
                
                if isinstance(deformers[index] , OpenMaya.MDagPath):
                    deformer_data.setdefault(deformers[index].fullPathName(), [])
                
                #===============================================================
                # if isinstance(deformers[index] , OpenMaya.MObject):                    
                #     mobejct_node = OpenMaya.MFnDependencyNode(deformers[index])
                #     
                #     
                #     deformer_data.setdefault(mobejct_node.name(), [])
                #===============================================================
                    
                                    


        if not deformer_data:
            return
        
        
        for k, v in deformer_data.items():
            parent_item = self.create_items(self.treewidget, k, 'test')
            for index in range (len(v)):
                child_item = self.create_items(parent_item, v[index], 'test') 
            self.treewidget.setItemExpanded(parent_item, 1)          


           
    def convert(self):
        print 'wipppppppppppppp'
        
        # mselection_list, component_weights = self.my_maya.getWeightsFromSelection()
        
        #print mselection_list
        #print  components
        #print weights
        
        # self.blendshape_to_cluster('pSphereShape1', 'blendShape4.pSphere4')
        
        self.lattice_to_cluster('pSphereShape1', 'cluster14Handle.translateX')
        
    
    def blendshape_to_cluster(self, object, attribute):
        
        from pymel import core        
        my_cluster = core.cluster()
        
        weights = self.my_maya.getWeightsFromEnvelope(object, object, attribute)
        
        self.my_maya.setClusterWeights(object, my_cluster[0].name(), weights)
        
    def lattice_to_cluster(self):
        
        weights = self.my_maya.getWeightsFromEnvelope(object, object, attribute)
        my.setClusterWeights('pSphereShape1', 'cluster15', weights)

        print weights



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Geometry(parent=None)
    window.show()
    sys.exit(app.exec_())
