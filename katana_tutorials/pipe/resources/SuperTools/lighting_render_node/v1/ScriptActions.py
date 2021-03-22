# ScriptActions.py - useful functions that are not part of the node API.
# Since this node is imported by both node and editor, it cannot contain any GUI code.
import os
import ast

import json
import shutil
import getpass

from PyQt4 import QtGui
from datetime import datetime

from core import scene
from core import render
from core import versions
from core import nodegraph
from core import scenegraph
from resources import studio_nodes

from Katana import NodegraphAPI


def reload_lighting(knode):
    load_lighting_asset_nodes(knode)


def load_lighting(knode):
    load_asset_data(knode)


def version_lighting(knode):
    set_lighting_versions(knode)


def render_lighting(knode):
    start_render(knode)


def publish_lighting(knode):
    publish_lighting_scene(knode)
    
    
def load_lighting_asset_nodes(knode):
    asset_nodes = nodegraph.get_studio_nodes(
        studio_nodes.STUDIO_NODE_KEY,
        value=studio_nodes.LIGHTING_ASSET_NODE_TYPE
        )
    parameter = knode.getParameter('studio_pipe.asset_node')
    if not asset_nodes:
        hints = ast.literal_eval(parameter.getHintString())
        hints['options'] = ['None']        
        parameter.setHintString(str(hints))
        parameter.setValue('None', 1.0)
        QtGui.QMessageBox.warning(
            None,
            'Warning',
            'Not fond any valid studio lookdev asset nodes',
            QtGui.QMessageBox.Ok
            )
        return              
    nodes = []    
    for asset_node in asset_nodes:
        nodes.append(asset_node.getName())
    hints = ast.literal_eval(parameter.getHintString())
    hints['options'] = nodes
    parameter.setHintString(str(hints))
    parameter.setValue(nodes[0], 1.0)
    print '#info: loaded lookdev asset nodes, success'
    

def load_asset_data(knode):      
    pipe_parameter = knode.getParameter('studio_pipe')
    asset_node = pipe_parameter.getChild('asset_node').getValue(1.0) 
    message = None
    if not asset_node:
        message = 'Not fond any valid lookdev asset nodes'
    kasset_node = NodegraphAPI.GetNode(asset_node)
    if not kasset_node:
        message = 'current node not valid'
    if message:
        QtGui.QMessageBox.warning(
            None, 'warning', message, QtGui.QMessageBox.Ok)
        return  
    inputs = get_asset_inputs(kasset_node)      
    pipe_parameter.getChild('show_path').setValue(inputs['show_path'], 1.0)    
    pipe_parameter.getChild('sequence').setValue(inputs['sequence'], 1.0)
    pipe_parameter.getChild('shot').setValue(inputs['shot'], 1.0)
    pipe_parameter.getChild('global_frame_range.i0').setValue(inputs['frame_range'][0], 1.0)
    pipe_parameter.getChild('global_frame_range.i1').setValue(inputs['frame_range'][1], 1.0)
    assets_parameter = pipe_parameter.getChild('assets')
    flush_parameter(knode)
    flush_knode(knode)
    for category in studio_nodes.CATEGORIES:
        if category not in inputs['assets']:
            continue
        for asset in inputs['assets'][category]:
            asset_parameter = assets_parameter.createChildNumberArray(asset, 2)   
            asset_parameter.getChild('i0').setValue(inputs['frame_range'][0], 1.0)  
            asset_parameter.getChild('i1').setValue(inputs['frame_range'][1], 1.0)                     
            #===================================================================
            # asset_parameter = assets_parameter.createChildString(asset, category)
            # hint = {'readOnly': 'True'}
            # asset_parameter.setHintString(str(hint))
            #===================================================================
    make_node_networks(knode, inputs['assets'])  
    camera_location = os.path.join(
        studio_nodes.SCENE_GRAPH_LOCATION, 'camera')
    camera_producer = scenegraph.get_producer(kasset_node, location=camera_location)
    camera_producers = scenegraph.list_specific_producer(camera_producer, 'camera')
    if not camera_producers:
        message = 'not found camera in the scene'
        QtGui.QMessageBox.warning(
            None, 'warning', message, QtGui.QMessageBox.Ok)
        return   
    pipe_parameter.getChild('render_camera').setValue(camera_producers[0].getFullName(), 1.0) 
    render_path = os.path.join(
        inputs['show_path'],
        'scene',
        inputs['sequence'],
        inputs['shot'],
        'render',
        )
    pipe_parameter.getChild('render_location').setValue(render_path, 1.0)    


