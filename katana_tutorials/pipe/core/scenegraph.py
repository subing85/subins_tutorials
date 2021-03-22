
from Katana import Nodes3DAPI
from Katana import NodegraphAPI


def get_producer(knode, location=None):
    '''
    :description get the scenegraph location producer
    :prama knode <Nodegraph Node Object>
    :param location <str>
    :example
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        scenegraph.get_producer(knode, location=None)    
    '''
    NodegraphAPI.SetNodeViewed(knode, True, exclusive=True)
    producer = Nodes3DAPI.GetGeometryProducer(node=knode)
    if location:
        producer = producer.getProducerByPath(location)
    return producer


def get_children(producer):
    '''
    :description get the children producer of specific producer
    :param producer <GeometryProducer object>
    :example
        from core import scenegraph
        producer = Nodes3DAPI.GetGeometryProducer()
        scenegraph.get_children(producer)
    '''
    children = []
    for child in producer.iterChildren():
        children.append(child)
    return children


def travel(producer):
    '''
    :description get all nested locations under the specific producer
    :param producer <GeometryProducer object>
    :example
        from core import scenegraph
        producer = Nodes3DAPI.GetGeometryProducer()
        scenegraph.travel(producer)    
    '''
    stack = [producer]
    locations = []
    while stack:
        child = stack.pop()
        children = child.iterChildren()
        locations.append(child)
        stack.extend(children)    
    return locations


def list_specific_producer(producer, specific_type):
    '''
    :description get specific type locations
    :param producer <GeometryProducer object>
    :param specific_type <str>
    :example
        from core import scenegraph
        producer = Nodes3DAPI.GetGeometryProducer()
        scenegraph.list_specific_producer(producer, 'material')    
    '''
    locations = travel(producer)
    specific_locations = []
    for location in locations:
        if specific_type != location.getType():
            continue
        specific_locations.append(location)
    return specific_locations


def show_to_location(producers):
    '''
    :description to print each producer to full name
    :param producers <list>
    :example
        from core import scenegraph
        scenegraph.show_to_location(producers)    
    '''
    for producer in producers:
        print producer.getFullName()
        

def get_attributes(producer, input_attributes=None):
    '''
    :description get producer(scenegraph location) attributes
    :param producer <GeometryProducer object>
    :example
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/world/character/batman'
        producer = scenegraph.get_producer(knode, location=location)
        attributes = scenegraph.get_attributes(producer)    
    '''
    if not input_attributes:
        input_attributes = producer.getAttributeNames()        
    attributes = []
    stack = input_attributes
    while stack:
        attribute = stack.pop()
        attributes.append(attribute)
        global_attribute = producer.getGlobalAttribute(attribute)
        if not global_attribute:
            continue
        data = global_attribute.getData()
        if data:
            continue
        for each in global_attribute.childNames():
            stack.append('%s.%s'%(attribute, each))
    return attributes


def get_attribute_value(producer, attribute):
    '''
    :description get producer valid attribute value (data)
    :param producer <GeometryProducer object>
    :param attribute <str>
    :example
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/world/character/batman'
        producer = scenegraph.get_producer(knode, location=location)
        attributes = scenegraph.get_attribute_value(producer, 'forceExpand')    
    '''
    global_attribute = producer.getGlobalAttribute(attribute)
    if not global_attribute:
        return None, None    
    attribute_type = global_attribute.type()
    tuple_size = global_attribute.getTupleSize()
    typed = '%s%s'%(attribute_type, tuple_size)
    data = global_attribute.getData()
    if not data:
        return None, None
    if len(data)==1:
        return data[0], typed, 
    return data, typed


def get_attribute_values(producer, attributes):
    '''
    :description get producer valid attributes value (data)
    :param producer <GeometryProducer object>
    :param attribute <list>
    :example
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/world/character/batman'
        producer = scenegraph.get_producer(knode, location=location)
        attributes = scenegraph.get_attributes(producer)
        attribute_values = scenegraph.get_attribute_values(producer, attributes)
    '''    
    attribute_values = {}    
    for attribute in attributes:
        value, typed = get_attribute_value(producer, attribute)
        if not value:
            continue
        attribute_values.setdefault(attribute, value)
    return attribute_values
        
        
def get_attribute_typed_values(producer, attributes):
    '''
    :description get producer valid attributes value (data)
    :param producer <GeometryProducer object>
    :param attribute <list>
    :example
        from core import scenegraph
        knode = NodegraphAPI.GetAllSelectedNodes()[0]
        location = '/root/world/character/batman'
        producer = scenegraph.get_producer(knode, location=location)
        attributes = scenegraph.get_attributes(producer)
        attribute_typed_values = scenegraph.get_attribute_typed_values(producer, attributes)
    '''    
    attribute_typed_values = {}    
    for attribute in attributes:
        value, typed = get_attribute_value(producer, attribute)
        if not value:
            continue
        contents = {
            'value': value,
            'type': typed
            }
        attribute_typed_values.setdefault(attribute, contents)
    return attribute_typed_values  

    


