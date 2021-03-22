from Katana import NodegraphAPI

'''
:description NodegraphAPI - Package to create and connect generic nodes.
'''


def get_scene_nodes():
    '''
    :description get all nodes from the scene
    :example
        from core import nodegraph
        scene_nodes = nodegraph.get_scene_nodes()
        print scene_nodes    
    '''
    nodes = []
    knodes = NodegraphAPI.GetAllNodes(includeDeleted=False)
    for knode in knodes:
        nodes.append(knode.getName())
    return nodes


def get_scene_typed_nodes(node_type):
    '''
    :description get all the nodes with the specified type.
    :param node_type <str>
    :example
        from core import nodegraph
        scene_nodes = nodegraph.get_scene_typed_nodes('Alembic_In')
        print scene_nodes        
    '''
    knodes = NodegraphAPI.GetAllNodesByType(node_type, includeDeleted=False)
    nodes = []
    for knode in knodes:
        nodes.append(knode.getName())
    return nodes 


def get_scene_registered_nodes():
    '''
    :description get all registered node types
    :example
        from core import nodegraph
        nodegraph.get_scene_registered_nodes()
    '''
    node_types = NodegraphAPI.GetNodeTypes()
    node_types.sort()
    for node_type in node_types:
        print node_type    
    print 'total:', len(node_types)
    

def get_scene_selected_nodes():
    '''
    :description get all selected nodes from the scene
    :example
        from core import nodegraph
        nodegraph.get_scene_selected_nodes()
    '''
    knodes = NodegraphAPI.GetAllSelectedNodes()
    nodes = []
    for knode in knodes:
        nodes.append(knode.getName())
    return nodes


def get_katana_nodes(nodes):
    '''
    :description find the node in the scene with given name
    :param nodes <list>
    :example
        from core import nodegraph
        nodes = ['katana_camera', 'PrimitiveCreate', 'camera_abc', 'test_node']
        nodegraph.get_katana_nodes(nodes)    
    '''
    knodes = []
    for node in nodes:
        if isinstance(node, str) or isinstance(node, unicode):
            knode = NodegraphAPI.GetNode(node)
        else:
            knode = node
        if knode:
            knodes.append(knode)
    return knodes


def get_scene_katana_nodes():
    '''
    :description get all node under the root node
    :example
        from core import nodegraph
        nodegraph.get_scene_katana_nodes()
    '''
    root_node = NodegraphAPI.GetRootNode()
    children = root_node.getChildren()
    return children


def set_frame_range(start_frame, end_frame):
    '''
    :description set the frame range (in and out time) of the current scene
    :param start_frame <int>
    :param end_frame <int>
    :example
        from core import nodegraph
        nodegraph.set_frame_range(1001, 1051)
    ''' 
    NodegraphAPI.SetInTime(start_frame, final=True)
    NodegraphAPI.SetOutTime(end_frame, final=True)
    NodegraphAPI.SetCurrentTime(start_frame, final=True)
    

def get_parameter_values(knode):
    '''
    :description travel node parameters and get the all values
    :param knode <Nodegraph Node Object>
    :example
        from core import nodegraph
        knodes = NodegraphAPI.GetAllSelectedNodes()
        nodegraph.get_parameter_values(knodes[0])
    ''' 
    parameters = knode.getParameters()
    children = parameters.getChildren()
    contents = {}
    stack = children
    while stack:
        parameter = stack.pop()
        if not parameter.getChildren():
            full_name = parameter.getFullName().split('.')[1:]
            full_name = '.'.join(full_name)            
            parameter_type = parameter.getType() 
            #===================================================================
            # if 'Array' in parameter_type:
            #     continue
            #===================================================================
            try:    
                parameter_value = parameter.getValue(1.0)
            except Exception:
                print parameter.getName()
                parameter_value = None
            content = {
                'value': parameter_value,
                'type': parameter_type
                }
            contents.setdefault(full_name, content)
            continue
        stack.extend(parameter.getChildren())
    return contents


def set_attributes(knode, **kwargs):
    '''
    :description set (update) the k node attribute values
    :param knode <Nodegraph Node Object>
    :example
        from core import nodegraph
        knodes = NodegraphAPI.GetAllSelectedNodes()
        nodegraph.set_attributes(knodes[0])
    '''     
    attributes = knode.getAttributes()
    for k, v in kwargs.items():
        attributes[k] = v
    knode.setAttributes(attributes)


def set_knode_enable(knodes=None):
    '''
    :description set the k node enable(bypassed false)
    :param knode <list>
    :example
        from core import nodegraph
        nodegraph.set_knode_enable()
    '''      
    if not knodes:
        knodes = NodegraphAPI.GetAllSelectedNodes()
    for knode in knodes:
        knode.setBypassed(False)


def set_knode_disable(knodes=None):
    '''
    :description set the k node disable(bypassed true)
    :param knode <list>
    :example
        from core import nodegraph
        nodegraph.set_knode_disable()
    '''      
    if not knodes:
        knodes = NodegraphAPI.GetAllSelectedNodes()
    for knode in knodes:
        knode.setBypassed(True)


def set_knode_locked(knodes=None):
    '''
    :description set the k node locked
    :param knodes <list>
    :example
        from core import nodegraph
        nodegraph.set_knode_locked()
    '''      
    if not knodes:
        knodes = NodegraphAPI.GetAllSelectedNodes()
    for knode in knodes:
        knode.setLocked(True)
        

def set_knode_unlocked(knodes=None):
    '''
    :description set the k node locked
    :param knodes <list>
    :example
        from core import nodegraph
        nodegraph.set_knode_locked()
    '''      
    if not knodes:
        knodes = NodegraphAPI.GetAllSelectedNodes()
    for knode in knodes:
        knode.setLocked(False)        


def get_studio_nodes(key, value=None):
    # group_nodes = NodegraphAPI.GetAllNodesByType('Group', includeDeleted=False)
    k_nodes = NodegraphAPI.GetAllNodes(includeDeleted=False) 
    studio_nodes = {}
    for k_node in k_nodes:
        parameter = k_node.getParameter(key)
        if not parameter:
            continue        
        node_value = parameter.getValue(1.0)
        if value:
            if parameter.getValue(1.0) != value:
                continue
            studio_nodes.setdefault(k_node, node_value)
        else:
            studio_nodes.setdefault(k_node, node_value)
    return studio_nodes

