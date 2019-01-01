from maya import OpenMaya
from maya import OpenMayaAnim


class Maya(object):

    def __init__(self, **kwargs):
        if 'node' in kwargs:
            node = kwargs['node']

        self.getObjecTypes()

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

    def hasMembership(self, deformer_mobject, geometry_dag_path, geometry_component):
        mfn_geometry_filter = OpenMayaAnim.MFnGeometryFilter(deformer_mobject)
        deformer_set = mfn_geometry_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        selectionList = OpenMaya.MSelectionList()
        mfn_set.getMembers(selectionList, True)

        if not selectionList.hasItem(geometry_dag_path, geometry_component):
            return False
        return True

    def getSelectedObjectShapeNode(self, shape_type=None):
        '''
            :param shape_type <init> example OpenMaya.MFn.kMesh(296)
        '''
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
        mdag_path.extendToShape()
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

#=========================================================================
#         mobject = node
#         if isinstance(node, str):
#             mobject = self.getMObject(node)
#
#         dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type,
#                                                        OpenMaya.MItDependencyGraph.kUpstream,
#                                                        OpenMaya.MItDependencyGraph.kDepthFirst,
#                                                        OpenMaya.MItDependencyGraph.kNodeLevel)
#
#         result = OpenMaya.MObjectArray()
#         while not dependency_graph.isDone():
#             current_item = dependency_graph.currentItem()
#             result.append(current_item)
#             dependency_graph.next()
#=========================================================================
        return result

    def getConnectedNode(self, node_type, mess=False):
        '''
            :param deformer <init> example OpenMaya.MFn.kClusterFilter(346)
            :param mess <bool>
            :return result <maya.OpenMaya.MObjectArray>
        '''
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
        if not node:
            return None
        if not isinstance(node, OpenMaya.MObject):
            node = self.getMObject(node)
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(node)
        dag_path_array = OpenMaya.MDagPathArray()
        mfn_skincluster.influenceObjects(dag_path_array)
        result = OpenMaya.MDagPathArray()
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
        '''
            example influence joint or object from lattice        
        '''
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
                print mfn_j.name()

    def getObjecTypes(self):
        self.object_types = {'mesh': OpenMaya.MFn.kMesh,
                             'blendShape': OpenMaya.MFn.kBlendShape,
                             'wire': OpenMaya.MFn.kWire,
                             'lattice': OpenMaya.MFn.kLattice,
                             'ffd': OpenMaya.MFn.kFFD,
                             # 'cluster': OpenMaya.MFn.kClusterFilter,
                             # 'clusterShape': OpenMaya.MFn.kCluster,

                             'cluster': OpenMaya.MFn.kCluster,
                             'clusterShape': OpenMaya.MFn.kClusterFilter,

                             'skinCluster': OpenMaya.MFn.kSkinClusterFilter,
                             'joint': OpenMaya.MFn.kJoint
                             }

    def getWeightsFromSelection(self):
        '''
        return mselection_list <maya.OpenMaya.MSelectionList>
        return component_weights <list> example [[maya.OpenMaya.MObject, OpenMaya.MFloatArray],
                                          [maya.OpenMaya.MObject, OpenMaya.MFloatArray]]
        '''

        mrich_selection = OpenMaya.MRichSelection()
        OpenMaya.MGlobal.getRichSelection(mrich_selection)

        mselection_list = OpenMaya.MSelectionList()
        mrich_selection.getSelection(mselection_list)
        mit_selection_list = OpenMaya.MItSelectionList(mselection_list)

        if not mit_selection_list.hasComponents():
            OpenMaya.MGlobal.displayError('your selection wrong!...')
            return None, None, None

        dag_paths = OpenMaya.MDagPathArray()
        # mobjects = OpenMaya.MObjectArray()
        indexs = []
        weights = []

        while not mit_selection_list.isDone():
            dag_path, mobject = OpenMaya.MDagPath(), OpenMaya.MObject()
            mit_selection_list.getDagPath(dag_path, mobject)
            if not mobject.hasFn(OpenMaya.MFn.kMeshVertComponent):
                OpenMaya.MGlobal.displayError('your some selection wrong!...')
                return None, None, None

            mfncomponent = OpenMaya.MFnComponent(mobject)
            index_component = OpenMaya.MFnSingleIndexedComponent(mobject)
            mfloat_array = OpenMaya.MFloatArray()
            mint_array = OpenMaya.MIntArray()

            for index in range(index_component.elementCount()):
                mindex = index_component.element(index)
                mweight = mfncomponent.weight(index)
                mint_array.append(mindex)
                mfloat_array.append(mweight.influence())

            dag_paths.append(dag_path)
            # mobjects.append(mobject)
            indexs.append(mint_array)
            weights.append(mfloat_array)
            mit_selection_list.next()

        return dag_paths, indexs, weights

    def setWeightsToSelection(self, deformer, dag_paths, indexs, weights):
        if not isinstance(deformer, OpenMaya.MObject):
            deformer = self.getMObject(deformer)

        deformer_mfn_geo_filter = OpenMayaAnim.MFnWeightGeometryFilter(
            deformer)

        for x in range(dag_paths.length()):
            current_dag_path = dag_paths[x]
            current_index = indexs[x]
            current_weight = weights[x]

            # indexs to components
            index_component = OpenMaya.MFnSingleIndexedComponent()
            components = index_component.create(
                OpenMaya.MFn.kMeshVertComponent)
            index_component.addElements(current_index)

            # add to deformer set
            mfn_geo_filter = OpenMayaAnim.MFnGeometryFilter(deformer)
            deformer_set = mfn_geo_filter.deformerSet()
            mfn_set = OpenMaya.MFnSet(deformer_set)
            mfn_set.addMember(current_dag_path, components)

            # set weight values
            deformer_mfn_geo_filter.setWeight(
                current_dag_path, components, current_weight)

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

        weight_geometry_filter = OpenMayaAnim.MFnWeightGeometryFilter(cluster_mobject)
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
            

    def getWeightsFromEnvelope(self, origin_object, envelope_object, attribute=None):
        if not isinstance(origin_object, OpenMaya.MObject):
            origin_object = self.getMObject(origin_object)
        if not isinstance(envelope_object, OpenMaya.MObject):
            envelope_object = self.getMObject(envelope_object)

        mfn_origin_mesh = OpenMaya.MFnMesh(origin_object)
        origin_point_array = OpenMaya.MFloatPointArray()
        mfn_origin_mesh.getPoints(origin_point_array, OpenMaya.MSpace.kObject)

        if attribute:
            node, attribute = attribute.split('.')
            mplug = self.getPlug(node, attribute)
            mplug.setInt(1)

        mfn_envelope_mesh = OpenMaya.MFnMesh(envelope_object)
        envelope_point_array = OpenMaya.MFloatPointArray()
        mfn_envelope_mesh.getPoints(
            envelope_point_array, OpenMaya.MSpace.kObject)

        if attribute:
            mplug.setInt(0)

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

    def getName(self, maya_object):

        if isinstance(maya_object, OpenMaya.MDagPath):
            # bprint maya_object.fullPathName()
            return maya_object.fullPathName()

        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            # print mfn_dependency_node.name()
            return mfn_dependency_node.name()

    def setSkinclusterWeights(self, skincluster, joint, shape, vertexs, weights):

        if not isinstance(skincluster, OpenMaya.MObject):
            skincluster = self.getMObject(skincluster)

        if not isinstance(joint, OpenMaya.MDagPath):
            joint = self.getDagPath(joint)

        if not isinstance(shape, OpenMaya.MDagPath):
            shape = self.getDagPath(shape)

        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(skincluster)
        joint_index = mfn_skincluster.indexForInfluenceObject(joint)

        old_values = OpenMaya.MFloatArray()

        for index in range(len(vertexs)):
            index_component = OpenMaya.MFnSingleIndexedComponent()
            component = index_component.create(OpenMaya.MFn.kMeshVertComponent)
            index_component.addElement(vertexs[index])

            mfn_skincluster.setWeights(shape, component, joint_index,
                                       weights[index], True, old_values)

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
            
            
    def getCenterPosition(self, dag_paths, type):
        x, y, z = 0, 0, 0        
        for each_dag_path in dag_paths:
            if type=='cluster':
                position = self.getClusterPosition(each_dag_path) 
            else:
                position = self.getJointPosition(each_dag_path)                           
            x += position[0]
            y += position[1]
            z += position[2]            
        center = [x/2, y/2, z/2]
        
        return center
    
    
    def createEmptyWeights(self, dag_path):
        
        if not isinstance(dag_path, OpenMaya.MDagPath):
            dag_path = self.getDagPath(dag_path)
            
        mmit_mesh_vertex = OpenMaya.MItMeshVertex(dag_path)    
        
        weights = OpenMaya.MFloatArray()
        memberships = OpenMaya.MIntArray()
    
        while not mmit_mesh_vertex.isDone ():
            weights.append(0)
            memberships.append(False)
            mmit_mesh_vertex.next()            
        return weights, memberships
    
    
    def addInfluence(self, joint, geometrys):
        if isinstance(joint, OpenMaya.MDagPath):
            joint = joint.fullPathName()        
        for each_geometry in geometrys:
            
            m_object = self.getMObject(each_geometry)
            m_skinclusters = self.getDeformerNodes(m_object, OpenMaya.MFn.kSkinClusterFilter)

            if not m_skinclusters.length():
                OpenMaya.MGlobal.displayWarning('\nCan not find skincluster \"%s\"' % each_geometry.encode())
                continue
            
            skincluster = self.getName(m_skinclusters[0])
            OpenMaya.MGlobal.executeCommand('skinCluster -e -ug -dr 4 -ps 0 \
                        -ns 10 -lw false -wt 0 -ai {} {}'.format(joint, skincluster))
            
            plug = self.getPlug(joint, 'liw') 
            plug.setBool(False)
            
        return True
    
    
    def findxIndexFromSkincluster(self, mfn_skincluster, joint_dag_path):        
        joints_dag_path_array = OpenMaya.MDagPathArray()
        mfn_skincluster.influenceObjects(joints_dag_path_array)
                
        influence_indexs = {}        
        for index in range (joints_dag_path_array.length()):
            current_joint = joints_dag_path_array[index].fullPathName()
            influence_indexs.setdefault(current_joint, index)
            
        if joint_dag_path.fullPathName() not in influence_indexs:
            OpenMaya.MGlobal.displayWarning('\nCan not find index of \"%s\"' % joint_dag_path.fullPathName())
            return
            
        return influence_indexs[joint_dag_path.fullPathName()]
            


