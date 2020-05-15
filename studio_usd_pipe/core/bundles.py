import os
import imp
import copy
import json  
import pkgutil

from studio_usd_pipe import resource
from studio_usd_pipe.core import common


class Bundles(object):
    
    def __init__(self, application, types, subfield):
        self.bundle_path = resource.getBundlePath(application, types, subfield)
        # print 'self.bundle_path', self.bundle_path
        self.container = {}  # execute = self.container[0] repair = self.container[1]
        
    def is_valid(self):
        module = common.get_module(os.path.join(self.bundle_path, '__init__.py'))
        if not module:
            return False
        return True
        if not hasattr(module, 'VALID'):
            return False
        return True
    
    def show_result(self, header, container, key):
        print '# header:', header
        index = 1
        temp_data = {}        
        for module in container[key]:
            temp_data.setdefault(module.ORDER, module)
        modules = temp_data.values()
        for index, module in enumerate(modules):
            values = container[key][module]
            if index > 1:
                print ''
            print ('%s. module key: ' % (index + 1)).rjust(15), module.KEY
            for value in values[0]:
                print ': '.rjust(15), value
            print 'message: '.rjust(15), values[1]
        if key:
            print '#info: execute success!...', header, '\n'
        else:     
            print '#warnings: execute failed!...', header, '\n'
    
    def execute(self, mode, output_path, repair=True, **kwargs):
        '''
            :param mode <str> 'validation' or 'extractor'
        '''
        self.container = {}  # execute = self.container[0] repair = self.container[1]
        self.execute_bundles(mode, 0, output_path, **kwargs)
        if not self.container:
            print '#warnings found any %s bundle in' % mode, output_path
            return None, None
        if True in self.container[0]:
            self.show_result(mode, self.container[0], True)
        if False in self.container[0]:
            self.show_result(mode, self.container[0], False)  
        if False in self.container[0] and repair:  # repair          
            for module, contents in self.container[0][False].items():
                status, values, message = self.execute_bundle(
                    module, mode, 1, output_path, **kwargs)
                if status:
                    if True not in self.container[0]:
                        self.container[0].setdefault(True, {})
                    self.container[0][True][module] = values, '\"repair\" %s' % message
                    self.container[0][False].pop(module)
                else:
                    exists_value = self.container[0][False][module][0]
                    exist_message = '<not able to repair> %s' % self.container[0][False][module][1]
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
        return self.container[0]
    
    def execute_bundle(self, module, mode, index, output_path, **kwargs):
        status, values, message = False, [], False
        if index == 0:
            status, values, message = module.execute(output_path=output_path, **kwargs)
        if index == 1:
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
        for x, module in bundles[mode].items():
            self.execute_bundle(module, mode, index, output_path, **kwargs)

    def get_bundles(self, types=None):
        if not self.is_valid():
            return None
        module_data = common.get_modules(self.bundle_path, module_types=types)
        return module_data

