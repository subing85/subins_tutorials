import json
import warnings
import logging

from pprint import pprint


from pymel import core
from maya import OpenMaya
from maya import OpenMayaAnim


class Connect(object):

    def __init__(self):

        self.crowd_parameter = 'crowd_type'

        #======================================================================
        # logging.basicConfig(level=logging.DEBUG,
        #                     format='%(asctime)s %(levelname)s %(message)s',
        #                     filename='/tmp/myapp.log',
        #                     filemode='w')
        #======================================================================

    def getDagPath(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getMObject(self, node):
        mselection = OpenMaya.MSelectionList()
        mselection.add(node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject

    def skeleton_type(self, mobject):
        if not isinstance(mobject, OpenMaya.MObject):
            mobject = self.getMObject(mobject)
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        if not mfn_dependency_node.hasAttribute(self.crowd_parameter):
            logging.warning('MObject not valid %s' %
                            mfn_dependency_node.name())
            return None
        mplug = mfn_dependency_node.findPlug(self.crowd_parameter)
        return mplug.asString()

    def getAnimCurves(self, mobject):
        if not isinstance(mobject, OpenMaya.MObject):
            mobject = self.getMObject(mobject)
        anim_node_data = {}
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)
        for x in range(mfn_dependency_node.attributeCount()):
            attribute = mfn_dependency_node.attribute(x)
            mfn_attribute = OpenMaya.MFnAttribute(attribute)
            attr_name = mfn_attribute.name()
            current_plug = mfn_dependency_node.findPlug(attr_name, True)
            if not current_plug.isConnected():
                continue
            mplug_array = OpenMaya.MPlugArray()
            current_plug.connectedTo(mplug_array, True, False)
            if mplug_array.length() != 1:
                continue
            connected_node = mplug_array[0].node()
            if not connected_node.hasFn(OpenMaya.MFn.kAnimCurve):
                continue
            anim_node_data.setdefault(mfn_attribute.name(), connected_node)
        return anim_node_data

    def read_ainmations(self, nodes):
        anim_datas = {}
        for each_node in nodes:
            anim_data = self.read_ainmation(each_node)
            anim_datas.setdefault(each_node.name().encode(), anim_data)
        return anim_datas

    def read_ainmation(self, mobject):
        '''
            from pymel import core
            from crowd.api import crowdMaya
            reload(crowdMaya)
            node = core.ls(sl=1)[0]        
            crowd_maya = crowdMaya.Connect()
            crowd_maya.read_ainmation(node)
        '''
        if not isinstance(mobject, OpenMaya.MObject):
            mobject = self.getMObject(mobject)

        anim_node_data = self.getAnimCurves(mobject)

        if not anim_node_data:
            logging.warning('not found any anim curve nodes')
            return

        anim_data = {}
        for attr, attr_mobject in anim_node_data.items():
            data = self.getAnimData(attr_mobject)
            anim_data.setdefault(attr.encode(), data)
        return anim_data

    def write_animations(self, nodes, datas):
        pass

    def write_animation(self, node, data):
        pass

    def getAnimData(self, mobject):
        mfn_anim_curve = OpenMayaAnim.MFnAnimCurve(mobject)

        pre_infinity = mfn_anim_curve.preInfinityType()
        post_infinity = mfn_anim_curve.postInfinityType()
        weighted_tangent = mfn_anim_curve.isWeighted()
        num_keys = mfn_anim_curve.numKeys()

        time_list = []
        key_list = []
        in_tangent_x_list = []
        in_tangent_y_list = []
        out_tangent_x_list = []
        out_tangent_y_list = []
        in_tangent_angle_list = []
        in_tangent_weight_list = []
        out_tangent_angle_list = []
        out_tangent_weight_list = []
        in_tangent_type_list = []
        out_tangent_type_list = []
        breakdown_list = []

        for index in range(num_keys):
            time = mfn_anim_curve.time(index).value()
            key_value = mfn_anim_curve.value(index)

            in_tangent_x = OpenMaya.MScriptUtil().asFloatPtr()
            in_tangent_y = OpenMaya.MScriptUtil().asFloatPtr()
            out_tangent_x = OpenMaya.MScriptUtil().asFloatPtr()
            out_tangent_y = OpenMaya.MScriptUtil().asFloatPtr()
            in_tangent_angle = OpenMaya.MAngle()
            in_tangent_weight = OpenMaya.MScriptUtil().asDoublePtr()
            out_tangent_angle = OpenMaya.MAngle()
            out_tangent_weight = OpenMaya.MScriptUtil().asDoublePtr()

            #==================================================================
            # mfn_anim_curve.getTangent(index, in_tangent_x, in_tangent_y, True)
            # mfn_anim_curve.getTangent(index, out_tangent_x, out_tangent_y, False)
            # mfn_anim_curve.getTangent(index, in_tangent_angle, in_tangent_weight, True)
            # mfn_anim_curve.getTangent(index, out_tangent_angle, out_tangent_weight, False)
            #==================================================================

            in_tangent_type = mfn_anim_curve.inTangentType(index)
            out_tangent_type = mfn_anim_curve.outTangentType(index)
            breakdown = mfn_anim_curve.isBreakdown(index)

            time_list.append(time)
            key_list.append(key_value)
            in_tangent_x_list.append(
                OpenMaya.MScriptUtil.getFloat(in_tangent_x))
            in_tangent_y_list.append(
                OpenMaya.MScriptUtil.getFloat(in_tangent_y))
            out_tangent_x_list.append(
                OpenMaya.MScriptUtil.getFloat(out_tangent_x))
            out_tangent_y_list.append(
                OpenMaya.MScriptUtil.getFloat(out_tangent_y))
            in_tangent_angle_list.append(in_tangent_angle.value())
            in_tangent_weight_list.append(
                OpenMaya.MScriptUtil.getDouble(in_tangent_weight))
            out_tangent_angle_list.append(out_tangent_angle.value())
            out_tangent_weight_list.append(
                OpenMaya.MScriptUtil.getDouble(out_tangent_weight))

            in_tangent_type_list.append(in_tangent_type)
            out_tangent_type_list.append(out_tangent_type)
            breakdown_list.append(breakdown)

        anim_curve_data = {}

        anim_curve_data['time'] = time_list
        anim_curve_data['key'] = key_list
        anim_curve_data['in_tangent_x'] = in_tangent_x_list
        anim_curve_data['in_tangent_y'] = in_tangent_y_list
        anim_curve_data['out_tangent_x'] = out_tangent_x_list
        anim_curve_data['out_tangent_y'] = out_tangent_y_list
        anim_curve_data['in_tangent_angle'] = in_tangent_angle_list
        anim_curve_data['in_tangent_weight'] = in_tangent_weight_list
        anim_curve_data['out_tangent_angle'] = out_tangent_angle_list
        anim_curve_data['out_tangent_weight'] = out_tangent_weight_list
        anim_curve_data['in_tangent_type'] = in_tangent_type_list
        anim_curve_data['out_tangent_type'] = out_tangent_type_list
        anim_curve_data['breakdown'] = breakdown_list
        anim_curve_data['name'] = mfn_anim_curve.name().encode()

        return anim_curve_data    
    
    def addMessageAttribute(self, mobject, long, short, value=None):     
        if isinstance(mobject, OpenMaya.MDagPath):
            mobject = mobject.node()
        if isinstance(mobject, str) or isinstance(mobject, unicode):
            mobject = self.getMObject(mobject)                    
        type_attribute = OpenMaya.MFnTypedAttribute()
        attribute_mobject = OpenMaya.MObject()
        attribute_mobject = type_attribute.create(long, short, OpenMaya.MFnData.kString)
        type_attribute.setKeyable(False)
        type_attribute.setWritable(True)
        type_attribute.setReadable(False)
        type_attribute.setStorable(True)
        type_attribute.setChannelBox(True)
        mfn_dependency_node = OpenMaya.MFnDependencyNode()  
        mfn_dependency_node.setObject(mobject)
        mfn_dependency_node.addAttribute(attribute_mobject)        
        if value:        
            mplug = mfn_dependency_node.findPlug(type_attribute.name())
            mplug.setString(value)       
        return mfn_dependency_node

