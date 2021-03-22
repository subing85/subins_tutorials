# Node.py - the node itself and the public scripting API, 
# which you can test if you get a reference to the node in the Python tab.

import os
import inputs
import resources

from core import scene

from Katana import NodegraphAPI


class LookdevRenderNode(NodegraphAPI.SuperTool):
    
    def __init__(self):
        self.hideNodegraphGroupControls()        
        print '\nlookdev render studio super tool'
        print self.getName()       
        print self.getType()        
        self.pipe_parameter = 'studio_pipe'       
        self.addInputPort('input')
        self.addOutputPort('output')
        self.add_parameters()
        self.set_parent()        
        self.add_node_dependency()
    
    def add_parameters(self): 
        attributes = inputs.get_attributes() 
        hints = inputs.get_hints()  
        parameter = self.getParameters()  
        pipe_parameter_group = parameter.createChildGroup(self.pipe_parameter)
        for attribute in attributes:
            child_parameter = pipe_parameter_group.createChildString(attribute, '')  
            if attribute not in hints:
                continue
            current_hint = hints[attribute]
            child_parameter.setHintString(str(current_hint))            
        pipe_parameter_group.getChild('asset_node').setValue('None', 1.0)        
        pipe_parameter_group.getChild('category').setValue(inputs.CATEGORIES[0], 1.0)
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
        
    def create_output_define(self):
        xml_scene = os.path.join(os.path.dirname(__file__), 'output_define.xml') 
        output_define = scene.xml_file_to_nodes(xml_scene, parent=self)
        return output_define[0]       
    
    def add_node_dependency(self):
        input_dot = NodegraphAPI.CreateNode('Dot', parent=self)
        # output_define = NodegraphAPI.CreateNode('RenderOutputDefine', parent=self)
        output_define = self.create_output_define()
        render = NodegraphAPI.CreateNode('Render', parent=self)
        output_dot = NodegraphAPI.CreateNode('Dot', parent=self)
        NodegraphAPI.SetNodePosition(input_dot, [100, 0])
        NodegraphAPI.SetNodePosition(output_define, [0, -100])
        NodegraphAPI.SetNodePosition(render, [0, -200])
        NodegraphAPI.SetNodePosition(output_dot, [100, -300])
        # dependency connections
        input_dot.getOutputPort('output').connect(output_define.getInputPort('input'))
        input_dot.getOutputPort('output').connect(output_dot.getInputPort('input'))
        output_define.getOutputPort('out').connect(render.getInputPort('input'))
        self.getSendPort('input').connect(input_dot.getInputPort('input'))
        output_dot.getOutputPort('output').connect(self.getReturnPort('output'))
        # set expressions
        attributes = {            
            'color_space': 'args.renderSettings.outputs.outputName.rendererSettings.colorSpace.value',
            'file_extension': 'args.renderSettings.outputs.outputName.rendererSettings.fileExtension.value',
            'render_camera': 'args.renderSettings.outputs.outputName.rendererSettings.cameraName.value',
            'render_location': 'args.renderSettings.outputs.outputName.locationSettings.renderLocation.value'
            }
        for driver, driven in attributes.items():
            expression = 'self.getNode().getParent().getParameter(\'%s.%s\').getValue(1.0)' % (
                self.pipe_parameter, driver)
            driven_parameter = output_define.getParameter(driven)
            driven_parameter.setExpression(expression)
        
