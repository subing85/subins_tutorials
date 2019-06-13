'''
stdioMaya.py 0.0.1 
Date: January 01, 2019
Last modified: June 13, 2019
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


class Maya(object):

    def __init__(self, **kwargs):
        if 'node' in kwargs:
            node = kwargs['node']

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

    def getName(self, maya_object):
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependency_node.name().encode()

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

    def getObjectShadingEngine(self, mobject):
        shading_engine_array = self.getDependences(
            mobject, OpenMaya.MFn.kShadingEngine)
        return shading_engine_array

    def getSelectedObjectShapeNode(self, shape_type=None):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        dag_path_array = OpenMaya.MDagPathArray()
        for x in range(mselection.length()):
            dag_path = OpenMaya.MDagPath()
            try:
                mselection.getDagPath(x, dag_path)
            except:
                dag_path = None
            if not dag_path:
                continue
            try:
                dag_path.extendToShape()
            except:
                dag_path = None
            if not dag_path:
                continue
            if shape_type:
                if not dag_path.hasFn(shape_type):
                    continue
            dag_path_array.append(dag_path)
        return dag_path_array

    def assignToShadingGroup(self, mobject, shading_group=None):
        if isinstance(mobject, str):
            mobject = self.getMObject(mobject)
        if isinstance(mobject, OpenMaya.MDagPath):
            mobject = mobject.node()
        if not shading_group:
            shading_group = self.getMObject('initialShadingGroup')
        if isinstance(shading_group, str):
            shading_group = self.getMObject(shading_group)
        mfn_set = OpenMaya.MFnSet(shading_group)
        mfn_set.addMember(mobject)

    def assignToMaterial(self, objects, shading_group):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand('sets -e -forceElement %s %s;' % (
            shading_group, ' '.join(objects)), mcommand_result,  True, True)
        results = []
        mcommand_result.getResult(results)
        return results

    def getAssignComponents(self, shading_group):
        if isinstance(shading_group, str):
            shading_group = self.getMObject(shading_group)
        mfn_set = OpenMaya.MFnSet(shading_group)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        component_data = {}
        if not selection_list.length():
            return mfn_set.name(), component_data
        for index in range(selection_list.length()):
            components = []
            selection_list.getSelectionStrings(components)
            if components in component_data.values():
                continue
            component_data.setdefault(index, components)
        return mfn_set.name(), component_data

    def getAssignObjects(self, shading_group):
        if isinstance(shading_group, str):
            shading_group = self.getMObject(shading_group)
        mfn_set = OpenMaya.MFnSet(shading_group)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        objects = []
        if not selection_list.length():
            return objects
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            m_object = OpenMaya.MObject()
            selection_list.getDagPath(index, m_dag_path, m_object)
            objects.append(m_dag_path.partialPathName())
        return objects

    def hasValidShadingEngine(self, shading_group, object=None):
        if isinstance(shading_group, str):
            shading_group = self.getMObject(shading_group)
        if isinstance(object, OpenMaya.MDagPath):
            object = object.partialPathName()
        if not shading_group.hasFn(OpenMaya.MFn.kShadingEngine):
            return False
        mfn_set = OpenMaya.MFnSet(shading_group)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        if not selection_list.length():
            return False
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            m_object = OpenMaya.MObject()
            selection_list.getDagPath(index, m_dag_path, m_object)
            if m_dag_path.partialPathName() == object:
                return True
        return False

    def undoChunk(self, tag):
        OpenMaya.MGlobal.executeCommand(
            'undoInfo -%sChunk;' % tag, False, False)

# end ####################################################################
