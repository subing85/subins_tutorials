import json

from maya import OpenMaya


class Connect(object):
    '''
        from uv_export.plugin import studioMaya
        reload(studioMaya)
        sm = studioMaya.Connect()
    '''

    def __init__(self, **kwargs):
        self.node = None
        if 'node' in kwargs:
            self.node = kwargs['node']
        self.file_path = self.getDirectory()

    def getDirectory(self):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'workspace -q -dir',
            mcommand_result,
            True,
            True
        )
        results = []
        mcommand_result.getResult(results)
        return results[0]

    def getDagPath(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getData(self, mdag_path):
        '''
            from uv_export.plugin import studioMaya
            reload(studioMaya)
            sm = studioMaya.Connect(node='pPlaneShape1')
            mdag_path = sm.getDagPath()
            sm.getData(mdag_path)       
        '''
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
        final_data = {
            'uv_sets': uv_data,
            # 'shape_node': mfn_mesh.name().encode()
            'shape_node': mdag_path.fullPathName()
        }
        return final_data

    def setData(self, data):
        self.node = data['shape_node']
        uv_sets = data['uv_sets']
        mdag_path = self.getDagPath()
        mfn_mesh = OpenMaya.MFnMesh(mdag_path)
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
            else:
                set_name = mfn_mesh.createUVSetWithName(set_name)
            mfn_mesh.setUVs(u_array, v_array, set_name)
            mfn_mesh.assignUVs(uv_counts, uv_ids, set_name)
        mfn_mesh.updateSurface()

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

    def write(self, path, data):
        try:
            with open(path, 'w') as file:
                file.write(json.dumps(data, indent=4))
            OpenMaya.MGlobal.displayInfo('Write success!...')
        except Exception as error:
            OpenMaya.MGlobal.displayError(str(error))

        #======================================================================
        # OpenMaya.MGlobal.displayInfo('ssssssssssss')
        # OpenMaya.MGlobal.displayWarning()
        # OpenMaya.MGlobal.displayError()
        #======================================================================
        
    def read(self, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
            OpenMaya.MGlobal.displayInfo('Read success!...')
            return data
        except Exception as error:
            OpenMaya.MGlobal.displayError(str(error))        
        
        
        