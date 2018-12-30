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

    def get_weight(self, mobject, cluster):
        pass

    def get_weights(self, mobject, clusters):
        pass

    def set_weight(self, cluster, weight):
        pass

    def set_weights(self, clusters, weights):
        pass

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
                        
            mit_messh_vertex = OpenMaya.MItMeshVertex(source_mobject)
            vertexs = range (mit_messh_vertex.count())            
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
                        
            mit_messh_vertex = OpenMaya.MItMeshVertex(source_mobject)
            vertexs = range (mit_messh_vertex.count())            
            self.setSkinclusterWeights(m_skinclusters[0], joint_dag_path, shape_dag_path, vertexs, weights)

    def lattice(self):
        self.wire()

    def cluster(self):
        self.wire()
