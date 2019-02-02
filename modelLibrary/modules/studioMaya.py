'''
stdioMaya.py 0.0.1 
Date: January 01, 2019
Last modified: January 26, 2019
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
            dag_path.extendToShape()
            if not dag_path:
                continue
            if shape_type:
                if not dag_path.hasFn(shape_type):
                    continue
            dag_path_array.append(dag_path)
        return dag_path_array

    def getParentNode(self, mobject):
        if not isinstance(mobject, OpenMaya.MObject):
            mobject = self.getMObject(mobject)
        mfn_dag_node = OpenMaya.MFnDagNode(mobject)
        parent_m_object = mfn_dag_node.parent(0)
        parent_mfn_dag_node = OpenMaya.MFnDagNode(parent_m_object)
        m_dag_path = OpenMaya.MDagPath()
        parent_mfn_dag_node.getPath(m_dag_path)
        return m_dag_path

    def createFloatArray(self, python_list):
        mfloat_array = OpenMaya.MFloatArray()
        mscript_util = OpenMaya.MScriptUtil()
        mscript_util.createFloatArrayFromList(python_list, mfloat_array)
        return mfloat_array

    def createIntArray(self, python_list):
        mint_array = OpenMaya.MIntArray()
        mscript_util = OpenMaya.MScriptUtil()
        mscript_util.createIntArrayFromList(python_list, mint_array)
        return mint_array

    def createFloatPointArray(self, python_list):
        mfloat_point_array = OpenMaya.MFloatPointArray()
        for x, y, z, w in python_list:
            mfloat_point_array.append(x, y, z, w)
        return mfloat_point_array

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

    def undoChunk(self, tag):
        OpenMaya.MGlobal.executeCommand('undoInfo -%sChunk;' % tag, False, False)

# end ####################################################################
