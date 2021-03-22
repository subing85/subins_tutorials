# ScriptActions.py - useful functions that are not part of the node API.
# Since this node is imported by both node and editor, it cannot contain any GUI code.

import os
import ast
import json
import shutil
import getpass
import resources

from PyQt4 import QtGui
from datetime import datetime

from core import scene
from core import render
from core import shader
from core import versions
from core import nodegraph
from core import scenegraph
from resources import studio_nodes

from Katana import NodegraphAPI


def reload_lookdev(knode):
    load_lookdev_asset_nodes(knode)


def load_lookdev(knode):
    load_asset_data(knode)


def version_lookdev(knode):
    set_lookdev_versions(knode)


def render_lookdev(knode):
    start_render(knode)


def publish_lookdev(knode):
    publish_lookdev_scene(knode)
    

def load_lookdev_asset_nodes(knode):
    asset_nodes = nodegraph.get_studio_nodes(
        studio_nodes.STUDIO_NODE_KEY,
        value=studio_nodes.LOOKDEV_ASSET_NODE_TYPE
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
    show_path = kasset_node.getParameter('show_path').getValue(1.0)
    category = kasset_node.getParameter('model_category').getValue(1.0)
    name = kasset_node.getParameter('model_name').getValue(1.0)
    location = os.path.join(
        studio_nodes.SCENE_GRAPH_LOCATION, category, name)
    producer = scenegraph.get_producer(kasset_node, location=location)
    if not producer:
        message = 'not found any asset categories'
        QtGui.QMessageBox.warning(
            None, 'warning', message, QtGui.QMessageBox.Ok)
        return   
    input_attributes = [
        'name',
        'category',
        'type',
        'version',
        'model',
        'lookdev'
        ]
    attributes = []
    for input_attribute in input_attributes:    
        attributes.append('geometry.arbitrary.%s.value' % input_attribute)
    attribute_values = scenegraph.get_attribute_values(producer, attributes)
    input_values = {}
    for k, v in attribute_values.items():
        current_attribute = k.rsplit('.', 2)[1]
        input_values.setdefault(current_attribute, v)       
    pipe_parameter.getChild('show_path').setValue(show_path, 1.0)    
    pipe_parameter.getChild('name').setValue(input_values['name'], 1.0)
    pipe_parameter.getChild('category').setValue(input_values['category'], 1.0)
    pipe_parameter.getChild('type').setValue('lookdev', 1.0)
    pipe_parameter.getChild('model').setValue(input_values['version'], 1.0)
    pipe_parameter.getChild('lookdev').setValue('None', 1.0)    
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
        show_path,
        'dumps',
        'render',
        'lookdev',
        input_values['name'],
        'render.exr'
        )
    pipe_parameter.getChild('render_location').setValue(render_path, 1.0) 
    

def set_lookdev_versions(knode):
    parameter = knode.getParameter('studio_pipe.version')
    hints = ast.literal_eval(parameter.getHintString())
    text = 'major'
    if hints['buttonText'] == 'major':
        text = 'minor'
    if hints['buttonText'] == 'minor':
        text = 'patch'
    hints['buttonText'] = text
    parameter.setHintString(str(hints))
    publish_path, typed = get_publish_path(knode)
    temp_version = versions.get_latest_version(publish_path, typed)    
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


def get_publish_path(knode):
    pipe_parameter = knode.getParameter('studio_pipe')    
    show_path = pipe_parameter.getChild('show_path').getValue(1.0)    
    name = pipe_parameter.getChild('name').getValue(1.0)
    category = pipe_parameter.getChild('category').getValue(1.0)
    typed = pipe_parameter.getChild('type').getValue(1.0)
    publish_path = os.path.join(
        show_path,
        'asset',
        category,
        name        
        )
    return publish_path, typed


def start_render(knode):
    pipe_parameter = knode.getParameter('studio_pipe')    
    render_mode = pipe_parameter.getChild('render_mode').getValue(1.0)
    frame_type = pipe_parameter.getChild('current_frame').getValue(1.0)    
    if frame_type == 'Yes':
        start_frame = int(NodegraphAPI.GetCurrentTime())
        end_frame = start_frame
    else:        
        start_frame = int(NodegraphAPI.GetInTime())
        end_frame = int(NodegraphAPI.GetOutTime())
    current_render_node = get_specfic_dependency_node(knode, 'Render')
    render.start_render(current_render_node, render_mode, [start_frame, end_frame])             
    

def get_specfic_dependency_node(knode, node_type):
    dependency_node = None
    for child in knode.getChildren():
        if child.getType() != node_type:
            continue
        dependency_node = child
        break
    return dependency_node


