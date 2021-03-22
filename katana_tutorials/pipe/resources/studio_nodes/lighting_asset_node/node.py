import os
import json
import resources

from core import versions
from core import nodegraph

from PyQt4 import QtGui
from Katana import NodegraphAPI

from resources import studio_nodes


def create_node():
    '''
    :description to create lighting asset node
    :param None
    :example
        from resources.studio_nodes.lighting_asset_node import node
        node.create_node()  
    '''       
    parent = NodegraphAPI.GetRootNode()
    knode = NodegraphAPI.CreateNode('Group', parent=parent)
    knode.setName(studio_nodes.LIGHTING_ASSET_NODE_TYPE)
    knode.addOutputPort('out')  
    add_parameters(knode)    
    NodegraphAPI.SetNodeViewed(knode, True, exclusive=True)
    NodegraphAPI.SetNodeEdited(knode, True, exclusive=True)
    

def add_parameters(knode):
    '''
    :description to create parameters on custom group node
    :param knode <NodegraphAPI node object>
    '''
    parameter = knode.getParameters()
    node_category_parameter = parameter.createChildString(
        studio_nodes.STUDIO_NODE_KEY, studio_nodes.LIGHTING_ASSET_NODE_TYPE)
    hint = {'readOnly': 'True'}
    node_category_parameter.setHintString(str(hint)) 
    show_path = resources.get_show_path()    
    show_path_parameter = parameter.createChildString('show_path', show_path)
    hint = {'widget': 'fileInput'}
    show_path_parameter.setHintString(str(hint))    
    sequence = parameter.createChildString('sequence', '')
    shot = parameter.createChildString('shot', '')
    create_button = parameter.createChildString('create_or_update', 'create_or_update')
    update_create_button(create_button)
    frame_range = parameter.createChildNumberArray('frame_ranage', 2)
    frame_range.getChild('i0').setValue('1001', 1.0)
    frame_range.getChild('i1').setValue('1025', 1.0)   
    hint = {'readOnly': 'True'}
    frame_range.setHintString(str(hint))      
    camera_group = parameter.createChildGroup('camera')
    character_group = parameter.createChildGroup('character')
    prop_group = parameter.createChildGroup('prop')
    set_group = parameter.createChildGroup('set')

    
def update_create_button(parameter):
    '''
    :description to update create button parameter hint sting value plus button signal
    :param parameter <Parameter object>
    '''      
    commands = [
        'from resources.studio_nodes.lighting_asset_node import node',
        'reload(node)',
        'node.create_button_action(parameter)'
        ]    
    command = '\n'.join(commands)
    hint = {
        'widget': 'scriptButton',
        'buttonText': 'create_or_update',
        'scriptText': command
        }
    parameter.setHintString(str(hint)) 
    
    
def create_button_action(parameter):
    knode = parameter.getNode()
    inputs = get_inputs(knode)
    make_node_networks(knode, inputs)    
    

def get_inputs(knode):
    '''
    :description collect the input data from custom asset group
    :param knode <NodegraphAPI node object>
    '''      
    show_path = knode.getParameter('show_path').getValue(1.0)
    sequence = knode.getParameter('sequence').getValue(1.0)
    shot = knode.getParameter('shot').getValue(1.0)
    inputs = {
        'show_path': show_path,
        'sequence': sequence,
        'shot': shot
        }
    return inputs 


def make_node_networks(knode, inputs):
    '''
    :description to create the dependency nodes inside the custom asset group
    :param knode <NodegraphAPI node object>
    :param inputs <dict>
    '''
    flush_parameter(knode)
    flush_knode(knode)
    animation_inputs, message = get_animation_inputs(
        inputs['show_path'], inputs['sequence'], inputs['shot'], 'animation')
    if not animation_inputs:
        print '#warnings: %s' % message   
        QtGui.QMessageBox.warning(None, 'warning', message, QtGui.QMessageBox.Ok)
        return    
    ing, x, y = 50, 0, 100
    merge_node = create_merge_node([0, 0], knode, 'puppet')   
    for puppet, contents in animation_inputs['puppets'].items():        
        category_parameter = upadte_category_parameter(
            knode, animation_inputs['version'], contents)
        puppet_group = create_puppet_group(knode, contents, [x, y], ing)
        y += ing
        input_port = merge_node.addInputPort(contents['name'])
        input_port.connect(puppet_group.getOutputPort('out'))
    frame_range = animation_inputs['frame_range']
    knode.getParameter('frame_ranage.i0').setValue(frame_range[0], 1.0)
    knode.getParameter('frame_ranage.i1').setValue(frame_range[1], 1.0)
    nodegraph.set_frame_range(frame_range[0], frame_range[1])
        

