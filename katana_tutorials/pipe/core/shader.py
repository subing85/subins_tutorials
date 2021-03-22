import os
import json

from core import scenegraph


def get_assigned_materials(producer):
    '''
    :description get assigned materials
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_assigned_materials(producer)
    '''
    locations = scenegraph.travel(producer)
    root_producer = producer.getRootProducer()
    assigned_materials = {}
    for location in locations:
        material_assign = location.getGlobalAttribute('materialAssign')
        if not material_assign:
            continue
        material = material_assign.getData()
        if not material:
            continue    
        material_producer = root_producer.getProducerByPath(material[0])
        if not material_producer:
            continue
        if material_producer.getType() != 'material':
            continue
        assigned_materials.setdefault(material[0], []).append(location)    
    return assigned_materials


def get_scene_materials(producer):
    '''
    :description get scene (all) materials
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_scene_materials(producer)
    '''    
    material_producers = scenegraph.list_specific_producer(producer, 'material')
    material_assigned_objects = get_material_assigned_objects(producer)
    scene_materials = {}   
    for material_producer in material_producers:        
        current_material = material_producer.getFullName()        
        assigned_objects = None
        if current_material in material_assigned_objects:            
            assigned_objects = material_assigned_objects[current_material]        
        scene_materials.setdefault(current_material, assigned_objects)
    return scene_materials


def get_material_assigned_objects(producer):
    '''
    :description get material assigned objects
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_material_assigned_objects(producer)
    '''    
    locations = scenegraph.travel(producer)    
    root_producer = producer.getRootProducer()    
    assigned_objects = {}
    for location in locations:
        material_assign = location.getGlobalAttribute('materialAssign')
        if not material_assign:
            continue
        material = material_assign.getData()
        if not material:
            continue    
        material_producer = root_producer.getProducerByPath(material[0])
        if not material_producer:
            continue
        if material_producer.getType() != 'material':
            continue
        assigned_objects.setdefault(material[0], []).append(location)    
    return assigned_objects


def get_object_assigned_material(producer):
    '''
    :description get material assigned objects
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_material_assigned_objects(producer)
    '''    
    locations = scenegraph.travel(producer)    
    root_producer = producer.getRootProducer()    
    assigned_objects = {}
    for location in locations:
        material_assign = location.getGlobalAttribute('materialAssign')
        if not material_assign:
            continue
        material = material_assign.getData()
        if not material:
            continue    
        material_producer = root_producer.getProducerByPath(material[0])
        if not material_producer:
            continue
        if material_producer.getType() != 'material':
            continue
        assigned_objects.setdefault(location.getFullName(), material[0])    
    return assigned_objects
        

def get_material_assigned_texture_maps(producer):
    '''
    :description get material assigned texture maps
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_material_assigned_texture_maps(producer)
    '''    
    assigned_materials = get_assigned_materials(producer)
    root_producer = producer.getRootProducer()
    assigned_texture_maps = {}
    for material in assigned_materials:
        material_producer = root_producer.getProducerByPath(material)
        texture_maps = get_texture_maps(material_producer)
        assigned_texture_maps.setdefault(material, texture_maps)
    return assigned_texture_maps


def get_scene_material_texture_maps(producer):
    '''
    :description get scene (all) material texture maps
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_scene_material_texture_maps(producer)
    '''        
    scene_materials = get_scene_materials(producer)
    root_producer = producer.getRootProducer()    
    scene_texture_maps = {}
    for material in scene_materials:
        material_producer = root_producer.getProducerByPath(material)
        texture_maps = get_texture_maps(material_producer)
        scene_texture_maps.setdefault(material, texture_maps)
    return scene_texture_maps

        