def publish_lookdev_scene(knode):
    '''
    # lookdev publish
        1. remapping source maps Done
        2. look file bake (klf) 
        3. katana scene
        4. xml scene
        5. publish information (scene description)
    '''
    bake_nodes = nodegraph.get_studio_nodes(
        studio_nodes.STUDIO_NODE_KEY,
        value=studio_nodes.LOOKDEV_BAKE_NODE_TYPE
        )
    message = None 
    if not bake_nodes:
        message = 'not fond any valid studio lookdev bake node'        
    if len(bake_nodes) > 1:        
        message = 'found more than one studio lookdev bake node'        
    if message:
        QtGui.QMessageBox.warning(None, 'Warning', message, QtGui.QMessageBox.Ok)
        return None
    input_data = get_input_data(knode)
    publish_dirname = os.path.join(
        input_data['show_path'],
        'asset',
        input_data['category'],
        input_data['name'],
        input_data['type'],
        input_data['version'],
        )
    if os.path.isdir(publish_dirname):
        shutil.rmtree(publish_dirname)
    bake_node = bake_nodes.keys()[0]
    updata_lookdev_bake(bake_node, input_data) 
    scenegraph_location = os.path.join(
        studio_nodes.SCENE_GRAPH_LOCATION, input_data['category'], input_data['name'])
    texture_remapping(knode, scenegraph_location, publish_dirname)
    current_scene = os.path.join(publish_dirname, input_data['name'])
    look_file_path = '%s.klf' % current_scene 
    xml_scene = '%s.xml' % current_scene   
    katana_scene = '%s.katana' % current_scene 
    # manifest_path = '.manifest' % current_scene   
    manifest_path = os.path.join(publish_dirname, 'manifest.json')      
    knodes = nodegraph.get_scene_katana_nodes()    
    scene.look_file_bake(bake_node, look_file_path, 0, force=True)    
    scene.nodes_to_xml_file(knodes, xml_scene, force=True)    
    scene.export_katana_nodes(knodes, katana_scene, force=True)
    manifest_data = {
        'pipe': 'aseet',
        'data': input_data,
        'user': getpass.getuser(),
        'date': datetime.now().strftime('%Y/%B/%d - %I:%M:%S:%p')
        }
    with (open(manifest_path, 'w')) as manifest:
        manifest.write(json.dumps(manifest_data, indent=4))
    set_lookdev_versions(knode)
    messages = [
        '<lookdev publish success>',
        publish_dirname,
        'name: '.rjust(10) + input_data['name'],
        'category: '.rjust(10) + input_data['category'],
        'type: '.rjust(10) + input_data['type'],
        'version: '.rjust(10) + input_data['version']        
        ]
    message_box = QtGui.QMessageBox.information(
        None, 'Success', '\n'.join(messages), QtGui.QMessageBox.Ok)
    if message_box:
        print '\n'.join(messages)
        os.system('xdg-open \"%s\"' % publish_dirname)        
    

def texture_remapping(knode, location, directory):    
    producer = scenegraph.get_producer(knode, location=location)
    if not producer:
        message = 'not able to find scenegraph location\n%s' % location
        QtGui.QMessageBox.warning(None, 'Warning', message, QtGui.QMessageBox.Ok)
        return None 
    texture_maps = shader.get_material_assigned_texture_maps(producer)
    source_image_dirname = os.path.join(directory, 'source_images')
    if not os.path.isdir(source_image_dirname):
        os.makedirs(source_image_dirname)
    remapped_source_maps = set()
    for material in texture_maps:
        for texture_map, nodes in texture_maps[material].items():
            source_image_path = os.path.join(source_image_dirname, os.path.basename(texture_map))            
            print 'source\t', texture_map
            print 'target\t', source_image_path            
            if source_image_path not in remapped_source_maps:            
                shutil.copy2(texture_map, source_image_path)
            for node in nodes:
                ktexture_node = NodegraphAPI.GetNode(node)
                if not ktexture_node:
                    print '#warnings: not found node <%s>' % node
                    continue                     
                parameter = ktexture_node.getParameter('parameters.filename.value')
                if not parameter:
                    print '#warnings: not found parameter <%s> parameters.filename.value' % node
                    continue
                parameter.setValue(source_image_path, 1.0)
                remapped_source_maps.add(source_image_path)
    return list(remapped_source_maps)


def updata_lookdev_bake(bake_node, input_data):    
    for attribute, value in input_data.items():
        parameter = bake_node.getParameter(attribute)
        parameter.setValue(value, 1.0)
        

def get_input_data(knode):
    attributes = [
        'show_path',
        'name',
        'category',
        'type',
        'next_version',
        'model',
        'lookdev'
        ]
    pipe_parameter = knode.getParameter('studio_pipe')  
    input_data = {}  
    for attribute in attributes:
        parameter_value = pipe_parameter.getChild(attribute).getValue(1.0)
        if attribute == 'next_version':
            attribute = 'version'
        input_data.setdefault(attribute, parameter_value)
    return input_data
    