def make_node_networks(knode, asset_inputs):
    input_dot = NodegraphAPI.CreateNode('Dot', parent=knode)
    output_dot = NodegraphAPI.CreateNode('Dot', parent=knode)
    ing, x, y = 300, 0, 0
    dot_x = ing * (len(asset_inputs)) / 2
    NodegraphAPI.SetNodePosition(input_dot, [dot_x, 0])
    NodegraphAPI.SetNodePosition(output_dot, [dot_x, -300])
    pipe_parameter = knode.getParameter('studio_pipe')
    for category in studio_nodes.CATEGORIES:
        if category not in asset_inputs:
            continue   
        for asset in asset_inputs[category]:
            output_define = create_output_define(knode)
            output_define.setName('%s_output_define' % asset)
            render_node = NodegraphAPI.CreateNode('Render', parent=knode)
            render_node.setName('%s_render' % asset)
            render_node.getParameter('passName').setValue('%s_render' % asset, 1.0)
            render_parameter = render_node.getParameters()
            render_asset_name = render_parameter.createChildString('asset_name', asset)  
            hint = {'readOnly': 'True'}
            render_asset_name.setHintString(str(hint)) 
            NodegraphAPI.SetNodePosition(output_define, [x, -100])
            NodegraphAPI.SetNodePosition(render_node, [x, -200])
            x += ing
            # dependency connections
            input_dot.getOutputPort('output').connect(output_define.getInputPort('input'))
            input_dot.getOutputPort('output').connect(output_dot.getInputPort('input'))
            output_define.getOutputPort('out').connect(render_node.getInputPort('input'))
            knode.getSendPort('input').connect(input_dot.getInputPort('input'))
            output_dot.getOutputPort('output').connect(knode.getReturnPort('output'))
            # set expressions
            attributes = {            
                'color_space': 'args.renderSettings.outputs.outputName.rendererSettings.colorSpace.value',
                'file_extension': 'args.renderSettings.outputs.outputName.rendererSettings.fileExtension.value',
                'render_camera': 'args.renderSettings.outputs.outputName.rendererSettings.cameraName.value',
                'render_location': 'args.renderSettings.outputs.outputName.locationSettings.renderLocation.value'
                }
            for driver, driven in attributes.items():
                if driver == 'render_location':
                    name = '/%s/%s.' % (asset, asset)                     
                    extension = 'self.getNode().getParent().getParameter(\'studio_pipe.file_extension\').getValue(1.0)' 
                    expression = 'self.getNode().getParent().getParameter(\'%s.%s\').getValue(1.0) + \'%s\' + %s' % (
                        'studio_pipe', driver, name, extension)
                else:
                    expression = 'self.getNode().getParent().getParameter(\'%s.%s\').getValue(1.0)' % (
                        'studio_pipe', driver)
                driven_parameter = output_define.getParameter(driven)
                driven_parameter.setExpression(expression)
                
    
def create_output_define(knode):
    xml_scene = os.path.join(os.path.dirname(__file__), 'output_define.xml') 
    output_define = scene.xml_file_to_nodes(xml_scene, parent=knode)
    return output_define[0]         

    
