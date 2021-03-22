

def create():
    '''
    :example
        from resources.studio_nodes import lookdev_bake_node
        reload(lookdev_bake_node)
        lookdev_bake_node.create()    
    '''
    import node
    reload(node)
    node.create_node()