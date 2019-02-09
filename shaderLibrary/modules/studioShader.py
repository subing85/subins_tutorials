'''
stdioShader.py 0.0.1 
Date: January 16, 2019
Last modified: January 26, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''
from pprint import pprint

import os

from datetime import datetime

from maya import OpenMaya
from pymel import core

from shaderLibrary.utils import platforms
from shaderLibrary.modules import readWrite
from shaderLibrary.modules import studioMaya
from shaderLibrary.modules import studioImage

reload(studioMaya)
reload(readWrite)


class Shader(studioMaya.Maya):

    def __init__(self, geometry_dag_path=None, path=None):
        self.geometry_dag_path = geometry_dag_path
        self.path = path
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()

        self.unknown_types = ['lightLinker', 'materialInfo', 'nodeGraphEditorInfo', 
                    'partition', 'groupId', 'hyperShadePrimaryNodeEditorSavedTabsInfo', 'renderPartition']

        self.default_nodes = [
            'defaultLightList1',
            'defaultShaderList1',
            'postProcessList1',
            'defaultRenderUtilityList1',
            'defaultRenderingList1',
            'lightList1',
            'defaultTextureList1',
            'lambert1',
            'particleCloud1',
            'initialShadingGroup',
            'initialParticleSE',
            'initialMaterialInfo',
            'shaderGlow1',
            'dof1',
            'defaultRenderGlobals',
            'defaultRenderQuality',
            'defaultResolution',
            'defaultLightSet',
            'defaultObjectSet',
            'defaultViewColorManager',
            'defaultColorMgtGlobals',
            'hardwareRenderGlobals',
            'characterPartition',
            'defaultHardwareRenderGlobals',
            'ikSystem',
            'hyperGraphInfo',
            'hyperGraphLayout',
            'globalCacheControl',
            'strokeGlobals',
            'dynController1',
            'lightLinker1',
            'layerManager',
            'defaultLayer',
            'renderLayerManager',
            'defaultRenderLayer',
            
            'hyperShadePrimaryNodeEditorSavedTabsInfo',
            'materialInfo1',
            'renderPartition',
            'renderGlobalsList1',
            'defaultLightList1',
            ]
        
        self.attribute_types = [
            'bool',
            'byte',
            'enum',
            'string',
            'long',
            'short',
            'typed',
            'float3',
            'float',
            'TdataCompound',
            'matrix',
            'time',
            'float2',
            'double',
            'doubleAngle',
            'char'
            'attributeAlias'
            ]
        self.valid_attribute =[
            'bool',
            'byte',
            'enum',
            'string',
            'long',
            'short',
            'typed',
            'float3',
            'float',
            'TdataCompound',
            'time',
            'float2',
            'double',
            'doubleAngle',
            'char'
            ]   

        
        
        self.shader_types = core.listNodeTypes('shader')
        self.texture_types = core.listNodeTypes('texture')
        self.utility_types = core.listNodeTypes('utility')        
        self.texture3d_types = core.listNodeTypes('texture/3D')
        self.textureenv_types = core.listNodeTypes('texture/Environment')
        self.light_types = core.listNodeTypes('light')
        self.rendering_types = core.listNodeTypes('rendering')
        self.postprocess_types = core.listNodeTypes('postProcess')
        
        self._node_types = {
            'shader': self.shader_types,
            'texture': self.texture_types + self.texture3d_types + self.textureenv_types, 
            'utility': self.utility_types,
            'light': self.light_types,
            'rendering': self.rendering_types,
            'postProcess': self.postprocess_types
            }        

    def had_valid(self, publish_file):
        rw = readWrite.ReadWrite(t='shader_net')
        rw.file_path = publish_file
        result = rw.has_valid()
        return result

    def create(self, fake=False):
        rw = readWrite.ReadWrite(t='shader_net')
        rw.file_path = self.path
        if fake:
            data = rw.get_info()
            return data

        data = rw.get_data()
        self.undoChunk('open')
        for index, shader_data in data.items():
            self.create_shader_net(shader_data)
        self.undoChunk('close')
        OpenMaya.MGlobal.executeCommand('undoInfo -closeChunk;')
        return True

    def save(self, file_path, name, image, user_comment=None):        
        mobject_arrary = self.getObjectShadingEngine(self.geometry_dag_path)        
        net_data = {}        
        for index in range(mobject_arrary.length()):          
            shader_data = self.get_shader_net(mobject_arrary[index])
            net_data.setdefault(index, shader_data)

        comment = '%s %s - shader networks' % (self.tool_kit_name, self.version)
        if user_comment:
            comment = '%s %s - shader networks\n%s' % (
                self.tool_kit_name, self.version, user_comment)
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about maya shader networks'
        type = 'shader_net'
        valid = True
        data = net_data
        tag = self.tool_kit_object
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                                 d=description, t=type, v=valid, data=data, tag=tag,
                                 path=file_path, name=name, format='shader')
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
            py_node = core.PyNode(each_node)            
            node_data.setdefault(py_node.name(), py_node.type())            
               
            attributes = py_node.listAttr(r=True, w=True, u=True, m=True, hd=True)            
            if not attributes:
                continue
            
            print '\n', each_node
            
            current_attribute_data = {}         
            for each_attribute in attributes:
                
                print '\n', each_attribute.type()
                
                if each_attribute.type() not in self.valid_attribute:
                    continue
                try:              
                    current_value = each_attribute.get()
                except:
                    current_value = '___unknown___'                                 
                
                current_attribute_data.setdefault(each_attribute.longName(), current_value)
                attribute_data.setdefault(each_node, current_attribute_data)
                
            # get connections
            current_connection_data = {}         
            
            connections= py_node.listConnections(s=False, d=True, p=True)
            if not connections:
                continue  
            for each_connection in connections:
                source_attribute = each_connection.listConnections(s=True, d=False, p=True)  
                if not source_attribute:
                    continue                 
                if each_connection.nodeName() in assign_objects: # to exclude the geometry connections
                    continue                
                if each_connection.nodeName() in self.default_nodes:# to exclude the unknown connections
                    continue
                
                current_connection_data.setdefault(source_attribute[0].longName(), []).append(each_connection.name())                                
                connection_data.setdefault(py_node.name(), current_connection_data)
            
        #get shader assign geometries       
        set_name, component_data = self.getAssignComponents(shading_engine)
                
        shader_data['nodes'] = node_data
        shader_data['attributes'] = attribute_data
        shader_data['connections'] = connection_data
        shader_data['geometries'] = component_data
        shader_data['shading_engine'] = set_name 
        
        return shader_data


    def create_shader_net(self, shader_data):        
        node_data = shader_data['nodes']
        attribute_data = shader_data['attributes']
        connection_data = shader_data['connections']
        geometry_data = shader_data['geometries']
        shading_engine = None
        
        py_nodes = {}
        for each_node, node_type in node_data.items():
            current_node = self.create_node(type=node_type, name=each_node)            
            if shader_data['shading_engine']==each_node:
                shading_engine = current_node                
            py_nodes.setdefault(each_node, current_node)
            
        
        for each_node, current_node  in py_nodes.items():  
               
            for each_attribute, values in attribute_data[each_node].items():                
                current_attribute = current_node.attr(each_attribute)
                try:
                    current_attribute.set(values)
                except Exception as error:
                    #print 'shader libaray warning \"set attri\" {}.{}\n\t{}'.format(current_node, each_attribute, error)
                    pass

            for parent_attribute, children in connection_data[each_node].items():
                current_parent_attribute = current_node.attr(parent_attribute)
                for each_child in children:
                    
                    child_node = each_child.split('.')[0]
                    current_child = None
                    
                    if child_node in py_nodes:                    
                        current_child = each_child.replace(child_node, py_nodes[child_node].name())
                        
                    if not current_child:
                        continue
                        
                    try:
                        current_parent_attribute.connect(current_child, f=True)
                    except Exception as error:                        
                        #print 'shader libaray warning \"connect attri\" {}\t{}\n\t{}'.format(current_parent_attribute, each_child, error)
                        pass
                                    
            if not shading_engine:
                continue            
            
            assign_components = []
            for index, components in geometry_data.items():
                for each_component in components:
                    if not core.objExists(each_component):
                        continue
                    assign_components.append(each_component)
                    
            # self.assignToMaterial(assign_components, shading_engine)
                

            
    def create_node(self, type=None, name=None):             
        if type=='shadingEngine':
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
        OpenMaya.MGlobal.executeCommand('listHistory %s' % object, mcommand_result, True, True)
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
