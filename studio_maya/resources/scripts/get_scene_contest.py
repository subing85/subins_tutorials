'''
get_scene_contest.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to find the maya objects details from the scenes.
'''

import json

from pymel import core


def get_data():
    contents = core.ls()
    transforms = core.listTransforms()
    defaults = get_defaults()
    node_data = {}
    nodes = []
    nodes_shapes = []
    for transform in transforms:
        if transform.type() != 'transform':
            continue
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
        if shape:
            nodes_shapes.append(shape.type())
    for content in contents:
        if content.name() in defaults:
            continue
        if content.name() in nodes:
            continue
        if content.type() in nodes_shapes:
            continue
        node_data.setdefault(content.type(), []).append(content.name())
    for nodetype, node_contents in node_data.items():
        print '\nType : ', nodetype
        if isinstance(node_contents, dict):
            for each, shape_nodes in node_contents.items():
                print 'Name : ', each
                for shape_node in shape_nodes['shapes']:
                    print 'shape : ', shape_node
                print '\n'
        else:
            for each in node_contents:
                print 'Name : ', each
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


data = get_data()
print "\nhttp://www.subins-toolkits.com", '\n', '-'*41
print json.dumps(data, indent=4)
