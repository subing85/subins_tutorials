import logging

from maya import OpenMaya
from crowd.api import crowdSkeleton



class Connect(object):

    def __init__(self, node=None):        
        self.node = node            
        # self.getParentAttributes()
        
        self.input_attribute = 'module_type'
        
        
    def setInputAttribute(self):
        pass
    
    
    def getInInputAttribute(self):
        pass
    
    
        
        
        




    def getPlugName(self):
        return 'crowdProxy'

    def getParentAttributes(self):
        self.k_type = ['typ', 'type']
        self.k_count = ['cnt', 'count']
        self.k_distance = ['ds', 'distance']
        self.k_row = ['rw', 'rows']
        self.k_column = ['cm', 'columns']
        self.k_row_offset = ['rwo', 'rowOffset']
        self.k_column_offset = ['cmo', 'columnOffset']        
        self.k_random = ['rm', 'random']
        
        attribute_pool = [
            self.k_type,
            self.k_count,
            self.k_row,
            self.k_column,
            self.k_row_offset,
            self.k_column_offset,
            self.k_random
        ]
        return attribute_pool
    
    def createParentAttributes(self, mobject=None):
        if not self.node:
            logging.warning('class initialize error(argument node=None).')
            return            
        enum_attribute = OpenMaya.MFnEnumAttribute()
        numeric_attribute = OpenMaya.MFnNumericAttribute()
        skeleton_type = self.getSkeletonTypes()
        
        type_attribute = self.createEnumAttribute(
            enum_attribute, self.k_type[1], self.k_type[0], skeleton_type)
        count_attribute = self.createIntAttribute(
            numeric_attribute, self.k_count[1], self.k_count[0])
        distance_attribute = self.createIntAttribute(
            numeric_attribute, self.k_distance[1], self.k_distance[0])    
        row_attribute = self.createIntAttribute(
            numeric_attribute, self.k_row[1], self.k_row[0])
        column_attribute = self.createIntAttribute(
            numeric_attribute, self.k_column[1], self.k_column[0])
        row_offset_attribute = self.createFloatAttribute(
            numeric_attribute, self.k_row_offset[1], self.k_row_offset[0])

        column_offset_attribute = self.createFloatAttribute(
            numeric_attribute, self.k_column_offset[1], self.k_column_offset[0])
                
        random_attribute = self.createFloatAttribute(
            numeric_attribute, self.k_random[1], self.k_random[0])

        mobject.addAttribute(self.node, type_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, count_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, distance_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, row_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, column_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, row_offset_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)
        mobject.addAttribute(self.node, column_offset_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)

        mobject.addAttribute(self.node, random_attribute, OpenMaya.MFnDependencyNode.kLocalDynamicAttr)

                         
    def getSkeletonTypes(self):
        crowd_skeleton = crowdSkeleton.Connect()
        skeleton_type = crowd_skeleton.getSkeletonTypes()
        if not skeleton_type:
            skeleton_type = ['None']
        return skeleton_type        
        

    def createEnumAttribute(self, attribute, name, short_name, data):
        current_attribute = attribute.create(name, short_name, 0)
        for index, each in enumerate(data):
            attribute.addField(each, index)
        attribute.setHidden(False)
        attribute.setKeyable(True)
        attribute.setWritable(True)
        attribute.setReadable(True)
        attribute.setStorable(True)
        return current_attribute

    def createIntAttribute(self, attribute, name, short_name, min=0, max=100):
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

    def createFloatAttribute(self, attribute, name, short_name, min=0.00, max=100.00):
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

    def createOutputAttribute(self, attribute, name, short_name):
        current_attribute = attribute.create(
            name, short_name, OpenMaya.MFnNumericData.kInt, 1)
        attribute.setWritable(True)
        attribute.setStorable(True)
        attribute.setReadable(True)
        attribute.setHidden(False)
        return current_attribute

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
