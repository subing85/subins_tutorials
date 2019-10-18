import os
import maya.OpenMaya as om
import pymel.core as pm
from alembic.Abc import *

from maya_abc_exporter.attribute_writer import MeshWriter
from maya_abc_exporter.archive_info import ArchiveInfo
from maya_abc_exporter.mesh_data import MeshData
from maya_abc_exporter.utils import get_dag_path_list, setToIMathArray, get_selected_obj_names

DEFAULT_OUT_FILENAME = 'out'
FILE_EXTENSION = 'abc'


def get_filepath_name(file_dir=None, filename=DEFAULT_OUT_FILENAME):
    if not file_dir:
        file_dir = os.path.dirname(os.path.abspath(__file__))
    else:
        file_dir = file_dir

    file_path_name = os.path.abspath(os.path.join(file_dir, filename))
    file_path_name = '{filename}.{ext}'.format(filename=file_path_name, ext=FILE_EXTENSION)
    return file_path_name


class MayaAbcExporter(object):
    def __init__(self):
        super(MayaAbcExporter, self).__init__()

        self.abc_info = ArchiveInfo()
        self._frame_range = [1, 1]
        self.output_dir = None

    @property
    def frame_range(self):
        return self._frame_range

    @frame_range.setter
    def frame_range(self, value):
        self.abc_info.start_frame = value[0]
        self.abc_info.end_frame = value[1]
        self._frame_range = value

    @property
    def output_dir(self):
        return self._output_dir

    @output_dir.setter
    def output_dir(self, filepath):
        if not filepath:
            self._output_dir = pm.workspace(q=True, fullName=True)
        else:
            self._output_dir = filepath

    def export_selected_mesh(self):
        sels = get_selected_obj_names()
        if len(sels)>1 or not sels:
            print 'please select one mesh.'
            return
        all_dagpaths = get_dag_path_list(obj_name=sels[0])
        for dag_path in all_dagpaths:
            obj_name = dag_path.partialPathName()

            filename = get_filepath_name(file_dir=self.output_dir, filename=obj_name)

            mesh_data = MeshData(dag_path)
            points = mesh_data.get_points()
            imath_point_array = setToIMathArray(P3fTPTraits, *points)

            mesh_writer = MeshWriter(dag_path=dag_path, filename=filename, archive_info=self.abc_info)
            mesh_writer.add_attribute(prop_name="custom")
            mesh_writer.set_attribute_value(value=imath_point_array)
            mesh_writer.write_poly()
            print 'Save to ', filename