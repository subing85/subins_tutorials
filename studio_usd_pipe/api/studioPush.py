import os
import ast
import copy
import time
import shutil
import getpass
import tempfile
import warnings
import subprocess

from distutils import version
from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import bundles
from studio_usd_pipe.core import database
from studio_usd_pipe.api import studioEnviron


class Push(object):
    
    def __init__(self, current_show, current_pipe):
        self.current_show = current_show
        self.current_pipe = current_pipe
        self.show_path = self.get_show_path()        
        self.time_stamp = time.time()
        self.container = {}
        self.parameters = {}        
    
    def get_show_path(self):
        environ = studioEnviron.Environ(self.current_show)
        show_path, valid = environ.get_environ_value('SHOW_PATH')
        return show_path
                  
    def get_publish_path(self, caption, subfield, version, temp=True, create=True):
        show_path = self.show_path        
        if temp:
            show_path = os.path.join(tempfile.gettempdir(), 'test_show')  
        publish_path = os.path.join(
            show_path,
            self.current_pipe,
            caption,
            subfield,
            version
            )
        if not create:
            return publish_path
        common.remove_directory(publish_path)
        os.makedirs(publish_path)
        return publish_path

    def make_inputs(self, **kwargs):               
        publish_path = self.get_publish_path(
            kwargs['caption'],
            kwargs['subfield'],
            kwargs['version'],
            temp=False,
            create=False
            )
        dt_object = datetime.fromtimestamp(self.time_stamp)
        modified = dt_object.strftime('%Y:%d:%B-%I:%M:%S:%p') 
        inputs = {
            'description': kwargs['description'],
            'standalone': kwargs['standalone'],
            'source': kwargs['source'],
            'subfield': kwargs['subfield'],
            'dependency': kwargs['dependency'],
            'application': kwargs['application'],
            'tag': kwargs['tag'],
            'version': kwargs['version'],
            'caption': kwargs['caption'],
            'type': kwargs['type'],
            'thumbnail': kwargs['thumbnail'],
            'user': getpass.getuser(),
            'modified': modified,
            'show_path': self.show_path,
            'location': publish_path,
            'show': self.current_show,
            'pipe': self.current_pipe,

            }
        #=======================================================================
        # example = {
        #     "application": "maya", 
        #     "description": "test", 
        #     "standalone": False, 
        #     "subfield": "model", 
        #     "show": "btm", 
        #     "modified": "2020:04:May-07:59:28:PM", 
        #     "pipe": "assets", 
        #     "source": "/venture/shows/assets/batman/batman_0.0.5.mb", 
        #     "show_path": "/venture/shows/batman", 
        #     "tag": "character", 
        #     "caption": "batman", 
        #     "user": "shreya", 
        #     "version": "5.0.0", 
        #     "dependency": "None", 
        #     "type": "interactive", 
        #     "thumbnail": "/usr/tmp/studio_pipe_temp_2020_04_May_Monday_07_59_24_PM.png", 
        #     "location": "/venture/shows/batman/assets/batman/model/5.0.0"
        # }
        #=======================================================================
        return inputs    

    def validate(self, repair=False, **kwargs):
        '''
            from studio_usd_pipe.api import studioPublish
            reload(studioPublish)
            inputs = {
                'description': 'test publish', 
                'dependency': 'None', 
                'subfield': 'model', 
                'caption': 'batman', 
                'tag': 'character', 
                'user': 'shreya', 
                'version': '8.0.0', 
                'type': 'interactive', 
                # 'thumbnail': '/venture/shows/icons/my_super_hero_rigging_.png',
                'source': '/venture/shows/batman/batman_0.0.3.mb'
                }
            pub = studioPublish.Publish(pipe='assets')  
            pub.validate(repair=True, **inputs)  
        '''
        input_data = self.make_inputs(**kwargs)
        valid, message = self.python_run('validator', repair=repair, **input_data)
        return valid, message          
           
    def extract(self, repair=False, **kwargs):
        inputs = self.make_inputs(**kwargs)
        valid, message = self.python_run('extractor', repair=repair, **inputs)
        extracted_data = self.get_extracted_data()
        manifest = self.extract_manifest(**inputs)    
        inputs.update(extracted_data)
        inputs['manifest'] = manifest
        self.parameters = inputs
        return valid, message           

    def extract_manifest(self, **kwargs):
        temp_publish_path = self.get_publish_path(
            kwargs['caption'],
            kwargs['subfield'],
            kwargs['version'],
            temp=True,
            create=False
            )
        publish_path = self.get_publish_path(
            kwargs['caption'],
            kwargs['subfield'],
            kwargs['version'],
            temp=False,
            create=False
            )
        # update temp show path to publish path                
        post_packed_data = self.get_post_packed_data(temp_publish_path, publish_path)
        kwargs.update(post_packed_data)
        extracted_thumbnail_key = '%s_thumbnail' % kwargs['subfield']
        if extracted_thumbnail_key in kwargs:
            # update the thumbnial from extracted data
            kwargs['thumbnail'] = kwargs[extracted_thumbnail_key][0]
        temp_manifest = os.path.join(temp_publish_path, '%s.manifest' % kwargs['caption'])
        manifest = common.create_manifest(temp_manifest, **kwargs)
        self.container[True]['manifest'] = [[manifest], 'success']
        return manifest
    
    def release(self):
        packing_data = self.get_packing_data()
        packing_data = sum(packing_data.values(), [])
        valid = self.move_to_publish(packing_data)
        if not valid:
            print '#warnings', 'deployed to spublish failed!...'
            return False, 'deployed to spublish failed!...'
        release_inputs = self.make_release_inputs()
        dbs = database.DataBase(self.current_show, self.current_pipe)
        dbs.create(release_inputs)
        print '\n#header registered info'
        sorted_data = common.sort_dictionary(release_inputs)
        for each in sorted_data:
            print '%s: '%each.rjust(15), release_inputs[each]['value']
        print 'successfully registered spublish'
        return True, 'successfully registered spublish'
    
    def make_release_inputs(self):
        keys = [
            'show',
            'pipe',
            'show_path',
            'application',
            'standalone',
            'caption',
            'version',
            'subfield',
            'type',
            'tag',
            'dependency',
            'modified',
            'location',
            'user'
            ]
        release_inputs = {}
        for index, key in enumerate(keys):
            if key not in self.parameters:
                continue
            parameter = {
                key : {
                    'value': self.parameters[key],
                    'order': index
                    }
                }
            release_inputs.update(parameter)
        return release_inputs

    def get_extracted_data(self):
        if True not in self.container:
            return False, 'failed!...'        
        if False in self.container:
            return False, 'found packing (extract) error!...'        
        extracted_data = {}
        container_instance = copy.deepcopy(self.container[True])
        for name in container_instance:
            stack = container_instance[name][0]    
            while stack:
                input = stack.pop()                         
                if isinstance(input, str) or isinstance(input, unicode):
                    if not os.path.exists(input):
                        continue
                    extracted_data.setdefault(name, []).append(input.encode())
                if isinstance(input, list):
                    stack.extend(input)
        if not extracted_data:
            False       
        return extracted_data    
    
    def get_packing_data(self):
        extracted_data = self.get_extracted_data()
        data = {}        
        for contents in extracted_data:
            values = extracted_data[contents]
            if not values:
                continue
            for value in values:
                if not os.path.isfile(value):
                    continue
                data.setdefault(contents, []).append(value)  
        return data
    
    def get_post_packed_data(self, search_for, replace_with):
        packing_data = self.get_packing_data()
        extracted_data = self.get_extracted_data()
        for contents in extracted_data:
            values = extracted_data[contents]        
        post_packed_data = copy.deepcopy(packing_data)
        for contents in packing_data:
            values = packing_data[contents]
            publish_paths = None
            if not values:
                continue
            if isinstance(values, list):
                publish_paths = []
                for value in values:
                    if not os.path.isfile(value):
                        continue
                    publish_paths.append(value.replace(search_for, replace_with))
            else:
                publish_paths = value.replace(search_for, replace_with)
            if not publish_paths:
                continue
            post_packed_data[contents] = publish_paths
        return post_packed_data
    
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
           
    def python_run(self, mode, repair=False, **kwargs):
        self.container = {}    
        temp_publish_path = self.get_publish_path(
            kwargs['caption'], kwargs['subfield'], kwargs['version'], temp=True, create=True)
        bundle = bundles.Bundles(kwargs['application'], 'push', kwargs['subfield'])
        temp, self.container = bundle.execute(mode, temp_publish_path, repair=repair, **kwargs)
        if not temp:
            return True, 'found any <%s> bundle' % mode
        if False in self.container:
            messages = []            
            print '#warnings'
            for module, contents in self.container[False].items():
                print '%s: ' % module.rjust(15), contents[1]
                messages.append('%s: %s' % (module, contents[1]))
            return False, '\n'.join(messages)
        return True, 'success!..' 
    
    def do_publish(self, repair=True, **kwargs):
        valid, message = self.validate(repair=True, **kwargs)
        if not valid:
            return valid, message
        valid, message = self.extract(repair=False, **kwargs)
        if not valid:
            return valid, message        
        valid, message = self.release()
        return valid, message        
    
    def do_standalone_publish(self, repair=True, **kwargs):
        application_module_path = resource.getModuleApplicationsPath()    
        module = common.get_subprocess_code(application_module_path, kwargs['application'])
        if not module:
            print '#warnings not found subprocess script for %s' % kwargs['application']
            return False, 'not found subprocess script'
        environ = studioEnviron.Environ(self.current_show)
        application_path, valid = environ.get_specific_environ_value(
            'show_applications', kwargs['application'], 'path')
        script_path = os.path.join(resource.getScriptPath(), 'maya/maya_release.py')
        kwargs['reapir'] = repair
        valid, message = module.execute(
            application_path, kwargs['source'], script_path, **kwargs)
        return valid, message
    
