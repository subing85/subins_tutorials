

def create():
    '''
    :example
        from resources.studio_nodes import lookdev_asset_node
        reload(lookdev_asset_node)
        lookdev_asset_node.create()    
    '''
    # from resources.studio_nodes.generic_asset_node import node
    import node
    reload(node)
    node.create_node()