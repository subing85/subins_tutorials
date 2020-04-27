import logging

from maya import OpenMaya
from maya import OpenMayaMPx

from crowd.api import skeleton
from crowd.api import crowdSetup


class Connect(OpenMayaMPx.MPxNode):
    plugin_name = 'subinsCrowd'
    node_id = OpenMaya.MTypeId(0x87000)

    type = OpenMaya.MObject()
    count = OpenMaya.MObject()
    row = OpenMaya.MObject()
    column = OpenMaya.MObject()
    offset = OpenMaya.MObject()
    random = OpenMaya.MObject()
    output = OpenMaya.MObject()

    kTypeAttrName = 'type'
    kTypeAttrShortName = 'typ'
    kCountAttrName = 'count'
    kCountAttrShortName = 'cnt'
    kRowAttrName = 'row'
    kRowAttrShortName = 'r'
    kColumnAttrName = 'column'
    kColumnAttrShortName = 'c'
    kOffsetAttrName = 'offset'
    kOffsetAttrShortName = 'of'
    kRandomAttrName = 'random'
    kRandomAttrShortName = 'rm'
    kOutputAttrName = 'output'
    kOutputAttrShortName = 'out'

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    def compute(self, plug, data):        
        if plug.isNull():
            return OpenMayaMPx.MPxNode.compute(plug, data)
        
        type_handle = OpenMaya.MDataHandle(data.inputValue(Connect.type))
        type_value = type_handle.asChar()
        
        count_handle = OpenMaya.MDataHandle(data.inputValue(Connect.count))
        count_value = count_handle.asLong()  
        
        row_handle = OpenMaya.MDataHandle(data.inputValue(Connect.row))
        row_value = row_handle.asLong()
        
        column_handle = OpenMaya.MDataHandle(data.inputValue(Connect.column))
        column_value = column_handle.asLong()  
        
        offset_handle = OpenMaya.MDataHandle(data.inputValue(Connect.offset))
        offset_value = offset_handle.asLong()  
        
        random_handle = OpenMaya.MDataHandle(data.inputValue(Connect.random))
        random_value = random_handle.asLong()
        
        print 'random_value', random_value

        self.crowd_setup(
            type=type_value,
            count=count_value,
            row=row_value,
            column=column_value,
            offset=offset_value,
            random=random_value
            )
        
    def crowd_setup(self, **kwargs):
        setup = crowdSetup.Connect(
            self,
            type=kwargs['type'],
            count=kwargs['count'],
            row=kwargs['row'],
            column=kwargs['column'],
            offset=kwargs['offset'],
            random=kwargs['random']              
            )    
        setup.create()


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(Connect())


def nodeInitializer():
    enum_attribute = OpenMaya.MFnEnumAttribute()
    numeric_attribute = OpenMaya.MFnNumericAttribute()

    skeleton_type = getSkeletonTypes()

    Connect.type = createEnumAttribute(
        enum_attribute, Connect.kTypeAttrName, Connect.kTypeAttrShortName, skeleton_type)
    Connect.count = createIntAttribute(
        numeric_attribute, Connect.kCountAttrName, Connect.kCountAttrShortName)
    Connect.row = createIntAttribute(
        numeric_attribute, Connect.kRowAttrName, Connect.kRowAttrShortName)
    Connect.column = createIntAttribute(
        numeric_attribute, Connect.kColumnAttrName, Connect.kColumnAttrShortName)
    Connect.offset = createFloatAttribute(
        numeric_attribute, Connect.kOffsetAttrName, Connect.kOffsetAttrShortName)
    Connect.random = createFloatAttribute(
        numeric_attribute, Connect.kRandomAttrName, Connect.kRandomAttrShortName)

    Connect.output = createOutputAttribute(
        numeric_attribute, Connect.kOutputAttrName, Connect.kOutputAttrShortName)

    Connect.addAttribute(Connect.type)
    Connect.addAttribute(Connect.count)
    Connect.addAttribute(Connect.row)
    Connect.addAttribute(Connect.column)
    Connect.addAttribute(Connect.offset)
    Connect.addAttribute(Connect.random)
    Connect.addAttribute(Connect.output)
    
    Connect.attributeAffects(Connect.type, Connect.output)
    Connect.attributeAffects(Connect.count, Connect.output)
    Connect.attributeAffects(Connect.row, Connect.output)
    Connect.attributeAffects(Connect.column, Connect.output)
    Connect.attributeAffects(Connect.offset, Connect.output)
    Connect.attributeAffects(Connect.random, Connect.output)

    #===========================================================================
    # Connect.mustCallValidateAndSet(Connect.type)
    # Connect.mustCallValidateAndSet(Connect.count)
    # Connect.mustCallValidateAndSet(Connect.row)
    # Connect.mustCallValidateAndSet(Connect.column)
    # Connect.mustCallValidateAndSet(Connect.offset)
    # Connect.mustCallValidateAndSet(Connect.random)
    #===========================================================================

    #=======================================================================
    # self.count = attribute.create(
    #     self.kCountAttrName, self.kCountAttrShortName, OpenMaya.MFnNumericData.kInt, 1)
    # self.output = attribute.create(
    #     self.kOutputAttrName, self.kOutputAttrShortName, OpenMaya.MFnNumericData.kInt, 1)
    # self.addAttribute(self.count)
    # self.addAttribute(self.output)
    # self.attributeAffects(self.count, self.output)
    #=======================================================================


def createEnumAttribute(attribute, name, short_name, data):
    current_attribute = attribute.create(name, short_name, 0)
    for index, each in enumerate(data):
        attribute.addField(each, index)
    attribute.setHidden(False)
    attribute.setKeyable(True)
    attribute.setWritable(True)
    attribute.setReadable(True)
    attribute.setStorable(True)
    return current_attribute


def createIntAttribute(attribute, name, short_name, min=0, max=100):
    current_attribute = attribute.create(
        name, short_name, OpenMaya.MFnNumericData.kInt, 1)
    attribute.setHidden(False)
    attribute.setKeyable(True)
    attribute.setWritable(True)
    attribute.setReadable(True)
    attribute.setStorable(True)
    attribute.setInternal(True)
    attribute.setMin(min)
    attribute.setMax(max)
    return current_attribute


def createFloatAttribute(attribute, name, short_name, min=0.00, max=100.00):
    current_attribute = attribute.create(
        name, short_name, OpenMaya.MFnNumericData.kFloat, 0.0)
    attribute.setHidden(False)
    attribute.setKeyable(True)
    attribute.setWritable(True)
    attribute.setReadable(True)
    attribute.setStorable(True)
    attribute.setInternal(True)
    attribute.setMin(min)
    attribute.setMax(max)
    return current_attribute


def createOutputAttribute(attribute, name, short_name):
    current_attribute = attribute.create(
        name, short_name, OpenMaya.MFnNumericData.kInt, 1)
    attribute.setWritable(True)
    attribute.setStorable(True)
    attribute.setReadable(True)
    attribute.setHidden(False)        
    return current_attribute   


def getSkeletonTypes():
    crowd_skeleton = skeleton.Connect()
    skeleton_type = crowd_skeleton.getSkeletonTypes()
    if not skeleton_type:
        skeleton_type = ['None']
    return skeleton_type


def removeAttribute(self, attribute, result=True):
    if not self.dependency_node.hasAttribute(attribute):
        if result:
            logging.warning('not found the attribute %s' % attribute)
        return
    attr_mobject = self.dependency_node.attribute(attribute)
    try:
        self.dependency_node.removeAttribute(attr_mobject)
    except Exception as error:
        logging.error('not found the attribute %s' % attribute)
