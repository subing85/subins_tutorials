

def create():
    '''
    :example
        from resources.studio_nodes import lookdev_template
        reload(lookdev_template)
        lookdev_template.create()    
    '''
    import node
    reload(node)
    node.create_node()