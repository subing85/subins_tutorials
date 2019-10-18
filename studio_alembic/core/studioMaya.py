'''
stdioMaya.py 0.0.1 
Date: January 01, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    stdioMaya is the function set for manage the maya objects.
    Its is custom api package of Maya API based on requirements.
    The purpose of the stdioMaya to validate, getting and setting maya objects.  
'''

import os
import json
import getpass
import binascii

from datetime import datetime
from pymel import core
from maya import OpenMaya
from maya import OpenMayaUI
from maya import OpenMayaAnim

from studio_alembic.core import mayaNodes


class Connect(object):
    '''
        from pymel import core
        core.select('toon_geo')
        from studio_alembic.core import studioMaya
        reload(studioMaya)        
        smaya = studioMaya.Connect()        
        mobject_array = smaya.getShadingEngines()        
        nodes = smaya.getShaderNodes(mobject_array) 
        data = smaya.getShaderData(nodes)   
        from pprint import pprint
        pprint (data)  
    '''
    def __init__(self, path):        
        self.stuio_path = path
        self.name = os.path.basename(os.path.splitext(path)[0])    
        self.metadata_format = '.metadata'
        self.manifset_format = '.manifest'
        self.unknown_types = mayaNodes.unknown_types()
        self.default_nodes = mayaNodes.default_nodes()
        self.valid_attribute = mayaNodes.valid_attribute()
        self.shading_node_types = mayaNodes.getShadingNodeTypes() 
        
    def isValid(self): 
        pass
    
    def getShapeNodes(self, mdag_paths):
        seen = set()
        shape_path_array = OpenMaya.MDagPathArray()
        for index in range(mdag_paths.length()):
            stack = [mdag_paths[index]]
            while stack:
                node = stack.pop()
                if node.fullPathName() in seen:
                    continue
                for child in range(node.childCount()):
                    child_node = node.child(child)
                    mfn_dagnode = OpenMaya.MFnDagNode(child_node)
                    mdag_path = OpenMaya.MDagPath()
                    mfn_dagnode.getPath(mdag_path)
                    if mfn_dagnode.typeName() == 'mesh':
                        shape_path_array.append(mdag_path)
                        seen.add(mfn_dagnode.fullPathName())
                    stack.append(mdag_path)                    
        return shape_path_array
            
    def getShadingEngines(self, mdag_paths):
        shading_engines = OpenMaya.MObjectArray()        
        seen = set()                  
        for index in range(mdag_paths.length()):
            engines = self.getShadingEngine(mdag_paths[index])                        
            for x in range(engines.length()):
                node_name = self.getName(engines[x])
                if node_name in seen:
                    continue
                shading_engines.append(engines[x])
                seen.add(node_name)        
        return shading_engines  
          
    def getShadingEngine(self, mdag_path):
        dependency_graph = OpenMaya.MItDependencyGraph(
            mdag_path.node(),
            OpenMaya.MFn.kShadingEngine,
            OpenMaya.MItDependencyGraph.kNodeLevel
            )       
        shading_engines = OpenMaya.MObjectArray() 
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            node_name = self.getName(current_item)
            if node_name not in self.default_nodes:
                shading_engines.append(current_item)
            dependency_graph.next()
        return shading_engines
    
    def getFrameRange(self):
        maim_control = OpenMayaAnim.MAnimControl()        
        min_time = maim_control.minTime()
        max_time = maim_control.maxTime()
        values =  (
            min_time.value(),
            max_time.value(),
        )
        return values    

    def setBoundingBox(self):
        m3d_view = OpenMayaUI.M3dView()
        for index in range (m3d_view.numberOf3dViews()):
            view = OpenMayaUI.M3dView()
            m3d_view.get3dView(index, view)
            view.setDisplayStyle(0)
            view.refresh()
                
    def exportShaderNetwork(self, mdag_paths):
        shape_mdag_paths = self.getShapeNodes(mdag_paths)      
        shading_engines = self.getShadingEngines(shape_mdag_paths)        
        shadder_path = self.getMayaDataPath(self.stuio_path, 'shader')                
        path = self._exportShaderNetwork(shading_engines, shadder_path)
        return path                       
    
    def _exportShaderNetwork(self, shading_engines, path):        
        self.clearCache(path)
        selection = OpenMaya.MSelectionList()
        for index in range(shading_engines.length()):
            mobject = shading_engines[index]
            mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
            if mfn_dependency_node.isDefaultNode():
                continue
            selection.add(mobject)
        if not selection.isEmpty():
            OpenMaya.MGlobal.setActiveSelectionList(selection)
            OpenMaya.MFileIO.exportSelected(path, None, True)
            return path
        return False
    
    def exportMetaData(self, mdag_paths):
        shape_mdag_paths = self.getShapeNodes(mdag_paths)      
        shading_engines = self.getShadingEngines(shape_mdag_paths)           
        path = '{}{}'.format(
            os.path.splitext(self.stuio_path)[0],
            self.metadata_format
        )
        path = self._exportMetaData(shading_engines, path)
        return path     
    
    def _exportMetaData(self, shading_engines, path):
        shader_nodes, assign_objects = self.getShaderNodes(shading_engines)        
        shader_data = self.getShaderData(shader_nodes, assign_objects)               
        self.clearCache(path)              
        decoded_data = self.decodeData(shader_data)    
        with(open(path, 'w')) as meta_data:
            meta_data.write(decoded_data)
            return path
        return False    
    
    def exportAlembic(self, mdag_paths):
        self.setBoundingBox()
        min, max = self.getFrameRange()
        format = 'ogawa'
        root = self.getRoot(mdag_paths)
        command = '-frameRange {} {} -dataFormat {}  {} -file {}'.format(
            min, max, format, root, self.stuio_path)
        core.AbcExport(j=command)        
        return self.stuio_path      
    
    def exportManifest(self, **kwargs):
        build_in_data = {
            'created_date': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'author': 'Subin Gopi',
            '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': '# WARNING! All changes made in this file will be lost!',
            'description': 'studio alembic plugin manifest',
            'type': 'studio_alembic',
            'valid': True,
            'user': getpass.getuser(),
            'data': kwargs
            }
        
        abspath = '{}{}'.format(
            os.path.splitext(self.stuio_path)[0], self.manifset_format
        )         
        with(open(abspath, 'w')) as manifest_data:
            manifest_data.write(json.dumps(build_in_data, indent=4))
            return abspath
        return False
    

    def export(self, mdag_paths):       
        engines = self.exportShaderNetwork(mdag_paths)
        metadata = self.exportMetaData(mdag_paths)
        alembic = self.exportAlembic(mdag_paths)
        
        data = {
            'basename': '',
            'shader': '',
            'metadata': '',
            'alembic': '',            
            'objects': '',
            'shader_engines': '',
            }        
        
        manifest = self.exportManifest(data)        

    
    def getRoot(self, mdag_paths):
        objects = []
        for index in range(mdag_paths.length()):            
            objects.append('-root %s'% mdag_paths[index].fullPathName())
        return ' '.join(objects)
    

            
    def getDagPaths(self, nodes):
        mdag_paths = OpenMaya.MDagPathArray()
        for node in nodes:
            mdag_path = self.getDagPath(node)
            mdag_paths.append(mdag_path)
        return mdag_paths        
            
    def getDagPath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path
    
    def getMObject(self, object):
        mselection = OpenMaya.MSelectionList()
        mselection.add(object)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject

    def getName(self, maya_object):  # to remove
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependencynode = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependencynode.name().encode()       
    
    def getAssignObjects(self, shading_engines):
        objects = []
        mfn_set = OpenMaya.MFnSet(shading_engines)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        if not selection_list.length():
            return objects
        for index in range(selection_list.length()):
            m_dag_path = OpenMaya.MDagPath()
            m_object = OpenMaya.MObject()
            selection_list.getDagPath(index, m_dag_path, m_object)
            if m_dag_path.partialPathName() in objects:
                continue
            objects.append(m_dag_path.partialPathName())
        return objects

    def getAssignComponents(self, shading_engine):
        mobject = self.getMObject(shading_engine)
        mfn_set = OpenMaya.MFnSet(mobject)
        selection_list = OpenMaya.MSelectionList()
        mfn_set.getMembers(selection_list, False)
        component_data = []
        if not selection_list.length():
            return mfn_set.name(), component_data
        for index in range(selection_list.length()):
            components = []
            selection_list.getSelectionStrings(components)
            if components in component_data:
                continue
            component_data.extend(components)            
        return mfn_set.name(), component_data  

    def getSelectedNodes(self):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        mdag_paths = OpenMaya.MDagPathArray()
        for index in range(mselection.length()):
            mobject = OpenMaya.MObject()
            mselection.getDependNode(0, mobject)
            if not mobject.hasFn(OpenMaya.MFn.kTransform) and not mobject.hasFn(OpenMaya.MFn.kMesh):
                continue
            mdagpath = OpenMaya.MDagPath()
            mselection.getDagPath(index, mdagpath)
            mdag_paths.append(mdagpath)
        return mdag_paths




    

    
    def getShaderNodes(self, shading_engine_mobjects):
        dependency_nodes = set()
        assign_objects = set()
        for index in range (shading_engine_mobjects.length()):
            current_nodes, assign_object = self.findShaderNodes(
                shading_engine_mobjects[index])            
            dependency_nodes.update(current_nodes) 
            assign_objects.update(assign_object)    
        return list(dependency_nodes), list(assign_objects)

    def findShaderNodes(self, mobject):
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        object_name = mfn_dependency_node.name().encode()
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'listHistory %s' % object_name, mcommand_result, True, True)    
        results = []
        mcommand_result.getResult(results)
        assign_objects = self.getAssignObjects(mobject)       
        results = []
        mcommand_result.getResult(results)
        networks = []
        for each_result in results:
            py_node = core.PyNode(each_result)
            if py_node.type() in self.unknown_types:
                continue
            if py_node.name() in self.default_nodes:
                continue            
            if py_node.name() in assign_objects:
                continue
            if each_result in networks:
                continue
            networks.append(each_result.encode())
        return networks, assign_objects
    
    def getShaderData(self, shader_nodes, assign_objects):
        node_data = {}
        attribute_data = {}
        connection_data = {}
        geometry_data = {}                    
        for shader_node in shader_nodes:
            py_node = core.PyNode(shader_node)
            node_data.setdefault(py_node.name(), py_node.type())
            attributes = py_node.listAttr(
                r=True, w=True, u=True, m=True, hd=True)
            if not attributes:
                continue
            # get attribute values
            current_attribute_data = {}
            for each_attribute in attributes:
                if each_attribute.type() not in self.valid_attribute:
                    continue
                try:
                    current_value = each_attribute.get()
                except:
                    current_value = '___unknown___'
                current_attribute_data.setdefault(
                    each_attribute.longName(), current_value)
                attribute_data.setdefault(shader_node, current_attribute_data)        
            # get connections
            current_connection_data = {}
            connections = py_node.listConnections(s=False, d=True, p=True)
            for each_connection in connections:
                if each_connection.nodeName() in assign_objects:
                    continue                               
                if each_connection.nodeName() in self.default_nodes:
                    continue
                if each_connection.nodeType() in self.unknown_types:
                    continue
                source_attribute = each_connection.listConnections(
                    s=True, d=False, p=True)
                if not source_attribute:
                    continue
                current_connection_data.setdefault(
                    source_attribute[0].longName(), []).append(each_connection.name())
            if current_connection_data:                    
                connection_data.setdefault(
                    py_node.name(), current_connection_data)               
            if py_node.type()=='shadingEngine':
                # get shader assign geometries
                set_name, component_data = self.getAssignComponents(py_node.name())
                geometry_data.setdefault(set_name, component_data)
        shader_data = {
            'nodes': node_data,
            'attributes': attribute_data,
            'connections': connection_data,
            'geometries': geometry_data,
        }
        return shader_data
    
    
    
    def create_shader_net(self, shader_data, assign_components):
        node_data = shader_data['nodes']
        attribute_data = shader_data['attributes']
        connection_data = shader_data['connections']
        shading_engine = None
        py_nodes = {}
        for each_node, node_type in node_data.items():
            current_node = self.create_node(type=node_type, name=each_node)
            if shader_data['shading_engine'] == each_node:
                shading_engine = current_node
            py_nodes.setdefault(each_node.encode(), current_node)
        for each_node, current_pynode in py_nodes.items():  # set attributes values
            if not attribute_data:
                continue
            if each_node not in attribute_data:
                continue
            for each_attribute, values in attribute_data[each_node].items():
                if not core.objExists('%s.%s' % (current_pynode.name(), each_attribute)):
                    continue
                current_attribute = current_pynode.attr(each_attribute)
                try:
                    current_attribute.set(values)
                except Exception as error:
                    print 'studio alembic warning \"set attri\" {}.{}\n\t{}'.format(
                        current_node, each_attribute, error)
        for each_node, current_pynode in py_nodes.items():  # set connections
            if not connection_data:
                continue
            if each_node not in connection_data:
                continue
            for parent_attribute, children in connection_data[each_node].items():
                current_parent_attribute = current_pynode.attr(
                    parent_attribute)
                for each_child in children:
                    child_node = each_child.split('.')[0]
                    current_child = None
                    if child_node in py_nodes:
                        current_child = each_child.replace(
                            child_node, py_nodes[child_node].name())
                    if not current_child:
                        continue
                    try:
                        current_parent_attribute.connect(current_child, f=True)
                    except Exception as error:
                        print 'studio alembic warning \"connect attri\" {}\t{}\n\t{}'.format(
                            current_parent_attribute, each_child, error)
        if not shading_engine:
            return True
        if assign_components:
            self.assignToMaterial(assign_components, shading_engine)
        return True

    def create_node(self, type=None, name=None):
        if type == 'shadingEngine':
            current_node = core.sets(r=True, nss=True, em=True, n=name)
        elif type in self.shading_node_type['shader']:
            current_node = core.shadingNode(type, asShader=True, n=name)
        elif type in self.shading_node_type['utility']:
            current_node = core.shadingNode(type, asUtility=True, n=name)
        elif type in self.shading_node_type['texture']:
            current_node = core.shadingNode(type, asTexture=True, n=name)
        elif type in self.shading_node_type['light']:
            current_node = core.shadingNode(type, asLight=True, n=name)
        elif type in self.shading_node_type['rendering']:
            current_node = core.shadingNode(type, asRendering=True, n=name)
        elif type in self.shading_node_type['postProcess']:
            current_node = core.shadingNode(type, asPostProcess=True, n=name)
        else:
            current_node = core.createNode(type, n=name)
        return current_node

    def assignToMaterial(self, objects, shading_group):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand('sets -e -forceElement %s %s;' % (
            shading_group, ' '.join(objects)), mcommand_result,  True, True)
        results = []
        mcommand_result.getResult(results)
        return results    






    def decodeData(self, data):
        json_data = json.dumps(data)        
        return binascii.b2a_base64(json_data)
    
    def encodeData(self, data):
        json_data = json.loads(binascii.b2a_base64(data))
        return json_data

    def clearCache(self, file):       
        if os.path.isfile(file):
            try:
                os.chmod(file, 0777)
            except:
                pass
            try:
                os.remove(file)                
            except Exception as error:
                print 'remove error', error   
        if not os.path.isdir(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))            
    
    def getMayaDataPath(self, root, type):        
        maya_type = {
            'mayaAscii': '.ma',
            'mayaBinary': '.mb'
        }               
        file_type = self.getMayaFileType(root)
        path = '{}_{}{}'.format(root, type, maya_type[file_type])
        return path            
    
    def getMayaFileType(self, path):
        types = {
            '.ma': 'mayaAscii',
            '.mb': 'mayaBinary'
        }          
        splitext = os.path.splitext(path)
        if splitext[1] in types:            
            return types[splitext[1]]
        else:            
            current_file = OpenMaya.MFileIO.currentFile()        
            if current_file.endswith('/untitled'):            
                return 'mayaAscii'   
            return OpenMaya.MFileIO.fileType()
    

    def getManifest(self):
        manifset_path = '{}{}'.format(
            os.path.splitext(self.stuio_path)[0],
            self.manifset_format
            )        
        if not os.path.isfile(manifset_path):
            return False 
        with(open(manifset_path, 'r')) as manifset_data:
            data = json.load(manifset_data)
            return data
        return False  




# end ####################################################################
