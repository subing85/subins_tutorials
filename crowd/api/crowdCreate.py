import os
import json
import pkgutil
import logging

from crowd import resource
from crowd.api import crowdPublish
from crowd.core import database
reload(resource)


class Connect(object):
    
    def __init__(self, **kwargs):
        self.type = None
        self.tag = None
        if 'type' in kwargs:
            self.type = kwargs['type']            
        if 'tag' in kwargs:            
            self.tag = kwargs['tag']
        
        self.resource_path = resource.getCreateResource(type=self.type) 
        
        self.bundle_value = {
            'failed': ['red', False],
            'error': ['magenta', False],
            'success': ['green', True],
            'runtime error': ['yellow', False]
        }
        self.components = {}

    def getBundleKeys(self):
        return self.bundle_value

    def getPackages(self):
        if not self.resource_path:
            return
        modules = {}
        for module_loader, name, ispkg in pkgutil.iter_modules([self.resource_path]):
            loader = module_loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'VALID'):
                continue
            order = 0                 
            if hasattr(module, 'ORDER'):
                order = module.ORDER            
            modules.setdefault(order, []).append(module)        
        return modules
    
    def do(self):
        publish = crowdPublish.Connect(type=self.type, tag=self.tag)      
        input_data = publish.getInputs(show=False)
        
        modules = self.getPackages()        
        for order, module in modules.items():
            for each_module in module:   
                if not hasattr(each_module, 'MODULE_TYPE'):
                    continue    
                if each_module.MODULE_TYPE not in input_data:
                    continue                
                print '\t', each_module.MODULE_TYPE
                print '\t', self.tag                           
                self.executeModule(
                    each_module, self.tag, input_data[each_module.MODULE_TYPE])

    def executeModule(self, module, tag, inputs):
        if not module:
            logging.warnings('publish build not valid', Warning)
            return
        if not self.type:
            logging.warnings('publish build type not valid', Warning)
            return
        try:
            result, data, message = module.testRun(tag, inputs)
        except Exception as except_error:
            result, data, message = 'runtime error', [], str(except_error)
        value = self.bundle_value[result][1]
        color = self.bundle_value[result][0] 
        return result, value, color, data, message
    
    def getTypes(self):
        return ['puppet']

    def getTags(self):
        return self.getSpecificDatas(1)

    
