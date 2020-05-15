'''
skincluster.py 0.0.1 
Date: January 01, 2019
Last modified: January 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    skincluster is the function set for skinClusters (smooth bindSkin) and joints. 
    Its is custom api from MFnSkinCluster Maya Class based on requirements.
    The purpose of the skincluster to create, getting and setting weights of the skincluster   
    Weights are per influence object for each component of each geometry that is deformed. 
    Influence objects can be joints or any transform.
'''

import copy

from maya import OpenMaya
from maya import OpenMayaAnim

from smartDeformer_maya2019.modules import studioMaya


class Skincluster(studioMaya.Maya):

    def __init__(self, **kwargs):
        self.source_geometry = None
        self.target_geometrys = None
        self.source_deformers = None
        self.target_deformers = None
        self.cluster_object = None

        if 'source_geometry' in kwargs:
            self.source_geometry = kwargs['source_geometry']
        if 'target_geometrys' in kwargs:
            self.target_geometrys = kwargs['target_geometrys']
        if 'source_deformers' in kwargs:
            self.source_deformers = kwargs['source_deformers']
        if 'target_deformers' in kwargs:
            self.target_deformers = kwargs['target_deformers']

    def create(self, name, clear=False):
        name = name.split('|')[-1]
        if clear:
            OpenMaya.MGlobal.clearSelectionList()
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('joint')
        mfn_dag_node.setName(name)
        joint_dag_path = OpenMaya.MDagPath()
        mfn_dag_node.getPath(joint_dag_path)
        return joint_dag_path, joint_dag_path.fullPathName().encode()

    def had_valid(self, joint):
        return self.hasJoint(joint)

    def get_weight(self, joint_dag_path):  # redo skin cluster
        m_skinclusters = self.getDependences(
            joint_dag_path, OpenMaya.MFn.kSkinClusterFilter)
        skin_cluster_data = {}
        for index in range(m_skinclusters.length()):
            m_dag_path, weights, memberships = self.read_weight(
                m_skinclusters[index], joint_dag_path)
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
            data = self.get_weight(each_dag_path)
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

    def read_weight(self, m_skincluster, joint_dag_path):
        if not isinstance(joint_dag_path, OpenMaya.MDagPath):
            joint_dag_path = self.getDagPath(joint_dag_path)
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skincluster)
        selection_list = OpenMaya.MSelectionList()
        m_float_array = OpenMaya.MFloatArray()
        mfn_skincluster.getPointsAffectedByInfluence(
            joint_dag_path, selection_list, m_float_array)
        deformer_set = mfn_skincluster.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        mfn_set.getMembers(selection_list, True)
        m_object = OpenMaya.MObject()
        m_dag_path = OpenMaya.MDagPath()
        selection_list.getDagPath(0, m_dag_path, m_object)
        # example joint_index =
        # mfn_skincluster.indexForInfluenceObject(joint_dag_path)
        joint_index = self.findxIndexFromSkincluster(
            mfn_skincluster, joint_dag_path)
        mit_geometry = OpenMaya.MItGeometry(m_dag_path)
        membership_list = []
        weight_list = []
        while not mit_geometry.isDone():
            component = mit_geometry.currentItem()
            float_array = OpenMaya.MFloatArray()
            membership = self.hasMembership(
                m_skincluster, m_dag_path, component)
            if not m_float_array:
                float_array = [0, 0, 0]
            else:
                if membership:
                    mfn_skincluster.getWeights(
                        m_dag_path, component, joint_index, float_array)
                else:
                    float_array = [0, 0, 0]
            membership_list.append(membership)
            weight_list.append(float_array[0])
            mit_geometry.next()
        return m_dag_path, weight_list, membership_list

    def write_weight(self, joint_dag_path, geometry_data):
        for each_geometry, geometrys in geometry_data.items():
            weights = geometrys['weights']
            mfloat_array = OpenMaya.MFloatArray()
            mscript_util = OpenMaya.MScriptUtil()
            mscript_util.createFloatArrayFromList(weights, mfloat_array)
            self.setSkinclusterWeights(
                each_geometry, joint_dag_path, mfloat_array)

    def create_mirror_flip(self, joint_dag_paths, axis, tag):
        for index in range(joint_dag_paths.length()):
            position = self.getJointPosition(joint_dag_paths[index])
            weight_data = self.get_weight(joint_dag_paths[index])
            mirror_position = position[0] * \
                axis[0], position[1] * axis[1], position[2] * axis[2]
            symmetry_weights = self.get_flip_weights(weight_data, axis)
            joint_dag_path, joint_name = self.create(
                '%s_joint' % tag, clear=True)
            target_position = mirror_position
            if tag == 'mirror':
                proxy_position = [1, 1, 1]
                proxy_position[axis.index(-1)] = 0
                target_position = [mirror_position[0] * proxy_position[0],
                                   mirror_position[1] * proxy_position[1],
                                   mirror_position[2] * proxy_position[2]]
            self.setJointPosition(joint_dag_path, target_position)
            target_weights = symmetry_weights
            if tag == 'mirror':
                target_weights = self.merge_weights(
                    weight_data['geometry'], symmetry_weights)
            target_datas = {}
            target_datas['geometry'] = target_weights
            target_datas['position'] = mirror_position
            target_datas['locked'] = False
            self.addInfluence(joint_dag_path, target_weights.keys())
            self.set_weight(joint_dag_path, target_datas)

    def get_flip_weights(self, geometry_data, axis):
        symmetry_weights = copy.deepcopy(geometry_data['geometry'])
        for each_geometry, weights_data in geometry_data['geometry'].items():
            geometry_dag_path = self.getDagPath(each_geometry)
            memberships = weights_data['memberships']
            weights = weights_data['weights']
            for index in range(len(weights)):
                symmetry_vertex_id = self.get_symmetry_vertex(
                    geometry_dag_path, index, axis)
                symmetry_weights[each_geometry]['weights'][symmetry_vertex_id] = weights[index]
                symmetry_weights[each_geometry]['memberships'][symmetry_vertex_id] = memberships[index]
        return symmetry_weights

    def merge_weights(self, weight_a, weight_b):
        merge_weight_data = copy.deepcopy(weight_a)
        for each_geometry, geometry_data in weight_a.items():
            weights_a = geometry_data['weights']
            memberships_a = geometry_data['memberships']
            for index in range(len(weights_a)):
                weight_index_b = weight_b[each_geometry]['weights']
                membership_index_b = weight_b[each_geometry]['memberships']
                merge_weight = weights_a[index] + weight_index_b[index]
                if merge_weight > 1:
                    merge_weight = 1
                current_memberships = True
                if not memberships_a[index] and not membership_index_b[index]:
                    current_memberships = False
                merge_weight_data[each_geometry]['weights'][index] = merge_weight
                merge_weight_data[each_geometry]['memberships'][index] = current_memberships
        return merge_weight_data

    def combine_weights(self, joint_dag_paths):
        weights_data = {}
        memberships_data = {}
        for index in range(joint_dag_paths.length()):
            weight_data = self.get_weight(joint_dag_paths[index])
            for each_geometry, geometry_data in weight_data['geometry'].items():
                weights = geometry_data['weights']
                memberships = geometry_data['memberships']
                weights_data.setdefault(each_geometry, []).append(weights)
                memberships_data.setdefault(
                    each_geometry, []).append(memberships)
        geometry_data = {}
        for index in range(len(weights_data)):
            geometry = weights_data.keys()[index]
            weights = {'weights': weights_data[geometry]}
            memberships = {'memberships': memberships_data[geometry]}
            geometry_data.setdefault(geometry, weights)
            geometry_data[geometry].update(memberships)
        combine_data = {}
        for each_geometry, geometry_weights in geometry_data.items():
            empty_weights, empty_memberships = self.createEmptyWeights(
                each_geometry)
            for index in range(len(geometry_weights['weights'])):
                current_weights = geometry_weights['weights'][index]
                current_memberships = geometry_weights['memberships'][index]
                for x in range(len(current_weights)):
                    if current_weights[x] > 1:
                        empty_weights[x] = 1
                    empty_weights[x] += current_weights[x]
                    if current_memberships[x]:
                        empty_memberships[x] = True
            combine_weights = {'weights': empty_weights}
            combine_memberships = {'memberships': empty_memberships}
            combine_data.setdefault(each_geometry, combine_weights)
            combine_data[each_geometry].update(combine_memberships)
        position = self.getCenterPosition(joint_dag_paths, 'skincluster')
        joint_dag_path, joint_name = self.create('combine_joint', clear=True)
        self.setJointPosition(joint_dag_path, position)
        combine_datas = {}
        combine_datas['geometry'] = combine_data
        combine_datas['position'] = position
        combine_datas['locked'] = False
        self.addInfluence(joint_dag_path, combine_data.keys())
        self.set_weight(joint_dag_path, combine_datas)

    def copy_weight(self, source_joint, target_joint):
        self.copy_weights(source_joint, target_joint)

    def copy_weights(self, source_joint, target_joint):
        weight_data = self.get_weight(source_joint)
        self.set_weight(target_joint, weight_data)

    def soft_selection(self):
        dag_paths, memberships, weights = self.getWeightsFromSelection()
        if not dag_paths:
            return
        if not self.target_deformers:
            x, y, z = self.get_center_of_selection()
            joint_dag_path, joint_name = self.create(
                'soft_selection_joint', clear=True)
            self.setJointPosition(joint_name, [x, y, z])
            self.addInfluence(joint_name, self.target_geometrys)
            self.target_deformers = [joint_name]
        for each_joint in self.target_deformers:
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(
                    each_geometry, each_joint, weights[0])
                plug = self.getPlug(each_joint, 'liw')
                plug.setBool(False)

    def blend_shape(self):
        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])
        for index in range(loop):
            weights = self.getWeightsFromEnvelope(
                self.source_geometry, self.source_geometry, self.source_deformers[index])
            _targt_deformer = self.target_deformers[index]
            if not self.target_deformers[index]:
                x, y, z = self.get_center_of_weights(
                    self.source_geometry, weights)
                name = '%s_blend_shape_joint' % self.source_deformers[index].replace(
                    '.', '_')
                joint_dag_path, joint_name = self.create(name, clear=True)
                self.setJointPosition(joint_name, [x, y, z])
                self.addInfluence(joint_name, self.target_geometrys)
                _targt_deformer = joint_name
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(
                    each_geometry, _targt_deformer, weights)
                plug = self.getPlug(_targt_deformer, 'liw')
                plug.setBool(False)

    def wire(self):
        self.to_specific_deformer('wire')

    def lattice(self):
        self.to_specific_deformer('lattice')

    def cluster(self):
        source_mobject = self.getMObject(self.source_geometry)

        from smartDeformer_maya2019.modules import cluster
        clu = cluster.Cluster()

        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])
        for index in range(loop):
            _targt_deformer = self.target_deformers[index]
            if not self.target_deformers[index]:
                name = '%s_cluster_joint' % self.source_deformers[index].replace(
                    '.', '_')
                joint_dag_path, joint_name = self.create(name, clear=True)
                x, y, z = self.getClusterPosition(self.source_deformers[index])
                self.setJointPosition(joint_name, [x, y, z])
                self.addInfluence(joint_name, self.target_geometrys)
                _targt_deformer = joint_name
            cluster_mobject = self.getDependences(
                _targt_deformer, OpenMaya.MFn.kClusterFilter)
            weight_data = clu.get_weight(self.source_deformers[index])
            weight_object = weight_data['geometry'].keys()[0]
            weights = weight_data['geometry'][weight_object]['weights']
            weight_array = OpenMaya.MFloatArray()
            mscript_util = OpenMaya.MScriptUtil()
            mscript_util.createFloatArrayFromList(weights, weight_array)
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(
                    each_geometry, _targt_deformer, weight_array)

    def to_skincluster(self):
        source_mobject = self.getMObject(self.source_geometry)
        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])
        for index in range(loop):
            _targt_deformer = self.target_deformers[index]
            if not self.target_deformers[index]:
                name = '%s_skincluster_joint' % self.source_deformers[index].replace(
                    '.', '_')
                joint_dag_path, joint_name = self.create(name, clear=True)
                x, y, z = self.getJointPosition(self.source_deformers[index])
                self.setJointPosition(joint_name, [x, y, z])
                self.addInfluence(joint_name, self.target_geometrys)
                _targt_deformer = joint_name
            jnt_dag_path = self.getDagPath(self.source_deformers[index])
            weight_data = self.get_weight(jnt_dag_path)
            weight_object = weight_data['geometry'].keys()[0]
            weights = weight_data['geometry'][weight_object]['weights']
            weight_array = OpenMaya.MFloatArray()
            mscript_util = OpenMaya.MScriptUtil()
            mscript_util.createFloatArrayFromList(weights, weight_array)
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(
                    each_geometry, _targt_deformer, weight_array)

    def to_specific_deformer(self, tag, lock=True):
        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])
        source_deformer_dag_path = OpenMaya.MDagPathArray()
        for index in range(loop):
            source_dag_path = self.getDagPath(self.source_deformers[index])
            source_deformer_dag_path.append(source_dag_path)
        for index in range(source_deformer_dag_path.length()):
            source_dag_path = source_deformer_dag_path[index]
            if source_dag_path.hasFn(OpenMaya.MFn.kCurve):  # to check to curve
                curve_weights = self.getWeightsFromCurve(
                    source_dag_path, self.source_geometry)
                for k, v in curve_weights.items():
                    name = '%s_%s_%s_joint' % (
                        self.source_deformers[index], k, tag)
                    joint_dag_path, joint_name = self.create(name, clear=True)
                    self.setJointPosition(joint_name, v['position'])
                    self.addInfluence(joint_name, self.target_geometrys)
                    for each_geometry in self.target_geometrys:
                        self.setSkinclusterWeights(
                            each_geometry, joint_name, v['weights'])
                        if lock:
                            plug = self.getPlug(joint_name, 'liw')
                            plug.setBool(lock)
            elif source_dag_path.hasFn(OpenMaya.MFn.kTransform) or source_dag_path.hasFn(OpenMaya.MFn.kJoint):
                _targt_deformer = self.target_deformers[index]
                if source_dag_path.hasFn(OpenMaya.MFn.kJoint):
                    children = self.getChildren(source_dag_path)
                elif source_dag_path.hasFn(OpenMaya.MFn.kTransform):
                    children = self.getChildren(
                        source_dag_path, mfn_shape=OpenMaya.MFn.kCluster)
                for cindex in range(children.length()):
                    self.unParent(children[cindex])
                if not self.target_deformers[index]:
                    name = '%s_%s_joint' % (self.source_deformers[index], tag)
                    joint_dag_path, joint_name = self.create(name, clear=True)
                    if source_dag_path.hasFn(OpenMaya.MFn.kJoint):
                        x, y, z = self.getJointPosition(
                            self.source_deformers[index])
                    else:
                        x, y, z = self.getClusterPosition(
                            self.source_deformers[index])
                    self.setJointPosition(joint_name, [x, y, z])
                    self.addInfluence(joint_name, self.target_geometrys)
                    _targt_deformer = joint_name
                attribute = '{}.translateX'.format(
                    self.source_deformers[index])
                weights = self.getWeightsFromEnvelope(
                    self.source_geometry, self.source_geometry, attribute)
                for each_geometry in self.target_geometrys:
                    self.setSkinclusterWeights(
                        each_geometry, _targt_deformer, weights)
                    if lock:
                        plug = self.getPlug(_targt_deformer, 'liw')
                        plug.setBool(lock)
                for rindex in range(children.length()):
                    self.parentTo(children[rindex], source_dag_path)
            else:
                OpenMaya.MGlobal.displayWarning('Your select is wrong!...')

# end ####################################################################
