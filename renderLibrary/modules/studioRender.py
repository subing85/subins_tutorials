import json

from maya import OpenMaya
from maya import OpenMayaRender


class Render(object):
    
    def __init__(self):
        self.render_Layer = OpenMayaRender.MFnRenderLayer()
        
   
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
            
    def get_current_layer(self):       
        current_layer = self.render_Layer.currentLayer()        
        return current_layer
    
    def get_layers(self):
        mobject_array = OpenMaya.MObjectArray()
        self.render_Layer.listAllRenderLayers(mobject_array)
        return mobject_array
    
    def get_default_layer(self):
        return self.render_Layer.defaultRenderLayer()
    
    def get_members(self):
        layer = self.get_current_layer()
        self.render_Layer.setObject(layer)
        mobject_array = OpenMaya.MObjectArray()        
        self.render_Layer.listMembers(mobject_array)
        return layer, mobject_array

    def get_knodes(self, mobjects):
        if isinstance(mobjects, OpenMaya.MObjectArray):
            mobjects = [mobjects[x] for x in range(mobjects.length())]
        stack = mobjects        
        parent = None
        knodes = {}
        while stack:    
            current_node = stack.pop()
            mfn_dagnode = OpenMaya.MFnDagNode(current_node)  
            if not  mfn_dagnode.childCount():
                knodes.setdefault(mfn_dagnode.typeName(), []).append(parent.name())
            for x in range(mfn_dagnode.childCount()):        
                child = mfn_dagnode.child(x) 
                parent = mfn_dagnode       
                stack.append(child)
        return knodes    
            
    def get_render_utils(self, layer, mobjects):        
        knodes = self.get_knodes(mobjects)        
        knode_typed = self.valid_knode_typed()
        render_utils = {'common': {}}
        
        override_parameters = self.get_layer_adjustment(layer)
        
        
        #print json.dumps(override_parameters, indent=4)
        #print json.dumps(knodes, indent=4)
        
        
        for typed, nodes in knodes.items():
            knodes = {}        
            for node in nodes:
                data = {
                    'type': typed,
                    'values': {}
                    }
                self.get_override_parameters(node, override_parameters)
                knodes.setdefault(node, data)
                
            if typed in knode_typed:                
                if knode_typed[typed] not in render_utils:
                    render_utils.setdefault(knode_typed[typed], {})                    
                render_utils[knode_typed[typed]].update(knodes)
            else:
                render_utils['common'].update(knodes)
                
        return render_utils
    
    
    def get_override_parameters(self, current_node, override_parameters):
        parameters = {}
        dagpath = self.get_dagpath(current_node)
        parent = dagpath.partialPathName()
        dagpath.extendToShape()
        child = dagpath.partialPathName()
        
        knodes = [parent, child]
        
        parameters = {
            'parent': {},
            'child': {}
            }
        
        for knode in knodes:
            for each in override_parameters:
                node, attribute = each.split('.')
                if knode!=node:
                    continue
                #print each
                value, typed = self.get_attribute_values(node, attribute)
                #print '\t', each, value, typed
                
                parameters[knode].setdefault(attribute, {})
                
        print json.dumps(parameters, indent=4)        
   
                
                
    def get_attribute_values(self, node, attribute):

        mcommand_result = OpenMaya.MCommandResult()               
        mel_command = 'getAttr "%s.%s"'%(node, attribute)
        
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        result_type = mcommand_result.resultType()
        value, typed = None, None
          
        
        if result_type==mcommand_result.kInvalid:
            value, typed = None, None
                  
        if result_type==mcommand_result.kInt:
            util = OpenMaya.MScriptUtil()  
            util.createFromInt(0)
            id_pointer = util.asIntPtr()
            mcommand_result.getResult(id_pointer)
            value = OpenMaya.MScriptUtil(id_pointer).asInt()
            typed = 'kInt'
            
        if result_type==mcommand_result.kInt64:
            util = OpenMaya.MScriptUtil()  
            util.createFromInt(0)
            id_pointer = util.asIntPtr()
            mcommand_result.getResult(id_pointer)
            value = OpenMaya.MScriptUtil(id_pointer).asInt()
            typed = 'kInt'
                            
        if result_type==mcommand_result.kIntArray:
            value = OpenMaya.MIntArray()
            mcommand_result.getResult(value)
            typed = 'kIntArray'            
            
        if result_type==mcommand_result.kInt64Array:
            value = OpenMaya.MIntArray()
            mcommand_result.getResult(value)
            typed = 'kIntArray'           
        
        if result_type==mcommand_result.kDouble:
            util = OpenMaya.MScriptUtil()  
            util.createFromDouble(0)
            id_pointer = util.asDoublePtr()
            mcommand_result.getResult(id_pointer)
            value = OpenMaya.MScriptUtil(id_pointer).asFloat()  
            typed = 'kDouble'   
        
        if result_type==mcommand_result.kDoubleArray:
            value = OpenMaya.MDoubleArray()
            mcommand_result.getResult(value)
            typed = 'kDoubleArray'   
                    
        if result_type==mcommand_result.kString:
            value = mcommand_result.stringResult()
            typed = 'kString'   
            
        if result_type==mcommand_result.kStringArray:
            value, typed = None, 'kStringArray'
            
        if result_type==mcommand_result.kVector:
            value = OpenMaya.MVector()
            mcommand_result.getResult(value)     
            typed = 'kVector'   
                    
        if result_type==mcommand_result.kVectorArray:
            value = OpenMaya.MVectorArray()
            mcommand_result.getResult(value)
            typed = 'kVectorArray'   
                                
        if result_type==mcommand_result.kMatrix:
            value = OpenMaya.MMatrix()
            mcommand_result.getResult(value)       
            typed = 'kMatrix'   
            
        if result_type==mcommand_result.kMatrixArray:
            value = OpenMaya.MMatrixArray()
            mcommand_result.getResult(value)       
            typed = 'kMatrixArray'   
    
        
        #===================================================================
        # print mcommand_result.kInvalid == 0
        # print mcommand_result.kInt == 1
        # print mcommand_result.kInt64 == 2
        # print mcommand_result.kIntArray == 3    
        # print mcommand_result.kInt64Array == 4
        # print mcommand_result.kDouble == 5
        # print mcommand_result.kDoubleArray == 6  
        # print mcommand_result.kString == 7
        # print mcommand_result.kStringArray == 8
        # print mcommand_result.kVector == 9
        # print mcommand_result.kVectorArray == 10      
        # print mcommand_result.kMatrix == 11
        # print mcommand_result.kMatrixArray == 12
        #===================================================================
    
        return value, typed
                
            
            
    def get_children(self, dagpath):       
        count = dagpath.childCount()
        children = []
        for x in range(count):    
            child = dagpath.child(x)    
            if not child.hasFn(OpenMaya.MFn.kTransform):
                continue
            children.append(child)
        return children
        


    
    
    

    
    
    
    
    
    def get_layer_adjustment(self, layer):
        if isinstance(layer, OpenMaya.MObject):                 
            self.render_Layer.setObject(layer)        
            layer = self.render_Layer.name()
        mcommand_result = OpenMaya.MCommandResult()                
        mel_command = 'editRenderLayerAdjustment -q -layer %s;'%layer
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        override_utils = []
        mcommand_result.getResult(override_utils)
        return override_utils    
                
                
                    
              
    def get_knode_types(self, typed):
        mcommand_result = OpenMaya.MCommandResult()
        mel_command = 'listNodeTypes \"%s\"'%typed
        OpenMaya.MGlobal.executeCommand(mel_command, mcommand_result, False, True)
        knode_types = []
        mcommand_result.getResult(knode_types)
        return knode_types
    


    
    def valid_knode_typed(self):        
        light_types = self.get_knode_types('light')
        camera_types = self.get_knode_types('camera')
        node_types = {}
        for each in light_types:
            node_types.setdefault(each, 'light')
        #for each in camera_types:
        #    node_types.setdefault(each, 'camera')
        for each in ['mesh', 'nurbsSurface']:
            node_types.setdefault(each, 'geometry')    
        return node_types          
            
        
        
        

    
    
    
    
