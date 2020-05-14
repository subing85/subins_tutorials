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

import os

from datetime import datetime

from maya import OpenMaya
from pymel import core

from shaderLibrary.utils import platforms
from shaderLibrary.modules import readWrite
from shaderLibrary.modules import studioMaya
from shaderLibrary.modules import studioImage
from shaderLibrary.modules import mayaNodes


class Shader(studioMaya.Maya):

    def __init__(self, geometry_dag_path=None, path=None):
        self.geometry_dag_path = geometry_dag_path
        self.path = path
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.unknown_types = mayaNodes.unknown_types()
        self.default_nodes = mayaNodes.default_nodes()
        self.valid_attribute = mayaNodes.valid_attribute()
        self._node_types = mayaNodes.getShadingNodeTypes()

    def had_valid(self, publish_file):
        rw = readWrite.ReadWrite(t='shader_net')
        rw.file_path = publish_file
        result = rw.has_valid()
        return result

    def create(self, assign, selected, fake=False):
        rw = readWrite.ReadWrite(t='shader_net')
        rw.file_path = self.path
        if fake:
            data = rw.get_info()
            return data
        data = rw.get_data()
        self.undoChunk('open')
        result = {True: None}
        maya_objects = []        
        if assign:  # disconnect remove exists shading_engine
            for index, shader_data in data.items():
                for objects in shader_data['geometries'].values():
                    exists_objects = [
                        each for each in objects if core.objExists(each)]
                    maya_objects.extend(exists_objects)
        if selected:
            selected_objects = core.ls(sl=True)
            for object in selected_objects:
                try:
                    shape_nodes = [
                        each.name() for each in object.getShapes()]
                except:
                    shape_nodes = []
                maya_objects.extend(shape_nodes) 
        if maya_objects:  # disconnect remove exists shading_engine
            self.disconnect_shader(maya_objects)            
        for index, shader_data in data.items():
            try:
                self.create_shader_net(
                    shader_data, assign=assign, assign_components=maya_objects)
            except Exception as error:
                result = {False: error}
        self.undoChunk('close')
        OpenMaya.MGlobal.executeCommand('undoInfo -closeChunk;')
        return result

    def save(self, file_path, name, image, user_comment=None):
        mobject_arrary = self.getObjectShadingEngine(self.geometry_dag_path)
        net_data = {}
        for index in range(mobject_arrary.length()):
            valid = self.hasValidShadingEngine(
                mobject_arrary[index], object=self.geometry_dag_path)
            if not valid:
                continue
            shader_data = self.get_shader_net(mobject_arrary[index])
            net_data.setdefault(index, shader_data)
        comment = '%s %s - shader networks' % (
            self.tool_kit_name, self.version)
        if user_comment:
            comment = '%s %s - shader networks\n%s' % (
                self.tool_kit_name, self.version, user_comment)
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about maya shader networks'
        type = 'shader_net'
        valid = True
        data = net_data
        tag = self.tool_kit_object
        rw = readWrite.ReadWrite(
            c=comment,
            cd=created_date,
            d=description,
            t=type,
            v=valid,
            data=data,
            tag=tag,
            path=file_path,
            name=name,
            format='shader')
        result, shader_path = rw.create()
        if False in result:
            return result
        studio_image = studioImage.ImageCalibration(
            path=file_path, name=name, format='png')
        image_path = studio_image.writeImage(image)
        print '\nresult', shader_path, image_path
        return result

    def had_file(self, dirname, name):
        rw = readWrite.ReadWrite(
            path=dirname, name=name, format='shader', t='shader_net')
        return rw.has_file()

    def get_image(self, shader_path):
        return shader_path.replace('.shader', '.png')

    def get_shader_net(self, shading_engine):
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

    def disconnect_shader(self, objects):
        maya_objects = []
        for each_object in objects:
            if not core.objExists(each_object):
                continue
            maya_objects.append(each_object)
        # self.assignToMaterial(maya_objects, 'initialShadingGroup')
        for each_object in objects:
            if not core.objExists(each_object):
                continue
            m_object = self.getMObject(each_object)
            mobject_arrary = self.getObjectShadingEngine(m_object)
            for index in range(mobject_arrary.length()):
                mfn_set = OpenMaya.MFnSet(mobject_arrary[index])
                mfn_set.clear()                

    def create_shader_net(self, shader_data, assign=True, assign_components=None):
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
        if not shading_engine:
            return True        
        if assign:
            assign_components = []
            for index, components in geometry_data.items():
                for each_component in components:
                    if not core.objExists(each_component):
                        continue
                    assign_components.append(each_component)
                    py_node = core.PyNode(each_component)
            self.assignToMaterial(assign_components, shading_engine)
        elif assign_components:
            self.assignToMaterial(assign_components, shading_engine)
        return True

    def create_node(self, type=None, name=None):
        current_node = None
        if type == 'shadingEngine':
            current_node = core.sets(r=True, nss=True, n=name)
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
