import os
import stat
import json
import time
import logging
import warnings
import pkgutil
import shutil

from crowd import resource
from crowd import utils
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

    def orders(self):
        data = [
            'skeleton',
            'puppet'
        ]
        return data

    def getDependencies(self):
        data = {
            'skeleton': 'skeleton',
            'puppet': 'skeleton'
        }
        return data

    def getDependency(self):
        data = self.getDependencies()
        if self.type not in data:
            logging.warning('not found any Dependency <%s>!...' % self.type)
            return None
        return data[self.type]

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
            if not hasattr(each_module, 'VALID'):
                continue
            if not hasattr(each_module, 'MODULE_TYPE'):
                continue
            if each_module.MODULE_TYPE != self.type:
                continue
            if not hasattr(each_module, 'BUNDLE_TYPE'):
                continue
            if valid:
                if not each_module.VALID:
                    continue
                current_module = each_module
            else:
                current_module = each_module
            if not current_module:
                continue
            bundle_type = each_module.BUNDLE_TYPE
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
            result, data, message = module.execute()
        except Exception as except_error:
            result, data, message = 'runtime error', [], str(except_error)
        value = self.bundle_value[result][1]
        color = self.bundle_value[result][0]
        return result, value, color, data, message

    def get_root_directory(self):
        return self.directory

    def get_type_directory(self):
        return os.path.join(self.directory, self.type)

    def get_tag_directory(self, current_tag=None):
        if current_tag:
            return os.path.join(self.directory, self.type, current_tag)
        return os.path.join(self.directory, self.type, self.tag)

    def commit(self):
        '''
            :description stroe pulish information to database        
        '''
        source = os.path.join(
            self.directory,
            self.type,
            self.tag
        )
        db = database.Connect(table=self.type)        
        if self.isExists():
            result = self.removeOriginData(self.tag)
            if not result:
                return False, 'Not able to remove <%s>'%self.tag
            result, message = db.overwrite(tag=self.tag, manifest=source)
        else:
            result, message = db.insert(tag=self.tag, manifest=source)
        return result, message

    def push(self, extract_bundle=None, comment=None, description=None, remote=None):
        '''
            :param data <dict>
            :param name <str>
            :param comment <str> optional
            :param description <str> optional
            :param valid <str> optional
            :param format <str> optional
        '''
        current_time = time.time()
        rw = readWrite.Connect(
            co=comment,
            de=description,
            fm=self.format,
            pa=self.directory,
            ty=self.type,
            tg=self.tag)

        components = {}
        for data, name in extract_bundle:
            rw.name = name
            write_file = rw.write(data, force=True, c_time=current_time)
            components.setdefault(name, write_file)
            os.chmod(write_file, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)

        origin_directory = os.path.join(
            self.directory, self.type, self.tag, 'scene%s' % os.path.splitext(remote)[-1])

        rw = readWrite.Connect(
            co=comment,
            de=description,
            fm='man',
            pa=self.directory,
            ty=self.type,
            tg=self.tag,
            cp=components.keys(),
            lo=components,
            rm=remote,
            na='manifest',
            og=origin_directory
        )
        manifest = rw.make_manifest(force=True, c_time=current_time)
        os.chmod(manifest, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        scene_file = self.pushScene(
            remote, origin_directory, current_time, force=True)
        os.chmod(scene_file, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        
    def pushScene(self, remote, origin_directory, current_time, force=False):
        if not force:
            if os.path.isfile(origin_directory):
                warnings.warn(
                    'already exists the file called %s' % origin_directory,
                    Warning
                )
                return
        if force:
            self.removeFile(origin_directory)                        
        shutil.copy2(remote, origin_directory)
        os.utime(origin_directory, (current_time, current_time))
        return origin_directory

    def getTypes(self):
        db = database.Connect()
        tables = db.get_tables()
        return tables

    def getTables(self):
        db = database.Connect(table=self.type)
        tags = db.get_columns()
        return tags

    def getDatas(self):
        db = database.Connect(table=self.type)
        data = db.select()
        return data

    def getData(self):
        data = self.getDatas()
        if not data:
            return None
        for each in data:
            if self.tag not in each:
                continue
            return each

    def getSpecificDatas(self, key):
        data = self.getDatas()
        if not data:
            return None
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
        rw = readWrite.Connect()
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
            rw = readWrite.Connect()
            rw.file_path = v
            current_data = rw.read(all=False)
            input_data.setdefault(k, current_data)
        if show:
            print json.dumps(input_data, indent=4)
            print json.dumps(locations, indent=4)
        return input_data

    def isExists(self, tag=None):
        if not tag:
            tag = self.tag
        tags = self.getTags()
        if tags:
            if tag in tags:
                return True
        return False

    def removeOriginData(self, tag):
        origin_directory = self.get_tag_directory(current_tag=tag)
        if not os.path.isdir(origin_directory):
            logging.warning('Not found directory <%s>' % origin_directory)
            return True
        result = True
        try:
            os.chmod(origin_directory, 0777)
        except Exception as error:
            logging.warning('\n#%s' % error)
        try:
            shutil.rmtree(origin_directory)
            result = True
        except Exception as error:
            logging.warning(str(error))
            result = False
        if not result:
            warnings.warn(
                '# OSError: Not able to remove directory <%s>' % origin_directory,
                Warning
            )
            return
        logging.info('#Successfully removed <%s>' % origin_directory)
        return result
    
    def removeFile(self, directory):
        if not os.path.isfile(directory):
            return
        try:
            os.chmod(directory, 0777)
            os.remove(directory)
        except Exception as result:
            warnings.warn(str(result), Warning)
            return False
        return True        
