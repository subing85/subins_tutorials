import os
import tempfile

from maya import OpenMaya
from maya import OpenMayaUI

from studio_usd_pipe import resource
from studio_usd_pipe.core import image

reload(resource)
reload(image)


class Maya(object):

    def __init__(self):
        self.valid_shapes = [OpenMaya.MFn.kMesh]
        self.scene_mobjects = OpenMaya.MObjectArray()        
        self.node_data = resource.getNodeData()
        
    def is_dagpath(self, mobject):           
        mobject = self.get_mobject(mobject)
        result = None
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
            if mfn_dependency_node.name() == object_nmae:
                return True       
            mit_dependency_nodes.next()
        return False
          
    def remove_node(self, mobject):
        #=======================================================================
        # if not self.object_exists(mobject):
        #     return
        # try:
        #     OpenMaya.MGlobal.deleteNode(mobject)            
        # except:
        #     pass
        #=======================================================================
        if not isinstance(mobject, str):
            mobject = self.get_name(mobject)
        if not self.object_exists(mobject):
            return
        mcommand_result = OpenMaya.MCommandResult()       
        mel_command = 'delete \"%s\"' % mobject 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
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
        
        print mel_command
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
        
    #===========================================================================
    # def has_null_node(self, mobject, mfn_type):
    #     mfn_dag_node = OpenMaya.MFnDagNode(mobject)        
    #     count = mfn_dag_node.childCount()        
    #     for x in range(count):
    #         child = mfn_dag_node.child(x)            
    #         if not child.hasFn(mfn_type):
    #             return False
    #     return True
    #===========================================================================
    
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
        
    def extract_transform_primitive(self, mfn_type, root_mobject=None):
        # OpenMaya.MFn.kMesh
        mit_dependency_nodes = OpenMaya.MItDependencyNodes(mfn_type)
        dag_paths = []
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item() 
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            if root_mobject:
                root = mfn_dag_node.fullPathName().split('|')[1]    
                current_root_mobject = self.get_mobject(root)
                if current_root_mobject != root_mobject:
                    mit_dependency_nodes.next()
                    continue  
            p_mobject = mfn_dag_node.parent(0)       
            p_dag_node = OpenMaya.MFnDagNode(p_mobject)
            p_dag_path = OpenMaya.MDagPath()
            p_dag_node.getPath(p_dag_path)
            if p_dag_path in dag_paths:                
                mit_dependency_nodes.next()
                continue
            dag_paths.append(p_dag_path)
            mit_dependency_nodes.next()
        dag_path_array = OpenMaya.MDagPathArray()
        for dag_path in dag_paths:
            dag_path_array.append(dag_path)
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
        
    def create_maya_id(self, mobject, inputs):
        attributes = self.sort_dictionary(inputs)
        self.remove_maya_id(mobject, inputs)
        hidden = {True: False, False: True} 
        for attribute in attributes:
            short = inputs[attribute]['short']
            type_attribute = OpenMaya.MFnTypedAttribute()
            sample_mobject = OpenMaya.MObject()
            sample_mobject = type_attribute.create(attribute, short, OpenMaya.MFnData.kString)
            type_attribute.setKeyable(False)
            type_attribute.setReadable(True)
            type_attribute.setChannelBox(False)
            type_attribute.setWritable(inputs[attribute]['locked'])
            type_attribute.setHidden(hidden[inputs[attribute]['show']])
            mfn_dependency_node = OpenMaya.MFnDependencyNode()  
            mfn_dependency_node.setObject(mobject)
            mfn_dependency_node.addAttribute(sample_mobject)
            mplug = mfn_dependency_node.findPlug(type_attribute.name())
            mplug.setString(inputs[attribute]['value'])     
                        
    def remove_maya_id(self, mobject, inputs):
        mfn_dependency = OpenMaya.MFnDependencyNode(mobject)
        for attribute in inputs:
            if not mfn_dependency.hasAttribute(attribute):
                continue
            attribute_mobject = mfn_dependency.attribute(attribute)
            mfn_dependency.removeAttribute(
                attribute_mobject,
                OpenMaya.MFnDependencyNode.kLocalDynamicAttr
                )  
            
    def set_locked(self, mobject, attributes=None, locked=True):
        
        print '\n-------------', mobject, '\n-------------------'
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
        if not isinstance(child, str):
            mfn_dagpath = OpenMaya.MFnDagNode(child)
            child = mfn_dagpath.fullPathName()            
        if not isinstance(parent, str):
            mfn_dagpath = OpenMaya.MFnDagNode(parent)
            parent = mfn_dagpath.fullPathName()                             
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'parent \"%s\" \"%s\" ' % (child, parent)
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
        results = []
        mcommand_result.getResult(results)
        mobject = self.get_mobject(results[0])   
        return mobject         
         
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
        OpenMaya.MGlobal.executeCommand(mel_command)            

    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order   
        
    def set_perspective_view(self):  
        OpenMaya.MGlobal.executeCommand('setNamedPanelLayout \"Single Perspective View\";') 
        position = {
            'translateX': 32, 'translateY': 8, 'translateZ': 63,
            'rotateX':-6, 'rotateY': 27, 'rotateZ': 0,
            'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
            }        
        for k, v in position.items():
            mplug = self.get_mplug('persp.%s'%k)
            attribute = mplug.attribute()
            if attribute.apiType() == OpenMaya.MFn.kDoubleAngleAttribute:
                value = OpenMaya.MAngle(v, OpenMaya.MAngle.kDegrees)
                mplug.setMAngle(value)
            else:   
                mplug.setFloat(v)  
        OpenMaya.MGlobal.executeCommand('fitPanel -selectedNoChildren;')
        
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
                'studio_pipe_temp.png'
            )            
        format = os.path.splitext(output_path)[-1].replace('.', '')        
        if not format:
            format = 'png'                    
        m_image.writeToFileWithDepth(output_path, format, False) 
        image.image_resize(output_path, output_path, width=width, height=height)
        return output_path, width, height
        
    def get_connections(self, node):        
        inputs = self.input_connections(node)
        data = {}
        for input in inputs:            
            output = self.output_connections(input)            
            output_attribute = output.split('.')[1]
            input_node, input_attribute = input.split('.')            
            data[output_attribute] = {
                'type': 'StringAttr',
                'value': '{}@{}'.format(input_attribute, input_node)
                }
        return data    
        
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
            
    def get_attributes(self, object, default=False):
        '''
            :param mobject <str> shading dependency node
            :param default <bool> False ignore default value 
        '''        
        attribute_types = {
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
                ]
            }        
        data = {}
        mplug_array = self.get_mplug_attributes(object) 
        
        for x in range(mplug_array.length()):
            attribute = mplug_array[x].attribute()
            
            

            #===================================================================
            # ramp1.colorEntryList[0].color kAttribute3Float
            # ramp1.colorEntryList[1].position kNumericAttribute
            # ramp1.colorEntryList[1].color kAttribute3Float
            # ramp1.colorEntryList[2].position kNumericAttribute
            # ramp1.colorEntryList[2].color kAttribute3Float
            # ramp1.colorEntryList[3].position kNumericAttribute
            # ramp1.colorEntryList[3].color kAttribute3Float
            # ramp1.uWave kNumericAttribute
            # ramp1.vWave kNumericAttribute
            #===================================================================


     
            value, type = 'null', None
            attribute = mplug_array[x].attribute()
            api_type = attribute.apiType() 
            if api_type in attribute_types['distance']:
                value, type = self.klinear_attribute(mplug_array[x])                
            if api_type in attribute_types['angle']:
                value, type = self.kangle_attribute(mplug_array[x])   
            if api_type in attribute_types['typed']:
                value, type = self.ktyped_attribute(mplug_array[x], attribute)  
            if api_type in attribute_types['matrix']:
                value, type = self.kmatrix_attribute(mplug_array[x])
            if api_type in attribute_types['numeric']:
                value, type = self.knumeric_attribute(mplug_array[x], attribute)            
            if api_type in attribute_types['enum']:
                value, type = self.kenum_attribute(mplug_array[x])
            if api_type in attribute_types['3float']:
                value, type = self.k3folat_attribute(mplug_array[x])
            if value == 'null':
                continue    
            attribute_name = '.'.join(mplug_array[x].name().split('.')[1:])
            data[attribute_name] = {
                'value': value,
                'type': type
                }  
        return data    
    
    def _get_mplug_attributes(self, object):        
        attributes = self.list_attributes(object)        
        normal_attributes = []
        remove_attributes = []        
        for attribute in attributes:   
            mplug = self.get_mplug('%s.%s'%(object, attribute))
            attr_mobject = mplug.attribute()            
            if mplug.isElement():
                for x in range (mplug.numChildren()):
                    remove_attributes.append(mplug.child(x).name())
            if mplug.isChild(): 
                if attr_mobject.apiType() in [OpenMaya.MFn.kAttribute3Double, OpenMaya.MFn.kAttribute3Float]:
                    if mplug.isDefaultValue():
                        continue
                    if mplug.name() in normal_attributes:
                        continue                     
                    normal_attributes.append(mplug.name())
                if attr_mobject.apiType()==OpenMaya.MFn.kNumericAttribute:
                    parent_mplug = mplug.parent()
                    parent_mobject = parent_mplug.attribute()
                    if parent_mobject.apiType()!=OpenMaya.MFn.kCompoundAttribute:
                        continue
                    # if mplug in normal_attributes:
                    #     continue
                    if mplug.isDefaultValue():
                        continue                        
                    normal_attributes.append(mplug.name())                    
                continue
            if mplug.isDefaultValue():
                continue               
            if mplug.name() in normal_attributes:
                continue        
            normal_attributes.append(mplug.name())   
        mplug_array = []
        for attribute in normal_attributes:
            if attribute in remove_attributes:
                continue
            mplug_array.append(attribute)  
        return mplug_array

    def get_mplug_attributes(self, object):        
        attributes = self.list_attributes(object)        
        normal_attributes = []
        remove_attributes = []        
        for attribute in attributes:   
            mplug = self.get_mplug('%s.%s'%(object, attribute))
            attr_mobject = mplug.attribute()            
            if mplug.isElement():
                for x in range (mplug.numChildren()):
                    remove_attributes.append(mplug.child(x))
            if mplug.isChild(): 
                if attr_mobject.apiType() in [OpenMaya.MFn.kAttribute3Double, OpenMaya.MFn.kAttribute3Float]:
                    #if mplug in normal_attributes:
                    #    continue            
                    if mplug.isDefaultValue():
                        continue
                    normal_attributes.append(mplug)
                if attr_mobject.apiType()==OpenMaya.MFn.kNumericAttribute:
                    parent_mplug = mplug.parent()
                    parent_mobject = parent_mplug.attribute()
                    if parent_mobject.apiType()!=OpenMaya.MFn.kCompoundAttribute:
                        continue
                    # if mplug in normal_attributes:
                    #     continue
                    if mplug.isDefaultValue():
                        continue                        
                    normal_attributes.append(mplug)                    
                continue
            if mplug.isDefaultValue():
                continue               
            if mplug in normal_attributes:
                continue        
            normal_attributes.append(mplug)   
        mplug_array = OpenMaya.MPlugArray()
        for attribute in normal_attributes:
            if attribute in remove_attributes:
                continue
            mplug_array.append(attribute)  
        return mplug_array   
    
    def list_attributes(self, node):
        mcommand_result = OpenMaya.MCommandResult()       
        mel_command = 'listAttr -r -c -w -o -u -m -hd  \"%s\"' % node 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, False, True)
        attributes = []
        mcommand_result.getResult(attributes)
        return attributes            
            
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
    
    def export_selected(self, node, output_path, **kwargs):
        format='mayaAscii'
        preserve_references=False
        force = False               
        if 'format' in kwargs:
            format = kwargs['format']
        if 'preserve_references' in kwargs:
            preserve_references = kwargs['preserve_references']
        if 'force' in kwargs:
            force = kwargs['force']            
               
        if os.path.isfile(output_path):      
            if not force:
                raise IOError('Cannot save, already file found <%s>'%output_path)            
            os.chmod(output_path, 0777)
            try:
                os.remove(output_path)
            except Exception as error:
                raise error                  
                                
        OpenMaya.MGlobal.selectByName(node)
        OpenMaya.MFileIO.exportSelected(output_path, format, preserve_references) 
