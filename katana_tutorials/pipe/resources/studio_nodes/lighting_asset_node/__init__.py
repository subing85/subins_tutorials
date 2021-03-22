

def create():
    '''
    :example
        from resources.studio_nodes import lighting_asset_node
        reload(lighting_asset_node)
        lighting_asset_node.create()    
    '''
    import node
    reload(node)
    node.create_node()