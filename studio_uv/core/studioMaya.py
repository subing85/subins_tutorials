'''
studioMaya.py 0.0.1 
Date: June 24, 2019
Last modified: August 03, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    Core functions
'''

import json

from maya import OpenMaya


class Connect(object):

    def __init__(self, **kwargs):
        self.node = None
        if 'node' in kwargs:
            self.node = kwargs['node']

    def getDagPath(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getData(self, mdag_path):
        mfn_mesh = OpenMaya.MFnMesh(mdag_path)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        uv_data = {}
        for index, set_name in enumerate(set_names):
            u_array = OpenMaya.MFloatArray()
            v_array = OpenMaya.MFloatArray()
            mfn_mesh.getUVs(u_array, v_array, set_name)
            uv_counts = OpenMaya.MIntArray()
            uv_ids = OpenMaya.MIntArray()
            mfn_mesh.getAssignedUVs(uv_counts, uv_ids, set_name)
            current_set_data = {
                'set_name': set_name.encode(),
                'u_array': list(u_array),
                'v_array': list(v_array),
                'uv_counts': list(uv_counts),
                'uv_ids': list(uv_ids)
            }
            uv_data.setdefault(index, current_set_data)
        num_polygons, polygon_vertices = self.getFacesVertices(mfn_mesh)
        final_data = {
            'uv_sets': uv_data,
            'long_name': mdag_path.fullPathName().encode(),
            'short_name': mdag_path.fullPathName().split('|')[-1],
            'shape_node': mfn_mesh.name().encode(),
            'num_polygons': num_polygons,
            'polygon_vertices': polygon_vertices
        }
        return final_data

    def setData(self, data):
        self.node = data['shape_node']
        uv_sets = data['uv_sets']
        mdag_path = self.getDagPath()
        mfn_mesh = OpenMaya.MFnMesh(mdag_path)

        validate = self.validateData(mfn_mesh, data)
        if not validate:
            message = 'readError: not match from data <%s> to scene <%s> polygon' % (
                data['shape_node'], mdag_path.fullPathName()
            )
            OpenMaya.MGlobal.displayWarning(message)
            return False
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        self.delete_uv_sets(mfn_mesh, set_names[1:])
        sorted_index = sorted(uv_sets.keys())
        for index in sorted_index:
            set_name = uv_sets[index]['set_name']
            u_array = self.createFloatArray(uv_sets[index]['u_array'])
            v_array = self.createFloatArray(uv_sets[index]['v_array'])
            uv_counts = self.createIntArray(uv_sets[index]['uv_counts'])
            uv_ids = self.createIntArray(uv_sets[index]['uv_ids'])
            if int(index) == 0:
                set_name = set_names[0]
                mfn_mesh.clearUVs(set_name)
            else:
                set_name = mfn_mesh.createUVSetWithName(set_name)
            # mfn_mesh.setCurrentUVSetName(set_name)
            # mfn_mesh.setSomeUVs(uv_ids, u_array, v_array, set_name)
            mfn_mesh.setUVs(u_array, v_array, set_name)
            mfn_mesh.assignUVs(uv_counts, uv_ids, set_name)
        mfn_mesh.updateSurface()
        return True

    def clear(self):
        mdag_path = self.getDagPath()
        mfn_mesh = OpenMaya.MFnMesh(mdag_path)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        self.delete_uv_sets(mfn_mesh, set_names[1:])
        mfn_mesh.clearUVs()
        mfn_mesh.updateSurface()

    def validateData(self, mfn_mesh, data):
        num_polygons, polygon_vertices = self.getFacesVertices(mfn_mesh)
        if num_polygons != data['num_polygons']:
            return False
        if polygon_vertices != data['polygon_vertices']:
            return False
        return True

    def getFacesVertices(self, mfn_mesh=None):
        num_polygons = mfn_mesh.numPolygons()
        polygon_vertices = []
        for index in range(num_polygons):
            mint_array = OpenMaya.MIntArray()
            mfn_mesh.getPolygonVertices(index, mint_array)
            polygon_vertices.append(list(mint_array))
        return num_polygons, polygon_vertices

    def getMfnMesh(self):
        mdag_path = self.getDagPath()
        mfn_mesh = OpenMaya.MFnMesh(mdag_path)
        return mfn_mesh

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

    def delete_uv_sets(self, mfn_mesh, set_names):
        for set_name in set_names:
            try:
                mfn_mesh.deleteUVSet(set_name)
            except Exception as error:
                print '\nDeleteError', error

    def write(self, path, data, result=True):
        try:
            with open(path, 'w') as file:
                file.write(json.dumps(data, indent=4))
            if result:
                OpenMaya.MGlobal.displayInfo('// Result: Write success!...')
        except Exception as error:
            OpenMaya.MGlobal.displayError(str(error))

    def read(self, path, result=True):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
            if result:
                OpenMaya.MGlobal.displayInfo('// Result: Read success!...')
            return data
        except Exception as error:
            OpenMaya.MGlobal.displayError(str(error))
