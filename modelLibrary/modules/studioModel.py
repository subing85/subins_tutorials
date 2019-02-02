'''
stdioModel.py 0.0.1 
Date: January 16, 2019
Last modified: January 26, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os

from datetime import datetime

from maya import OpenMaya

from modelLibrary.utils import platforms
from modelLibrary.modules import readWrite
from modelLibrary.modules import studioMaya
from modelLibrary.modules import studioImage


class Model(studioMaya.Maya):

    def __init__(self, geometry_dag_paths=None, path=None):
        self.geometry_dag_paths = geometry_dag_paths
        self.path = path
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()

    def had_valid(self, publish_file):
        rw = readWrite.ReadWrite(t='polygon')
        rw.file_path = publish_file
        result = rw.has_valid()
        return result

    def create(self, fake=False):

        rw = readWrite.ReadWrite(t='polygon')
        rw.file_path = self.path
        if fake:
            data = rw.get_info()
            return data

        data = rw.get_data()
        self.undoChunk('open')
        for index, polydon_data in data.items():
            self.create_polygon_mesh(
                polydon_data, dag_path=self.geometry_dag_paths)
        self.undoChunk('close')
        OpenMaya.MGlobal.executeCommand('undoInfo -closeChunk;')

        return True

    def save(self, file_path, name, image, user_comment=None):
        data = {}
        for index in range(self.geometry_dag_paths.length()):
            polygon_data = self.get_polygon_mesh(
                self.geometry_dag_paths[index])
            data.setdefault(index, polygon_data)
        comment = '%s %s - polygon' % (self.tool_kit_name, self.version)
        if user_comment:
            comment = '%s %s - polygon\n%s' % (
                self.tool_kit_name, self.version, user_comment)
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about maya polygon'
        type = 'polygon'
        valid = True
        data = data
        tag = self.tool_kit_object
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                                 d=description, t=type, v=valid, data=data, tag=tag,
                                 path=file_path, name=name, format='model')
        mode_path = rw.create()
        studio_image = studioImage.ImageCalibration(
            path=file_path, name=name, format='png')
        image_path = studio_image.writeImage(image)
        print '\nresult', mode_path, image_path

    def had_file(self, dirname, name):
        rw = readWrite.ReadWrite(
            path=dirname, name=name, format='model', t='polygon')
        return rw.has_file()

    def set_polygon_mesh(self):
        data = self.get_polygon_mesh(self.object)
        return data

    def get_image(self, model_path):
        return model_path.replace('.model', '.png')

    def get_polygon_mesh(self, m_dag_path):
        mfn_mesh = OpenMaya.MFnMesh(m_dag_path)
        point_array = OpenMaya.MFloatPointArray()
        mfn_mesh.getPoints(point_array, OpenMaya.MSpace.kObject)
        vertex_count = OpenMaya.MIntArray()
        vertex_array = OpenMaya.MIntArray()
        mfn_mesh.getVertices(vertex_count, vertex_array)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        uvs_data = {}
        for index in range(len(set_names)):
            u_array = OpenMaya.MFloatArray()
            v_array = OpenMaya.MFloatArray()
            mfn_mesh.getUVs(u_array, v_array, set_names[index])
            uv_counts = OpenMaya.MIntArray()
            uv_ids = OpenMaya.MIntArray()
            mfn_mesh.getAssignedUVs(uv_counts, uv_ids, set_names[index])
            current_set = {}
            current_set['set_name'] = set_names[index]
            current_set['u_array'] = list(u_array)
            current_set['v_array'] = list(v_array)
            current_set['uv_counts'] = list(uv_counts)
            current_set['uv_ids'] = list(uv_ids)
            uvs_data.setdefault(index, current_set)
        vertice_list = []
        for index in range(point_array.length()):
            vertice_list.append(
                (point_array[index].x, point_array[index].y, point_array[index].z, point_array[index].w))
        parent_mobject = mfn_mesh.parent(0)
        parent_mfn_dag_node = OpenMaya.MFnDagNode(parent_mobject)
        data = {}
        data['name'] = {
            'transform': parent_mfn_dag_node.name().encode(),
            'shape': mfn_mesh.name().encode()
        }
        data['vertices'] = vertice_list
        data['vertex_count'] = list(vertex_count)
        data['vertex_list'] = list(vertex_array)
        data['uvs'] = uvs_data
        data['num_edges'] = mfn_mesh.numEdges()
        data['num_face_vertices'] = mfn_mesh.numFaceVertices()
        data['num_polygons'] = mfn_mesh.numPolygons()
        data['num_normals'] = mfn_mesh.numNormals()
        data['num_uv_sets'] = mfn_mesh.numUVSets()
        data['num_uvs'] = mfn_mesh.numUVs()
        data['num_vertices'] = mfn_mesh.numVertices()
        return data

    def create_polygon_mesh(self, data, dag_path=None):
        vertex_array = self.createFloatPointArray(data['vertices'])
        vertex_count = self.createIntArray(data['vertex_count'])
        vertex_list = self.createIntArray(data['vertex_list'])
        num_vertices = data['num_vertices']
        num_polygons = data['num_polygons']
        uvs = data['uvs']
        if dag_path:
            if not isinstance(dag_path, OpenMaya.MDagPath):
                dag_path = self.getDagPath(dag_path)

            mfn_mesh = OpenMaya.MFnMesh(dag_path)
            self.delete_all_uv_sets(dag_path)
        else:
            mfn_mesh = OpenMaya.MFnMesh()
            mfn_mesh.create(num_vertices, num_polygons,
                            vertex_array, vertex_count, vertex_list)
        uv_set_names = []
        mfn_mesh.getUVSetNames(uv_set_names)
        for index, uv_set in uvs.iteritems():
            set_name = uv_set['set_name']
            u_array = self.createFloatArray(uv_set['u_array'])
            v_array = self.createFloatArray(uv_set['v_array'])
            uv_counts = self.createIntArray(uv_set['uv_counts'])
            uv_ids = self.createIntArray(uv_set['uv_ids'])
            new_set_name = uv_set_names[0]
            if int(index) > 0:
                new_set_name = mfn_mesh.createUVSetWithName(set_name)
            mfn_mesh.setUVs(u_array, v_array, new_set_name)
            mfn_mesh.assignUVs(uv_counts, uv_ids, new_set_name)
        self.assignToShadingGroup(mfn_mesh.object())
        mfn_mesh.setName(data['name']['shape'].encode())
        parent_mobject = mfn_mesh.parent(0)
        parent_mfn_dag_node = OpenMaya.MFnDagNode(parent_mobject)
        parent_mfn_dag_node.setName(data['name']['transform'].encode())
        mfn_mesh.updateSurface()

    def delete_all_uv_sets(self, dag_path):
        mfn_mesh = OpenMaya.MFnMesh(dag_path)
        setNames = []
        mfn_mesh.getUVSetNames(setNames)
        for each in setNames[1:]:
            try:
                mfn_mesh.deleteUVSet(each)
            except Exception as error:
                print '\nUV delete error', error

    def copy_uvs(self, source_dag_path, target_dag_path):
        polygon_data = self.getPolygonMesh(source_dag_path)
        self.createPolygonMesh(polygon_data, dag_path=target_dag_path)

# end ####################################################################
