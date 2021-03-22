import os
import resources

from PyQt4 import QtGui
from Katana import NodegraphAPI

from resources import studio_nodes


def create_node():
    '''
    :description to create generic asset node
    :param None
    :example
        from resources.studio_nodes.generic_asset_node import node
        node.create_node()  
    '''       
    parent = NodegraphAPI.GetRootNode()
    knode = NodegraphAPI.CreateNode('Group', parent=parent)
    knode.setName(studio_nodes.GENERIC_ASSET_NODE_TYPE)    
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
        studio_nodes.STUDIO_NODE_KEY, studio_nodes.GENERIC_ASSET_NODE_TYPE)
    hint = {'readOnly': 'True'}
    node_category_parameter.setHintString(str(hint))    
    show_path = resources.get_show_path()    
    show_path_parameter = parameter.createChildString('show_path', show_path)
    hint = {'widget': 'fileInput'}
    show_path_parameter.setHintString(str(hint))
    add_parameter = parameter.createChildString('add', 'add')
    # add bitton hint string button signal
    update_add_button(add_parameter)       
    assets_parameter = parameter.createChildGroup('assets')
    update_parameter = parameter.createChildString('create_or_update', 'create_or_update')
    # create bitton hint string button signal
    update_create_button(update_parameter)
    

def update_add_button(parameter):
    '''
    :description to update add button parameter hint sting value plus button signal
    :param parameter <Parameter object>
    '''      
    commands = [
        'from resources.studio_nodes.generic_asset_node import node',
        'node.add_button_action(parameter)'
        ]    
    command = '\n'.join(commands)
    hint = {
        'widget': 'scriptButton',
        'buttonText': 'add',
        'scriptText': command
        }
    parameter.setHintString(str(hint))   


def add_button_action(parameter):  # not change the function name
    '''
    :description to create dynamic parameters from add button signal
    :param parameter <Parameter object>
    '''    
    knode = parameter.getNode()
    assets_parameter = knode.getParameter('assets')  
    asset_parameter = assets_parameter.createChildGroup('asset1')
    name_parameter = asset_parameter.createChildString('name', '')
    category_parameter = asset_parameter.createChildString('category', '')
    hint = {
        'widget': 'popup',
        'options': studio_nodes.CATEGORIES
        }
    category_parameter.setHintString(str(hint))
    category_parameter.setValue(studio_nodes.CATEGORIES[0], 1.0)
    version_parameter = asset_parameter.createChildString('version', '0.0.0')
    remove_parameter = asset_parameter.createChildString('remove', 'remove')
    # remove bitton hint string button signal
    update_remove_button(remove_parameter)
    

def update_remove_button(parameter): 
    '''
    :description to update the remove button, parameter hint sting value plus button signal
    :param parameter <Parameter object>
    '''      
    commands = [
        'from resources.studio_nodes.generic_asset_node import node',
        'node.remove_button_action(parameter)'
        ]    
    command = '\n'.join(commands)
    hint = {
        'widget': 'scriptButton',
        'buttonText': 'remove',
        'scriptText': command
        }
    parameter.setHintString(str(hint))   
    
    
def remove_button_action(parameter):  # not change the function name
    '''
    :description to remove current parameter group from remove button signal
    :param parameter <Parameter object>
    '''     
    knode = parameter.getNode()
    assets_parameter = knode.getParameter('assets')
    parent_parameter = parameter.getParent()    
    assets_parameter.deleteChild(parent_parameter)
    

