import maya.OpenMaya as om
from imath import *


class MeshData(object):
     def __init__(self, dagpath):
        super(MeshData, self).__init__()

        self.mesh_fn = om.MFnMesh(dagpath)
        self.dag_node = om.MFnDagNode(dagpath)

     def get_points(self):
         """
         Storage for the vertex list for this mesh into point array.

         :Return:
                    EX:
                     [V3f(-11.8104429, 106.812759, -149.725311),
                     V3f(-11.8439445, 106.808167, -149.66568),
                     V3f(-11.8298216, 106.813248, -149.688171)]
         """
         m_point_array = om.MFloatPointArray()
         self.mesh_fn.getPoints(m_point_array)
         points = list()
         for i in range(m_point_array.length()):
             point = m_point_array[i]
             points.append(V3f(point.x, point.y, point.z))
         return points

     def get_vertices(self):
         """
         :Return: m_vid_array - Storage for the vertex list.
                  m_face_count_array - Vertex count per polygon.

         """
         m_vid_array = om.MIntArray()
         m_face_count_array = om.MIntArray()
         self.mesh_fn.getVertices(m_face_count_array, m_vid_array)
         return [m_vid_array, m_face_count_array]

     def get_bbox_end_points(self):
         """

         :Return: list of twp bounding box points
         :Rtype: `list(OpenMaya.MPoint)`
         """
         max = self.dag_node.boundingBox().max()
         min = self.dag_node.boundingBox().min()
         return [max, min]

     def get_trasform_info(self):
         """

         :Return: list of translation, rotation, and scales
                  Ex:
                    translation
                    # Result: [0.0, 0.0, 0.0] #
                    rotation
                    # Result: [[0.0, 0.0, 1.0], 0.0] #
                    scales
                    # Result: [1.0, 1.0, 1.0] #
         """
         #  Get translation
         transMatrix = om.MTransformationMatrix(self.dag_node.transformationMatrix())
         translation = transMatrix.translation(om.MSpace.kWorld)
         translation = list(translation)

         #  Get rotation
         q = transMatrix.rotation()
         v = om.MVector()
         angUtil = om.MScriptUtil()
         angUtil.createFromDouble(0)
         angDoub = angUtil.asDoublePtr()
         q.getAxisAngle(v, angDoub)
         a = om.MScriptUtil.getDouble(angDoub)
         rotation = [[v[x] for x in range(3)], a]

         #  Get scale
         scaleUtil = om.MScriptUtil()
         scaleUtil.createFromList([0,0,0], 3)
         scaleVec = scaleUtil.asDoublePtr()
         transMatrix.getScale(scaleVec, om.MSpace.kWorld)
         scales = [om.MScriptUtil.getDoubleArrayItem(scaleVec,i) for i in range(0, 3)]

         return [translation, rotation, scales]