def upadte_category_parameter(knode, typed_version, contents):
    '''
    :description update the category parameter with puppets  
    :param knode <NodegraphAPI node object>
    :param typed_version <str>
    :param contents <dict>
    '''     
    parameter = knode.getParameter(contents['category'])    
    category_parameter = parameter.createChildStringArray(contents['name'], 6)
    category_parameter.setTupleSize(2)
    hint = {'readOnly': 'True'}
    category_parameter.setHintString(str(hint))  
    data = [
        'model', contents['model'],
        'lookdev', contents['lookdev'],
        'animation', typed_version        
        ]    
    for index, each in enumerate(data):
        child_param = category_parameter.getChildByIndex(index)
        child_param.setValue(each.encode(), 1.0)
    update_button = parameter.createChildString('update', '')
    animation_commands = [
        'from resources.studio_nodes.lighting_asset_node import node',
        'reload(node)',
        'node.update_version_action(\'animation\', parameter, \'%s\', \'%s\')' % (
            contents['name'], contents['category'])
        ]
    lookdev_commands = [
        'from resources.studio_nodes.lighting_asset_node import node',
        'reload(node)',
        'node.update_version_action(\'lookdev\', parameter, \'%s\', \'%s\')' % (
            contents['name'], contents['category'])
        ]
    animation_command = '\n'.join(animation_commands)
    lookdev_command = '\n'.join(lookdev_commands)
    lookdev_text = 'update_lookdev'
    flat = 0
    if contents['category'] == 'camera':  
        lookdev_text = ''
        flat = 1
        lookdev_command = None  
    hint = {
        'widget': 'scriptToolbar',
        'buttonData': [
            {
                'text': 'update_animation',
                'flat': 0,
                'scriptText': animation_command
                },
            {
                'text': lookdev_text,
                'flat': flat,
                'scriptText': lookdev_command
                }
            ]
        }
    update_button.setHintString(str(hint))
    return category_parameter 
            
        
def create_merge_node(position, parent, name):
    '''
    :description to create merge node inside the custom asset group
    :param parent <NodegraphAPI node object>
    :param position <list>
    '''      
    merge_node = NodegraphAPI.CreateNode('Merge', parent=parent)   
    merge_node.setName('%s_merge' % name)    
    NodegraphAPI.SetNodePosition(merge_node, position) 
    out_port = merge_node.getOutputPort('out')
    if not parent.getOutputPort('out'):    
        parent.addOutputPort('out')   
    return_port = parent.getReturnPort('out')
    return_port.connect(out_port)
    return merge_node   


def create_puppet_group(knode, contents, position, ing):
    '''
    :description create asset groups and its dependency nodes 
    :param knode <NodegraphAPI node object>
    :param contents <dict>
    :param position <list>
    :param ing <int>
    '''    
    puppet_group = NodegraphAPI.CreateNode('Group', parent=knode)
    puppet_group.setName('%s_group' % contents['name'])
    NodegraphAPI.SetNodePosition(puppet_group, position)
    puppet_group.addOutputPort('out')
    merge_node = create_merge_node([0, 0], puppet_group, contents['name'])    
    input_port = merge_node.addInputPort('input')
    look_resolve, look_assign = None, None
    if contents['category'] != 'camera':    
        look_resolve = NodegraphAPI.CreateNode('LookFileResolve', parent=puppet_group)
        look_resolve.setName('%s_resolve' % contents['name'])
        look_resolve.getOutputPort('out').connect(input_port)
        look_assign = NodegraphAPI.CreateNode('LookFileAssign', parent=puppet_group) 
        look_assign.setName('%s_klf' % contents['name'])
        look_assign.getOutputPort('out').connect(look_resolve.getInputPort('A'))
        input_port = look_assign.getInputPort('input')
        klf_parameter = look_assign.getParameter('args.lookfile.asset')
        expression = get_expression('lookdev', contents['category'], contents['name'], 'i3')
        klf_parameter.getChild('value').setExpression(expression)  
        klf_parameter.getChild('enable').setValue(True, 1.0)
        cel_parameter = look_assign.getParameter('CEL')
        puppet_location = os.path.join(
            studio_nodes.SCENE_GRAPH_LOCATION, contents['category'], contents['name']) 
        cel_parameter.setValue(puppet_location.encode(), 1.0)              
    alembic_node = NodegraphAPI.CreateNode('Alembic_In', parent=puppet_group) 
    alembic_node.setName('%s_alembic' % contents['name'])
    alembic_node.getOutputPort('out').connect(input_port)
    scenegraph_location = os.path.join(
        studio_nodes.SCENE_GRAPH_LOCATION, contents['category'])
    name_parameter = alembic_node.getParameter('name')
    name_parameter.setValue(scenegraph_location.encode(), 1.0)    
    name_parameter.setUseNodeDefault(False)
    abc_parameter = alembic_node.getParameter('abcAsset')
    expression = get_expression('animation', contents['category'], contents['name'], 'i5')
    abc_parameter.setExpression(expression)
    abc_parameter.setUseNodeDefault(False)
    # set the position
    x, y = [0, 100]    
    for each in [look_resolve, look_assign, alembic_node]:
        if not each:
            continue
        NodegraphAPI.SetNodePosition(each, [x, y])
        y += ing
    return puppet_group
    