def get_texture_maps(material_producer):
    '''
    :description get texture maps from material producer
    :param material_producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_texture_maps(material_producer)
    '''        
    texture_maps = {}
    dependency_nodes = get_material_dependency_nodes(material_producer)
    if not dependency_nodes:
        return texture_maps
    for dependency_node in dependency_nodes:
        filename = get_node_filename(material_producer, dependency_node)        
        if not filename:
            continue        
        sourcename = get_node_sourcename(material_producer, dependency_node)        
        if not sourcename:
            sourcename = dependency_node            
        texture_maps.setdefault(filename, []).append(sourcename)
    return texture_maps   


def get_material_dependency_nodes(material_producer):
    '''
    :description get material dependency nodes
    :param material_producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_material_dependency_nodes(material_producer)
    '''    
    global_attribute = material_producer.getGlobalAttribute('material.nodes')
    if not global_attribute:
        return None
    dependency_nodes = global_attribute.childNames()
    return dependency_nodes


def get_node_filename(material_producer, node):
    '''
    :description get material dependency node file name (source file)
    :param material_producer <GeometryProducer object>
    :param node <str>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_node_filename(material_producer, 'body_texture')
    '''  
    attribute = 'material.nodes.%s.parameters.filename' % node
    filename = material_producer.getGlobalAttribute(attribute)
    if not filename:
        return None        
    filenames = filename.getData()
    if not filenames:
        return None
    return filenames[0]


def get_node_sourcename(material_producer, node):
    '''
    :description get material dependency node source name (source name)
    :param material_producer <GeometryProducer object>
    :param node <str>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_node_sourcename(material_producer, 'body_texture')
    '''      
    attribute = 'material.nodes.%s.srcName' % node
    sourcename = material_producer.getGlobalAttribute(attribute)
    if not sourcename:
        return None        
    sourcenames = sourcename.getData()
    if not sourcenames:
        return None
    return sourcenames[0]


def get_assigned_shader_networks(producer):
    '''
    :description get assigned shader networks data
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_assigned_shader_networks(producer)    
    '''
    assigned_materials = get_assigned_materials(producer)
    root_producer = producer.getRootProducer()
    assigned_shader_networks = {}
    for assigned_material in assigned_materials:
        material_producer = root_producer.getProducerByPath(assigned_material)
        shader_networks = get_shader_networks(material_producer)
        assigned_shader_networks.setdefault(assigned_material, shader_networks)
        assigned_locations = get_assigned_locations(assigned_materials[assigned_material])
        materail_assigments = {'assigned_locations': assigned_locations}       
        assigned_shader_networks[assigned_material].update(materail_assigments)
    return assigned_shader_networks


def get_scene_shader_networks(producer, polymesh=False):
    '''
    :description get scene (all) shader networks data
    :param producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        producer = scenegraph.get_producer(knode, location=None)
        shader.get_scene_shader_networks(producer, polymesh=False)      
    '''
    scene_materials = get_scene_materials(producer)
    root_producer = producer.getRootProducer()
    scene_shader_networks = {}
    for scene_material in scene_materials:
        material_producer = root_producer.getProducerByPath(scene_material)
        shader_networks = get_shader_networks(material_producer)
        scene_shader_networks.setdefault(scene_material, shader_networks)
        assigned_locations = get_assigned_locations(scene_materials[scene_material], polymesh=polymesh)
        materail_assigments = {'assigned_locations': assigned_locations}       
        scene_shader_networks[scene_material].update(materail_assigments)        
    return scene_shader_networks    


def get_assigned_locations(object_producers, polymesh=False):
    '''
    :description convert GeometryProducer object to string (location)
    :param object_producers <list>
    :param polymesh <bool>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'       
        object_producers = scenegraph.get_producer(knode, location=location)
        shader.get_assigned_locations([object_producers])      
    '''        
    if not object_producers:
        return None
    assigned_locations = {}
    
    for object_producer in object_producers:
        if object_producer.getType()=='curves':
            continue        
        if not polymesh:
            if object_producer.getType()=='polymesh':
                continue            
        child = object_producer.getFirstChild()
        if child.getType()=='polymesh':
            typed = 'polymesh'
        else:
            typed = object_producer.getType()
        assigned_locations.setdefault(object_producer.getFullName(), typed)
    return assigned_locations
        

