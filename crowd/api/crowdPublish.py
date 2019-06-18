import os
import json
import time
import logging
import pkgutil
import shutil


from pprint import pprint
from datetime import datetime

from crowd import resource
from crowd.core import readWrite
from crowd.core import database

reload(resource)
reload(readWrite)
reload(database)


class Connect(object):

    def __init__(self, **kwargs): 
        self.type = None
        self.tag = None          
        self.format = 'json'
                
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'tag' in kwargs:           
            self.tag = kwargs['tag']        
        if 'format' in kwargs:           
            self.format = kwargs['format']      
              
        self.resource_path = resource.getPublishResource(type=self.type)        
        self.directory = resource.getPublishDirectory()
        
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
        module_data = []
        for module_loader, name, ispkg in pkgutil.iter_modules([self.resource_path]):
            loader = module_loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'VALID'):
                continue
            module_data.append(module)
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

    def executeModule(self, module):
        if not module:
            logging.warnings('publish build not valid', Warning)
            return
        if not self.type:
            logging.warnings('publish build type not valid', Warning)
            return
        try:
            result, data, message = module.testRun()
        except Exception as except_error:
            result, data, message = 'runtime error', [], str(except_error)

        value = self.bundle_value[result][1]
        color = self.bundle_value[result][0]        
        return result, value, color, data, message
    
    def do(self, data=None, name=None, comment=None, description=None):
        '''
            :param data <dict>
            :param name <str>
            :param comment <str> optional
            :param description <str> optional
            :param valid <str> optional
            :param format <str> optional
        ''' 
        rw = readWrite.ReadWrite( 
            co=comment,
            de=description, 
            fm=self.format,
            pa=self.directory,
            na=name,
            ty=self.type,
            tg=self.tag)           
        rw.write(data, force=True)
        self.components.setdefault(name, rw.file_path)

    def commit(self, origin=None, comment=None, description=None):        
        source = os.path.join(
            self.directory, self.tag, 'scene%s'%os.path.splitext(origin)[-1])         
        
        rw = readWrite.ReadWrite( 
            de=description,
            ty=self.type,
            tg=self.tag,
            cp=self.components.keys(),
            pa=self.directory,
            lo=self.components,
            su=source,
            og=origin,
            co=comment,
            na='manifest',
            fm='man'
            )       
        manifest = rw.commit(force=True)
        current_time = time.time()                 
        shutil.copy2(origin, source)            
        os.utime(source,(current_time, current_time))
        
        db = database.Database(table=self.type)
        db.create()
        db.insert(tag=self.tag, manifest=os.path.dirname(source))        
        print 'write success!...', '<%s>'% source        
        
    def getTypes(self):
        db = database.Database()
        tables = db.get_tables()
        return tables
    
    def getTables(self):
        db = database.Database(table=self.type)
        tags = db.get_columns()
        return tags
               
    def getDatas(self):
        db = database.Database(table=self.type)
        data = db.select()
        return data
    
    def getData(self):
        datas = self.getDatas()        
        for each in datas:
            if self.tag not in each:
                continue
            return each
        
    def getSpecificDatas(self, key):    
        data = self.getDatas()
        keys = []        
        for each in data:
            keys.append(each[key])            
        return keys             
            
    def getTags(self):    
        return self.getSpecificDatas(1)
                
    def getDirectory(self):
        data = self.getData() 
        return data[4]   

    def getManifestData(self, show=False):
        path = self.getDirectory()
        rw = readWrite.ReadWrite()        
        rw.file_path = os.path.join(path, 'manifest.man')
        infom_dict = rw.read(all=True)
        if show:
            print json.dumps(infom_dict, indent=4)        
        return infom_dict
    
    def getLocations(self):
        infom_dict = self.getManifestData(show=False)        
        return infom_dict['location']
    
    def getInputs(self, show=False):
        locations = self.getLocations()
        input_data = {}
        for k, v in locations.items():
            rw = readWrite.ReadWrite()        
            rw.file_path = v   
            current_data = rw.read(all=False)            
            input_data.setdefault(k, current_data)        
        if show:
            print json.dumps(input_data, indent=4)
            print json.dumps(locations, indent=4) 
        return input_data
                
        
        
        
            
