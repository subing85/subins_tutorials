from pymel import core


def get_data():
    contents = core.ls()
    transforms = core.listTransforms()
    defaults = get_defaults()
    node_data = {}
    nodes = []
    for transform in transforms:
        shape = transform.getShape()
        if shape:
            shapes = [each.name() for each in transform.getShapes()]
            t_data = {transform.name(): shapes}
            node_data.setdefault(shape.type(), {})
            node_data[shape.type()].setdefault(
                transform.name(), {'shapes': shapes})
            nodes.extend(shapes)
        else:
            node_data.setdefault(transform.type(), []).append(transform.name())
        nodes.append(transform.name())
    for content in contents:
        if content.name() in defaults:
            continue
        if content.name() in nodes:
            continue
        node_data.setdefault(content.type(), []).append(content.name())

    for nodetype, node_contents in node_data.items():
        print '\nType: \t', nodetype
        if isinstance(node_contents, dict):
            for each, shape_nodes in node_contents.items():
                print '\tName:\t', each
                for shape_node in shape_nodes['shapes']:
                    print '\t\tshape:\t', shape_node
                print '\n'
        else:
            for each in node_contents:
                print '\tName:\t', each
    return node_data


def get_defaults():
    default = [each.name() for each in core.ls(dn=True)]
    default.extend([
        'persp',
        'perspShape',
        'top',
        'topShape',
        'front',
        'frontShape',
        'side',
        'sideShape',
        'lightLinker1',
        'layerManager',
        'defaultLayer',
        'renderLayerManager',
        'defaultRenderLayer',
        'uiConfigurationScriptNode',
        'sceneConfigurationScriptNode'
    ])
    return default

get_data()
