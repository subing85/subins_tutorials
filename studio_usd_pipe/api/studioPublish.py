import json

import os
import ast
import copy
import time
import shutil
import getpass
import tempfile
import warnings
import subprocess

from datetime import datetime
from distutils import version

from studio_usd_pipe import resource
from studio_usd_pipe.core import asset
from studio_usd_pipe.core import common
from studio_usd_pipe.core import publish
from studio_usd_pipe.core import database
from studio_usd_pipe.core import preferences

reload(publish)
reload(database)
reload(asset)


class Publish(object):
    
    def __init__(self, standalone=False, pipe=None, subfield=None):
        self.standalone = standalone
        self.subfield = subfield    
        pref = preferences.Preferences()
        input_dirname = pref.get() 
        self.show_path = input_dirname['show_directory']
        self.mayapy_path = input_dirname['mayapy_directory']  
        self.time_stamp = time.time()
        self.identity_key = '##..##'
        self.container = {}
        self.parameters = {}
        if not pipe:        
            self.pipe, self.pipe_data = self.get_pipe_data()
        else:
            self.pipe = pipe
            self.pipe_data = resource.getPipeData()['pipe'][pipe]
        self.dbs = database.DataBase(self.pipe)
       
    def has_valid_subfield(self):
        if not self.pipe_data:
            return True
        return False
        
    def get_pipe_data(self):
        pipe_data = resource.getPipeData()
        current_pipe = None
        for pipe, contents in pipe_data['pipe'].items():            
            for each in contents['subfield']['values']:                
                if each != self.subfield:
                    continue
                current_pipe = pipe
        if not current_pipe:
            return None, None
        return current_pipe, pipe_data['pipe'][current_pipe]
    
    def get(self):
        data = self.dbs.get()        
        db_data = {}
        for table, contents in data.items():  
            keys = {
                'tag': contents['tag'],
                'caption': contents['caption'],
                'user': contents['user'],
                'modified': contents['modified'],
                'location': contents['location'],
                'type': contents['type']        
                }
            if contents['caption'] not in db_data:
                db_data.setdefault(contents['caption'], {})
            if contents['subfield'] not in db_data[contents['caption']]:
                db_data[contents['caption']].setdefault(contents['subfield'], {}) 
            db_data[contents['caption']][contents['subfield']].setdefault(
                contents['version'], keys)
        return db_data        
    
    def get_subfields(self, caption, db_data=None):
        if not db_data:
            db_data = self.get()
        subfield_data = {}
        if caption in db_data:
            subfield_data = db_data[caption]
        return subfield_data
    
    def get_version_data(self, caption, subfield=None, db_data=None):
        if not subfield:
            subfield = self.subfield
        subfield_data = self.get_subfields(caption, db_data=db_data)
        version_data = {}
        for k, v in subfield_data.items():    
            if k != subfield:
                continue        
            version_data.update(v)        
        return version_data
    
    def get_versions(self, caption, subfield=None, db_data=None):
        if not subfield:
            subfield = self.subfield        
        version_data = self.get_version_data(caption, subfield=subfield, db_data=db_data)
        versions = version_data.keys()        
        versions.sort(key=version.StrictVersion)
        versions.reverse()    
        return versions    

    def get_version_contents(self, caption, version, subfield=None, db_data=None):
        if not subfield:
            subfield = self.subfield   
        data = self.get_subfields(caption, db_data=db_data)
        if subfield not in data:
            raise ValueError(
                'Not found <{}> in the database'.format(subfield))
        if version not in data[subfield]:
            raise ValueError(
                'Not found <{} {}> in the database'.format(subfield, version))
        return data[subfield][version]

    def get_specific_key_captions(self, key, db_data=None):
        if not db_data:
            db_data = self.get()
        key_data = {}
        for sasset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    specific_key = subfields[subfield][version][key]                    
                    if specific_key in key_data:                    
                        if sasset in key_data[specific_key]:
                            continue                    
                    key_data.setdefault(specific_key, []).append(sasset)
        return key_data   

    def get_type_caption(self, db_data=None):
        type_data = self.get_specific_key_captions('type', db_data=db_data)
        return type_data   

    def get_tag_caption(self, db_data=None):
        tag_data = self.get_specific_key_captions('tag', db_data=db_data)
        return tag_data
       
    def get_specific_captions_key(self, key, db_data=None):
        if not db_data:
            db_data = self.get()
        key_data = {}
        for sasset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    if key not in subfields[subfield][version]:
                        continue
                    specific_key = subfields[subfield][version][key]
                    if sasset not in key_data:
                        key_data.setdefault(sasset, [])
                    if specific_key in key_data[sasset]:
                        continue
                    key_data.setdefault(sasset, []).append(specific_key)
        return key_data
    
    def get_caption_type(self, db_data=None):
        type_data = self.get_specific_captions_key('type', db_data=db_data)
        return type_data        

    def get_caption_tag(self, db_data=None):
        type_data = self.get_specific_captions_key('tag', db_data=db_data)
        return type_data    
    
    def get_asset_more_data(self, caption, version, subfield=None):
        if not subfield:
            subfield = self.subfield   
        manifest_path = os.path.join(
            self.show_path,
            self.pipe,
            caption,
            subfield,
            version,
            '{}.manifest'.format(caption)
            )
        data = resource.get_input_data(manifest_path)
        sorted_data = copy.deepcopy(data)
        extrude = ['caption', 'tag', 'user', 'modified', 'location', 'type']
        for each in data:
            if each not in extrude:
                continue
            sorted_data.pop(each)
        return sorted_data
    
    def get_dependencies(self, caption, db_data=None):
        if not db_data:
            db_data = self.get()        
        dependencies = self.get_versions(
            caption, subfield='model', db_data=db_data)
        dependencies = ['None'] + dependencies
        return dependencies
    
    def get_dependency(self, caption, subfild):
        pass
    

    def get_latest_version(self, caption, subfield=None):
        if not subfield:
            subfield = self.subfield          
        versions = self.get_versions(caption, subfield=subfield)
        if not versions:
            return None
        return versions[0]
     
    def get_next_version(self, caption, index, subfield=None, latest_version=None):
        '''
            index 0, 1, 2 = MAJOR0, MINOR, PATCH
        '''
        if not latest_version:
            latest_version = self.get_latest_version(caption, subfield=subfield)
        if not latest_version:
            return '0.0.0'
        major, minor, patch = latest_version.split('.')
        if index == 0:
            n_version = '{}.{}.{}'.format(int(major) + 1, 0, 0)
        if index == 1:
            n_version = '{}.{}.{}'.format(major, int(minor) + 1, 0)
        if index == 2:
            n_version = '{}.{}.{}'.format(major, minor, int(patch) + 1)
        return n_version
    
    def get_publish_path(self, caption, version, temp=True, create=True):
        dirname = os.path.join(tempfile.gettempdir(), 'test_show')        
        if not temp:
            dirname = self.show_path
        publish_path = os.path.join(
            dirname,
            self.pipe,
            caption,
            self.subfield,
            version
            )
        if not create:
            return publish_path
        common.remove_directory(publish_path)
        os.makedirs(publish_path)
        return publish_path  
    
    def make_inputs(self, **kwargs):        
        publish_path = self.get_publish_path(
            kwargs['caption'], kwargs['version'], temp=False, create=False)
        dt_object = datetime.fromtimestamp(self.time_stamp)
        modified = dt_object.strftime('%Y:%d:%B-%I:%M:%S:%p') 
        inputs = {
            'pipe': self.pipe,
            'caption': kwargs['caption'],
            'subfield': kwargs['subfield'],
            'version': kwargs['version'],
            'type': kwargs['type'],
            'tag': kwargs['tag'],
            'dependency': kwargs['dependency'],
            'thumbnail': kwargs['thumbnail'],
            'description': kwargs['description'],
            'modified': modified,
            'user': getpass.getuser(),
            'source_maya': kwargs['source_maya'],
            'show_path': self.show_path,
            'mayapy': self.mayapy_path,
            'location': publish_path       
            }
        return inputs
    
    def validate(self, repair=False, **kwargs):
        '''
            from studio_usd_pipe.api import studioPublish
            reload(studioPublish)
            inputs = {
                'description': 'test', 
                'subfield': 'model', 
                'caption': 'batman', 
                'tag': 'character', 
                'version': '3.0.0', 
                'type': 'non-interactive', 
                'thumbnail': 'path',
                'source_maya': '/venture/shows/assets/batman/batman_0.0.3.mb'
                }
            pipe = 'assets'
            subfield = inputs['subfield']
            pub = studioPublish.Publish(pipe=pipe, subfield=subfield)  
            pub.validate(repair=True, **inputs)  
        '''
        inputs = self.make_inputs(**kwargs)
        valid, message = self.run('validator', repair=repair, **inputs)
        return valid, message
    
    def extract(self, repair=False, **kwargs):
        '''
            from studio_usd_pipe.api import studioPublish
            reload(studioPublish)
            inputs = {
                'description': 'test', 
                'subfield': 'model', 
                'caption': 'batman', 
                'tag': 'character', 
                'version': '3.0.0', 
                'type': 'non-interactive', 
                'thumbnail': 'path',
                'source_maya': '/venture/shows/assets/batman/batman_0.0.3.mb'
                }
            pipe = 'assets'
            subfield = inputs['subfield']
            pub = studioPublish.Publish(pipe=pipe, subfield=subfield)  
            pub.extract(**inputs)          
        '''
        inputs = self.make_inputs(**kwargs)
        valid, message = self.run('extractor', repair=repair, **inputs)
        extracted_data = self.get_extracted_data()        
        inputs.update(extracted_data)
        manifest = self.extract_manifest(**inputs)       
        inputs['manifest'] = manifest
        self.parameters = inputs
        return valid, message
    
    def extract_manifest(self, **kwargs):
        temp_publish_path = self.get_publish_path(
            kwargs['caption'], kwargs['version'], temp=True, create=False)
        temp_manifest = os.path.join(temp_publish_path, '%s.manifest' % kwargs['caption'])
        manifest = asset.create_asset_manifest(temp_manifest, **kwargs)
        self.container[True]['manifest'] = [[manifest], 'success']  
        return manifest

    def run(self, mode, repair=False, **kwargs):    
        temp_publish_path = self.get_publish_path(
            kwargs['caption'], kwargs['version'], temp=True, create=True)
        if self.standalone:
            self.mayapy_run(mode, temp_publish_path, repair=repair, open_maya=True, **kwargs)
        else:
            self.python_run(mode, temp_publish_path, repair=repair, open_maya=False, **kwargs)
            
        if False in self.container:
            messages = []            
            print '#warnings'
            for module, contents in self.container[False].items():
                print '%s: ' % module.rjust(15), contents[1]
                messages.append('%s: %s' % (module, contents[1]))
            return False, '\n'.join(messages)
        return True, 'success!..'
    
    def python_run(self, mode, output_path, repair=False, open_maya=False, **kwargs):    
        '''
        :param mode <str> 'validator' or 'extractor'
        '''    
        if open_maya:  # open maya file
            from studio_usd_pipe.api import studioMaya
            smaya = studioMaya.Maya()
            smaya.open_maya(kwargs['source_maya'], None)        
        core_publish = publish.Publish(self.subfield)
        temp, self.container = core_publish.execute(mode, output_path, repair=repair, **kwargs)
        if self.standalone:
            print self.identity_key, self.container  # do not remove, important line
        return self.container 
    
    def mayapy_run(self, mode, output_path, repair=False, open_maya=False, **kwargs):
        argeuments = common.make_argeuments(**kwargs)        
        commands = [
            'from studio_usd_pipe.api import studioPublish',
            'pub=studioPublish.Publish(standalone=True,pipe=\'%s\',subfield=\'%s\')' % (self.pipe, self.subfield),
            'container=pub.python_run(\'%s\',\'%s\',repair=%s,open_maya=%s,%s)' % (
                mode, output_path, repair, open_maya, argeuments)
            ]
        batch_path = common.make_maya_batch(
            'spublish', self.mayapy_path, commands, source_path=None)
        popen = subprocess.Popen(
            [self.mayapy_path, '-s', batch_path], shell=False, stdout=subprocess.PIPE)
        popen_result = popen.stdout.readlines()
        communicate = popen.communicate()
        if not popen_result:
            return False, 'failed'
        spack_return = None
        for each in popen_result:            
            if self.identity_key in each:
                spack_return = each.split('##..##')[-1]
                continue
            print each.replace('\n', '')
        if not spack_return:
            return False, 'failed'        
        self.container = ast.literal_eval(spack_return.strip())
        return self.container    
     
    def get_extracted_data(self):
        if True not in self.container:
            return False, 'failed!...'        
        if False in self.container:
            return False, 'found packing (extract) error!...'        
        data = {}    
        for name in self.container[True]:        
            for input in self.container[True][name][0]:
                if isinstance(input, unicode):
                    input = input.encode()
                if not isinstance(input, str):
                    continue
                input = input.encode()
                if not input:
                    continue
                if not os.path.exists(input):
                    continue
                data.setdefault(name, []).append(input)
        if not data:
            False       
        return data    
    
    def release(self):
        extracted_data = self.get_extracted_data()
        
        import json
        print '\n\nextracted_data..............'
        print json.dumps(extracted_data, indent=4)
        
        data = []        
        for contents in extracted_data:
            values = extracted_data[contents]
            if not values:
                continue
            for value in values:
                if not os.path.isfile(value):
                    continue
                data.append(value)
        valid = self.move_to_publish(data)
        if not valid:
            print '#warnings', 'deployed to publish failed!...'
            return False, 'deployed to publish failed!...'
        kwargs = {
            'caption': {
                'value': self.parameters['caption'],
                'order': 0
                },
            'version': {
                'value': self.parameters['version'],
                'order': 1
                },
            'subfield': {
                'value': self.parameters['subfield'],
                'order': 2
                },
            'type': {
                'value': self.parameters['type'],
                'order': 3
                },
            'tag': {
                'value': self.parameters['tag'],
                'order': 4
                },
            'dependency': {
                'value': self.parameters['dependency'],
                'order': 5
                },
            'modified': {
                'value': self.parameters['modified'],
                'order': 6
                },
            'location': {
                'value': self.parameters['location'],
                'order': 7
                },
            'user': {
                'value': self.parameters['user'],
                'order': 8
                }           
            } 
        self.dbs.create(kwargs)
        print '\n#header registered info'
        print 'pipe: '.rjust(15), self.parameters['pipe']
        print 'caption: '.rjust(15), self.parameters['caption']
        print 'subfield: '.rjust(15), self.parameters['subfield']
        print 'type: '.rjust(15), self.parameters['type']
        print 'tag: '.rjust(15), self.parameters['tag']
        print 'dependency: '.rjust(15), self.parameters['dependency']
        print 'location: '.rjust(15), self.parameters['location']
        print 'successfully registered publish'
        return True, 'successfully registered publish'

    def move_to_publish(self, data):
        common.remove_directory(self.parameters['location'])
        if not os.path.isdir(self.parameters['location']):
            os.makedirs(self.parameters['location'])
        valids = []
        for each in data:
            if not os.path.isfile(each):
                continue
            basename = each.rsplit(self.parameters['version'], 1)[-1]
            target = '%s%s' % (self.parameters['location'], basename)
            if not os.path.isdir(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            os.utime(each, (self.time_stamp, self.time_stamp)) 
            try:            
                shutil.copy2(each, target)
            except Exception as IOError:
                print '#warnings', IOError
                valids.append(False)
        if False in valids:
            return False           
        return True    