def get_animation_inputs(show_path, sequence, shot, typed):
    '''
    :description get the animation published scene description
    :param show_path <str>
    :param sequence <str>
    :param shot <str>
    :param typed <str>
    '''      
    animation_dirname = os.path.join(
        show_path,
        'scene',
        sequence,
        shot
        )
    if not os.path.isdir(animation_dirname):
        message = 'not found any valid %s publish' % typed 
        return None, message
    latest_version = versions.get_latest_version(animation_dirname, typed)
    if not latest_version:
        message = 'not found any %s publish versions' % typed
        return None, message
    # read scene description
    manifest_path = os.path.join(
        animation_dirname, typed, latest_version, 'manifest.json')
    if not os.path.isfile(manifest_path):
        message = 'not found any valid %s manifest (scene description)' % typed
        return None, message
    with (open(manifest_path, 'r')) as manifest:
        data = json.load(manifest)
        scene_data = data['data']
        return scene_data, None
 

def get_expression(typed, category, puppet, parameter):
    '''
    :description make the expression
    :param typed <str>
    :param category <str>
    :param puppet <str>
    :param parameter <katana parameter object>
    '''          
    if typed == 'animation':   
        expressions = [
            'self.getNode().getParent().getParent().getParameter(\'show_path\').getValue(1.0)',
            '\'scene\'',
            'self.getNode().getParent().getParent().getParameter(\'sequence\').getValue(1.0)',
            'self.getNode().getParent().getParent().getParameter(\'shot\').getValue(1.0)',
            '\'animation\'',
            'self.getNode().getParent().getParent().getParameter(\'%s.%s.%s\').getValue(1.0)' % (
                category, puppet, parameter),
            '\'%s.abc\'' % puppet
            ]
    if typed == 'lookdev':  
        expressions = [
            'self.getNode().getParent().getParent().getParameter(\'show_path\').getValue(1.0)',
            '\'asset\'',
            '\'%s\'' % category,
            '\'%s\'' % puppet,
            '\'lookdev\'',
            'self.getNode().getParent().getParent().getParameter(\'%s.%s.%s\').getValue(1.0)' % (
                category, puppet, parameter),
            '\'%s.klf\'' % puppet
            ]
    expression = ' + \'/\' + '.join(expressions)
    return expression   
    

def update_version_action(typed, parameter, puppet, category):
    column, publish_dirname = None, None
    inputs = get_inputs(parameter.getNode())
    if typed == 'animation':
        column = 'i5'
        publish_dirname = os.path.join(
            inputs['show_path'],
            'scene',
            inputs['sequence'],
            inputs['shot']
            )
        latest_version = versions.get_latest_version(publish_dirname, typed)
    elif typed == 'lookdev':
        column = 'i3'
        dependency_versions = versions.get_asset_dependency_versions(
            inputs['show_path'], category, puppet, 'lookdev', 'model')
        model_version = get_model_version(parameter, puppet)
        latest_version = 'None'
        if model_version in dependency_versions:
            lookdev_versions = dependency_versions[model_version]
            if lookdev_versions:
                latest_version = lookdev_versions[0]
    current_version, version_parameter = get_current_version(parameter, puppet, column)    
    if current_version == latest_version:
        message = 'not found any new versions\ncurrent version is the latest version'        
        QtGui.QMessageBox.information(None, 'information', message, QtGui.QMessageBox.Ok) 
        return
    message = 'Are you sure, want to update?\n%s to %s' % (current_version, latest_version)
    replay = QtGui.QMessageBox.question(
        None, 'question', message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    if replay == QtGui.QMessageBox.No:
        print  'abort the animation updates!...'
        return
    version_parameter.setValue(latest_version, 1.0)          


def get_current_version(parameter, puppet, column):
    '''
    :description get the current version
    :param parameter <katana parameter object>
    :param puppet <str>
    :param column <str>
    '''        
    parent_parameter = parameter.getParent()  # character.batman
    child_parameter = parent_parameter.getChild('%s.%s' % (puppet, column))
    current_version = child_parameter.getValue(1.0)    
    return current_version, child_parameter


def get_model_version(parameter, puppet):
    '''
    :description get the current model version
    :param parameter <katana parameter object>
    :param puppet <str>
    '''      
    parent_parameter = parameter.getParent()  # character.batman
    child_parameter = parent_parameter.getChild('%s.i1' % (puppet))
    model_version = child_parameter.getValue(1.0)    
    return model_version 


def flush_parameter(knode):
    '''
    :description remove all children under the category parameters
    :param knode <NodegraphAPI node object>
    '''      
    categories = ['camera', 'character', 'prop', 'set']
    for category in categories:
        parameter = knode.getParameter(category) 
        if not parameter:
            continue
        for child in parameter.getChildren():
            parameter.deleteChild(child)
    

def flush_knode(knode):
    '''
    :description remove all dependency of custom asset group
    :param parent <NodegraphAPI node object>
    '''       
    for child in knode.getChildren():
        child.delete()
                            