def get_asset_inputs(knode):
    show_path = knode.getParameter('show_path').getValue(1.0)
    sequence = knode.getParameter('sequence').getValue(1.0)
    shot = knode.getParameter('shot').getValue(1.0)
    start_frame = knode.getParameter('frame_ranage.i0').getValue(1.0)
    end_frame = knode.getParameter('frame_ranage.i1').getValue(1.0) 
    asset_data = {}    
    for category in studio_nodes.CATEGORIES:
        if category == 'camera':
            continue
        category_parameter = knode.getParameter(category)
        for child in category_parameter.getChildren():
            if child.getType() != 'stringArray':
                continue
            asset_data.setdefault(
                category_parameter.getName(), []).append(child.getName())
    inputs = {
        'show_path': show_path,
        'sequence': sequence,
        'shot': shot,
        'frame_range': [start_frame, end_frame],
        'assets': asset_data
        }
    return inputs


def set_lighting_versions(knode):
    parameter = knode.getParameter('studio_pipe.version')
    hints = ast.literal_eval(parameter.getHintString())
    text = 'major'
    if hints['buttonText'] == 'major':
        text = 'minor'
    if hints['buttonText'] == 'minor':
        text = 'patch'
    hints['buttonText'] = text
    parameter.setHintString(str(hints))
    publish_path = get_publish_path(knode)
    temp_version = versions.get_latest_version(publish_path, 'lighting')    
    latest_version = None
    if temp_version:
        latest_version = temp_version      
    index = versions.PATTERN[text]    
    next_version = versions.get_next_version(index, latest_version)
    pipe_parameter = knode.getParameter('studio_pipe')
    if not latest_version:
        latest_version = 'None'
    pipe_parameter.getChild('latest_version').setValue(latest_version, 1.0)    
    pipe_parameter.getChild('next_version').setValue(next_version, 1.0)
    render_path = os.path.join(
        publish_path,
        'render',
        next_version
        )
    pipe_parameter.getChild('render_location').setValue(render_path, 1.0)       


def get_publish_path(knode):
    pipe_parameter = knode.getParameter('studio_pipe')    
    show_path = pipe_parameter.getChild('show_path').getValue(1.0)    
    sequence = pipe_parameter.getChild('sequence').getValue(1.0)
    shot = pipe_parameter.getChild('shot').getValue(1.0)    
    publish_path = os.path.join(
        show_path,
        'scene',
        sequence,
        shot,
        )    
    return publish_path


def start_render(knode):
    render_input_data = get_render_input_data(knode)    
    for asset, frame_range in render_input_data['assets'].items():
        current_render_node = find_render_node(knode, asset)
        print '\n#info: render', asset, current_render_node.getName()
        render.start_render(current_render_node, render_input_data['render_mode'], frame_range)
        

def find_render_node(knode, asset):    
    render_node = None
    for child in knode.getChildren():
        if child.getType() != 'Render':
            continue
        # pass_name = child.getParameter('passName').getValue(1.0)
        # asset_name = pass_name.rsplit('_render', 1)[0]
        asset_name = child.getParameter('asset_name').getValue(1.0)
        if asset != asset_name:
            continue
        render_node = child
        break            
    return render_node
        
    
def get_render_input_data(knode):
    pipe_parameter = knode.getParameter('studio_pipe')  
    assets_parameter = pipe_parameter.getChild('assets')    
    render_mode = pipe_parameter.getChild('render_mode').getValue(1.0)
    frame_type = pipe_parameter.getChild('current_frame').getValue(1.0)    
    assets_data = {}   
    for assets_child in assets_parameter.getChildren():
        if frame_type == 'Yes':
            start_frame = int(NodegraphAPI.GetCurrentTime())
            end_frame = start_frame
        else:
            start_frame = assets_child.getChild('i0').getValue(1.0)
            end_frame = assets_child.getChild('i1').getValue(1.0)        
        assets_data.setdefault(assets_child.getName(), [start_frame, end_frame])  
    show_path = pipe_parameter.getChild('show_path').getValue(1.0)    
    sequence = pipe_parameter.getChild('sequence').getValue(1.0)
    shot = pipe_parameter.getChild('shot').getValue(1.0)
    global_start_frame = pipe_parameter.getChild('global_frame_range.i0').getValue(1.0)
    global_end_frame = pipe_parameter.getChild('global_frame_range.i1').getValue(1.0)
    next_version = pipe_parameter.getChild('next_version').getValue(1.0)
    render_input_data = {
        'assets': assets_data,
        'render_mode': render_mode,
        'frame_type': frame_type,
        'show_path': show_path,
        'type': 'lighting',
        'sequence': sequence,
        'shot': shot,
        'version': next_version,
        'frame_range': [
            global_start_frame,
            global_end_frame
            ]
        }
    return render_input_data


