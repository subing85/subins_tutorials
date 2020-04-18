import os
import imp
import copy
import pkgutil

from studio_usd_pipe import resource

from pprint import pprint

class Publish(object):
    
    def __init__(self, subfield):
        self.bundle_path = resource.getPublishBundlePath(subfield)
        self.container = {} # execute = self.container[0] repair = self.container[1]
        
    def is_valid(self):
        module = imp.load_source(
            '__init__', os.path.join(self.bundle_path, '__init__.py'))
        if not hasattr(module, 'VALID'):
            return False
        if not module.VALID:
            return False
        return True
    
    def show_result(self, header, container, key):
        print '# header:', header
        index = 1
        for module, v in container[key].items():
            
            if index>1:
                print ''
            print ('%s. module key: '%index).rjust(15), module.KEY
            for value in v[0]:
                print ': '.rjust(15), value
            print 'message: '.rjust(15), v[1]
            index+=1
        if key:
            print '#info: execute success!...', header, '\n'
        else:     
            print '#warnings: execute failed!...', header, '\n'
    
    def execute(self, mode, output_path, repair=True, **kwargs):
        self.container = {} # execute = self.container[0] repair = self.container[1]
        self.execute_bundles(mode, 0, output_path, **kwargs)
        print self.container
        if True in self.container[0]:
            self.show_result('validation', self.container[0], True)
        if False in self.container[0]:
            self.show_result('validation', self.container[0], False)            
        if False in self.container[0] and repair: # repair          
            for module, contents in self.container[0][False].items():
                status, values, message = self.execute_bundle(
                    module, mode, 1, **kwargs)
                if status:
                    self.container[0][True][module] = values, '\"repair\" %s'%message
                    self.container[0][False].pop(module)
                else:
                    exists_value = self.container[0][False][module][0]
                    exist_message = '<not able to repair> %s'% self.container[0][False][module][1]
                    self.container[0][False][module] = exists_value, exist_message
            if True in self.container[1]:
                self.show_result('repair', self.container[1], True)
            if False in self.container[1]:
                self.show_result('repair', self.container[1], False)     
            if not self.container[0][False]:
                self.container[0].pop(False)                
        if True in self.container[0]:
            if not self.container[0][True]:
                self.container[0].pop(True)
        string_container = self.convert_key_container()             
        return self.container[0], string_container[0]
    
    def execute_bundle(self, module, mode, index, output_path, **kwargs):
        status, values, message = False, [], False
        if index==0:
            status, values, message = module.execute(output_path=output_path, **kwargs)
        if index==1:
            status, values, message = module.repair(**kwargs)
        # execute = self.container[0] repair = self.container[1]
        if index not in self.container:
            self.container.setdefault(index, {})
        if status not in self.container[index]:
            self.container[index].setdefault(status, {})
        self.container[index][status].setdefault(
            module, [values, message]
            )  
        return status, values, message
                   
    def execute_bundles(self, mode, index, output_path, **kwargs):
        bundles = self.get_bundles()
        if mode not in bundles:
            return
        container = {}   
        for x, module in bundles[mode].items():
            self.execute_bundle(module, mode, index, output_path, **kwargs)
        return container
        
    def convert_key_container(self):        
        string_container = {}
        for index, valids in self.container.items():
            string_container[index] = {}
            for valid, modules in valids.items():
                string_container[index][valid] = {}
                for module, contents in modules.items():
                    string_container[index][valid][module.__name__] = contents
        return string_container

    def get_bundles(self):
        if not self.is_valid():
            return None
        module_data = {}
        for module_loader, name, ispkg in pkgutil.iter_modules([self.bundle_path]):
            loader = module_loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'TYPE'):
                continue
            if not hasattr(module, 'VALID'):
                continue
            if not hasattr(module, 'ORDER'):
                continue
            if module.TYPE not in module_data:
                module_data.setdefault(module.TYPE, {})
            module_data[module.TYPE].setdefault(module.ORDER, module)
        return module_data

