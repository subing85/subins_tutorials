

def create():
    '''
    :example
        from resources.studio_nodes import generic_asset_node
        reload(generic_asset_node)
        generic_asset_node.create()    
    '''
    # from resources.studio_nodes.asset_node import node
    import node
    reload(node)
    node.create_node()
