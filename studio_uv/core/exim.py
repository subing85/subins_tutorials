'''
exim.py 0.0.1 
Date: June 24, 2019
Last modified: August 03, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    None
'''

import copy
import json

from pymel import core
from studio_uv.core import studioMaya


def execute(*args):
    '''
        :example 0 type, 1 repeat, 2 select, 3 directory, 4 query, 5 objects
    '''
    if args[0] == 'export' and args[3] and not args[4]:
        export_uv(args[2], args[3], args[5])
    if args[0] == 'import' and args[3] and not args[4]:
        import_uv(args[3], args[2], args[1], args[5])
    if args[4] and args[5] == 'True' and args[3]:
        nodes = get_influance_objects(args[3])
        return nodes


def export_uv(type, directory, objects):
    if type in ['selected', 'all']:
        polygons = get_polygons(type)
    elif objects:
        strips = objects.replace(' ', '')
        polygons = strips.split(',')
    else:
        core.displayWarning('wrong arguments or inputs!...')
        return
    if not polygons:
        core.displayWarning('wrong arguments %s!...' % objects)
        return
    studio_maya = studioMaya.Connect()
    uv_data_bundle = {}
    exported_polygons = []
    result = True
    for index, polygon in enumerate(polygons):
        exported_polygons.append(polygon)
        if not core.objExists(polygon):
            core.displayWarning(
                'not found the object called <%s>!...' % polygon)
            result = False
            continue
        studio_maya.node = polygon
        mdag_path = studio_maya.getDagPath()
        data = studio_maya.getData(mdag_path)
        uv_data_bundle.setdefault(index, data)
    studio_maya.write(directory, uv_data_bundle, result=False)
    print '\npolygons\n\t', '\n\t'.join(exported_polygons)
    print '// Result:',  directory
    if not result:
        core.displayWarning('export not completed!...')
        return
    core.displayInfo('export success!...')


def import_uv(directory, entity, repeat, objects):
    studio_maya = studioMaya.Connect()
    data = studio_maya.read(directory, result=False)
    if entity == 'matching':
        uv_data = find_from_scene(data)
    elif entity == 'selected':
        polygons = core.ls(sl=True)
        uv_data = find_from_scene(data, mode=True, polygons=polygons)
    elif entity == 'all':
        uv_data = find_from_data(data)
    elif objects:
        strips = objects.replace(' ', '')
        polygons = strips.split(',')
        uv_data = find_from_scene(data, polygons=polygons)
    else:
        uv_data = None
        core.displayWarning('wrong arguments or inputs!...')
        return
    if not uv_data:
        core.displayWarning('wrong arguments %s!...' % objects)
        return
    imported_result = {}
    result = True
    for index, contents in uv_data.items():
        uv_contents = contents[0:1]
        if repeat:
            uv_contents = contents
        for content in uv_contents:
            try:
                set_data = studio_maya.setData(content)
                imported_result.setdefault(
                    True, []).append(content['shape_node'])
            except Exception as error:
                imported_result.setdefault(
                    False, []).append(content['shape_node'])
                set_data = None
            if not set_data:
                result = False
    print '\npolygons\n', json.dumps(imported_result, indent=4)
    if not result:
        core.displayWarning('import not completed!...')
        return
    core.displayInfo('// Result: import success!...')


def get_polygons(type):
    if type == 'selected':
        nodes = core.ls(sl=True)
        all_polygons = core.listTransforms(type='mesh')
        polygons = []
        for node in nodes:
            if node not in all_polygons:
                continue
            polygons.append(node)
    elif type == 'all':
        polygons = core.listTransforms(type='mesh')
    polygons = [polygon.fullPath() for polygon in polygons]
    return polygons


def find_from_scene(data, mode=False, polygons=None):
    studio_maya = studioMaya.Connect()
    if not polygons:
        polygons = core.listTransforms(type='mesh')
    scene_polygons = {}
    for index, contents in data.items():
        for polygon in polygons:
            if isinstance(polygon, str) or isinstance(polygon, unicode):
                polygon = core.PyNode(polygon)
            if mode:
                if contents['short_name'] != polygon.fullPath().split('|')[-1]:
                    continue
            num_polygons_data = contents['num_polygons']
            polygon_vertices_data = contents['polygon_vertices']
            studio_maya.node = polygon.name()
            mfn_mesh = studio_maya.getMfnMesh()
            num_polygons, polygon_vertices = studio_maya.getFacesVertices(
                mfn_mesh)
            if num_polygons_data != num_polygons:
                continue
            if polygon_vertices_data != polygon_vertices:
                continue
            scene_contents = copy.deepcopy(contents)
            scene_contents['shape_node'] = polygon.name()
            scene_contents['long_name'] = polygon.fullPath()
            scene_contents['short_name'] = polygon.fullPath().split('|')[-1]
            scene_polygons.setdefault(index, []).append(scene_contents)
    return scene_polygons


def find_from_data(data, polygons=None):
    data_polygons = {}
    for index, contents in data.items():
        short_name = contents['short_name']
        long_name = contents['long_name']
        num_polygons = contents['num_polygons']
        polygon_vertices = contents['polygon_vertices']
        if core.objExists(long_name):
            current_node = short_name
        elif core.objExists(short_name):
            current_node = short_name
        else:
            current_node = None
        if not current_node:
            continue
        node_instances = [each.fullPath() for each in core.ls(current_node)]
        for node in node_instances:
            data_contents = copy.deepcopy(contents)
            data_contents['shape_node'] = node
            data_contents['long_name'] = node
            data_contents['short_name'] = node.split('|')[-1]
            data_polygons.setdefault(index, []).append(data_contents)
    return data_polygons


def get_influance_objects(directory):
    studio_maya = studioMaya.Connect()
    data = studio_maya.read(directory)
    nodes = []
    sorted_index = sorted(data.keys())
    for index in sorted_index:
        nodes.append(data[index]['long_name'].encode())
    print json.dumps(nodes, indent=4)
    return nodes
