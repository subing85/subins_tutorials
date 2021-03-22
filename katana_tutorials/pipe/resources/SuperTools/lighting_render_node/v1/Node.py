# Node.py - the node itself and the public scripting API, 
# which you can test if you get a reference to the node in the Python tab.
import os
import inputs
import resources

from core import scene

from Katana import NodegraphAPI


class LightingRenderNode(NodegraphAPI.SuperTool):
    
    def __init__(self):
        self.hideNodegraphGroupControls()        
        print '\nlighting render studio super tool'
        print self.getName()       
        print self.getType()        
        self.pipe_parameter = 'studio_pipe'       
        self.addInputPort('input')
        self.addOutputPort('output')
        self.add_parameters()
        self.set_parent()        
        
    def add_parameters(self):       
        attributes = inputs.get_attributes() 
        hints = inputs.get_hints()  
        parameter = self.getParameters()  
        pipe_parameter_group = parameter.createChildGroup(self.pipe_parameter)
        for attribute in attributes:            
            if 'type' not in hints[attribute]:            
                child_parameter = pipe_parameter_group.createChildString(attribute, '')  
            else:
                if hints[attribute]['type'] == 'NumberArray':
                    child_parameter = pipe_parameter_group.createChildNumberArray(attribute, 2)
                    child_parameter.getChild('i0').setValue('1001', 1.0)
                    child_parameter.getChild('i1').setValue('1025', 1.0)
                if hints[attribute]['type'] == 'Group':         
                    child_parameter = pipe_parameter_group.createChildGroup(attribute)
            if attribute not in hints:
                continue
            current_hint = hints[attribute]
            child_parameter.setHintString(str(current_hint))   
        pipe_parameter_group.getChild('asset_node').setValue('None', 1.0)        
        pipe_parameter_group.getChild('render_mode').setValue(inputs.RENDER_MODES[0], 1.0)
        pipe_parameter_group.getChild('current_frame').setValue('Yes', 1.0)        
        pipe_parameter_group.getChild('color_space').setValue(inputs.COLOR_SPACE[0], 1.0)
        pipe_parameter_group.getChild('file_extension').setValue(inputs.FILE_EXTENSION[0], 1.0)            
            
    def set_parent(self):
        selected_nodes = NodegraphAPI.GetAllSelectedNodes()
        if not selected_nodes:
            return
        output_ports = selected_nodes[-1].getOutputPorts()
        outport = None
        inputport = None
        for output_port in output_ports:
            connected_port = output_port.getConnectedPorts()
            outport = output_port
            if not connected_port:
                continue
            inputport = connected_port[-1]
            break        
        if outport:
            outport.connect(self.getInputPort('input'))
        dx, dy = 0, 0
        if inputport:
            self.getOutputPort('output').connect(inputport)
            dx, dy = NodegraphAPI.GetNodePosition(inputport.getNode())
        ux, uy = NodegraphAPI.GetNodePosition(selected_nodes[-1])
        mx = (ux + dx) / 2
        my = (uy + dy) / 2        
        NodegraphAPI.SetNodePosition(self, [mx, my])            
                     
