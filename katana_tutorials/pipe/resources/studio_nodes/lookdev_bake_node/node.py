from Katana import NodegraphAPI

from resources import studio_nodes


def create_node():
    '''
    :description to create lookdev bake node
    :param None
    :example
        from resources.studio_nodes.lookdev_bake_node import node
        node.create_node()  
    '''       
    parent = NodegraphAPI.GetRootNode()
    knode = NodegraphAPI.CreateNode('LookFileBake', parent=parent)
    knode.setName(studio_nodes.LOOKDEV_BAKE_NODE_TYPE)    
    add_parameters(knode)    
    NodegraphAPI.SetNodeViewed(knode, True, exclusive=True)
    NodegraphAPI.SetNodeEdited(knode, True, exclusive=True)  
    

def add_parameters(knode):
    '''
    :description to create parameters on custom look file bake node
    :param knode <NodegraphAPI node object>
    '''    
    parameter = knode.getParameters()
    node_category_parameter = parameter.createChildString(
        studio_nodes.STUDIO_NODE_KEY, studio_nodes.LOOKDEV_BAKE_NODE_TYPE)
    hint = {'readOnly': 'True'}
    node_category_parameter.setHintString(str(hint))    
    attributes = [
        'show_path',
        'name',
        'category',
        'type',
        'version',
        'model',
        'lookdev'
        ]    
    for attribute in attributes:
        node_parameter = parameter.createChildString(
            attribute, '')
        hint = {'readOnly': 'True'}
        node_parameter.setHintString(str(hint))        
    
