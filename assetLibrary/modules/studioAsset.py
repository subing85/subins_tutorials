'''
stdioShader.py 0.0.1 
Date: January 16, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

from pprint import pprint
import os
import json
import tempfile
import subprocess
import tempfile
import warnings

from datetime import datetime


from assetLibrary.utils import platforms
from assetLibrary.modules import readWrite
from assetLibrary.modules import studioImage

from assetLibrary import resources


reload(studioImage)


class Asset(object):

    def __init__(self, path=None, paths=None, image=None):
        self.path = path
        self.paths = paths
        self.image = image
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.output_path = tempfile.gettempdir()
        self.asset_setname = 'asset_set'
        self.maya_types = {'.mb': 'mayaBinary', '.ma': 'mayaAscii'}
        
        
    def get_format(self):
        if not self.path:
            return None           
        current_format = os.path.splitext(self.path)[-1]          
        if current_format not in  self.maya_types:
            return None            
        self.maya_type = self.maya_types[current_format]
        return self.maya_type

    def had_valid(self, publish_file):
        rw = readWrite.ReadWrite(t='asset')
        rw.file_path = publish_file
        result = rw.has_valid()
        return result
    
    def read_data(self, type, paths):
        rw = readWrite.ReadWrite(t='asset')
        rw.file_path = paths
        #=======================================================================
        # if fake:
        #     rw.file_path = self.paths[-1]
        #     data = rw.get_info()
        #     return data        
        #=======================================================================
        result = {True: None}     
        asset_data = {}      
        for each_path in self.paths:
            rw.file_path = each_path
            if type=='info':
                data = rw.get_info()
            if type=='data':
                data = rw.get_data()
            asset_data.setdefault(each_path, data)
        return asset_data

    def create(self, mode, create_type, fake=False, maya_path=None, output_path=None):
        paths = self.paths
        if fake:
            paths = [self.paths[-1]] 
                   
        asset_data = self.read_data('info', paths)        
        if fake:            
            return asset_data
        
        if mode=='standalone':
            result = self.create_maya_file(asset_data, create_type, maya_path, output_path)
        if mode=='maya':
            result = self.create_assets(asset_data, create_type) 
            
        return result     
                  
    
    
    def create_maya_file(self, data, create_type, maya_path, output_path):
        bash_file = os.path.join(tempfile.gettempdir(), 'asset_library.py')
        if os.path.isfile(bash_file):
            try:
                os.chmod(folder_path, 0777)
                os.remove(bash_file)
            except:
                pass
        
        core_type = 'core.createReference(asset_path, iv=True, ns=asset_name)'
        if create_type=='import':
            core_type = 'core.importFile(asset_path, iv=True, ns=asset_name)'
        
        if not output_path:
            output_path = tempfile.gettempdir()
            
        current_time =  datetime.now().strftime('%Y_%d_%B_%I_%M_%S_%p')            
        output_file = os.path.join(output_path, 'asset_bundle_{}.ma'.format(current_time))
            
        asset_data = self.read_data('data', self.paths)
        
        data = [
            '#!{}/bin/mayapy'.format(maya_path),
            'from maya import standalone',
            'standalone.initialize(name="python")',
            'from pymel import core',
            'data = {}'.format(asset_data),
            'for each_asset in  data:',
            '\tasset_name = data[each_asset][\'name\']',
            '\tasset_path = data[each_asset][\'path\']',
            '\tasset_format = data[each_asset][\'format\']',            
            '\t{}'.format(core_type),
            '\tprint asset_path',
            'core.saveAs(\'{}\', typ=\'mayaBinary\')'.format(output_file),
            'standalone.uninitialize(name=\'python\')'
            ]      

        bash_data = open(bash_file, 'w')
        try:
            bash_data.write('\n'.join(data))
        except Exception as error:
            warnings.warn(str(error), Warning)
        finally:
            bash_data.close()    
        
        try:
            os.chmod(bash_file, 0o777)
        except Exception as error:
            warnings.warn(str(error), Warning) 

        # result = subprocess.call (bash_file, stdout=None, shell=True, stderr=None)
        
        return output_file
        
        

    def create_assets(self, data, create_type):
        from pymel import core
        self.set_bounding_box()             
        for each_asset in  data:
            asset_name = data[each_asset]['name']
            asset_path = data[each_asset]['path']
            asset_format = data[each_asset]['format']            
            if create_type=='reference':
                core.createReference(asset_path, iv=True, ns=asset_name)
            if create_type=='import':
                core.importFile(asset_path, iv=True, ns=asset_name)
        return True

    def save(self, file_path, name, user_comment=None):
        comment = '%s %s - asset' % (
            self.tool_kit_name, self.version)
        if user_comment:
            comment = '%s %s - asset\n%s' % (
                self.tool_kit_name, self.version, user_comment)
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about asset'
        type = 'asset'
        valid = True
        
        format = self.get_format()        
        data = {
            'name': name,
            'path': self.path,
            'format': format
            }
        
        tag = self.tool_kit_object
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                                 d=description, t=type, v=valid, data=data, tag=tag,
                                 path=file_path, name=name, format='asset')
        result, shader_path = rw.create()
        if False in result:
            return result
        studio_image = studioImage.ImageCalibration(
            path=file_path, name=name, format='png')
        
        image_path = studio_image.writeImage(self.image)
        
        
        print '\nresult', shader_path, image_path
        return result

    def had_file(self, dirname, name):
        rw = readWrite.ReadWrite(
            path=dirname, name=name, format='asset', t='asset')
        return rw.has_file()

    def get_image(self, shader_path):
        return shader_path.replace('.asset', '.png')
    
    
    def set_bounding_box(self):    
        from pymel import core
        panels = core.getPanel(type='modelPanel')        
        for each_panel in panels :
            core.modelEditor(each_panel, e=True, da='boundingBox')    
            

    def get_asset(self, shading_engine):
        shader_data = {}
        node_data = {}
        attribute_data = {}
        connection_data = {}
        geometry_data = []
        nodes = self.getNetworks(shading_engine)  # get nodes
        assign_objects = self.getAssignObjects(shading_engine)
        # get attribute values
        for each_node in nodes:
            if each_node in assign_objects:
                continue
            if each_node in self.default_nodes:
                continue
            py_node = core.PyNode(each_node)
            node_data.setdefault(py_node.name(), py_node.type())
            attributes = py_node.listAttr(
                r=True, w=True, u=True, m=True, hd=True)
            if not attributes:
                continue
            current_attribute_data = {}
            for each_attribute in attributes:
                if each_attribute.nodeName() in assign_objects:
                    continue
                if each_attribute.type() not in self.valid_attribute:
                    continue
                try:
                    current_value = each_attribute.get()
                except:
                    current_value = '___unknown___'
                current_attribute_data.setdefault(
                    each_attribute.longName(), current_value)
                attribute_data.setdefault(each_node, current_attribute_data)
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
                # temp block if each_connection.nodeName() in assign_objects:
                # to exclude the geometry connections
                # temp block  continue
                # temp block if each_connection.nodeName() in self.default_nodes:
                # to exclude the unknown connections
                # temp block   continue
                current_connection_data.setdefault(source_attribute[0].longName().encode(), [
                ]).append(each_connection.name().encode())
                connection_data.setdefault(
                    py_node.name().encode(), current_connection_data)
        # get shader assign geometries
        set_name, component_data = self.getAssignComponents(shading_engine)
        shader_data['nodes'] = node_data
        shader_data['attributes'] = attribute_data
        shader_data['connections'] = connection_data
        shader_data['geometries'] = component_data
        shader_data['shading_engine'] = set_name
        return shader_data

    def disconnect_shader(self, geometry_data):
        assign_objects = []
        for index, components in geometry_data.items():
            for each_component in components:
                if not core.objExists(each_component):
                    continue
                py_node = core.PyNode(each_component)
                if py_node.node().name() in assign_objects:
                    continue
                assign_objects.append(py_node.node().name())

        for each_object in assign_objects:
            m_object = self.getMObject(each_object)
            mobject_arrary = self.getObjectShadingEngine(m_object)
            for index in range(mobject_arrary.length()):
                valid = self.hasValidShadingEngine(
                    mobject_arrary[index], object=each_object)
                if not valid:
                    continue
                mfn_set = OpenMaya.MFnSet(mobject_arrary[index])
                try:
                    mfn_set.removeMember(m_object)
                except:
                    set_pynode = core.PyNode(mfn_set.name())
                    dag_members = set_pynode.attr(
                        'dagSetMembers').listConnections(s=True, d=False, p=True)
                    face_members = set_pynode.attr(
                        'memberWireframeColor').listConnections(s=False, d=True, p=True)
                    for each_member in dag_members + face_members:
                        try:
                            each_member.disconnect()
                        except:
                            pass

    def create_asset(self, shader_data, assign=False):
        node_data = shader_data['nodes']
        attribute_data = shader_data['attributes']
        connection_data = shader_data['connections']
        geometry_data = shader_data['geometries']
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
                    print 'shader libaray warning \"set attri\" {}.{}\n\t{}'.format(
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
                        print 'shader libaray warning \"connect attri\" {}\t{}\n\t{}'.format(
                            current_parent_attribute, each_child, error)
        if not assign:
            return True
        if not shading_engine:
            return True
        assign_components = []
        for index, components in geometry_data.items():
            for each_component in components:
                if not core.objExists(each_component):
                    continue
                assign_components.append(each_component)
                py_node = core.PyNode(each_component)
        self.assignToMaterial(assign_components, shading_engine)
        return True

    def create_node(self, type=None, name=None):
        if type == 'shadingEngine':
            current_node = core.sets(r=True, nss=True, em=True, n=name)
        elif type in self._node_types['shader']:
            current_node = core.shadingNode(type, asShader=True, n=name)
        elif type in self._node_types['utility']:
            current_node = core.shadingNode(type, asUtility=True, n=name)
        elif type in self._node_types['texture']:
            current_node = core.shadingNode(type, asTexture=True, n=name)
        elif type in self._node_types['light']:
            current_node = core.shadingNode(type, asLight=True, n=name)
        elif type in self._node_types['rendering']:
            current_node = core.shadingNode(type, asRendering=True, n=name)
        elif type in self._node_types['postProcess']:
            current_node = core.shadingNode(type, asPostProcess=True, n=name)
        else:
            current_node = core.createNode(type, n=name)
        return current_node

    def getNetworks(self, object):
        if not object:
            return
        if isinstance(object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(object)
            object = mfn_dependency_node.name().encode()
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'listHistory %s' % object, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        networks = []
        for each_result in results:
            py_node = core.PyNode(each_result)
            if py_node.type() in self.unknown_types:
                continue
            if each_result in networks:
                continue
            networks.append(each_result.encode())
        return networks

# end ####################################################################
