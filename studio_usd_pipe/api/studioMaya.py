
import os
import sys
import json
import math
import tempfile

from maya import OpenMaya
from maya import OpenMayaUI

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets


class Maya(object):

    def __init__(self):
        self.maya_format = 'mayaAscii'
        # self.usd_format = 'pxrUsdImport'
        self.valid_shapes = [OpenMaya.MFn.kMesh]
        self.scene_mobjects = OpenMaya.MObjectArray()        
        self.node_data = resource.getNodeData()
        self.attribute_container = self.attribute_bundles()

    def is_dagpath(self, mobject):           
        mobject = self.get_mobject(mobject)
        result = False
        try:
            OpenMaya.MFnDagNode(mobject)
            result = True        
        except:
            result = False        
        return result 
    
    def get_dagpath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path
    
    def get_mobject(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject
    
    def get_mobject_dagpath(self, mobject):
        mdag_path = OpenMaya.MDagPath()
        mdagpath = OpenMaya.MDagPath()
        mdagpath.getAPathTo(mobject, mdag_path)
        return mdag_path    

    def get_mplug(self, node_attribute):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add(node_attribute)
        mselection.getPlug(0, mplug)
        return mplug   
     
    def get_shape_node(self, mdag_path):
        try:
            mdag_path.extendToShape()
        except:
            mdag_path = None
        return mdag_path  
   
    def get_name(self, maya_object):
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependency_node.name().encode()
        if isinstance(maya_object, OpenMaya.MFnDagNode):
            return maya_object.fullPathName().encode()
        
    def get_default_nodes(self):        
        nodes = []        
        for node in self.node_data['default_nodes']:
            if not self.object_exists(node):
                continue            
            mobject = self.get_mobject(node)
            nodes.append(mobject)
        return nodes    
    
    def get_unknown_types(self):
        return self.node_data['unknown_types']           

    def get_node_type(self, node):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'nodeType \"%s\"' % node
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, False)
        return mcommand_result.stringResult()
    
    def object_exists(self, object_nmae):
        if isinstance(object_nmae, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(object_nmae)
            object_nmae = mfn_dependency_node.name()
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()
            mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)            
            if mfn_dependency_node.typeName() == 'dagNode':
                mit_dependency_nodes.next()
                continue
            if '|' in object_nmae:
                object_nmae = object_nmae.split('|')[-1]            
            if mfn_dependency_node.name() == object_nmae:
                return True       
            mit_dependency_nodes.next()
        return False
    
    def get_children(self, mobject):       
        if not self.is_dagpath(mobject):
            return None
        dag_path = self.get_dagpath(mobject)
        count = dag_path.childCount()
        children = OpenMaya.MObjectArray()
        for x in range(count):    
            child = dag_path.child(x)    
            if not child.hasFn(OpenMaya.MFn.kTransform):
                continue
            children.append(child)
        return children
        
    def get_ktransform(self, mobject, world=True):
        if world:
            dag_path = mobject
            if isinstance(mobject, OpenMaya.MObject):
                dag_path = self.get_mobject_dagpath(mobject)
            m_matrix = dag_path.inclusiveMatrix()
            transform_matrix = OpenMaya.MTransformationMatrix(m_matrix)
        else:
            mfn_transform = OpenMaya.MFnTransform(mobject)        
            transform_matrix = mfn_transform.transformation()
        mvector = transform_matrix.getTranslation(OpenMaya.MSpace.kWorld)       
        translation = [mvector.x, mvector.y, mvector.z]                    
        m_euler = transform_matrix.eulerRotation()
        angles = [m_euler.x, m_euler.y, m_euler.z]
        rotation = [math.degrees(angle) for angle in angles]            
        scale_util = OpenMaya.MScriptUtil()
        scale_util.createFromList([0, 0, 0], 3)
        double = scale_util.asDoublePtr()
        transform_matrix.getScale(double, OpenMaya.MSpace.kWorld)
        scale = [OpenMaya.MScriptUtil.getDoubleArrayItem(double, x) for x in range(3)]
        data = {
            'translate': translation,
            'rotate': rotation,
            'scale': scale
            }                 
        return data           
        
    def create_ktransform(self, name, data):
        mfn_transform = OpenMaya.MFnTransform()
        mfn_transform.create()
        mfn_transform.setName(name)        
        tx, ty, tz = data['translate']                
        translate_mvector = OpenMaya.MVector(tx, ty, tz)
        mfn_transform.setTranslation(translate_mvector, OpenMaya.MSpace.kTransform)        
        radians = [math.radians(x) for x in data['rotate']]
        euler_rotation = OpenMaya.MEulerRotation(radians[0], radians[1], radians[2])
        mfn_transform.setRotation(euler_rotation)
        scale_util = OpenMaya.MScriptUtil()
        scale_util.createFromList(data['scale'], 3)
        double = scale_util.asDoublePtr()
        mfn_transform.setScale(double)
        return mfn_transform
    
    def set_ktransform(self, mobject, data):
        mfn_transform = OpenMaya.MFnTransform(mobject)
        tx, ty, tz = data['translate']                
        translate_mvector = OpenMaya.MVector(tx, ty, tz)
        mfn_transform.setTranslation(translate_mvector, OpenMaya.MSpace.kTransform) 
        radians = [math.radians(x) for x in data['rotate']]
        euler_rotation = OpenMaya.MEulerRotation(radians[0], radians[1], radians[2])
        mfn_transform.setRotation(euler_rotation)
        scale_util = OpenMaya.MScriptUtil()
        scale_util.createFromList(data['scale'], 3)
        double = scale_util.asDoublePtr()
        mfn_transform.setScale(double)
        return mfn_transform        
          
    def remove_node(self, mobject):
        if isinstance(mobject, unicode):
            mobject = mobject.encode()                    
        if not isinstance(mobject, str):
            mobject = self.get_name(mobject)
        if not self.object_exists(mobject):
            return
        mcommand_result = OpenMaya.MCommandResult()       
        mel_command = 'delete \"%s\"' % mobject 
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
    
    def remove_nodes(self, mobject_arry):
        nodes = []
        for x in range(mobject_arry.length()):
            if not self.object_exists(mobject_arry[x]):
                continue            
            name = self.get_name(mobject_arry[x])
            nodes.append(name)            
        mcommand_result = OpenMaya.MCommandResult()     
        mel_command = 'delete %s' % ' '.join(nodes) 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)        
        
    def create_mpoint_array(self, array):
        m_point_array = OpenMaya.MPointArray()
        for x, y, z, w in array:
            m_point_array.append(x, y, z, w)
        return m_point_array
    
    def create_mdouble_array(self, array):
        mdouble_array = OpenMaya.MDoubleArray()
        for x in array:
            mdouble_array.append(x)
        return mdouble_array                
                            
    def create_float_array(self, python_list):
        mfloat_array = OpenMaya.MFloatArray()
        mscript_util = OpenMaya.MScriptUtil()
        mscript_util.createFloatArrayFromList(python_list, mfloat_array)
        return mfloat_array

    def create_int_array(self, python_list):
        mint_array = OpenMaya.MIntArray()
        mscript_util = OpenMaya.MScriptUtil()
        mscript_util.createIntArrayFromList(python_list, mint_array)
        return mint_array

    def create_floatpoint_array(self, python_list):
        mfloat_point_array = OpenMaya.MFloatPointArray()
        for x, y, z, w in python_list:
            mfloat_point_array.append(x, y, z, w)
        return mfloat_point_array 
    
    def has_same_hierarchy(self, root, child):
        mfn_dag_node = OpenMaya.MFnDagNode(child)    
        root_node = mfn_dag_node.fullPathName().split('|')[1]            
        child_mobject = self.get_mobject(root_node)
        if root != child_mobject:
            return False
        return True                       
                  
    def extract_depend_nodes(self, default=False):        
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes()          
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():            
            mobject = mit_dependency_nodes.item()
            if mobject.hasFn(OpenMaya.MFn.kWorld):
                mit_dependency_nodes.next()
                continue       
            if mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()
                continue            
            if self.is_dagpath(mobject):                
                mit_dependency_nodes.next()                           
                continue                   
            if mobject in default_nodes:
                mit_dependency_nodes.next()                           
                continue                                                      
            mobjects.append(mobject)   
            mit_dependency_nodes.next()
        return mobjects    
    
    def extract_null_transform(self, root_mobject=None):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kTransform)
        dag_path_array = OpenMaya.MDagPathArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()   
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            if root_mobject:
                root = mfn_dag_node.fullPathName().split('|')[1]    
                current_root_mobject = self.get_mobject(root)
                if current_root_mobject != root_mobject:
                    mit_dependency_nodes.next()
                    continue        
            dag_path = OpenMaya.MDagPath()
            mfn_dag_node.getPath(dag_path)
            shape_mobject = self.get_shape_node(dag_path)
            if shape_mobject:
                mit_dependency_nodes.next()
                continue            
            dag_path_array.append(dag_path)            
            mit_dependency_nodes.next()
        return dag_path_array 
    
    def extract_transform_primitive(self, mfn_type, shape=True, parent_mobject=None):
        dag_path_array = OpenMaya.MDagPathArray()
        seen = []
        mit_dependency_nodes = OpenMaya.MItDependencyNodes(mfn_type)
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item() 
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            if parent_mobject:
                current_root = mfn_dag_node.fullPathName().split('|')[1]    
                current_root_mobject = self.get_mobject(current_root)
                if current_root_mobject != parent_mobject:
                    mit_dependency_nodes.next()
                    continue
            if not shape:        
                p_mobject = mfn_dag_node.parent(0)       
                mfn_dag_node = OpenMaya.MFnDagNode(p_mobject)
            p_dag_path = OpenMaya.MDagPath()
            mfn_dag_node.getPath(p_dag_path) 
            if p_dag_path in seen:
                mit_dependency_nodes.next()
                continue
            seen.append(p_dag_path)
            dag_path_array.append(p_dag_path)
            mit_dependency_nodes.next()
        dag_path_array = OpenMaya.MDagPathArray(dag_path_array)  
        return dag_path_array

    def extract_top_transforms(self, default=False):
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes()    
        mit_dependency_nodes = OpenMaya.MItDependencyNodes(OpenMaya.MFn.kTransform)
        dag_path_array = OpenMaya.MDagPathArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            p_mobject = mfn_dag_node.parent(0)
            if not p_mobject.hasFn(OpenMaya.MFn.kWorld):
                mit_dependency_nodes.next()    
                continue             
            if mobject in default_nodes:
                mit_dependency_nodes.next()                           
                continue            
            dag_path = OpenMaya.MDagPath()
            mfn_dag_node.getPath(dag_path)                                                                     
            dag_path_array.append(dag_path)   
            mit_dependency_nodes.next()            
        return dag_path_array   
    
    def create_group(self, name):
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('transform')
        mfn_dag_node.setName(name)
        return mfn_dag_node   
        
    def create_pipe_ids(self, mobject, id_data):
        attributes = common.sort_dictionary(id_data)
        self.remove_pipe_ids(mobject, id_data)
        data = {}
        hidden = {True: False, False: True} 
        for attribute in attributes:
            short = id_data[attribute]['short']
            type_attribute = OpenMaya.MFnTypedAttribute()
            sample_mobject = OpenMaya.MObject()
            sample_mobject = type_attribute.create(attribute, short, OpenMaya.MFnData.kString)
            type_attribute.setKeyable(False)
            type_attribute.setReadable(True)
            type_attribute.setChannelBox(False)
            type_attribute.setWritable(id_data[attribute]['locked'])
            type_attribute.setHidden(hidden[id_data[attribute]['show']])
            mfn_dependency_node = OpenMaya.MFnDependencyNode()  
            mfn_dependency_node.setObject(mobject)
            mfn_dependency_node.addAttribute(sample_mobject)
            mplug = mfn_dependency_node.findPlug(type_attribute.name())
            if not id_data[attribute]['value']:
                data.setdefault(attribute, 'no value updated')
            else:
                mplug.setString(id_data[attribute]['value'].encode())
                data.setdefault(attribute, id_data[attribute]['value'])
            mplug.setLocked(id_data[attribute]['locked'])
        return data
                
    def set_pipe_ids(self, mobject, inputs):
        dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute, value in inputs.items():
            if not dependency_node.hasAttribute(attribute):
                continue
            mplug = dependency_node.findPlug(attribute)
            if not value:
                continue
            mplug.setLocked(False)
            mplug.setString(value)
            mplug.setLocked(True)

    def update_pipe_ids(self, mobject, id_data=None):
        if not id_data:
            id_data = resource.getPipeIDData()        
        removed_ids = self.removed_pipe_ids(mobject, id_data=id_data)
        exists_attributes = set(id_data.keys()).difference(removed_ids)
        dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute in exists_attributes:
            mplug = dependency_node.findPlug(attribute)
            id_data[attribute]['value'] = mplug.asString()         
        self.create_pipe_ids(mobject, id_data)      
            
    def has_valid_pipe_ids(self, mobject, inputs):
        data = []
        dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        for attribute in inputs:            
            if dependency_node.hasAttribute(attribute):
                continue
            data.append(attribute)
        if data:
            return False
        return True    

    def get_pipe_id_data(self, mobject, id_data=None):
        if not id_data:
            id_data = resource.getPipeIDData()
        data = {}
        dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute in id_data:
            if not dependency_node.hasAttribute(attribute):
                continue
            mplug = dependency_node.findPlug(attribute)
            id_value = mplug.asString()
            order = None
            if 'order' in id_data[attribute]:
                order = id_data[attribute]['order']
            data[attribute] = {
                'order': order,
                'value': id_value
            }        
        if len(data)!=len(id_data):
            return data, False
        return data, True

    def removed_pipe_ids(self, mobject, id_data=None):
        if not id_data:
            id_data = resource.getPipeIDData()
        removed_ids = []
        dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute in id_data:
            if dependency_node.hasAttribute(attribute):
                continue
            removed_ids.append(attribute)
        return removed_ids    
                        
    def remove_pipe_ids(self, mobject, inputs):
        mfn_dependency = OpenMaya.MFnDependencyNode(mobject)
        for attribute in inputs:
            if not mfn_dependency.hasAttribute(attribute):
                continue
            attribute_mobject = mfn_dependency.attribute(attribute)
            mplug = mfn_dependency.findPlug(attribute)
            mplug.setLocked(False)            
            mfn_dependency.removeAttribute(
                attribute_mobject,
                OpenMaya.MFnDependencyNode.kLocalDynamicAttr
                )  
            
    def set_locked(self, mobject, attributes=None, locked=True):
        if not attributes:
            attributes = [
                'translateX', 'translateY', 'translateZ',
                'rotateX', 'rotateY', 'rotateZ',
                'scaleX', 'scaleY', 'scaleZ',
                'visibility',
                ]
        for attribute in attributes:    
            dependency_node = OpenMaya.MFnDependencyNode(mobject)
            attr_mobject = dependency_node.attribute(attribute)
            mplug = dependency_node.findPlug(attr_mobject)
            mplug.setLocked(locked)         
         
    def disconnect_chanelbox(self, mobject):        
        dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        attributes = [
            'translateX', 'translateY', 'translateZ',
            'rotateX', 'rotateY', 'rotateZ',
            'scaleX', 'scaleY', 'scaleZ',
            'visibility',
            'translate', 'rotate', 'scale'     
            ]            
        for attribute in attributes:    
            attr_mobject = dependency_node.attribute(attribute)
            output_plug = dependency_node.findPlug(attr_mobject)
            if not output_plug.isConnected():
                continue
            input_plugs = OpenMaya.MPlugArray()
            output_plug.connectedTo(input_plugs, 1, 0)
            dg_modifier = OpenMaya.MDGModifier()
            dg_modifier.disconnect(input_plugs[0], output_plug)
            dg_modifier.doIt() 
            
    def set_parent(self, child, parent):
        if isinstance(child, OpenMaya.MObject):
            child = OpenMaya.MFnDagNode(child)
        if isinstance(parent, OpenMaya.MObject):
            parent = OpenMaya.MFnDagNode(parent)
        self.unparent(child)
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'parent \"%s\" \"%s\" ' % (child.fullPathName(), parent.fullPathName())
        print mel_command
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
        mobject = self.get_mobject(results[0])   
        return mobject
    
    def unparent(self, mobject):
        if isinstance(mobject, str) or isinstance(mobject, unicode):
            mobject = self.get_mobject(mobject)
            mobject = OpenMaya.MFnDagNode(mobject)
        if isinstance(mobject, OpenMaya.MObject) or isinstance(mobject, OpenMaya.MDagPath):
            mobject = OpenMaya.MFnDagNode(mobject)
        if not self.has_parent(mobject):
            return
        mel_command = 'parent -w \"%s\"' % mobject.fullPathName()
        OpenMaya.MGlobal.executeCommand(mel_command, False, True)
        
    def has_parent(self, mobject):
        if isinstance(mobject, str) or isinstance(mobject, unicode):
            mobject = self.get_mobject(mobject)
            mobject = OpenMaya.MFnDagNode(mobject)
        if isinstance(mobject, OpenMaya.MObject) or isinstance(mobject, OpenMaya.MDagPath):
            mobject = OpenMaya.MFnDagNode(mobject)        
        parent_mobject = mobject.parent(0)
        if parent_mobject.hasFn(OpenMaya.MFn.kWorld):
            return False
        return True
          
    def freeze_transformations(self, node):
        if not isinstance(node, str):
            node = self.get_name(node)
        mcommand_result = OpenMaya.MCommandResult()        
        mel_command = 'makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1 \"%s\"' % node
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
        return results         
         
    def set_default_position(self, mobject):
        self.freeze_transformations(mobject)
        attributes = [       
            'scalePivotZ', 'rotatePivotX', 'rotatePivotY',
            'rotatePivotZ', 'scalePivotX', 'scalePivotY'
            ]
        for attribute in attributes:    
            dependency_node = OpenMaya.MFnDependencyNode(mobject)
            attr_mobject = dependency_node.attribute(attribute)
            mplug = dependency_node.findPlug(attr_mobject)
            mplug.setFloat(0.0)
           
    def delete_history(self, node): 
        dep = OpenMaya.MFnDagNode(node)
        node = dep.fullPathName()            
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'bakePartialHistory -preCache \"%s\"' % node 
        OpenMaya.MGlobal.executeCommand(mel_command, False, True)            
        
    def set_perspective_view(self):  
        position = {
            'translateX': 19, 'translateY': 10, 'translateZ': 38,
            'rotateX':-6, 'rotateY': 27, 'rotateZ': 0,
            'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
            } 
        for k, v in position.items():
            mplug = self.get_mplug('persp.%s' % k)
            attribute = mplug.attribute()
            if attribute.apiType() == OpenMaya.MFn.kDoubleAngleAttribute:
                value = OpenMaya.MAngle(v, OpenMaya.MAngle.kDegrees)
                mplug.setMAngle(value)
            else:   
                mplug.setFloat(v)
        mel_commands = [
            'setNamedPanelLayout \"Single Perspective View\";',
            'fitPanel -selectedNoChildren;'
            ]
        for mel_command in mel_commands:
            try:
                OpenMaya.MGlobal.executeCommand(mel_command, False, True)
            except Exception:
                pass               
        
    def vieport_snapshot(self, output_path=None, width=2048, height=2048):
        OpenMaya.MGlobal.clearSelectionList()
        m3d_view = OpenMayaUI.M3dView.active3dView()
        if not m3d_view.isVisible():
            OpenMaya.MGlobal.displayWarning('Active 3d View not visible!...')
            return   
        m3d_view.refresh(True, True, True)
        m_image = OpenMaya.MImage()
        m3d_view.readColorBuffer(m_image, True)        
        if not output_path:
            output_path = os.path.join(
                tempfile.gettempdir(),
                'studio_pipe_temp_%s.png' % resource.getCurrentDateKey()
            ) 
        format = os.path.splitext(output_path)[-1].replace('.', '')        
        if not format:
            format = 'png'                    
        m_image.writeToFileWithDepth(output_path, format, False) 
        swidgets.image_resize(output_path, output_path, width=width, height=width)
        return output_path, width, height
        
    def get_connections(self, node):        
        inputs = self.input_connections(node)
        data = {}
        for input in inputs:            
            output = self.output_connections(input)            
            output_mplug = self.get_mplug(output)
            value, type = self.get_attribute_type(output_mplug)
            
            if not type:
                continue
            
            output_attribute = output.split('.')[1]
            input_node, input_attribute = input.split('.')            
            data[output_attribute] = {
                'type': type,
                'value': '{}@{}'.format(input_attribute, input_node)
                }
        return data
    
    def set_connections(self, mobject, data):
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute, contents in data.items():    
            input_attribute, input_node = contents['value'].split('@')
            output_mplug = mfn_dependency_node.findPlug(attribute)
            input_mplug = self.get_mplug('%s.%s' % (input_node, input_attribute))
            dgMod = OpenMaya.MDGModifier()
            dgMod.connect(input_mplug, output_mplug)
            dgMod.doIt()
        
    def input_connections(self, node):                           
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'listConnections -s on -d off -p on \"%s\"' % (node)
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        inputs = []
        mcommand_result.getResult(inputs)
        return inputs         
         
    def output_connections(self, node):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'listConnections -s off -d on -p on \"%s\"' % (node)
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        outputs = []
        mcommand_result.getResult(outputs)
        if outputs:        
            return outputs[0]
        return None
    
    def list_attributes(self, node, default=False):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'listAttr -r -w -u -m -hd \"%s\"' % (node)
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        outputs = []
        mcommand_result.getResult(outputs)
        mplug_array = OpenMaya.MPlugArray()
        for output in outputs:
            mplug = self.get_mplug('%s.%s' % (node, output))
            if default:
                mplug_array.append(mplug)
            else:
                if mplug.isDefaultValue():
                    continue
                mplug_array.append(mplug)
        return mplug_array
    
    def get_mplug_attributes(self, node, default=False):
        mplugs = self.list_attributes(node, default=default)
        unused_attributes = []    
        for x in range(mplugs.length()):
            attribute = mplugs[x].attribute() 
            if mplugs[x].isElement():
                unused_attributes.append(mplugs[x])
            if attribute.apiType() == OpenMaya.MFn.kNumericAttribute:
                if not mplugs[x].isChild():
                    continue
                # remove if attribute is child of compound attribute
                parent_mplug = mplugs[x].parent()
                parent_mobject = parent_mplug.attribute()
                if parent_mobject.apiType() == OpenMaya.MFn.kCompoundAttribute:
                    continue
                unused_attributes.append(mplugs[x])        
        mplug_array = OpenMaya.MPlugArray()
        for x in range(mplugs.length()):
            if mplugs[x] in unused_attributes:
                continue
            mplug_array.append(mplugs[x])
        return mplug_array  
         
    def get_attributes(self, node, default=False):
        '''
            :param node <str> maya node
            :param default <bool> False ignore default value      
        '''
        mplug_array = self.get_mplug_attributes(node, default=default)
        attribute_data = {}
        for x in range(mplug_array.length()):
            value, type = self.get_attribute_type(mplug_array[x])
            # attribute_name = mplug_array[x].partialName()
            attribute_name = mplug_array[x].name().split('.')[1]
            attribute_data[attribute_name] = {
                'value': value,
                'type': type
                }
        return attribute_data

    def set_attributes(self, mobject, data):
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for attribute, contents in data.items():
            mplug = mfn_dependency_node.findPlug(attribute)
            type = contents['type']
            value = contents['value']
            
            if contents['type'] == 'IntAttr':
                try:
                    mplug.setInt(contents['value'])
                except Exception as error:
                    print 'error', error, mplug.name()
                             
            if contents['type'] == 'FloatAttr':
                try:
                    mplug.setFloat(contents['value'])
                except Exception as error:
                    print 'error', error, mplug.name()
                            
            if contents['type'] in ['2FloatAttr', '3FloatAttr']:
                for x in range(mplug.numChildren()):
                    child_mplug = mplug.child(x)
                    try:
                        child_mplug.setFloat(contents['value'][x])
                    except Exception as error:
                        print 'error', error, mplug.name()
            
            if contents['type'] == 'StringAttr':
                try:
                    mplug.setString(contents['value'])
                except Exception as error:
                    print 'error', error, mplug.name()
                 
            if contents['type'] == 'BoolAttr':
                try:
                    mplug.setBool(contents['value'])
                except Exception as error:
                    print 'error', error, mplug.name()
    
    def get_attribute_type(self, mplug):
        attribute = mplug.attribute()
        if attribute.apiType() in self.attribute_container['distance']:
            return self.klinear_attribute(mplug)                
        if attribute.apiType() in self.attribute_container['angle']:
            return self.kangle_attribute(mplug)   
        if attribute.apiType() in self.attribute_container['typed']:
            return self.ktyped_attribute(mplug, attribute)  
        if attribute.apiType() in self.attribute_container['matrix']:
            return self.kmatrix_attribute(mplug)
        if attribute.apiType() in self.attribute_container['numeric']:
            return self.knumeric_attribute(mplug, attribute)            
        if attribute.apiType() in self.attribute_container['enum']:
            return self.kenum_attribute(mplug)
        if attribute.apiType() in self.attribute_container['3float']:
            return self.k3folat_attribute(mplug)
        if attribute.apiType() in self.attribute_container['2float']:
            return self.k2folat_attribute(mplug)
        # add new attribute types
        return 'null', None       
         
    def kenum_attribute(self, mplug):        
        value = mplug.asInt()
        return value, 'IntAttr'
     
    def kmatrix_attribute(self, mplug):
        mfn_matrix = OpenMaya.MFnMatrixData(mplug.asMObject())
        value = mfn_matrix.matrix()
        return value, 'FloatAttr'
        
    def kangle_attribute(self, mplug):        
        value = mplug.asMAngle().value()
        return value, 'FloatAttr'
     
    def klinear_attribute(self, mplug):
        value = mplug.asMDistance().value()        
        return value, 'FloatAttr'
     
    def k3folat_attribute(self, mplug):    
        value = []
        for x in range(mplug.numChildren()):
            child_mplug = mplug.child(x)
            value.append(child_mplug.asFloat())
        return value, '3FloatAttr'
     
    def k2folat_attribute(self, mplug):    
        value = []
        for x in range(mplug.numChildren()):
            child_mplug = mplug.child(x)
            value.append(child_mplug.asFloat())
        return value, '2FloatAttr'
 
    def knumeric_attribute(self, mplug, attribute):    
        mfn_numeric_attribute = OpenMaya.MFnNumericAttribute(attribute)
        unit_type = mfn_numeric_attribute.unitType()
        if unit_type == OpenMaya.MFnNumericData.kBoolean:
            value = mplug.asBool()          
            return value, 'IntAttr'        
        int_data = [
            OpenMaya.MFnNumericData.kShort,
            OpenMaya.MFnNumericData.kInt,
            OpenMaya.MFnNumericData.kLong,
            OpenMaya.MFnNumericData.kByte
            ]                   
        if unit_type in int_data:
            value = mplug.asInt()          
            return value, 'IntAttr'   
        double_data = [
            OpenMaya.MFnNumericData.kFloat,
            OpenMaya.MFnNumericData.kDouble,
            OpenMaya.MFnNumericData.kAddr
            ]            
        if unit_type in double_data:
            value = mplug.asDouble()          
            return value, 'FloatAttr'
        return 'null', None
         
    def ktyped_attribute(self, mplug, attribute):  
        mfn_typed_attribute = OpenMaya.MFnTypedAttribute(attribute)
        attribute_type = mfn_typed_attribute.attrType()        
        if attribute_type == OpenMaya.MFnData.kMatrix:  # matrix
            mfn_matrix_data = OpenMaya.MFnMatrixData(mplug.asMObject())
            value = mfn_matrix_data.matrix()
            return value, 'FloatAttr'
        if attribute_type == OpenMaya.MFnData.kString:  # string
            value = mplug.asString()      
            return value, 'StringAttr'
        return 'null', None
    
    def attribute_bundles(self):
        attributes = {
            'distance': [
                OpenMaya.MFn.kDoubleLinearAttribute,
                OpenMaya.MFn.kFloatLinearAttribute
                ],
            'angle': [    
                OpenMaya.MFn.kDoubleAngleAttribute,
                OpenMaya.MFn.kFloatAngleAttribute
                ],
            'typed': [
                OpenMaya.MFn.kTypedAttribute
                ],
            'matrix': [
                OpenMaya.MFn.kMatrixAttribute
                ],
            'numeric': [
                OpenMaya.MFn.kNumericAttribute 
                ],
            'enum': [   
                OpenMaya.MFn.kEnumAttribute
                ],
            '3float': [
                OpenMaya.MFn.kAttribute3Float,
                OpenMaya.MFn.kAttribute3Double,
                # OpenMaya.MFn.kCompoundAttribute                
                ],
            '2float': [
                OpenMaya.MFn.kAttribute2Float,
                OpenMaya.MFn.kAttribute2Double
                ],
            'ramp': [
                OpenMaya.MFn.kCompoundAttribute                
                ]      
            } 
        return attributes

    def list_knode_types(self, node_type):        
        mcommand_result = OpenMaya.MCommandResult()        
        mel_command = 'listNodeTypes \"%s\"' % node_type
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
        return results      
    
    def export_selected(self, nodes, output_path, **kwargs):
        if isinstance(nodes, str) or isinstance(nodes, unicode):
            nodes = [nodes]
        format = self.maya_format
        preserve_references = False
        force = False               
        if 'format' in kwargs:
            format = kwargs['format']
        if 'preserve_references' in kwargs:
            preserve_references = kwargs['preserve_references']
        if 'force' in kwargs:
            force = kwargs['force']            
        if os.path.isfile(output_path):      
            if not force:
                raise IOError('Cannot save, already file found <%s>' % output_path)            
            os.chmod(output_path, 0777)
            try:
                os.remove(output_path)
            except Exception as error:
                raise error                  
        mselection_list = OpenMaya.MSelectionList()
        for node in nodes:
            mselection_list.add(node)    
        OpenMaya.MGlobal.setActiveSelectionList(mselection_list)
        # OpenMaya.MGlobal.selectByName(node)
        OpenMaya.MFileIO.exportSelected(output_path, format, preserve_references) 
        OpenMaya.MGlobal.clearSelectionList()        
    
    def set_bounding_box(self):
        m3d_view = OpenMayaUI.M3dView()
        for index in range (m3d_view.numberOf3dViews()):
            view = OpenMayaUI.M3dView()
            m3d_view.get3dView(index, view)
            view.setDisplayStyle(0)
            view.refresh()
            
    def get_current_file(self):
        mfileio = OpenMaya.MFileIO()
        current_file = mfileio.currentFile() 
        file_type = mfileio.fileType()
        if os.path.isfile(current_file):
            return current_file, file_type
        return None, None    
    
    def new_maya_scene(self):
        mfile = OpenMaya.MFileIO()  
        mfile.newFile(True)        
            
    def open_maya(self, maya_file, file_type=None):
        '''
        :parm file_type <str> 'mayaAscii', 'mayaBinary', 'pxrUsdImport', 'OBJ'
        '''        
        mfile = OpenMaya.MFileIO()
        mfile.open(maya_file, file_type, True, mfile.kLoadDefault, True)
            
    def import_maya(self, maya_file, file_type=None, namespace=None):
        '''
        :parm file_type <str> 'mayaAscii', 'mayaBinary', 'pxrUsdImport', 'OBJ'
        '''
        mfile = OpenMaya.MFileIO()
        mfile.importFile(maya_file, file_type, True, namespace, True)

    def reference_maya(self, maya_file, deferred=False, locked=False, namespace=None):
        mfile = OpenMaya.MFileIO()        
        mfile.reference(maya_file, deferred, locked, namespace)        
        
    def has_plugin_loaded(self, plugin):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'pluginInfo -q -loaded \"%s\"' % plugin
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        id_pointer = util.asIntPtr()
        mcommand_result.getResult(id_pointer)
        return OpenMaya.MScriptUtil(id_pointer).asBool()                 
       
    def load_plugin(self, plugin):        
        loaded = self.has_plugin_loaded(plugin)
        if loaded:
            sys.stderr.write('#warnings: already loaded <%s>' % plugin)
            return
        mel_command = 'loadPlugin -qt %s' % plugin
        try:
            OpenMaya.MGlobal.executeCommand(mel_command, False, True)
            print 'plugin register', plugin 
        except:
            sys.stderr.write('failed to register command: %s' % plugin)
            
    def load_plugins(self, plugins=None):   
        if not plugins:     
            data = resource.getPluginData()
            plugins = data['maya']
        for plugin in plugins:
            self.load_plugin(plugin)           
