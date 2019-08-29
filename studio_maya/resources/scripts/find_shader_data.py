'''
find_shader_data.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to find the shader details from the scenes.
'''


import os
import json
import tempfile
import webbrowser

from pymel import core


def unknown_types():
    node_types = [
        'lightLinker',
        'materialInfo',
        'nodeGraphEditorInfo',
        'partition',
        'groupId',
        'hyperShadePrimaryNodeEditorSavedTabsInfo',
        'renderPartition',
        'timeToUnitConversion'
    ]
    return node_types


def get_shader_nodes():
    default_shader = ['lambert1', 'particleCloud1']
    default_shader_list = core.ls(type='defaultShaderList')
    shaders = []
    for each in default_shader_list:
        nodes = core.listConnections(each, s=True, d=False)
        for node in nodes:
            if node.name() in default_shader:
                continue
            shaders.append(node)
    return shaders


def get_networks(shader):
    if not object:
        return
    nodes = shader.listHistory()
    unknown_nodes = unknown_types()
    default_nodes = core.ls(dn=True)
    dependency_nodes = []
    for node in nodes:
        if node.type() in unknown_nodes:
            continue
        if node in default_nodes:
            continue
        if node in dependency_nodes:
            continue
        dependency_nodes.append(node)
    return dependency_nodes


def get_data():
    data = {}
    shaders = get_shader_nodes()
    for x, shader in enumerate(shaders):
        dependency_nodes = get_networks(shader)
        colour = None
        if core.objExists('%s.color' % shader.name()):
            color_attr = shader.attr('color')
            colour = color_attr.get()
            if color_attr.listConnections(s=True, d=False):
                colour = 'already connected'
        shader_data = {
            'shader_name': shader.name().encode(),
            'node_type': shader.type().encode(),
            'color_value': colour,
            'dependency_nodes': {}
        }
        dependency_data = {}
        for index, node in enumerate(dependency_nodes):
            dependency_data = {
                'node_name': node.name().encode(),
                'node_type': node.type().encode()
            }
            if node.type() == 'file':
                source_image = node.getAttr('fileTextureName')
                dependency_data.update({'source_image': source_image.encode()})
            shader_data['dependency_nodes'].setdefault(
                index + 1, dependency_data)
        data.setdefault(x + 1, shader_data)
    return data


def validateo(output_path=None, write=False):
    if not output_path:
        output_path = os.path.join(
            tempfile.gettempdir(), 'studio_maya_shader_data.txt')
    if os.path.isfile(output_path):
        try:
            os.chmod(output_path, 0777)
        except:
            pass
        try:
            os.remove(output_path)
        except Exception as error:
            print str(error)
    data = get_data()
    if write:
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(data, indent=4))
    return data, output_path


data, path = validateo(write=True)
print "\nhttp://www.subins-toolkits.com", '\n', '-'*41
print json.dumps(data, indent=4)
try:
    webbrowser.open(path)
except Exception as error:
    print str(error)
