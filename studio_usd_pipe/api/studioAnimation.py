import os
import tempfile

from maya import OpenMaya
from maya import OpenMayaAnim

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.api import studioMaya
reload(studioMaya)


class Animation(studioMaya.Maya):
    
    def __init__(self):
        super(Animation, self).__init__()
        
        
    def get_animation_data(self, mobject):
        transform_nodes = self.extract_transform(root_mobject=mobject)
        data = {}
        for x in range(transform_nodes.length()):
            model_data = self.get_kanimation(transform_nodes[x].node())
            if not model_data:
                continue
            model_data['order'] = x
            data.setdefault(transform_nodes[x].fullPathName(), model_data)            
        return data

    def get_kanimation(self, mobject) :
        '''
            import json
            from studio_usd_pipe.api import studioAnimation
            reload(studioAnimation)
            sanim = studioAnimation.Animation()
            mobject = sanim.get_mobject('pSphere1')
            data = sanim.get_kanimation(mobject)
            print json.dumps(data, indent=4)
        '''
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mobject)        
        anmation_data = {}
        for index in range (mfn_dependency_node.attributeCount()) :
            attribute = mfn_dependency_node.attribute(index)
            mplug = mfn_dependency_node.findPlug(attribute) 
            anim_curve_mobject = self.get_anim_curve(mplug)
            if not anim_curve_mobject:
                continue
            curve_data = self.get_kanimCurve(anim_curve_mobject)
            mfnAttribute = OpenMaya.MFnAttribute(mplug.attribute())            
            anmation_data.setdefault(mfnAttribute.name(), curve_data) 
        return anmation_data  
    
    def get_anim_curve(self, mplug):
        connections = OpenMaya.MPlugArray()
        mplug.connectedTo (connections, 1, 0)        
        for index in range (connections.length()) :  
            connected_mplug = connections[index]
            connected_mobject = connected_mplug.node() 
            if not connected_mobject.hasFn(OpenMaya.MFn.kAnimCurve) :
                continue
            return connected_mobject
        return None
    
    def get_tanget(self, mfn_anim_curve, index, tanget):
        mscript_util_x = OpenMaya.MScriptUtil()
        tangent_x = mscript_util_x.asFloatPtr()        
        mscript_util_y = OpenMaya.MScriptUtil()
        tangent_y = mscript_util_y.asFloatPtr()
        mfn_anim_curve.getTangent(index, tangent_x, tangent_y, tanget)
        x_value = mscript_util_x.getFloat(tangent_x)
        y_value = mscript_util_y.getFloat(tangent_y)
        return x_value, y_value
    
    def get_tanget_angle_weight(self, mfn_anim_curve, index, tanget):
        mangle = OpenMaya.MAngle()
        mscript_util = OpenMaya.MScriptUtil()
        mweight = mscript_util.asDoublePtr()           
        mfn_anim_curve.getTangent(index, mangle, mweight, tanget)        
        angle = mangle.asDegrees()        
        weight = mscript_util.getDouble(mweight)
        return angle, weight     
        
    def get_kanimCurve(self, mobject):               
        mfn_anim_curve = OpenMayaAnim.MFnAnimCurve(mobject)        
        pre_infinity_type = mfn_anim_curve.preInfinityType()  # preInfinityType        
        post_infinity_type = mfn_anim_curve.postInfinityType()  # postInfinityType
        static = mfn_anim_curve.isStatic()
        weighted = mfn_anim_curve.isWeighted()  
        num_keys = mfn_anim_curve.numKeys()
        times = []
        values = []     
        in_tangents = []
        out_tangents = []        
        in_tangents_angle_weight = []
        out_tangents_angle_weight = []
        int_angents_type = []
        out_tangents_type = []
        breakdowns = []
        weights_locked = []
        tangents_locked = []   
        for index in range (num_keys):
            time = mfn_anim_curve.time(index).value()
            value = mfn_anim_curve.value(index)              
            intangent_x, intangent_y = self.get_tanget(mfn_anim_curve, index, True)  # In Tangent
            outtangent_x, outtangent_y = self.get_tanget(mfn_anim_curve, index, False)  # Out Tangent
            intangent_angle, intangent_weight = self.get_tanget_angle_weight(mfn_anim_curve, index, True)  # In Tangent angle and weight
            outtangent_angle, outtangent_weight = self.get_tanget_angle_weight(mfn_anim_curve, index, False)  # out Tangent angle and weight
            in_tangent_type = mfn_anim_curve.inTangentType(index)  # In Tangent Type   
            out_tangent_type = mfn_anim_curve.outTangentType(index)  # Out Tangent Type    
            breakdown = mfn_anim_curve.isBreakdown(index)  # isBreakdown
            weight_locked = mfn_anim_curve.weightsLocked(index)
            tangent_locked = mfn_anim_curve.tangentsLocked(index)
            times.append(time)
            values.append(value)
            in_tangents.append([intangent_x, intangent_y])
            out_tangents.append([outtangent_x, outtangent_y])
            in_tangents_angle_weight.append([intangent_angle, intangent_weight])
            out_tangents_angle_weight.append([outtangent_angle, outtangent_weight])
            int_angents_type.append(in_tangent_type) 
            out_tangents_type.append(out_tangent_type) 
            breakdowns.append(breakdown) 
            weights_locked.append(weight_locked)
            tangents_locked.append(tangent_locked)
        anim_curve_data = {
            'anim_curve': mfn_anim_curve.name(),
            'pre_infinity_type': pre_infinity_type,
            'post_infinity_type': post_infinity_type,
            'static': static,
            'weighted': weighted,
            'time': times,
            'value': values,
            'num_keys': num_keys,
            'in_tangent': in_tangents,
            'out_tangent': out_tangents,
            'in_tangent_angle_weight': in_tangents_angle_weight,
            'out_tangent_angle_weight': out_tangents_angle_weight,
            'in_tangent_type': int_angents_type,
            'out_tangent_type': out_tangents_type,
            'breakdown': breakdowns,
            'weightlocked': weights_locked,
            'tangentlocked': tangents_locked,
            }   
        return anim_curve_data
    
    def create_animation(self, name, data):        
        self.inset_kanimation(name, data)
    
    def inset_kanimation(self, name, data):
        self.create_kanimation(name, data)
    
    def replace_kanimation(self, name, data):       
        self.remove_kanimation(name, data)
        self.create_kanimation(name, data)
        
    def remove_kanimation(self, name, data):
        for attribute, contents in data.items():            
            mplug = self.get_mplug('%s.%s' % (name, attribute))        
            mfn_anim_curve = self.create_animation_curve(mplug)
            if not mfn_anim_curve:
                continue
            self.remove_node(mfn_anim_curve.name())
         
    def create_kanimation(self, name, data):
        '''
            import json
            from studio_usd_pipe.api import studioAnimation
            reload(studioAnimation)
            sanim = studioAnimation.Animation()
            mobject = sanim.get_mobject('pSphere1')
            data = sanim.get_kanimation(mobject)
            sanim.create_kanimation('pCube1', data)        
        '''
        for attribute, contents in data.items():            
            mplug = self.get_mplug('%s.%s' % (name, attribute))
            mfn_anim_curve = self.create_animation_curve(mplug)
            self.set_animation_values(mfn_anim_curve, contents)

    def create_animation_curve(self, mplug) :
        anim_curve = self.get_anim_curve(mplug)
        if anim_curve:
            mfn_anim_curve = OpenMayaAnim.MFnAnimCurve(anim_curve)       
        else:
            mfn_anim_curve = OpenMayaAnim.MFnAnimCurve()    
            anim_curve_type = mfn_anim_curve.timedAnimCurveTypeForPlug(mplug)            
            mfn_anim_curve.create(mplug, anim_curve_type)            
        return mfn_anim_curve
    
    def set_animation_values(self, mfn_anim_curve, values):
        mfn_anim_curve.setIsWeighted(values['weighted'])   
        mfn_anim_curve.setPreInfinityType(values['pre_infinity_type'])
        mfn_anim_curve.setPostInfinityType(values['post_infinity_type'])
        mtime_array = OpenMaya.MTimeArray()
        mdouble_array = OpenMaya.MDoubleArray()    
        for index in range (len(values['time'])) :    
            mtime_array.append(OpenMaya.MTime(values['time'][index], OpenMaya.MTime.uiUnit()))
            mdouble_array.append(values['value'][index])
        mfn_anim_curve.addKeys(mtime_array, mdouble_array, 0, 0, 1)
        for index in range(mtime_array.length()):
            mfn_anim_curve.setTangent(index, values['in_tangent'][index][0], values['in_tangent'][index][1], True)
            mfn_anim_curve.setTangent(index, values['out_tangent'][index][0], values['out_tangent'][index][1], False)
            intangent_mangle = OpenMaya.MAngle(values['in_tangent_angle_weight'][index][0])        
            outtangent_mangle = OpenMaya.MAngle(values['out_tangent_angle_weight'][index][0])   
            mfn_anim_curve.setTangent(index, intangent_mangle, values['in_tangent_angle_weight'][index][1], True)
            mfn_anim_curve.setTangent(index, outtangent_mangle, values['out_tangent_angle_weight'][index][1], False)
            mfn_anim_curve.setInTangentType(index, values['in_tangent_type'][index])
            mfn_anim_curve.setOutTangentType(index, values['out_tangent_type'][index])               
            mfn_anim_curve.setIsBreakdown(index, values['breakdown'][index])

    def create_kalembic(self, node, frame_range=[1001, 1001], attributes=None, output_path=None):
        self.set_bounding_box()
        if not frame_range:
            frame_range = self.get_frame_range()
        if not attributes:
            attributes = resource.getPipeIDData()
        attributes = ' -attr ' + ' -attr '.join(attributes.keys())
        if not output_path:
            output_path = os.path.join(tempfile.gettempdir(),'temp_%s.abc' % common.get_dynamic_name())
        format = 'ogawa'
        output_path = '%s.abc' % (os.path.splitext(output_path)[0])
        mel_command = 'AbcExport -j \"-frameRange %s %s %s -uvWrite -dataFormat %s -root %s -file %s";' % (
            frame_range[0], frame_range[1],
            attributes,
            format,
            node,
            output_path
            )
        # example AbcExport -j "-frameRange 1 120 -attr spipe -attr scaption -uvWrite -dataFormat ogawa -root |pCube1 -file /venture/box.abc";
        OpenMaya.MGlobal.executeCommand(mel_command, False, True)
        return output_path
    

    
