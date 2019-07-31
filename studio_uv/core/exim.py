import copy
import json

from pymel import core
from studio_uv.core import studioMaya


def execute(*args):
    if args[0] == 'export' and args[3] and not args[4] and not args[6]:
        export_uv(args[2], args[3])
    if args[0] == 'import' and args[3] and not args[4] and not args[6]:
        import_uv(args[2], args[3], args[1])
    if args[4] and args[5] == 'True' and args[3]:
        get_influance_objects(args[3])
    if args[0] == 'import' and args[3] and not args[4]:
        import_uv(args[2], args[3], args[1])


def export_uv(type, directory):
    if type in ['selected', 'all']:
        polygons = get_polygons(type)
    else:
        strips = type.replace(' ', '')
        polygons = strips.split(',')
    studio_maya = studioMaya.Connect()
    uv_data_bundle = {}
    for index, polygon in enumerate(polygons):
        studio_maya.node = polygon
        mdag_path = studio_maya.getDagPath()
        data = studio_maya.getData(mdag_path)
        uv_data_bundle.setdefault(index, data)
    studio_maya.write(directory, uv_data_bundle)
    print '// Result:',  directory
    core.displayInfo('export success!...')


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


def import_uv(entity, directory, repeat):
    studio_maya = studioMaya.Connect()
    data = studio_maya.read(directory)
    if entity == 'matching':
        uv_data = find_from_scene(data)
    elif entity == 'selected':
        polygons = core.ls(sl=True)
        uv_data = find_from_scene(data, polygons=polygons)
    elif entity == 'all':
        uv_data = find_from_data(data)
    else:
        strips = entity.replace(' ', '')
        polygons = strips.split(',')
        uv_data = find_from_scene(data, polygons=polygons)
    result = True
    for index, contents in uv_data.items():
        uv_contents = contents[0:1]
        if repeat:
            uv_contents = contents
        for content in uv_contents:
            try:
                set_data = studio_maya.setData(content)
                print 'Success: node name - ', content['shape_node']
            except Exception as error:
                print 'Failed: node name - ', content['shape_node'], '\t', error
            if not set_data:
                result = False
    if not result:
        core.displayWarning('import not completed!...')
        return
    core.displayInfo('// Result: import success!...')


def find_from_scene(data, polygons=None):
    studio_maya = studioMaya.Connect()
    if not polygons:
        polygons = core.listTransforms(type='mesh')
    scene_polygons = {}
    for index, contents in data.items():
        for polygon in polygons:
            if isinstance(polygon, str) or isinstance(polygon, unicode):
                polygon = core.PyNode(polygon)
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


def find_from_data(data):
    data_polygons = {}
    for index, contents in data.items():
        short_name = contents['short_name']
        long_name = contents['long_name']
        num_polygons = contents['num_polygons']
        polygon_vertices = contents['polygon_vertices']
        current_node = None
        if core.objExists(long_name):
            current_node = long_name
        elif core.objExists(short_name):
            current_node = short_name
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