def get_asset_input_data(knode):
    asset_data = {}
    pipe_parameter = knode.getParameter('studio_pipe')
    asset_node = pipe_parameter.getChild('asset_node').getValue(1.0) 
    kasset_node = NodegraphAPI.GetNode(asset_node)
    if not kasset_node:
        return asset_data
    parameters = kasset_node.getParameters()
    for category in parameters.getChildren():
        if category.getName() not in studio_nodes.CATEGORIES:
            continue    
        for asset in category.getChildren():
            if asset.getType() != 'stringArray':
                continue        
            model = asset.getChild('i1').getValue(1.0)
            lookdev = asset.getChild('i3').getValue(1.0)
            animation = asset.getChild('i5').getValue(1.0)        
            data = {
                'model': model,
                'lookdev': lookdev,
                'animation': animation
                }
            asset_data.setdefault(asset.getName(), data)    
    return asset_data


def publish_lighting_scene(knode):
    '''
    # lookdev publish
        1. katana scene
        2. xml scene
        3. publish information (scene description)
    '''
    input_data = get_render_input_data(knode)    
    asset_input_data = get_asset_input_data(knode)
    input_data['asset_vesrions'] = asset_input_data
    publish_dirname = os.path.join(
        input_data['show_path'],
        'scene',
        input_data['sequence'],
        input_data['shot'],
        input_data['type'],
        input_data['version']
        )         
    if os.path.isdir(publish_dirname):
        shutil.rmtree(publish_dirname)  
    current_scene = os.path.join(publish_dirname, 'scene')
    xml_scene = '%s.xml' % current_scene   
    katana_scene = '%s.katana' % current_scene     
    knodes = nodegraph.get_scene_katana_nodes()    
    scene.nodes_to_xml_file(knodes, xml_scene, force=True)    
    scene.export_katana_nodes(knodes, katana_scene, force=True)
    manifest_path = os.path.join(publish_dirname, 'manifest.json')      
    manifest_data = {
        'pipe': 'scene',
        'data': input_data,
        'user': getpass.getuser(),
        'date': datetime.now().strftime('%Y/%B/%d - %I:%M:%S:%p')
        }
    with (open(manifest_path, 'w')) as manifest:
        manifest.write(json.dumps(manifest_data, indent=4))
    set_lighting_versions(knode)
    messages = [
        '<lookdev publish success>',
        publish_dirname,
        'sequence: '.rjust(10) + input_data['sequence'],
        'shot: '.rjust(10) + input_data['shot'],
        'type: '.rjust(10) + input_data['type'],
        'version: '.rjust(10) + input_data['version']        
        ]
    message_box = QtGui.QMessageBox.information(
        None, 'Success', '\n'.join(messages), QtGui.QMessageBox.Ok)
    if message_box:
        print '\n'.join(messages)
        os.system('xdg-open \"%s\"' % publish_dirname)                    

    
def flush_parameter(knode):
    '''
    :description remove all children under the assets parameter
    :param knode <NodegraphAPI node object>
    '''     
    parameter = knode.getParameter('studio_pipe.assets')
    for child in parameter.getChildren():
        parameter.deleteChild(child)    

    
def flush_knode(knode):
    '''
    :description remove all dependency of custom asset group
    :param parent <NodegraphAPI node object>
    '''       
    for child in knode.getChildren():
        child.delete()    
    
