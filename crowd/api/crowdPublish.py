import logging
import pkgutil

from crowd import resource

reload(resource)


class Publish(object):

    def __init__(self, type=None):

        self.publish_type = type
        self.resource_path = resource.getPublishPath(type=type)

        self.bundle_value = {
            'failed': ['red', False],
            'error': ['magenta', False],
            'success': ['green', True],
            'runtime error': ['yellow', False]
        }

    def getBundleKeys(self):
        return self.bundle_value

    def getPackages(self):
        if not self.resource_path:
            return
        module_data = []
        modules = []
        for module_loader, name, ispkg in pkgutil.iter_modules([self.resource_path]):
            modules.append(name)
            loader = module_loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'VALID'):
                continue
            module_data.append(module)
        if not self.publish_type:
            return modules
        return module_data

    def getValidate(self, valid=True):
        module_data = self.getModules(valid=valid)
        if 'validate' not in module_data:
            logging.warning('not found <validate> in the publish bundle!...')
            return
        return module_data['validate']

    def getExtract(self, valid=True):
        module_data = self.getModules(valid=valid)
        if 'extract' not in module_data:
            logging.warning('not found <extract> in the publish bundle!...')
            return
        return module_data['extract']

    def getModules(self, valid=True):
        module_data = {}
        data = self.getPackages()
        for each_module in data:
            current_module = None
            current_dict = each_module.__dict__
            if 'VALID' not in current_dict:
                continue
            if 'MODULE_TYPE' not in current_dict:
                continue
            if valid:
                if not current_dict['VALID']:
                    continue
                current_module = each_module
            else:
                current_module = each_module
            if not current_module:
                continue
            bundle_type = 'unknown'
            if 'BUNDLE_TYPE' in current_dict:
                bundle_type = current_dict['BUNDLE_TYPE']
            module_data.setdefault(bundle_type, []).append(current_module)
        return module_data

    def executeValidateModule(self, module):
        if not module:
            logging.warnings('publish build not valid', Warning)
            return
        if not self.publish_type:
            logging.warnings('publish build type not valid', Warning)
            return
        try:
            result, data, message = module.testRun()
        except Exception as except_error:
            result, data, message = 'runtime error', [], str(except_error)

        value = self.bundle_value[result][1]
        color = self.bundle_value[result][0]
        return result, value, color, data, message
    
    
    def executeExtractModule(self, module):        
        result, value, color, data, message = self.executeValidateModule(module)
        
        
        
        
        