def get_shader_networks(material_producer):
    '''
    :description get shader network dependency nodes and its prameter values
    :param material_producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'       
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_shader_networks(material_producer)      
    '''      
    dependency_nodes = get_material_dependency_nodes(material_producer)
    shader_networks = {
        'nodes': {},
        'terminals': {}
        }
    for dependency_node in dependency_nodes:
        shader_parameters = get_node_parameters(material_producer, dependency_node)
        shader_networks['nodes'].setdefault(dependency_node, shader_parameters)
    material_parameters = get_material_parameters(material_producer)
    shader_networks['terminals'] = material_parameters
    return shader_networks


def get_material_parameters(material_producer):
    '''
    :description get material terminals prameter values
    :param material_producer <GeometryProducer object>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'       
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_material_parameters(material_producer)      
    '''     
    attributes = ['material.terminals']      
    material_attributes = scenegraph.get_attributes(material_producer, input_attributes=attributes) 
    material_values = scenegraph.get_attribute_typed_values(material_producer, material_attributes)
    material_parameters = {}
    for k, v in material_values.items():
        paramter = k.rsplit('material.terminals.', 1)[1]
        material_parameters.setdefault(paramter, v) 
    return material_parameters    
        

def get_node_parameters(material_producer, node):    
    '''
    :description get the node prameter values
    :param material_producer <GeometryProducer object>
    :param node <str>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/materials/body_material'       
        material_producer = scenegraph.get_producer(knode, location=location)
        shader.get_node_parameters(material_producer, 'face_texture')      
    '''        
    attributes = [
        'material.nodes.%s.name' % node,
        'material.nodes.%s.type' % node,
        'material.nodes.%s.target' % node,
        'material.nodes.%s.parameters' % node,
        'material.nodes.%s.connections' % node        
        ]
    shader_parameters = {
        'primary': {},
        'parameters': {},
        'connections': {}
        }
    # get the primary values such as name, type, traget
    primary_values = scenegraph.get_attribute_typed_values(material_producer, attributes[0:3])
    for k, v in primary_values.items():
        paramter = k.rsplit('material.nodes.%s.' % node, 1)[1]
        shader_parameters['primary'].setdefault(paramter, v)
    # get the node modified parameter values    
    prameter_attributes = scenegraph.get_attributes(material_producer, input_attributes=attributes[3:4])    
    parameter_values = scenegraph.get_attribute_typed_values(material_producer, prameter_attributes)
    for k, v in parameter_values.items():
        paramter = k.rsplit('material.nodes.%s.parameters.' % node, 1)[1]
        shader_parameters['parameters'].setdefault(paramter, v)    
    # get the node connection values    
    connection_attributes = scenegraph.get_attributes(material_producer, input_attributes=attributes[4:5])
    connection_values = scenegraph.get_attribute_typed_values(material_producer, connection_attributes)
    for k, v in connection_values.items():
        paramter = k.rsplit('material.nodes.%s.connections.' % node, 1)[1]
        shader_parameters['connections'].setdefault(paramter, v)    
    
    return shader_parameters


def export_shader_networks(producer, export_path):
    '''
    :description export the katana shader network as as custom format(scene description)
    :param material_producer <GeometryProducer object>
    :param export_path <str>
    :example
        from core import shader
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        path = '/venture/shows/katana_tutorials/dumps/shader/test_001.shader'       
        shader.export_shader_networks(material_producer, path)     
    '''   
    dirname, format = os.path.splitext(export_path)    
    shader_path = '%s.shader'%dirname    
    if not os.path.isdir(os.path.dirname(dirname)):
        os.makedirs(os.path.dirname(dirname))
    shader_networks = get_scene_shader_networks(producer, polymesh=False)    
    with (open(shader_path, 'w')) as shader:
        shader.write(json.dumps(shader_networks, indent=4))        
        return shader_path
    return None
    
    









        
