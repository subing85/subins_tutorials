from pprint import pprint
from maya import OpenMaya
from maya import OpenMayaAnim

import studioMaya

from smartDeform.modules import studioMaya
reload(studioMaya)


class Skincluster(studioMaya.Maya):

    def __init__(self, **kwargs):

        self.source_geometry = None
        self.target_geometrys = None
        self.source_deformers = None
        self.target_deformers = None

        if 'source_geometry' in kwargs:
            self.source_geometry = kwargs['source_geometry']
        if 'target_geometrys' in kwargs:
            self.target_geometrys = kwargs['target_geometrys']
        if 'source_deformers' in kwargs:
            self.source_deformers = kwargs['source_deformers']
        if 'target_deformers' in kwargs:
            self.target_deformers = kwargs['target_deformers']

    def create(self, name=None):
        from maya import cmds

        cluster, clusterHandle = cmds.cluster(ihs)
        return cluster, clusterHandle

    def get_weight(self, joint_dag_path):        
        m_skinclusters = self.getDependences(joint_dag_path, OpenMaya.MFn.kSkinClusterFilter)        
        skin_cluster_data = {}
        for index in range (m_skinclusters.length()):      
            m_dag_path, weights, memberships = self.read_weight(m_skinclusters[index], joint_dag_path)            
            weight = {}
            weight['weights'] = weights
            weight['memberships'] = memberships            
            skin_cluster_data.setdefault(m_dag_path.fullPathName(), weight)
        
        x, y, z = self.getJointPosition(joint_dag_path) 
        plug = self.getPlug(joint_dag_path.fullPathName(), 'liw')
        
        data = {}
        data['geometry'] = skin_cluster_data
        data['position'] = [x, y, z]
        data['locked'] = plug.asBool()
  
        return data            

    def get_weights(self, joints):

        skincluster_weights = {}        
        for each_dag_path in joints:       
            data  = self.get_weight(each_dag_path)            
            joint_handle = each_dag_path.fullPathName().encode()
            
            skincluster_weights.setdefault(joint_handle, data)       
        return skincluster_weights

    def set_weight(self, joint_dag_path, joint_data):        
        geometry_data = joint_data['geometry']
        position = joint_data['position']
        locked = joint_data['locked']           
        
        plug = self.getPlug(joint_dag_path.fullPathName(), 'liw') 
        plug.setBool(False) 
        self.write_weight(joint_dag_path, geometry_data)
        
        if locked:        
            plug.setBool(locked) 


    def set_weights(self, data):        
        for each_joint, joint_data in data.items(): 
            joint_dag_path = self.getDagPath(each_joint)            
            self.set_weight(joint_dag_path, joint_data)

    def softSelection(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'
        
        if not self.target_deformers:
            # cluster, clustserHandle = self.create()
            # self.target_defomrer = clusterHandle
            pass

        dag_paths, indexs, weights = self.getWeightsFromSelection()        
        if not dag_paths:
            return
                
        for each_joint in self.target_deformers:            
            m_skinclusters = self.getDependences(each_joint, OpenMaya.MFn.kSkinClusterFilter)
            joint_dag_path = self.getDagPath(each_joint)
            mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skinclusters[0])
            
            for x in range (len(self.target_geometrys)):
                each_shape = self.target_geometrys[x]
                shape_dag_path = self.getDagPath(each_shape)                
                self.setSkinclusterWeights(m_skinclusters[0], joint_dag_path, 
                        shape_dag_path, indexs[x], weights[x])



    def blendShape(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):
            weights = self.getWeightsFromEnvelope(source_mobject, source_mobject, self.source_deformers[index])

            m_skinclusters = self.getDependences(self.target_deformers[index], OpenMaya.MFn.kSkinClusterFilter)
            joint_dag_path = self.getDagPath(self.target_deformers[index])
            mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skinclusters[0])            
            shape_dag_path = self.getDagPath(self.target_geometrys[0])
                        
            mit_mesh_vertex = OpenMaya.MItMeshVertex(source_mobject)
            vertexs = range (mit_mesh_vertex.count())            
            self.setSkinclusterWeights(m_skinclusters[0], joint_dag_path, shape_dag_path, vertexs, weights)
                
                

    def wire(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):            
            attribute = '{}.translateX'.format(self.source_deformers[index])
            weights = self.getWeightsFromEnvelope(source_mobject, source_mobject, attribute)
            
            m_skinclusters = self.getDependences(self.target_deformers[index], OpenMaya.MFn.kSkinClusterFilter)
            joint_dag_path = self.getDagPath(self.target_deformers[index])
            mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skinclusters[0])            
            shape_dag_path = self.getDagPath(self.target_geometrys[0])
                        
            mit_mesh_vertex = OpenMaya.MItMeshVertex(source_mobject)
            vertexs = range (mit_mesh_vertex.count())            
            self.setSkinclusterWeights(m_skinclusters[0], joint_dag_path, shape_dag_path, vertexs, weights)

    def lattice(self):
        self.wire()

    def cluster(self):
        self.wire()
        
        
    def read_weight(self, m_skincluster, joint_dag_path):
        '''       
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skincluster) 
               
        selection_list = OpenMaya.MSelectionList()
        m_float_array = OpenMaya.MFloatArray()        
        mfn_skincluster.getPointsAffectedByInfluence(joint_dag_path, selection_list, m_float_array)
        
        m_dag_path = OpenMaya.MDagPath()
        selection_list.getDagPath(0, m_dag_path)
        
        return m_dag_path, m_float_array
        '''
    
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skincluster)        
        selection_list = OpenMaya.MSelectionList()
        m_float_array = OpenMaya.MFloatArray()        
        mfn_skincluster.getPointsAffectedByInfluence(joint_dag_path, selection_list, m_float_array)        
        m_dag_path = OpenMaya.MDagPath()
        selection_list.getDagPath(0, m_dag_path)
        
        joint_index = mfn_skincluster.indexForInfluenceObject(joint_dag_path)
        
        mit_geometry = OpenMaya.MItGeometry(m_dag_path)
        membership_list = []
        weight_list = []
        
        while not mit_geometry.isDone():
            component = mit_geometry.currentItem()
            float_array = OpenMaya.MFloatArray()
        
            membership = self.hasMembership(m_skincluster, m_dag_path, component)
        
            if membership:
                mfn_skincluster.getWeights(m_dag_path, component, joint_index, float_array)
            else:
                float_array = [0, 0, 0]
                                
            membership_list.append(membership)
            weight_list.append(float_array[0])   
                     
            mit_geometry.next()
        
        return m_dag_path, weight_list, membership_list
    

    def write_weight(self, joint_dag_path, geometry_data):        
        for each_geometry,  geometrys in geometry_data.items():            
            weights = geometrys['weights']
            # memberships = geometrys['memberships']
            
            geometry_dag_path = self.getDagPath(each_geometry)
            skincluster_mobjects = self.getDeformerNodes(geometry_dag_path, OpenMaya.MFn.kSkinClusterFilter)
            
            if not skincluster_mobjects:
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find skincluster \"%s\"' % each_geometry.encode())                
                continue
            
            if not skincluster_mobjects.length():
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find skincluster \"%s\"' % each_geometry.encode())                
                continue
                        
            mit_mesh_vertex = OpenMaya.MItMeshVertex(geometry_dag_path.node())
            vertexs = range (mit_mesh_vertex.count())
                                                  
            self.setSkinclusterWeights(skincluster_mobjects[0], joint_dag_path, geometry_dag_path, vertexs, weights)                


    
    
    