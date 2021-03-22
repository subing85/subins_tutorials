

def create():
    '''
    :example
        from resources.studio_nodes import lighting_template
        reload(lighting_template)
        lighting_template.create()    
    '''
    import node
    reload(node)
    node.create_node()