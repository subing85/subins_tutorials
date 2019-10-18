from imath import *
import math
import pymel.core as pm
import alembic
from alembic.Abc import *
from alembic.AbcGeom import *

from maya_abc_exporter.maya_mesh_data import MeshData
from maya_abc_exporter.archive_info import ArchiveInfo


def setToIMathArray(type_traits, *in_list):
    """
    Set to imath array.

    :Param iTPTraits: alembic abc type traits.
                      (can look at Alembic/Abc/TypedPropertyTraits.h)
                      Ex: Int32TPTraits, P3fTPTraits,...
    :Param iList:
    :Return: imath array object
    :Rtype: imath.V3fArray
    """
    array = type_traits.arrayType(len(in_list))
    for i in range(len(in_list)):
        array[i] = in_list[i]
    return array


class MeshWriter(object):
    def __init__(self, dag_path=None, filename=None, archive_info=None):
        super(MeshWriter, self).__init__()
        self.dag_path = dag_path
        self.filename = filename
        self.archive_info = archive_info or ArchiveInfo()
        self.custom_param = None

    def write_poly(self):
        mesh_schema = self.meshObj.getSchema()

        #   Set sample
        frame_range = self.archive_info.end_frame - self.archive_info.start_frame + 1
        for i in range(frame_range):
            currentFrame = self.archive_info.start_frame + i
            pm.currentTime(currentFrame)

            # Get current mesh data
            mesh_data = MeshData(self.dag_path)

            points = mesh_data.get_points()
            imath_point_array = setToIMathArray(P3fTPTraits, *points)

            vids, fcounts = mesh_data.get_vertices()
            imath_face_indices = setToIMathArray(Int32TPTraits, *list(vids))
            imath_face_counts = setToIMathArray(Int32TPTraits, *list(fcounts))

            bbox_max_point, bbox_min_point = mesh_data.get_bbox_end_points()
            imath_bbox = Box3d(V3d(bbox_min_point.x, bbox_min_point.y, bbox_min_point.z), V3d(bbox_max_point.x, bbox_max_point.y, bbox_max_point.z))

            trans_info = mesh_data.get_trasform_info()

            # Set xform sample
            xsamp = XformSample()
            xsamp.setTranslation(V3d(*trans_info[0]))
            xsamp.setRotation(V3d(*trans_info[1][0]), math.degrees(trans_info[1][1]))
            xsamp.setScale(V3d(*trans_info[2]))
            self.xform.getSchema().set(xsamp)

            # Set mesh sample
            mesh_samp = OPolyMeshSchemaSample(imath_point_array, imath_face_indices, imath_face_counts)
            mesh_samp.setSelfBounds(imath_bbox)
            mesh_schema.set(mesh_samp)

    def add_attribute(self, prop_name="custom", geometry_scope=GeometryScope.kVertexScope):
        oarch = alembic.Abc.OArchive(self.filename)
        top = oarch.getTop()
        obj_name = self.dag_path.partialPathName()
        tsidx = top.getArchive().addTimeSampling(self.archive_info.ts)

        #   Create top xform
        self.xform = OXform(top, str(obj_name), tsidx)

        #   Create mesh
        self.meshObj = OPolyMesh(self.xform, '{}Shape'.format(obj_name), tsidx)

        #   Add custom property
        arb_geom_param = self.meshObj.getSchema().getArbGeomParams()
        parent = arb_geom_param

        #   Add custom property
        self.custom_param = OP3fGeomParam(parent, prop_name, False, geometry_scope, 1)
        return self.custom_param

    def set_attribute_value(self, value, geometry_scope=GeometryScope.kVertexScope):
        samp = OP3fGeomParamSample(value, geometry_scope)
        samp.setVals(value)
        self.custom_param.set(samp)
        self.custom_param.setTimeSampling(self.archive_info.ts)
