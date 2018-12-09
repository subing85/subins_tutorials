from maya import OpenMaya
from maya import OpenMayaAnim


class Maya(object):

    def __init__(self, **kwargs):
        if 'node' in kwargs:
            self.node = kwargs['node']

    def getDagPath(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        dag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, dag_path)
        return dag_path

    def getDependNode(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject

    def getShapeNode(self, shape_type):
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
            if not dag_path.hasFn(shape_type):
                continue
            shapes.append(dag_path)
        return shapes

    def getDeformNode(self, deformer_type):
        '''
            :param deformer <init> example OpenMaya.MFn.kClusterFilter(346)
        '''
        current_node = self.getDependNode()
        stack = []
        nodes = [current_node]
        result = OpenMaya.MObjectArray()
        while nodes:
            node = nodes.pop()
            mfn_dependency_node = OpenMaya.MFnDependencyNode(node)
            attribute_count = mfn_dependency_node.attributeCount()
            for x in range(attribute_count):
                attribute = mfn_dependency_node.attribute(x)
                plug = mfn_dependency_node.findPlug(attribute)
                plug_array = OpenMaya.MPlugArray()
                plug.connectedTo(plug_array, True, False)
                current_array = plug_array[0]

                if not current_array:
                    continue
                mobject = current_array.node()
                if not mobject.hasFn(deformer_type):
                    continue
                my_node = OpenMaya.MFnDependencyNode(mobject)
                result.append(my_node.object())
                if current_array.node() in stack:
                    continue

                stack.append(current_array.node())
                nodes.append(current_array.node())
        return result