def update_create_button(parameter):
    '''
    :description to update create button parameter hint sting value plus button signal
    :param parameter <Parameter object>
    '''      
    commands = [
        'from resources.studio_nodes.generic_asset_node import node',
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
    '''
    :description to create asset node networks from create_or_update button signal
    :param parameter <Parameter object>
    '''    
    knode = parameter.getNode()
    inputs = get_inputs(knode)
    make_node_networks(knode, inputs)
    

def get_inputs(knode):
    '''
    :description collect the input data from custom asset group
    :param knode <NodegraphAPI node object>
    '''      
    assets_parameter = knode.getParameter('assets')
    inputs = {}
    for child in assets_parameter.getChildren():
        name = child.getChild('name')
        category = child.getChild('category')
        version = child.getChild('version')
        contents = {
            'name': name.getValue(1.0),
            'category': category.getValue(1.0),
            'version': version.getValue(1.0)
            }
        inputs.setdefault(child.getName(), contents)
    return inputs


def make_node_networks(knode, inputs):
    '''
    :description to create the dependency nodes inside the custom asset group
    :param knode <NodegraphAPI node object>
    :param inputs <dict>
    '''    
    flush_knode(knode)
    ing, x, y = -50, 0, 0    
    position = [0, (len(inputs) * ing) + -50]
    merge_node = create_merge_node(position, knode)
    assets = sorted(inputs.keys())
    for asset in assets:
        position = [x, y]
        alembic_node = create_alembic_node(inputs[asset], position, asset, knode)
        y += ing
        input_port = merge_node.addInputPort(inputs[asset]['name'])
        input_port.connect(alembic_node.getOutputPort('out'))
        

def create_merge_node(position, parent):
    '''
    :description to create merge node inside the custom asset group
    :param parent <NodegraphAPI node object>
    :param position <list>
    '''      
    merge_node = NodegraphAPI.CreateNode('Merge', parent=parent)   
    merge_node.setName('assets_merge')    
    NodegraphAPI.SetNodePosition(merge_node, position) 
    out_port = merge_node.getOutputPort('out')
    if not parent.getOutputPort('out'):    
        parent.addOutputPort('out')   
    return_port = parent.getReturnPort('out')
    return_port.connect(out_port)
    return merge_node       


def create_alembic_node(contents, position, current_asset, parent):
    '''
    :description to create the alembic node inside the custom asset group
    :param contents <dict>
    :param position <list>
    :param current_asset <str>
    :param parent <NodegraphAPI node object>
    '''        
    alembic_node = NodegraphAPI.CreateNode('Alembic_In', parent=parent)    
    alembic_node.setName('%s_abc' % contents['name'])    
    NodegraphAPI.SetNodePosition(alembic_node, position)
    scenegraph_location = os.path.join(
        studio_nodes.SCENE_GRAPH_LOCATION, contents['category'])
    location_parameter = alembic_node.getParameter('name')
    location_parameter.setValue(scenegraph_location, 1.0)
    location_parameter.setUseNodeDefault(False)
    abc_parameter = alembic_node.getParameter('abcAsset')
    expression = get_expression(current_asset)
    abc_parameter.setExpression(expression)
    abc_parameter.setUseNodeDefault(False)
    source_path = abc_parameter.getValue(1.0)
    if not os.path.isfile(source_path):
        version = os.path.basename(os.path.split(source_path)[0])
        message = 'not found %s version %s %s\n' % (contents['name'], version, source_path)
        QtGui.QMessageBox.warning(None, 'warning', message, QtGui.QMessageBox.Ok)
            
    return alembic_node


def get_expression(paremeter):
    '''
    :description to make alembic source expresion string
    '''     
    expressions = [
        'self.getNode().getParent().getParameter(\'show_path\').getValue(1.0)',
        '\'asset\'',
        'self.getNode().getParent().getParameter(\'assets.%s.category\').getValue(1.0)' % paremeter,
        'self.getNode().getParent().getParameter(\'assets.%s.name\').getValue(1.0)' % paremeter,
        '\'model\'',
        'self.getNode().getParent().getParameter(\'assets.%s.version\').getValue(1.0)' % paremeter,
        'self.getNode().getParent().getParameter(\'assets.%s.name\').getValue(1.0) + \'.abc\'' % paremeter
        ]
    expression = ' + \'/\' + '.join(expressions)
    return expression

      
def flush_knode(knode):
    '''
    :description remove all dependency of custom asset group
    :param parent <NodegraphAPI node object>
    '''       
    for child in knode.getChildren():
        child.delete()
        
