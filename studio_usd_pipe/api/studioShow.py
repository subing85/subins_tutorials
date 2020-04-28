import os
import glob
import json
import copy
import threading
import subprocess

from studio_usd_pipe import resource
from studio_usd_pipe.core import common


class Show(object):
    
    def __init__(self, show=None):
        self.show = show
        self.format = resource.getPresetFormat()
        self.preset_path = resource.getShowPresetPath()

    def get_show_configure_data(self):        
        data = resource.getShowConfigureData()
        return data
    
    def get_presets(self):
        presets = glob.glob('%s/*%s' % (self.preset_path, self.format))
        return presets
        
    def get_preset_data(self):  
        # include all show presets with common application data
        preset_data = {}        
        presets = self.get_presets()
        if not presets:
            return preset_data
        common_applications_data = self.get_common_applications()            
        for preset in presets:
            data = resource.getInputData(preset)
            current_show = data['current_show']['show']['long_name']
            preset_data.setdefault(current_show, data)
            # add new bash key to each show applications            
            for each_application in data['show_applications']:
                version = data['show_applications'][each_application]['version']
                bash_path = resource.getBinApplicationPath(current_show, version)
                data['show_applications'][each_application]['bash'] = bash_path
            data['common_applications'] = common_applications_data
        return preset_data
    
    def get_show_preset_data(self, current_show):
        # duplicate and merge show short name to preset data               
        preset_data = self.get_preset_data()
        merge_data = copy.deepcopy(preset_data)    
        for content in preset_data:
            name = preset_data[content]['current_show']['show']['show_name']
            merge_data.setdefault(name.encode(), preset_data[content])
        if current_show not in merge_data:
            print '#warnings: not found show <%s> in the preset' % current_show
            return None
        return merge_data[current_show]
    
    def get_application_versions(self, current_show): 
        versions = {}               
        data = self.get_show_preset_data(current_show)
        if not data:
            return versions
        for application in ['show_applications', 'common_applications']:
            for each in data[application]:
                contents = {
                    'long_name': data[application][each]['version'],
                    'application_type': application
                    }
                versions.setdefault(each, contents)
        return versions
    
    def get_current_application(self, current_show, application):
        versions = self.get_application_versions(current_show)
        if application in versions:
            return application, versions[application]['application_type']    
        for name, contents in versions.items():
            if contents['long_name'] != application:
                continue
            return name, contents['application_type']  
        return None, None
    
    def get_applications_data(self):
        applications_data = resource.getApplicationsData() 
        return applications_data['applications']
    
    def get_applications_versions(self):
        versions = {} 
        data = self.get_applications_data() 
        if not data:
            return versions
        for each in data:
            versions.setdefault(
                each,
                data[each]['version']
                )
        return versions
    
    def get_application(self, application):
        versions = self.get_applications_versions()
        if application in versions:
            return application        
        for k, v in versions.items():
            if v != application:
                continue
            return k
        return None

    def get_common_applications(self):
        common_applications_path = resource.getCommonApplicationsPath()
        module_data = common.get_modules(
            common_applications_path, module_types=['common_application'])
        if not module_data:
            return None
        if 'common_application' not in module_data:
            return None
        application_data = {}                
        for order, module in module_data['common_application'].items():
            module_path = os.path.join(module.__path__[-1], 'main.sh')
            if not os.path.isfile(module_path):
                continue
            contents = {
                "exe": module_path,
                'bash': module_path,
                "path": os.path.dirname(module_path),
                "version": '%s%s' % (module.KEY, module.VERSION),
                "order": order,
                "icon": os.path.join(resource.getIconPath(), module.ICON)              
                }
            application_data.setdefault(module.KEY, contents)
        return application_data
        
    def get_shows(self, preset_data=None, verbose=True):
        if not preset_data:
            preset_data = self.get_preset_data()
        if not preset_data:
            return None
        current_shows = {}
        for each_show in preset_data:
            current_show = preset_data[each_show]['current_show']
            show_names = [
                current_show['show']['show_name'].encode(),
                current_show['show']['long_name'].encode()
                ]
            current_shows.setdefault(current_show['show']['order'], show_names)
        if verbose:
            print json.dumps(current_shows, indent=4)
        return current_shows
    
    def get_flatten_shows(self, preset_data=None):
        if not preset_data:
            preset_data = self.get_preset_data()
        current_shows = self.get_shows(preset_data=preset_data, verbose=False)
        if not current_shows:
            return None
        flatten_shows = sum(current_shows.values(), [])
        return flatten_shows
                
    def get_next_order(self):
        current_shows = self.get_shows(verbose=False)
        if not current_shows:
            return 0
        return len(current_shows)
        
    def create_bin_show_application(self, current_show, application, application_path, force=False): 
        application_template = resource.getApplicationTemplatePath()
        if not os.path.isfile(application_template):
            print '#warnings: not found application template <%s>' % application_template
            return False
        bin_path = resource.getBinApplicationPath(current_show, application)
        valid = True
        if os.path.isfile(bin_path):
            if not force:
                print '#warnings: already found <%s>' % application  
                return False
            try:
                os.chmod(bin_path, 0777)
                os.remove(bin_path)
                valid = True
            except Exception as error:
                valid = False
                print '#error: ', error
        if not valid:            
            return False
        input_data = resource.getData(application_template)  
        search = 'echo \'application.exe %s\'' % resource.getIdentityKey()
        if search not in input_data:
            print '\n', application_template
            print '#warnings: not found identity key word <%s>' % search  
            return False
        replaced_data = input_data.replace(search, application_path)
        if not os.path.isdir(os.path.dirname(bin_path)):
            os.makedirs(os.path.dirname(bin_path))
        with open(bin_path, 'w') as file:
            data = file.write(replaced_data)
            os.chmod(bin_path, 0o777)
            print '#info: successfully registered studio pipe application <%s>' % application
            return True
        return False
        
    def create_show_preset(self, label, input_data):
        show_contents = input_data['current_show']['show']
        exists_shows = self.get_flatten_shows()
        if exists_shows:
            if show_contents['long_name'] in exists_shows:
                return False, show_contents['long_name'], 'already exists'
            if show_contents['show_name'] in exists_shows:
                return False, show_contents['show_name'], 'already exists' 
        # update input data
        template_header = common.get_template_header()
        template_header['modified'] = common.get_modified_date()
        template_header['description'] = 'show configure preset'
        template_header['enable'] = True
        template_header['type'] = 'show_config'
        template_header['data'] = input_data
        if not os.path.isdir(self.preset_path):
            os.makedirs(self.preset_path)
        path = os.path.join(
            self.preset_path, '%s%s' % (label, self.format))
        if os.path.isfile(path):
            return False, path, 'already exists' 
        # create preset
        with (open(path, 'w')) as preset:
            preset.write(json.dumps(template_header, indent=4))
        # create bin application batch
        valids = []    
        for application in input_data['show_applications']:
            version = input_data['show_applications'][application]['version']
            exe_path = input_data['show_applications'][application]['exe']
            valid = self.create_bin_application(show_contents['long_name'], version, exe_path, force=True)
            valids.append(valid)
        if False in valids:
            return False, 'create application', 'failed!...'
        return True, path, 'done!...'
    
    def set_environ(self, input_data):        
        for k, v in input_data.items():
            value = v
            if isinstance(v, list):
                value = ':'.join(v)
            else:
                value = str(v)
            if os.getenv(k.upper()):
                value = os.environ[k.upper()] + ':' + str(value)                
            os.environ[k.upper()] = value
    
    def launch(self, current_show, application_type, current_application, contents=None, thread=True):
        if not contents:
            contents = self.get_show_preset_data(current_show)
        current_application_contents = contents[application_type][current_application]
        self.set_environ(contents['current_show']['show'])  # set show environments        
        self.set_environ(current_application_contents)  # set current show_application environments     
        bash_path = current_application_contents['bash']
        if not os.path.isfile(bash_path):
            print "#error: not found", bash_path
            return
        if not thread:        
            self.execute_command(bash_path)
            return
        self.thread_state = threading.Condition()
        self.palyThread = threading.Thread(target=self.execute_command, args=([bash_path]))
        self.palyThread.daemon = True
        self.palyThread.start()
        
    def execute_command(self, command):
        popen = subprocess.Popen(
            [command], shell=False, stdout=subprocess.PIPE)
        popen_result = popen.stdout.readlines()        
        communicate = popen.communicate()   

