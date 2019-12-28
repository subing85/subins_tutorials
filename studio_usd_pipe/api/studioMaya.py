import os
import tempfile

from maya import OpenMaya
from maya import OpenMayaUI

from PySide2 import QtGui
from PySide2 import QtCore

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from __builtin__ import False


class Maya(object):

    def __init__(self):
        self.valid_shapes = [OpenMaya.MFn.kMesh]
        self.scene_mobjects = OpenMaya.MObjectArray()
        
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

    def get_plug(self, node, attribute):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add("%s.%s" % (node, attribute))
        mselection.getPlug(0, mplug)
        return mplug    
    
    def get_root_mobject(self, mobject):
        mfn_dagnode = OpenMaya.MFnDagNode(mobject) 
        full_name = mfn_dagnode.fullPathName() 
        print  full_name      
        # mobject = self.get_mobject(full_name.split('|')[0])
        return mobject
    
    def get_name(self, maya_object):
        if isinstance(maya_object, OpenMaya.MDagPath):
            return maya_object.fullPathName().encode()
        if isinstance(maya_object, OpenMaya.MObject):
            mfn_dependency_node = OpenMaya.MFnDependencyNode(maya_object)
            return mfn_dependency_node.name().encode()
        
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
        
    def get_default_nodes(self, type=True):
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'ls -defaultNodes', mcommand_result, True, True)
        nodes = []
        mcommand_result.getResult(nodes)
        cameras = [
            'persp',
            'top',
            'front',
            'side',
            'perspShape',
            'topShape',
            'frontShape',
            'sideShape',
            'lightLinker1',
            'shapeEditorManager',
            'poseInterpolatorManager',
            'layerManager',
            'defaultLayer',
            'renderLayerManager',
            'defaultRenderLayer',
            'ikSCsolver',
            'ikRPsolver',
            'ikSplineSolver',
            'hikSolver'            
            ]          
        nodes.extend(cameras) 
        nodes = list(set(nodes))       
        mobjects = []
        if type:      
            mobjects = OpenMaya.MObjectArray()     
        for node in nodes:
            if not self.object_exists(node):
                continue
            mobject = self.get_mobject(node)
            mobjects.append(mobject)
        return mobjects        
        
    def object_exists(self, mobject):
        if isinstance(mobject, unicode) :
            mobject = mobject.encode()        
        if not isinstance(mobject, str) :
            mobject = self.get_name(mobject)
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'objExists \"%s\"' % mobject
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, True, True)
        script_util = OpenMaya.MScriptUtil()
        index_ptr = script_util.asIntPtr()        
        mcommand_result.getResult(index_ptr)
        value = script_util.getInt(index_ptr)
        data = {0: False, 1: True}
        return data[value]  
          
    def remove_node(self, mobject):
        #=======================================================================
        # if not self.object_exists(mobject):
        #     return
        # try:
        #     OpenMaya.MGlobal.deleteNode(mobject)            
        # except:
        #     pass
        #=======================================================================
        if isinstance(mobject, unicode) :
            mobject = mobject.encode()        
        if not isinstance(mobject, str):
            mobject = self.get_name(mobject)
        if not self.object_exists(mobject):
            return
        mcommand_result = OpenMaya.MCommandResult()       
        mel_command = 'delete \"%s\"' % mobject 
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
        results = []
        mcommand_result.getResult(results)
        
    def has_null_node(self, mobject, mfn_type):
        mfn_dag_node = OpenMaya.MFnDagNode(mobject)        
        count = mfn_dag_node.childCount()        
        for x in range(count):
            child = mfn_dag_node.child(x)            
            if not child.hasFn(mfn_type):
                return False
        return True
    
    def has_same_hierarchy(self, root, child):
        mfn_dag_node = OpenMaya.MFnDagNode(child)    
        root_node = mfn_dag_node.fullPathName().split('|')[1]            
        child_mobject = self.get_mobject(root_node)
        if root!=child_mobject:
            return False
        return True
                  
    def extract_depend_nodes(self, default=False):        
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes(type=False)            
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
    
    def extract_transform(self, root_mobject):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobject_array = OpenMaya.MObjectArray()
        data = {} 
        seen = data
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()            
            if not mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()
                continue 
            valid = self.has_null_node(root_mobject, OpenMaya.MFn.kTransform)
            if not valid:
                mit_dependency_nodes.next()    
                continue                 
            valid = self.has_same_hierarchy(root_mobject, mobject)
            if not valid:
                mit_dependency_nodes.next()    
                continue
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            seen = seen.setdefault(mfn_dag_node.fullPathName(), {})
            mit_dependency_nodes.next() 
        return data     
        
    def extract_transform_primitive(self, mfn_type, root_mobject=None):
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        mobjects = []
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            if not mobject.hasFn(mfn_type):
                mit_dependency_nodes.next()    
                continue                                    
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            p_mobject = mfn_dag_node.parent(0)
            if p_mobject in mobjects:
                mit_dependency_nodes.next()    
                continue            
            if root_mobject: 
                valid = self.has_same_hierarchy(root_mobject, mobject)
                if not valid:
                    mit_dependency_nodes.next()    
                    continue
            mobjects.append(p_mobject)   
            mit_dependency_nodes.next()                
        mobject_array = OpenMaya.MObjectArray()    
        for mobject in mobjects:
            mobject_array.append(mobject)
        return mobject_array   
          
        
    def extract_top_transforms(self, default=False):
        default_nodes = []
        if not default:     
            default_nodes = self.get_default_nodes(type=False)    
        mit_dependency_nodes = OpenMaya.MItDependencyNodes()
        transform_mobjects = OpenMaya.MObjectArray()
        while not mit_dependency_nodes.isDone():
            mobject = mit_dependency_nodes.item()                
            if not mobject.hasFn(OpenMaya.MFn.kTransform):
                mit_dependency_nodes.next()    
                continue             
            mfn_dag_node = OpenMaya.MFnDagNode(mobject)
            p_mobject = mfn_dag_node.parent(0)
            if not p_mobject.hasFn(OpenMaya.MFn.kWorld):
                mit_dependency_nodes.next()    
                continue             
            if mobject in default_nodes:
                mit_dependency_nodes.next()                           
                continue                                             
            transform_mobjects.append(mobject)   
            mit_dependency_nodes.next()            
        return transform_mobjects        
        
    def assign_shading_group(self, mobject, shading_group=None):
        if not shading_group:
            shading_group = self.get_mobject('initialShadingGroup')
        mfn_set = OpenMaya.MFnSet(shading_group)
        mfn_set.addMember(mobject)
        
    def create_maya_id(self, mobject, inputs):
        attributes = common.sorted_order(inputs)
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
         
    def create_group(self, name):        
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('transform')
        mfn_dag_node.setName(name)
        return mfn_dag_node
    
    def create_world(self, mfn_dag_node, parent=False):
        parent_node = OpenMaya.MFnDependencyNode(mfn_dag_node.object())
        mplug_x = parent_node.findPlug('boundingBoxMaxX')
        mplug_z = parent_node.findPlug('boundingBoxMaxZ')        
        radius = max([mplug_x.asFloat(), mplug_z.asFloat()])
        world_data = resource.getWroldData()
        world_node = self.set_kcurve(world_data, radius=radius + 0.5, name='world') 
        if parent:
            children = OpenMaya.MObjectArray()
            for x in range (mfn_dag_node.childCount()): 
                children.append(mfn_dag_node.child(x))                
            for x in range(children.length()):                
                self.set_parent(children[x], world_node.object())   
            self.set_parent(world_node.object(), mfn_dag_node.object())
        return world_node

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
        if not isinstance(child, str):
            mfn_dagpath = OpenMaya.MFnDagNode(child)
            child = mfn_dagpath.fullPathName()            
        if not isinstance(parent, str):
            mfn_dagpath = OpenMaya.MFnDagNode(parent)
            parent = mfn_dagpath.fullPathName()                             
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'parent \"%s\" \"%s\" ' % (child, parent)
        OpenMaya.MGlobal.executeCommand(
            mel_command, mcommand_result, True, True)
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
            mel_command, mcommand_result, True, True)
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

            
    def set_perspective_view(self):  
        OpenMaya.MGlobal.executeCommand('setNamedPanelLayout \"Single Perspective View\";') 
        OpenMaya.MGlobal.executeCommand('fitPanel -selectedNoChildren;')
        position = {
            'translateX': 10, 'translateY': 10, 'translateZ': 30,            
            'rotateX': -10, 'rotateY': 20, 'rotateZ': 0,
            'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
            }        
        for k, v in position.items():
            mplug = self.get_plug('persp', k)
            mplug.setFloat(v)        
        
    def vieport_snapshot(self, time_stamp, output_path=None, width=2048, height=2048):
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
        self.image_resize(output_path, output_path, time_stamp=None, width=width, height=height)
        os.utime(output_path, (time_stamp, time_stamp))
        return output_path, width, height    
    
    def image_resize(self, image_path, output_path, time_stamp=None, width=2048, height=2048):
        q_image = QtGui.QImage(image_path)
        sq_scaled = q_image.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding) 
        if sq_scaled.width() <= sq_scaled.height():
            x = 0
            y = (sq_scaled.height()-height)/2
        elif sq_scaled.width() >= sq_scaled.height():
            x = (sq_scaled.width()-width)/2
            y = 0
        copy = sq_scaled.copy(x, y, width, height) 
        copy.save(output_path)
        if time_stamp:
            os.utime(output_path, (time_stamp, time_stamp))
        return image_path
    
    def assign_shading_engine(self, mobject, shading_group=None):
        if not shading_group:            
            shading_group = 'initialShadingGroup'
        if isinstance(shading_group, str):
            shading_group = self.get_mobject(shading_group)
        mfn_set = OpenMaya.MFnSet(shading_group)
        mfn_set.addMember(mobject)

    def delete_uv_sets(self, mfn_mesh, set_names):
        for set_name in set_names:
            try:
                mfn_mesh.deleteUVSet(set_name)
            except Exception as error:
                print '\nDeleteError', error
    
    def get_shading_engine(self, mobject):
        dependency_graph = OpenMaya.MItDependencyGraph(
            mobject,
            OpenMaya.MFn.kShadingEngine,
            OpenMaya.MItDependencyGraph.kDownstream,
            OpenMaya.MItDependencyGraph.kDepthFirst,
            OpenMaya.MItDependencyGraph.kNodeLevel
            )
        shading_engines = OpenMaya.MObjectArray()
        while not dependency_graph.isDone():
            current_item = dependency_graph.currentItem()
            shading_engines.append(current_item)
            dependency_graph.next()
        return shading_engines
                            
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
    
    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order   
        
    def get_kcurve(self, mobject):        
        mfn_curve = OpenMaya.MFnNurbsCurve(mobject)                
        cvs_array = OpenMaya.MPointArray()        
        mfn_curve.getCVs(cvs_array, OpenMaya.MSpace.kObject)
        knots_array = OpenMaya.MDoubleArray()
        mfn_curve.getKnots(knots_array)
        vertices = []
        for x in range(cvs_array.length()):
            array = [
                cvs_array[x].x,
                cvs_array[x].y,
                cvs_array[x].z,
                cvs_array[x].w
            ]            
            vertices.append(array)
        data = {
            'control_vertices': vertices,
            'knots': list(knots_array),
            'degree': mfn_curve.degree(),
            'form': mfn_curve.form(),
            'name': mfn_curve.name()  
            }        
        return data
        
    def create_kcurve(self, data, radius=1, name=None):
        cv_array = self.create_mpoint_array(data['control_vertices'])
        knots_array = self.create_mdouble_array(data['knots'])
        mfn_curve = OpenMaya.MFnNurbsCurve()
        mfn_curve.create(
            cv_array,
            knots_array,
            data['degree'],
            data['form'],
            False,
            True,
            )
        mfn_curve.updateCurve() 
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mfn_curve.parent(0))
        mfn_dependency_node.setName(name)        
        mplug_x = mfn_dependency_node.findPlug('scaleX')
        mplug_y = mfn_dependency_node.findPlug('scaleY')  
        mplug_z = mfn_dependency_node.findPlug('scaleZ')  
        mplug_x.setFloat(radius)
        mplug_y.setFloat(radius)
        mplug_z.setFloat(radius)
        self.freeze_transformations(mfn_dependency_node.object())
        return mfn_dependency_node    
    
    def get_kmodel(self, mobject):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        point_array = OpenMaya.MFloatPointArray()
        mfn_mesh.getPoints(point_array, OpenMaya.MSpace.kObject)
        vertex_count = OpenMaya.MIntArray()
        vertex_array = OpenMaya.MIntArray()
        mfn_mesh.getVertices(vertex_count, vertex_array)        
        vertice_list = []
        for index in range(point_array.length()):
            points = point_array[index]
            vertice_list.append((points.x, points.y, points.z, points.w))
        #=======================================================================
        # parent_mobject = mfn_mesh.parent(0)
        # parent_mfn_dag_node = OpenMaya.MFnDagNode(parent_mobject)
        #=======================================================================
        data = {
            'vertices': vertice_list,
            'vertex_count': list(vertex_count),
            'vertex_list': list(vertex_array),
            'num_vertices': mfn_mesh.numVertices(),
            'num_polygons': mfn_mesh.numPolygons(),
            'shape':  mfn_mesh.name(),
            }
        return data    
    
    def create_kmodel(self, data):
        num_vertices = data['num_vertices']
        num_polygons = data['num_polygons']
        vertex_array = self.create_floatpoint_array(data['vertices'])
        vertex_count = self.create_int_array(data['vertex_count'])
        vertex_list = self.create_int_array(data['vertex_list'])        
        mfn_mesh = OpenMaya.MFnMesh()
        mfn_mesh.create(
            num_vertices,
            num_polygons,
            vertex_array,
            vertex_count,
            vertex_list
            )        
        # rename        
        mfn_mesh.setName(data['shape'])        
        parent_mobject = mfn_mesh.parent(0)
        #=======================================================================
        # parent_mfn_dag_node = OpenMaya.MFnDagNode(parent_mobject)
        # parent_mfn_dag_node.setName(name)
        # self.assign_shading_engine(mfn_mesh.object())
        #=======================================================================
        mfn_mesh.updateSurface()
        return mfn_mesh
    
    def get_kuv(self, mobject):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)
        data = {}
        for index, set_name in enumerate(set_names):
            u_array = OpenMaya.MFloatArray()
            v_array = OpenMaya.MFloatArray()
            mfn_mesh.getUVs(u_array, v_array, set_name)
            uv_counts = OpenMaya.MIntArray()
            uv_ids = OpenMaya.MIntArray()
            mfn_mesh.getAssignedUVs(uv_counts, uv_ids, set_name)
            uvset_data = {
                'u_array': list(u_array),
                'v_array': list(v_array),
                'uv_counts': list(uv_counts),
                'uv_ids': list(uv_ids),
                'order': index
                }
            data.setdefault(set_name, uvset_data)
        return data        

    def create_kuv(self, mobject, data):
        mfn_mesh = OpenMaya.MFnMesh(mobject)
        set_names = []
        mfn_mesh.getUVSetNames(set_names)                
        self.delete_uv_sets(mfn_mesh, set_names)        
        sorted_data = self.sort_dictionary(data)        
        for index, set_name in enumerate(sorted_data):
            contents = data[set_name]
            u_array = self.create_float_array(contents['u_array'])
            v_array = self.create_float_array(contents['v_array'])
            uv_counts = self.create_int_array(contents['uv_counts'])
            uv_ids = self.create_int_array(contents['uv_ids'])            
            if index==0:
                mfn_mesh.clearUVs(set_name)
                mfn_mesh.renameUVSet(set_names[0], set_name)
            else:
                set_name = mfn_mesh.createUVSetWithName(set_name)                
            mfn_mesh.setUVs(u_array, v_array, set_name)
            mfn_mesh.assignUVs(uv_counts, uv_ids, set_name)
        mfn_mesh.updateSurface()
        return mfn_mesh
    
    
    def get_kpreviewshader(self, mobject):
        mobject_array = self.get_shading_engine(mobject)
        
        if not mobject_array.length():
            raise Exception('can not found any assignment to shading engine!...')
 
        
    
    
    def create_kshader(self, data):
        pass
    


    
    
    
    
    
          
        
        
                            
            
    #===========================================================================
    # def get_shadingengine(self, mobject):
    #     shading_engine_array = self.get_dependences(
    #         mobject, OpenMaya.MFn.kShadingEngine)
    #     return shading_engine_array    
    # 
    # def get_networks(self, mshader_engine):
    #     if not object:
    #         return
    #     mfn_dependency_node = OpenMaya.MFnDependencyNode(mshader_engine)
    #     shader_engine = mfn_dependency_node.name().encode()
    #     mcommand_result = OpenMaya.MCommandResult()
    #     OpenMaya.MGlobal.executeCommand(
    #         'listHistory %s' % shader_engine, mcommand_result, True, True)
    #     nodes = []
    #     mcommand_result.getResult(nodes)        
    #     assign_objects = self.get_assign_objects(mshader_engine)
    #     networks = []
    #     for node in nodes:
    #         py_node = core.PyNode(node)
    #         if py_node.type() in self.default_node_types:
    #             continue
    #         if node in self.default_nodes:
    #             continue                        
    #         if node in networks:
    #             continue
    #         if node in assign_objects:
    #             continue
    #         networks.append(node.encode())
    #     return networks, assign_objects   
    # 
    # def get_assign_objects(self, mshading_engine):
    #     mfn_set = OpenMaya.MFnSet(mshading_engine)
    #     selection_list = OpenMaya.MSelectionList()
    #     mfn_set.getMembers(selection_list, False)
    #     objects = []
    #     if not selection_list.length():
    #         return objects
    #     for index in range(selection_list.length()):
    #         m_dag_path = OpenMaya.MDagPath()
    #         selection_list.getDagPath(index, m_dag_path)
    #         objects.append(m_dag_path.partialPathName())
    #     return objects
    # 
    # def get_assign_components(self, mshading_engine):
    #     mfn_set = OpenMaya.MFnSet(mshading_engine)
    #     selection_list = OpenMaya.MSelectionList()
    #     mfn_set.getMembers(selection_list, False)
    #     component_data = {}
    #     if not selection_list.length():
    #         return mfn_set.name(), component_data
    #     for index in range(selection_list.length()):
    #         components = []
    #         selection_list.getSelectionStrings(components)
    #         if components in component_data.values():
    #             continue
    #         component_data.setdefault(index, components)
    #         
    #     return mfn_set.name(), component_data
    # 
    # def assigin_lambert(self, mobjects):        
    #     for x in range(mobjects.length()):
    #         pass
    #         
    # 
    # def get_default_node_types(self):    
    #     node_types = [
    #         'lightLinker',
    #         'materialInfo',
    #         'nodeGraphEditorInfo',
    #         'partition',
    #         'groupId',
    #         'hyperShadePrimaryNodeEditorSavedTabsInfo',
    #         'renderPartition',
    #         'timeToUnitConversion'
    #         ]
    #     return node_types
    # 
    # def get_valid_attribute(self):
    #     attr_types = [
    #         'bool',
    #         'byte',
    #         'enum',
    #         'string',
    #         'long',
    #         'short',
    #         'typed',
    #         'float3',
    #         'float',
    #         'TdataCompound',
    #         'time',
    #         'float2',
    #         'double',
    #         'doubleAngle',
    #         'char'
    #     ]
    #     return attr_types    
    # 
    # def has_node(self, mfn_dag_node, node_type):        
    #     for x in range (mfn_dag_node.childCount()): 
    #         child_object = mfn_dag_node.child(x)
    #         if child_object.hasFn(node_type):          
    #             return True
    #     return False                
    #             
    # def get_shape_node(self, chidren):
    #     for child in chidren:
    #         if child.type() != 'mesh':
    #             continue
    #         return [child]
    #     return chidren
    #===========================================================================

