'''
stdioMaya.py 0.0.1 
Date: January 01, 2019
Last modified: January 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    stdioMaya is the function set for manage the maya objects.
    Its is custom api package of Maya API based on requirements.
    The purpose of the stdioMaya to validate, getting and setting maya objects.  
'''


from maya import OpenMaya
from maya import OpenMayaAnim


class Maya(object):

    def __init__(self, **kwargs):
        if 'node' in kwargs:
            node = kwargs['node']
        self.getObjecTypes()

    def hasCluster(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath()
        mfn_dag_node = OpenMaya.MFnDagNode(dag_path)
        cluster_dag_path = mfn_dag_node.dagPath()
        try:
            cluster_dag_path.extendToShape()
        except:
            cluster_dag_path = None
        if not dag_path:
            return False
        if not cluster_dag_path:
            return False
        if not cluster_dag_path.hasFn(OpenMaya.MFn.kCluster):
            return False
        return True

    def hasJoint(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        if not dag_path.hasFn(OpenMaya.MFn.kJoint):
            return False
        return True

    def hasMembership(self, deformer_mobject, geometry_dag_path, geometry_component):
        mfn_geometry_filter = OpenMayaAnim.MFnGeometryFilter(deformer_mobject)
        deformer_set = mfn_geometry_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        selectionList = OpenMaya.MSelectionList()
        mfn_set.getMembers(selectionList, True)
        if not selectionList.hasItem(geometry_dag_path, geometry_component):
            return False
        return True

    def getDagPath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getMObject(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject

    def getPlug(self, node, attribute):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add("%s.%s" % (node, attribute))
        mselection.getPlug(0, mplug)
        return mplug

    def getVertexsMObjects(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        mit_geometry = OpenMaya.MItGeometry(dag_path)
        mselection = OpenMaya.MSelectionList()
        while not mit_geometry.isDone():
            component = mit_geometry.currentItem()
            mselection.add(dag_path, component, True)
            mit_geometry.next()
        components = OpenMaya.MObject()
        mselection.getDagPath(0, dag_path, components)
        return components

    def getDagPathMembers(self, mobject):
        if not isinstance(mobject, OpenMaya.MObject):
            mobject = self.getMObject(mobject)
        mfn_geometry_filter = OpenMayaAnim.MFnGeometryFilter(mobject)
        deformer_set = mfn_geometry_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        dag_path_array = OpenMaya.MDagPathArray()
        for index in range(selection_list.length()):
            dag_path = OpenMaya.MDagPath()
            selection_list.getDagPath(index, dag_path)
            dag_path_array.append(dag_path)
        return dag_path_array

    def getSelectedObjectShapeNode(self, shape_type=None):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        shapes = []
        for x in range(mselection.length()):
            dag_path = OpenMaya.MDagPath()
            mselection.getDagPath(x, dag_path)
            dag_path.extendToShape()
            if not dag_path:
                continue
            if shape_type:
                if not dag_path.hasFn(shape_type):
                    continue
            shapes.append(dag_path)
        return shapes

    def getSelectedDagPaths(self):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        dag_path_array = OpenMaya.MDagPathArray()
        for x in range(mselection.length()):
            dag_path = OpenMaya.MDagPath()
            try:
                mselection.getDagPath(x, dag_path)
            except:
                pass
            dag_path_array.append(dag_path)
        return dag_path_array

    def getShapeNode(self, node, shape_type=None):
        mdag_path = self.getDagPath(node)
        try:
            mdag_path.extendToShape()
        except:
            mdag_path = None
        if not mdag_path:
            return
        if shape_type:
            if not mdag_path.hasFn(shape_type):
                return
        return mdag_path

    def getDependences(self, mobject, node_type, upstream=False, downstream=False):
        if isinstance(mobject, str):
            mobject = self.getMObject(mobject)
        if isinstance(mobject, OpenMaya.MDagPath):
            mobject = mobject.node()
        if not upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type)
        if upstream and not downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type,
                                                           OpenMaya.MItDependencyGraph.kUpstream,
                                                           OpenMaya.MItDependencyGraph.kDepthFirst,
                                                           OpenMaya.MItDependencyGraph.kNodeLevel)
        if not upstream and downstream:
            dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type,
                                                           OpenMaya.MItDependencyGraph.kDownstream,
                                                           OpenMaya.MItDependencyGraph.kDepthFirst,
                                                           OpenMaya.MItDependencyGraph.kNodeLevel)
        result = OpenMaya.MObjectArray()
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            result.append(current_item)
            dependency_graph.next()
        return result

    def getDeformerNodes(self, node, node_type):
        result = self.getDependences(
            node, node_type, upstream=True, downstream=False)
        return result

    def getConnectedNode(self, node_type, mess=False):
        stack = []
        nodes = [self.getMObject()]
        result = OpenMaya.MObjectArray()
        index = 0
        while nodes:
            if index == 1000:
                break
            node = nodes.pop()
            mfn_dependency_node = OpenMaya.MFnDependencyNode(node)
            attribute_count = mfn_dependency_node.attributeCount()
            for x in range(attribute_count):
                attribute = mfn_dependency_node.attribute(x)
                plug = mfn_dependency_node.findPlug(attribute)
                plug_array = OpenMaya.MPlugArray()
                plug.connectedTo(plug_array, True, True)
                if not plug_array[0]:
                    continue
                mobject = plug_array[0].node()
                obj_dependency_node = OpenMaya.MFnDependencyNode(mobject)
                maya_node = obj_dependency_node.object()
                if obj_dependency_node.name() in stack:
                    continue
                if maya_node.hasFn(node_type):
                    result.append(mobject)
                    if mess:
                        print obj_dependency_node.name()
                stack.append(obj_dependency_node.name())
                nodes.append(maya_node)
                index += 1
        return result

    def getSkinclusterJoints(self, node):
        result = OpenMaya.MDagPathArray()
        if not node:
            return result
        if not isinstance(node, OpenMaya.MObject):
            node = self.getMObject(node)
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(node)
        dag_path_array = OpenMaya.MDagPathArray()
        mfn_skincluster.influenceObjects(dag_path_array)
        for index in range(dag_path_array.length()):
            result.append(dag_path_array[index])
        return result

    def getBlenshapeAttributes(self, mobjects):
        mplug_array = OpenMaya.MPlugArray()
        for index in range(mobjects.length()):
            mobject = mobjects[index]
            if not isinstance(mobjects[index], OpenMaya.MObject):
                mobject = self.getMObject(mobjects[index])
            mfndependency_node = OpenMaya.MFnDependencyNode(mobject)
            mplug = OpenMaya.MPlug()
            mselection_list = OpenMaya.MSelectionList()
            mselection_list.add("%s.weight" % mfndependency_node.name())
            mselection_list.getPlug(0, mplug)
            for x in range(mplug.numElements()):
                current_element = mplug.elementByLogicalIndex(x)
                mplug_array.append(current_element)
        return mplug_array

    def getDeformerJoints(self, mobjects):
        joint_data = {}
        for index in range(mobjects.length()):
            joint_data.setdefault(mobjects[index], OpenMaya.MDagPathArray())
            skinclusters = self.getDeformerNodes(
                mobjects[index], OpenMaya.MFn.kSkinClusterFilter)
            if not skinclusters:
                continue
            joints = self.getSkinclusterJoints(skinclusters[0])
            if not joints:
                continue
            joint_data.setdefault(mobjects[index], joints)
        return joint_data

    def getClusterHandle(self, mobjects):
        cluster_data = {}
        for index in range(mobjects.length()):
            mobject_array = OpenMaya.MObjectArray()
            cluster_data.setdefault(mobjects[index], mobject_array)
            cluster_shape = self.getDeformerNodes(
                mobjects[index], OpenMaya.MFn.kCluster)
            if cluster_shape.length() == 0:
                continue
            for x in range(cluster_shape.length()):
                mfn_dag_node = OpenMaya.MFnDagNode(cluster_shape[x])
                parent_mobject = mfn_dag_node.parent(0)
                mobject_array.append(parent_mobject)
            cluster_data.setdefault(mobjects[index], mobject_array)
        return cluster_data

    def getWireDeformerData(self, mwire_objects):
        for index in range(mwire_objects.length()):
            curve_object = self.getDeformerNodes(
                mwire_objects[index], OpenMaya.MFn.kCurve)
            joints = self.getDeformerJoints(curve_object)
            for j, v in joints.items():
                mfn_j = OpenMaya.MFnDependencyNode(j)

    def getObjecTypes(self):
        self.object_types = {'mesh': OpenMaya.MFn.kMesh,
                             'blendShape': OpenMaya.MFn.kBlendShape,
                             'wire': OpenMaya.MFn.kWire,
                             'lattice': OpenMaya.MFn.kLattice,
                             'ffd': OpenMaya.MFn.kFFD,
                             'cluster': OpenMaya.MFn.kCluster,
                             'clusterShape': OpenMaya.MFn.kClusterFilter,
                             'skincluster': OpenMaya.MFn.kSkinClusterFilter,
                             'joint': OpenMaya.MFn.kJoint
                             }

    def getWeightsFromSelection(self):
        mrich_selection = OpenMaya.MRichSelection()
        OpenMaya.MGlobal.getRichSelection(mrich_selection)
        mselection_list = OpenMaya.MSelectionList()
        mrich_selection.getSelection(mselection_list)
        mit_selection_list = OpenMaya.MItSelectionList(mselection_list)
        if not mit_selection_list.hasComponents():
            OpenMaya.MGlobal.displayError('your selection wrong!...')
            return None, None, None
        dag_paths = OpenMaya.MDagPathArray()
        memberships = []
        weights = []
        while not mit_selection_list.isDone():
            dag_path, mobject = OpenMaya.MDagPath(), OpenMaya.MObject()
            mit_selection_list.getDagPath(dag_path, mobject)
            if not mobject.hasFn(OpenMaya.MFn.kMeshVertComponent):
                OpenMaya.MGlobal.displayError('your some selection wrong!...')
                return None, None, None
            mit_geometry = OpenMaya.MItGeometry(dag_path)
            weight_array = OpenMaya.MFloatArray()
            membership_array = []
            while not mit_geometry.isDone():
                index = mit_geometry.index()
                weight_array.append(0)
                membership_array.append(False)
                mit_geometry.next()
            mfncomponent = OpenMaya.MFnComponent(mobject)
            index_component = OpenMaya.MFnSingleIndexedComponent(mobject)
            for index in range(index_component.elementCount()):
                index_id = index_component.element(index)
                m_weight = mfncomponent.weight(index)
                weight_array[index_id] = m_weight.influence()
                membership_array[index_id] = True
            dag_paths.append(dag_path)
            memberships.append(membership_array)
            weights.append(weight_array)
            mit_selection_list.next()
        return dag_paths, memberships, weights

    def getWeightsFromEnvelope(self, origin_dag_path, envelope_dag_path, attribute=None):
        print 'origin_dag_path\t', origin_dag_path
        if not isinstance(origin_dag_path, OpenMaya.MDagPath):
            origin_dag_path = self.getDagPath(origin_dag_path)
        if not isinstance(envelope_dag_path, OpenMaya.MDagPath):
            envelope_dag_path = self.getDagPath(envelope_dag_path)
        mfn_origin_mesh = OpenMaya.MFnMesh(origin_dag_path)
        origin_point_array = OpenMaya.MFloatPointArray()
        mfn_origin_mesh.getPoints(origin_point_array, OpenMaya.MSpace.kObject)
        if attribute:
            node, attribute = attribute.split('.')
            mplug = self.getPlug(node, attribute)
            mplug.setInt(mplug.asInt() + 1)
        mfn_envelope_mesh = OpenMaya.MFnMesh(envelope_dag_path)
        envelope_point_array = OpenMaya.MFloatPointArray()
        mfn_envelope_mesh.getPoints(
            envelope_point_array, OpenMaya.MSpace.kObject)
        if attribute:
            mplug.setInt(mplug.asInt() - 1)
        if envelope_point_array.length() != origin_point_array.length():
            raise Exception('# Target does not match with base.')
            return
        weights = OpenMaya.MFloatArray()
        for index in range(origin_point_array.length()):
            origin_mvector = OpenMaya.MVector(origin_point_array[index])
            envelope_mvector = OpenMaya.MVector(envelope_point_array[index])
            length = origin_mvector - envelope_mvector
            weights.append(length.length())
        return weights

    def getWeightsFromCurve(self, curve_dag_path, geomerty_dag_path):
        if not isinstance(geomerty_dag_path, OpenMaya.MDagPath):
            geomerty_dag_path = self.getDagPath(geomerty_dag_path)
        if not isinstance(curve_dag_path, OpenMaya.MDagPath):
            curve_dag_path = self.getDagPath(curve_dag_path)
        weights = {}
        mfn_nurbs_curve = OpenMaya.MFnNurbsCurve(curve_dag_path)
        for cv in range(mfn_nurbs_curve.numCVs()):
            mfn_origin_mesh = OpenMaya.MFnMesh(geomerty_dag_path)
            origin_point_array = OpenMaya.MFloatPointArray()
            mfn_origin_mesh.getPoints(
                origin_point_array, OpenMaya.MSpace.kObject)
            position = OpenMaya.MPoint()
            mfn_nurbs_curve.getCV(cv, position)
            ing_position = OpenMaya.MPoint(
                position.x + 1, position.y, position.z)
            mfn_nurbs_curve.setCV(cv, ing_position)
            mfn_nurbs_curve.updateCurve()
            mfn_envelope_mesh = OpenMaya.MFnMesh(geomerty_dag_path)
            envelope_point_array = OpenMaya.MFloatPointArray()
            mfn_envelope_mesh.getPoints(
                envelope_point_array, OpenMaya.MSpace.kObject)
            mfn_nurbs_curve.setCV(cv, position)
            mfn_nurbs_curve.updateCurve()
            cv_weights = OpenMaya.MFloatArray()
            for index in range(origin_point_array.length()):
                origin_mvector = OpenMaya.MVector(origin_point_array[index])
                envelope_mvector = OpenMaya.MVector(
                    envelope_point_array[index])
                length = origin_mvector - envelope_mvector
                cv_weights.append(length.length())
            weight_data = {}
            weight_data['position'] = [position.x, position.y, position.z]
            weight_data['weights'] = cv_weights
            weights.setdefault(cv, weight_data)
        return weights

    def getName(self, maya_object):
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependency_node.name().encode()

    def getCenterPosition(self, dag_paths, type):
        x, y, z = 0, 0, 0
        for index in range(dag_paths.length()):
            if type == 'cluster':
                position = self.getClusterPosition(dag_paths[index])
            else:
                position = self.getJointPosition(dag_paths[index])
            x += position[0]
            y += position[1]
            z += position[2]
        center = [x / dag_paths.length(), y / dag_paths.length(),
                  z / dag_paths.length()]
        return center

    def get_symmetry_vertex(self, geometry_dag_path, vertex_id, axis=[-1, 1, 1]):
        mfn_mesh = OpenMaya.MFnMesh(geometry_dag_path)
        position_m_point = OpenMaya.MPoint()
        mfn_mesh.getPoint(vertex_id, position_m_point, OpenMaya.MSpace.kWorld)
        symmetry_position = OpenMaya.MPoint()
        symmetry_position.x = position_m_point.x * axis[0]
        symmetry_position.y = position_m_point.y * axis[1]
        symmetry_position.z = position_m_point.z * axis[2]
        closest_m_point = OpenMaya.MPoint()
        m_script_util = OpenMaya.MScriptUtil()
        index_ptr = m_script_util.asIntPtr()
        prev_index = m_script_util.asIntPtr()
        mfn_mesh.getClosestPoint(
            symmetry_position, closest_m_point, OpenMaya.MSpace.kWorld, index_ptr)
        int_index = m_script_util.getInt(index_ptr)
        mit_mesh_polygon = OpenMaya.MItMeshPolygon(geometry_dag_path)
        mit_mesh_polygon.setIndex(int_index, prev_index)
        face_vertex_array = OpenMaya.MIntArray()
        mit_mesh_polygon.getVertices(face_vertex_array)
        vector_lengths = []
        for each_vertex in face_vertex_array:
            vertex_symmetry_position = OpenMaya.MPoint()
            mfn_mesh.getPoint(
                each_vertex, vertex_symmetry_position, OpenMaya.MSpace.kWorld)
            vertex_symmetry_vector = OpenMaya.MVector(vertex_symmetry_position)
            symmetry_vector = OpenMaya.MVector(symmetry_position)
            mVectorLength = vertex_symmetry_vector - symmetry_vector
            length = mVectorLength.length()
            vector_lengths.append(length)
        closest_vertex = min(vector_lengths)
        vertexIndex = vector_lengths.index(closest_vertex)
        symmetry_vertex_id = face_vertex_array[vertexIndex]
        return symmetry_vertex_id

    def get_center_of_selection(self):
        mselection_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection_list)
        mit_selection_list = OpenMaya.MItSelectionList(mselection_list)
        x, y, z = 0, 0, 0
        count = 0
        while not mit_selection_list.isDone():
            dag_path, mobject = OpenMaya.MDagPath(), OpenMaya.MObject()
            mit_selection_list.getDagPath(dag_path, mobject)
            mfncomponent = OpenMaya.MFnComponent(mobject)
            index_component = OpenMaya.MFnSingleIndexedComponent(mobject)
            mfn_mesh = OpenMaya.MFnMesh(dag_path)
            count += index_component.elementCount()
            for index in range(index_component.elementCount()):
                index_id = index_component.element(index)
                m_point = OpenMaya.MPoint()
                mfn_mesh.getPoint(index_id, m_point)
                x += m_point.x
                y += m_point.y
                z += m_point.z
            mit_selection_list.next()
        return x / count, y / count, z / count

    def get_center_of_weights(self, geometry_dag_path, weights):
        if not isinstance(geometry_dag_path, OpenMaya.MDagPath):
            geometry_dag_path = self.getDagPath(geometry_dag_path)
        mfn_mesh = OpenMaya.MFnMesh(geometry_dag_path)
        x, y, z = 0, 0, 0
        count = 0
        for index in range(weights.length()):
            if weights[index] <= 0:
                continue
            m_point = OpenMaya.MPoint()
            mfn_mesh.getPoint(index, m_point)
            x += m_point.x
            y += m_point.y
            z += m_point.z
            count += 1
        return x / count, y / count, z / count

    def setClusterWeights(self, dag_path, cluster_mobject, weights):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        if not isinstance(cluster_mobject, OpenMaya.MObject):
            cluster_mobject = self.getMObject(cluster_mobject)
        components = self.getVertexsMObjects(dag_path)
        mfn_geo_filter = OpenMayaAnim.MFnGeometryFilter(cluster_mobject)
        deformer_set = mfn_geo_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        mfn_set.addMember(dag_path, components)
        weight_geometry_filter = OpenMayaAnim.MFnWeightGeometryFilter(
            cluster_mobject)
        weight_geometry_filter.setWeight(dag_path, components, weights)

    def setMembership(self, geomotry_dag_path, deformer_mobject, memberships):
        mfn_geo_filter = OpenMayaAnim.MFnGeometryFilter(deformer_mobject)
        deformer_set = mfn_geo_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        add_selection_lst = OpenMaya.MSelectionList()
        remove_selection_lst = OpenMaya.MSelectionList()
        mit_geometry = OpenMaya.MItGeometry(geomotry_dag_path)
        while not mit_geometry.isDone():
            index = mit_geometry.index()
            component = mit_geometry.currentItem()
            if memberships[index]:
                add_selection_lst.add(geomotry_dag_path, component)
            else:
                remove_selection_lst.add(geomotry_dag_path, component)
            mit_geometry.next()
        if not add_selection_lst.isEmpty():
            mfn_set.addMembers(add_selection_lst)
        if not remove_selection_lst.isEmpty():
            mfn_set.removeMembers(remove_selection_lst)

    def setSkinclusterWeights(self, geometry_dag_path, joint_dag_path, weights):
        if not isinstance(geometry_dag_path, OpenMaya.MDagPath):
            geometry_dag_path = self.getDagPath(geometry_dag_path)
        if not isinstance(joint_dag_path, OpenMaya.MDagPath):
            joint_dag_path = self.getDagPath(joint_dag_path)
        components = self.getVertexsMObjects(geometry_dag_path)
        skin_cluster = self.getSkincluster(geometry_dag_path)
        skincluster_mobject = self.getMObject(skin_cluster)
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(skincluster_mobject)
        # example joint_index =
        # mfn_skincluster.indexForInfluenceObject(joint_dag_path)
        joint_index = self.findxIndexFromSkincluster(
            mfn_skincluster, joint_dag_path)
        joint_index_arry = OpenMaya.MIntArray()
        joint_index_arry.append(joint_index)
        old_values = OpenMaya.MFloatArray()
        mfn_skincluster.setWeights(
            geometry_dag_path, components, joint_index_arry, weights, True, old_values)

    def getClusterPosition(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        mfn_transform = OpenMaya.MFnTransform(dag_path)
        m_transformation_matrix = mfn_transform.transformation()
        m_point = m_transformation_matrix.rotatePivot(OpenMaya.MSpace.kWorld)
        return m_point.x, m_point.y, m_point.z

    def getJointPosition(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        mfn_transform = OpenMaya.MFnTransform(dag_path)
        m_vector = mfn_transform.translation(OpenMaya.MSpace.kWorld)
        return m_vector.x, m_vector.y, m_vector.z

    def setClusterPosition(self, dag_path, position):
        attributes_x = ['originX', 'rotatePivotX', 'scalePivotX']
        attributes_y = ['originY', 'rotatePivotY', 'scalePivotY']
        attributes_z = ['originZ', 'rotatePivotZ', 'scalePivotZ']
        if isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = dag_path.fullPathName()
        for index in range(3):
            plug_x = self.getPlug(dag_path, attributes_x[index])
            plug_y = self.getPlug(dag_path, attributes_y[index])
            plug_z = self.getPlug(dag_path, attributes_z[index])
            plug_x.setFloat(position[0])
            plug_y.setFloat(position[1])
            plug_z.setFloat(position[2])

    def setJointPosition(self, dag_path, position):
        if isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = dag_path.fullPathName()
        plug_x = self.getPlug(dag_path, 'translateX')
        plug_y = self.getPlug(dag_path, 'translateY')
        plug_z = self.getPlug(dag_path, 'translateZ')
        plug_x.setFloat(position[0])
        plug_y.setFloat(position[1])
        plug_z.setFloat(position[2])

    def createEmptyWeights(self, dag_path):
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
        mmit_mesh_vertex = OpenMaya.MItMeshVertex(dag_path)
        weights = OpenMaya.MFloatArray()
        memberships = OpenMaya.MIntArray()
        while not mmit_mesh_vertex.isDone():
            weights.append(0)
            memberships.append(False)
            mmit_mesh_vertex.next()
        return weights, memberships

    def addInfluence(self, joint, geometrys):
        if isinstance(joint, OpenMaya.MDagPath):
            joint = joint.fullPathName()
        for each_geometry in geometrys:
            m_object = self.getMObject(each_geometry.encode())
            m_skinclusters = self.getDeformerNodes(
                m_object, OpenMaya.MFn.kSkinClusterFilter)
            if not m_skinclusters.length():
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find skincluster \"%s\"' % each_geometry.encode())
                continue
            skincluster = self.getName(m_skinclusters[0])
            OpenMaya.MGlobal.executeCommand(
                'skinCluster -e  -dr 4 -lw true -wt 0 -ai {} {}'.format(joint, skincluster))
            # to lock plug = self.getPlug(joint, 'liw')
            # to lock plug.setBool(False)
        return True

    def findxIndexFromSkincluster(self, mfn_skincluster, joint_dag_path):
        joints_dag_path_array = OpenMaya.MDagPathArray()
        mfn_skincluster.influenceObjects(joints_dag_path_array)
        influence_indexs = {}
        for index in range(joints_dag_path_array.length()):
            current_joint = joints_dag_path_array[index].fullPathName()
            influence_indexs.setdefault(current_joint, index)
        if joint_dag_path.fullPathName() not in influence_indexs:
            OpenMaya.MGlobal.displayWarning(
                '\nCan not find index of \"%s\"' % joint_dag_path.fullPathName())
            return
        return influence_indexs[joint_dag_path.fullPathName()]

    def getParents(self, object_dag_path):
        if not isinstance(object_dag_path, OpenMaya.MDagPath):
            object_dag_path = self.getDagPath(object_dag_path)
        mfn_dag_node = OpenMaya.MFnDagNode(object_dag_path)
        parents = OpenMaya.MDagPathArray()
        for index in range(mfn_dag_node.parentCount()):
            current_parent = mfn_dag_node.parent(index)
            parent_mfn_dag_node = OpenMaya.MFnDagNode(current_parent)
            if not parent_mfn_dag_node.fullPathName():
                continue
            parent_dag_Path = self.getDagPath(
                parent_mfn_dag_node.fullPathName().encode())
            parents.append(parent_dag_Path)
        return parents

    def getChildren(self, object_dag_path, mfn_shape=None):
        if not isinstance(object_dag_path, OpenMaya.MDagPath):
            object_dag_path = self.getDagPath(object_dag_path)
        if mfn_shape:
            shape_dag_path = self.getShapeNode(object_dag_path, mfn_shape)
        mfn_dag_node = OpenMaya.MFnDagNode(object_dag_path)
        chidren = OpenMaya.MDagPathArray()
        for index in range(mfn_dag_node.childCount()):
            current_child = mfn_dag_node.child(index)
            child_mfn_dag_node = OpenMaya.MFnDagNode(current_child)
            if not child_mfn_dag_node.fullPathName():
                continue
            child_dag_Path = self.getDagPath(
                child_mfn_dag_node.fullPathName().encode())
            if mfn_shape:
                if not shape_dag_path:
                    continue
                if shape_dag_path.isValid() and child_dag_Path.isValid():
                    if shape_dag_path.apiType() == child_dag_Path.apiType():
                        continue
            chidren.append(child_dag_Path)
        return chidren

    def unParent(self, object):
        if not object:
            return
        if isinstance(object, OpenMaya.MDagPath):
            object = object.fullPathName().encode()
        if isinstance(object, OpenMaya.MObject):
            mfn_dag_node = OpenMaya.MFnDagNode(object)
            object = mfn_dag_node.fullPathName().encode()
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'parent -w %s' % object, mcommand_result, True, True)
        OpenMaya.MGlobal.clearSelectionList()
        results = []
        mcommand_result.getResult(results)
        return results

    def parentTo(self, source, target):
        if not source or not target:
            return
        if isinstance(source, OpenMaya.MDagPath):
            source = source.fullPathName().encode()
        if isinstance(source, OpenMaya.MObject):
            mfn_dag_node = OpenMaya.MFnDagNode(source)
            source = mfn_dag_node.fullPathName().encode()
        if isinstance(target, OpenMaya.MDagPath):
            target = target.fullPathName().encode()
        if isinstance(target, OpenMaya.MObject):
            mfn_dag_node = OpenMaya.MFnDagNode(target)
            target = mfn_dag_node.fullPathName().encode()
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand('parent %s %s' % (
            source, target), mcommand_result, True, True)
        OpenMaya.MGlobal.clearSelectionList()
        results = []
        mcommand_result.getResult(results)
        return results

    def getSkincluster(self, geometry):
        if isinstance(geometry, OpenMaya.MDagPath):
            geometry = geometry.fullPathName().encode().split('|')[-1]
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'findRelatedSkinCluster(\"%s\");' % geometry, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        return results[0].encode()

# end ####################################################################
