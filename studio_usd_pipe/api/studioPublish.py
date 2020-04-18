import json

import os
import ast
import copy
import time
import shutil
import getpass
import tempfile
import subprocess

from datetime import datetime
from distutils import version


from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import publish
from studio_usd_pipe.core import database
from studio_usd_pipe.core import preferences


reload(publish)
reload(database)


class Publish(object):
    
    def __init__(self, standalone=False, pipe=None, subfield=None):
        self.standalone = standalone
        self.subfield = subfield    
        pref = preferences.Preferences()
        input_dirname = pref.get() 
        self.show_path = input_dirname['show_directory']
        self.mayapy_path = input_dirname['mayapy_directory']  
        self.stamped_time = time.time()
        self.identity_key = '##..##'
        self.container = {}
        self.parameters = {}
        
        if not pipe:        
            self.pipe, self.pipe_data = self.get_pipe_data()
        else:
            self.pipe = pipe
            self.pipe_data = resource.getPipeData()['pipe'][pipe]
        
        self.dbs = database.DataBase(self.pipe)
        
        # print self.pipe
        # print json.dumps(self.pipe_data, indent=4) 
        # print json.dumps(self.pipe_data.keys(), indent=4) 
       
    def has_valid_subfield(self):
        if not self.pipe_data:
            return True
        return False
        
    def get_pipe_data(self):
        pipe_data = resource.getPipeData()
        current_pipe = None
        for pipe, contents in pipe_data['pipe'].items():            
            for each in contents['subfield']['values']:                
                if each!=self.subfield:
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
                'date': contents['date'],
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
            if k!=subfield:
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
        for asset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    specific_key = subfields[subfield][version][key]                    
                    if specific_key in key_data:                    
                        if asset in key_data[specific_key]:
                            continue                    
                    key_data.setdefault(specific_key, []).append(asset)
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
        for asset, subfields in db_data.items():
            for subfield in subfields:
                for version in subfields[subfield]:
                    if key not in subfields[subfield][version]:
                        continue
                    specific_key = subfields[subfield][version][key]
                    if asset not in key_data:
                        key_data.setdefault(asset, [])
                    if specific_key in key_data[asset]:
                        continue
                    key_data.setdefault(asset, []).append(specific_key)
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
        extrude = ['caption', 'tag', 'user', 'date', 'location', 'type']
        for each in data:
            if each not in extrude:
                continue
            sorted_data.pop(each)
        return sorted_data

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
    
    
    def _get_publish_path(self, caption, version):
        publish_path = os.path.join(
            self.show_path,
            self.pipe,
            caption,
            self.subfield,
            version
            )
        return publish_path
    
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
        if os.path.isdir(publish_path):
            try:
                os.chmod(publish_path, 0777)
            except Exception as error:
                print '# warnings', error
            try:
                shutil.rmtree(publish_path)   
            except Exception as error:
                print '# warnings', error
        os.makedirs(publish_path)
        return publish_path
    
    
    
    
    def validate(self, repair=False, **kwargs):
        valid, message = self.run('validator', repair=repair, **kwargs)
        return valid, message
    
    def extract(self, repair=False, **kwargs):
        valid, message = self.run('extractor', repair=repair, **kwargs)
        self.parameters = kwargs
        return valid, message
    
    def release(self):    
        data, message = self.get_extracted_data()
        if not data:
            return data, message
        publish_path = self.get_publish_path(
            self.parameters['caption'], self.parameters['version'], temp=False, create=True)
        
        print '\npublish_path', publish_path, '\n\n'
                
        result = self.move_to_publish(data, publish_path)
        
        return
            
        if not result:
            return        
        date = time.strftime('%Y/%d/%B - %I/%M/%S/%p', time.gmtime(self.time_stamp))
        kwargs = {
            'caption': {
                'value': self.caption,
                'order': 0
                },
            'version': {
                'value': self.version,
                'order': 1
                },
            'subfield': {
                'value': self.subfield,
                'order': 2
                },
            'type': {
                'value': self.type,
                'order': 3
                },
            'tag': {
                'value': self.tag,
                'order': 4
                },
            'date': {
                'value': date,
                'order': 5
                },
            'location': {
                'value': self.publish_path,
                'order': 6
                }
            } 
        self.dbs.create(kwargs)
    
    def move_to_publish(self, data, publish_path):
        ['/tmp/test_show/assets/batman/model/3.0.0/man.txt' ]   
        for each in data:
            print each
            print publish_path, '\n'
        
        
        #=======================================================================
        # for each in data:
        #     if not self.data[key]:
        #         continue
        #     for each in self.data[key]:
        #         if not each:
        #             continue
        #         path = each.replace(temp_pack_path, self.publish_path)
        #         if os.path.isdir(each):
        #             if not os.path.isdir(path):
        #                 os.makedirs(path)
        #                 self.set_time_stamp(path)
        #         if os.path.isfile(each):                 
        #             if not os.path.isdir(os.path.dirname(path)):
        #                 os.makedirs(os.path.dirname(path))
        #             try:            
        #                 shutil.copy2(each, path)
        #             except Exception as IOError:
        #                 print IOError
        #                 return False
        #=======================================================================
        return True
    
            
    
    
    
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
                print '%s: '%module.KEY.rjust(15), contents[1]
                messages.append('%s: %s'%(module.KEY, contents[1]))
            return False, '\n'.join(messages)
        return True, 'success!..'
    
    def python_run(self, mode, output_path, repair=False, open_maya=False, **kwargs):    
        '''
        :param mode <str> 'validator' or 'extractor'
        '''    
        if open_maya: # open maya file
            from studio_usd_pipe.api import studioMaya
            smaya = studioMaya.Maya()
            smaya.open_maya(kwargs['source_maya'], None)        
        core_publish = publish.Publish(self.subfield)
        temp, self.container = core_publish.execute(mode, output_path, repair=repair, **kwargs)
        
        if self.standalone:
            print self.identity_key, self.container # do not remove, important line
            
        return self.container 
    
    def mayapy_run(self, mode, output_path, repair=False, open_maya=False, **kwargs):
        argeuments = common.make_argeuments(**kwargs)        
        commands = [
            'from studio_usd_pipe.api import studioPublish',
            'pub=studioPublish.Publish(standalone=True,pipe=\'%s\',subfield=\'%s\')'%(self.pipe, self.subfield),
            'container=pub.python_run(\'%s\',\'%s\',repair=%s,open_maya=%s,%s)'%(
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
        data = []     
        for name in self.container[True]:        
            for input in self.container[True][name][0]:
                if not os.path.exists(input):
                    continue
                os.utime(input, (self.time_stamp, self.time_stamp))                    
                data.append(input)
        if not data:
            False, 'not extracted any data!...'            
        return data, 'success!...'
                
        




        


    
    def _release(self, bundle, *kwargs):
        print json.dumps(bundle, indent=4)
        self.data = {}
        self.source_maya = bundle['source_file']
        self.caption = bundle['caption']
        self.version = bundle['version'] 
        self.thumbnail = None
        if 'thumbnail' in bundle:
            self.thumbnail = bundle['thumbnail']
        self.type = bundle['type']
        self.tag = bundle['tag']
        self.description = bundle['description']   
        self.time_stamp = bundle['time_stamp'] 
        
        self.publish_path = os.path.join(
            self.show_path,
            self.entity,
            self.caption,
            self.subfield,
            self.version
            )      
    

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
        

            
            
            

            
    def collect_packed(self):        
        if not self.publish_path:
            self.publish_path = self.get_pulish_path()
        self.packed_bundle = {
            'caption': self.bundle['caption'],
            'version': self.bundle['version'],
            'type': self.bundle['type'],
            'tag': self.bundle['tag'],
            'subfield': self.bundle['subfield'],
            'thumbnail': self.bundle['thumbnail'],
            'description': self.bundle['description'],
            'time_stamp': self.stamped_time,
            'user': getpass.getuser(),
            # 'date': time.strftime('%Y/%d/%B - %I/%M/%S/%p', time.gmtime(self.stamped_time)),
            'source_file': self.bundle['source_file'],
            'show_path': self.show_path,
            'mayapy': self.mayapy_path,
            'publish_path': self.publish_path        
            }
        return self.packed_bundle



#===============================================================================
# inputs = {
#     'description': 'test', 
#     'subfield': 'model', 
#     'caption': 'batman', 
#     'tag': 'character', 
#     'version': '3.0.0', 
#     'type': 'non-interactive', 
#     'thumbnail': 'path'
#     }
#      
# pipe = 'assets'
# subfield = inputs['subfield']
# pub = Publish(pipe=pipe, subfield=subfield)
#      
# pub.validate(repair=True, **inputs)  
#===============================================================================
 

