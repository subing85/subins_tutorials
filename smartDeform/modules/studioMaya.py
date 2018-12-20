from maya import OpenMaya
from maya import OpenMayaAnim


class Maya(object):

    def __init__(self, **kwargs):
        if 'node' in kwargs:
            node = kwargs['node']

        self.getObjecTypes()
        
    def create_cluster(self, name, position, parent=None):
        pass
    
    def create_Joint(self, name, position, parent=None):
        pass
    
    def create_dag_node(self, name, position, parent=None):
        pass
    
    def create_dependency_node(self, name, parent=None):
        pass

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

    def getVertexsMObjects(self, node):
        dag_path = self.getDagPath(node)
        mit_geometry = OpenMaya.MItGeometry(dag_path)
        mselection = OpenMaya.MSelectionList()
        
        while not mit_geometry.isDone():
            component = mit_geometry.currentItem()
            mselection.add(dag_path, component, True)
            mit_geometry.next()

        components = OpenMaya.MObject()
        mselection.getDagPath(0, dag_path, components)
        return components

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

    def getShapeNode(self, node, shape_type=None):
        mdag_path = self.getDagPath(node)
        mdag_path.extendToShape()
        if not mdag_path:
            return
        if shape_type:
            if not mdag_path.hasFn(shape_type):
                return
        return mdag_path

    def getDeformerNodes(self, node, node_type):
        mobject = node
        if isinstance(node, str):
            mobject = self.getMObject(node)

        dependency_graph = OpenMaya.MItDependencyGraph(mobject, node_type,
                                                       OpenMaya.MItDependencyGraph.kUpstream,
                                                       OpenMaya.MItDependencyGraph.kDepthFirst,
                                                       OpenMaya.MItDependencyGraph.kNodeLevel)

        result = OpenMaya.MObjectArray()
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            result.append(current_item)
            dependency_graph.next()
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
            mselectionList = OpenMaya.MSelectionList()
            mselectionList.add("%s.weight" % mfndependency_node.name())
            mselectionList.getPlug(0, mplug)
            for x in range(mplug.numElements()):
                current_element = mplug.elementByLogicalIndex(x)
                mplug_array.append(current_element)

        return mplug_array
    
    def getDeformerJoints(self, mobjects):
        '''
            example influence joint or object from lattice        
        '''
        joint_data = {}        
        for index in range (mobjects.length()):
            skinclusters = self.getDeformerNodes(mobjects[index], OpenMaya.MFn.kSkinClusterFilter)       
            if not skinclusters:
                continue
            joints = self.getSkinclusterJoints(skinclusters[0])
            if not joints:
                continue
            joint_data.setdefault(mobjects[index], joints)
        return joint_data
    
    def getClusterHandle(self, mobjects):
        cluster_data = {}
        for index in range (mobjects.length()):            
            cluster_shape = self.getDeformerNodes(mobjects[index], OpenMaya.MFn.kCluster)
            if cluster_shape.length()==0:
                continue
                       
            mobject_array = OpenMaya.MObjectArray()
            for x in range (cluster_shape.length()):    
                mfn_dag_node = OpenMaya.MFnDagNode(cluster_shape[x])
                parent_mobject = mfn_dag_node.parent(0)
                mobject_array.append(parent_mobject)
            cluster_data.setdefault(mobjects[index], mobject_array)
        return cluster_data
 
    
    
    
    def getWireDeformerData(self, mwire_objects):
        
        for index in range (mwire_objects.length()):
            curve_object = self.getDeformerNodes(mwire_objects[index], OpenMaya.MFn.kCurve)

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

        pass

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
        dag_paths = []
        mobjects = []
        weights = []

        while not mit_selection_list.isDone():
            dag_path, mobject = OpenMaya.MDagPath(), OpenMaya.MObject()
            mit_selection_list.getDagPath(dag_path, mobject)
            if not mobject.hasFn(OpenMaya.MFn.kMeshVertComponent):
                continue

            mfncomponent = OpenMaya.MFnComponent(mobject)
            index_component = OpenMaya.MFnSingleIndexedComponent(mobject)
            mfloat_array = OpenMaya.MFloatArray()

            for index in range(index_component.elementCount()):
                mweight = mfncomponent.weight(index)
                mfloat_array.append(mweight.influence())

            dag_paths.append(dag_path)
            mobjects.append(mobject)
            weights.append(mfloat_array)
            mit_selection_list.next()

        return dag_paths, mobjects, weights

    def setWeightsToSelection(self, deformer, dag_paths, mobjects, weights):
        if not isinstance(deformer, OpenMaya.MObject):
            deformer = self.getMObject(deformer)

        deformer_mfn_geo_filter = OpenMayaAnim.MFnWeightGeometryFilter(
            deformer)

        for x in range(len(dag_paths)):
            current_dag_path = dag_paths[x]
            current_mobject = mobjects[x]
            current_weight = weights[x]

            # add to deformer set
            mfn_geo_filter = OpenMayaAnim.MFnGeometryFilter(deformer)
            deformer_set = mfn_geo_filter.deformerSet()
            mfn_set = OpenMaya.MFnSet(deformer_set)
            mfn_set.addMember(current_dag_path, current_mobject)

            # set weight values
            deformer_mfn_geo_filter.setWeight(
                current_dag_path, current_mobject, current_weight)

    def setClusterWeights(self, object, cluster,  weights):

        cluster_mobject = self.getMObject(cluster)
        dag_path = self.getDagPath(object)
        components = self.getVertexsMObjects(object)

        mfn_geo_filter = OpenMayaAnim.MFnGeometryFilter(cluster_mobject)
        deformer_set = mfn_geo_filter.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        mfn_set.addMember(dag_path, components)


        weight_geometry_filter = OpenMayaAnim.MFnWeightGeometryFilter (cluster_mobject)
        weight_geometry_filter.setWeight (dag_path, components, weights)

        

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
    
    def maya_object_to_python_string(self, maya_objects):        
        for index in range (maya_objects.length()):            
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_objects[index])
            print maya_objects[index], '\t',  maya_objects[index].apiTypeStr(), mfn_dependency_node.name()   
     
