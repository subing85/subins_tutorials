from pprint import pprint
from maya import OpenMaya
from maya import OpenMayaAnim

import studioMaya

from smartDeform.modules import studioMaya
reload(studioMaya)


class Cluster(studioMaya.Maya):

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

    def create(self, name):
        from maya import cmds
        # cmds.select(cl=True)
        name = name.split('|')[-1]
        OpenMaya.MGlobal.clearSelectionList()
        cluster, clusterHandle = cmds.cluster(n=name)
        # cluster, clusterHandle = OpenMaya.MGlobal.executeCommand('cluster -n %s' % name, True, False)
        return cluster, clusterHandle

    def get_weight(self, cluster_handle):
        cluster = self.getDependences(cluster_handle, OpenMaya.MFn.kClusterFilter)
        if not cluster:
            raise ValueError('can not find the cluster node!...')
        weights = self.read_weight(cluster[0])
        x, y, z = self.getClusterPosition(cluster_handle)
        data = {}
        data['geometry'] = weights
        data['position'] = [x, y, z]

        return data

    def get_weights(self, cluster_handles):
        cluster_weights = {}
        for each_handle in cluster_handles:
            data = self.get_weight(each_handle)
            cluster_handle = each_handle.fullPathName().encode()
            cluster_weights.setdefault(cluster_handle, data)
        return cluster_weights

    def set_weight(self, mcluster, geometry_data):
        self.write_weight(mcluster, geometry_data)

    def set_weights(self, data):
        for each_handle, each_data in data.items():
            geometry_data = each_data['geometry']
            position = each_data['position']

            cluster, clusterHandle = self.create(each_handle)
            self.setClusterPosition(clusterHandle, position)
            cluster_mobject = self.getMObject(cluster.encode())

            self.set_weight(cluster_mobject, geometry_data)

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

        for each_cluster in self.target_deformers:
            tc_mobject = self.getDependences(
                each_cluster, OpenMaya.MFn.kClusterFilter)
            tm_dag_paths = OpenMaya.MDagPathArray()

            for each_target in self.target_geometrys:
                tm_dag_path = self.getDagPath(each_target)
                tm_dag_paths.append(tm_dag_path)

            self.setWeightsToSelection(
                tc_mobject[0], tm_dag_paths, indexs, weights)

    def blendShape(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):
            cluster_mobject = self.getDependences(
                self.target_deformers[index], OpenMaya.MFn.kClusterFilter)
            weights = self.getWeightsFromEnvelope(
                source_mobject, source_mobject, self.source_deformers[index])
            self.setClusterWeights(
                self.target_geometrys[0], cluster_mobject[0], weights)

    def wire(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):
            attribute = '{}.translateX'.format(self.source_deformers[index])
            cluster_mobject = self.getDependences(
                self.target_deformers[index], OpenMaya.MFn.kClusterFilter)
            weights = self.getWeightsFromEnvelope(
                source_mobject, source_mobject, attribute)
            self.setClusterWeights(
                self.target_geometrys[0], cluster_mobject[0], weights)

    def lattice(self):
        self.wire()

    def skinCluster(self):
        self.wire()

    def read_weight(self, mcluster):
        mfn_weight_filter = OpenMayaAnim.MFnWeightGeometryFilter(mcluster)
        dag_paths = self.getDagPathMembers(mcluster)

        weights = {}
        for index in range(dag_paths.length()):
            mit_geometry = OpenMaya.MItGeometry(dag_paths[index])
            membership_list = []
            weight_list = []
            while not mit_geometry.isDone():
                component = mit_geometry.currentItem()
                float_array = OpenMaya.MFloatArray()

                membership = self.hasMembership(
                    mcluster, dag_paths[index], component)

                if membership:
                    mfn_weight_filter.getWeights(
                        dag_paths[index], component, float_array)
                else:
                    float_array = [0, 0, 0]

                membership_list.append(membership)
                weight_list.append(float_array[0])
                mit_geometry.next()

            weight = {}
            weight['weights'] = weight_list
            weight['memberships'] = membership_list

            geometry = dag_paths[index].fullPathName().encode()
            weights.setdefault(geometry, weight)

        return weights

    def write_weight(self, cluster_mobject, geometry_data):

        for each_geometry, each_data, in geometry_data.items():
            # redu
            try:
                dag_path = self.getDagPath(each_geometry)
            except:
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find object called \"%s\"' % each_geometry)
                continue

            dag_path = self.getDagPath(each_geometry)

            weights = each_data['weights']
            memberships = each_data['memberships']
            mfloat_array = OpenMaya.MFloatArray()
            mscript_util = OpenMaya.MScriptUtil()
            mscript_util.createFloatArrayFromList(weights, mfloat_array)

            self.setClusterWeights(dag_path, cluster_mobject, mfloat_array)
            self.setMembership(dag_path, cluster_mobject, memberships)
