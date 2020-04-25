import os
import glob
import json
import copy

from studio_usd_pipe import resource
from studio_usd_pipe.core import common


class Show(object):
    
    def __init__(self, show=None):
        self.show = show
        self.format = resource.getPresetFormat()
        self.package_path = resource.getPackagePath()
        self.package_name = resource.getPackageName()
        self.preset_path = os.path.join(
            self.package_path, self.package_name, 'presets/shows')

    def get_show_configure_data(self):        
        data = resource.getShowConfigureData()
        return data
    
    def get_presets(self):
        presets = glob.glob('%s/*%s' % (self.preset_path, self.format))
        return presets
        
    def get_preset_data(self):  # include all show presets
        presets = self.get_presets()
        if not presets:
            return None
        preset_data = {}
        for preset in presets:
            data = resource.getInputData(preset)
            preset_data.setdefault(
                data['current_show']['show']['long_name'], data)
        return preset_data
    
    def get_show_preset_data(self, show):                
        preset_data = self.get_preset_data()   
        merge_data = copy.deepcopy(preset_data)    
        for k, v in preset_data.items():
            merge_data.setdefault(v['show']['name'], v)
        if show not in merge_data:
            print '#warnings: not found show in the preset <%s>' % show
            return None
        return merge_data[show]
    
    def get_shows(self, preset_data=None, verbose=True):
        if not preset_data:
            preset_data = self.get_preset_data()
        if not preset_data:
            return None
        shows = {}
        for each_show in preset_data:
            current_show = preset_data[each_show]['current_show']
            show_names = [
                current_show['show']['name'],
                current_show['show']['long_name']
                ]
            shows.setdefault(current_show['show']['order'], show_names)
        if verbose:
            print json.dumps(shows, indent=4)
        return shows
    
    def get_flatten_shows(self, preset_data=None):
        if not preset_data:
            preset_data = self.get_preset_data()
        shows = self.get_shows(preset_data=preset_data, verbose=False)
        if not shows:
            return None
        flatten_shows = sum(shows.values(), [])
        return flatten_shows
                
    def get_next_order(self):
        shows = self.get_shows(verbose=False)
        if not shows:
            return 0
        return len(shows)
        
    def create_bin_tool(self, show, name, tool_path, force=False): 
        tool_template = os.path.join(
            resource.getTemplatePath(), 'tool_template.txt')
        bin_path = os.path.join(
            self.package_path, self.package_name, 'bin', show, name, 'main.sh')
        valid = True
        if os.path.isfile(bin_path):
            if not force:
                print '#warnings: already found <%s>' % name  
                return
            try:
                os.chmod(bin_path, 0777)
                os.remove(bin_path)
                valid = True
            except Exception as error:
                valid = False
                print '#error: ', error
                
        if not valid:            
            return 
        input_data = resource.getData(tool_template)  
        search = 'echo \'tool.exe %s\'' % resource.getIdentityKey()
        if search not in input_data:
            print '\n', tool_template
            print '#warnings: not found identity key word <%s>' % search  
            return
        replaced_data = input_data.replace(search, tool_path)
        if not os.path.isdir(os.path.dirname(bin_path)):
            os.makedirs(os.path.dirname(bin_path))
        with open(bin_path, 'w') as file:
            data = file.write(replaced_data)
            os.chmod(bin_path, 0o777)
            print '#info: successfully registered studio pipe tool <%s>' % name
            return True
        
    def create_show_preset(self, label, input_data):
        show_contents = input_data['current_show']['show']
        exists_shows = self.get_flatten_shows()
        if exists_shows:
            if show_contents['long_name'] in exists_shows:
                return False, show_contents['long_name'], 'already exists'
            if show_contents['name'] in exists_shows:
                return False, show_contents['name'], 'already exists' 
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
        for application in input_data['applications']:
            version = input_data['applications'][application]['version']
            exe_path = input_data['applications'][application]['exe']
            self.create_bin_tool(show_contents['long_name'], version, exe_path, force=True)
        return True, path, 'done!...'
    
    def launch(self, show, tool, contents=None):
        if not contents:
            contents = self.get_show_preset_data(show)
        # set show environments
        for k, v in contents['show'].items():
            value = v
            if isinstance(v, list):
                value = ':'.join(v)
            os.environ[k.upper()] = str(value)
                   
        # set tool environments
        for k, v in contents['tool'].items():
            value = v
            if isinstance(v, list):
                value = ':'.join(v)
            os.environ[k.upper()] = str(value)
        
        # create shell script
        shell_script = os.path.join(
                self.preset_path,
                self.package_name,
                'bin/tool/main.sh'
                )
        
        print shell_script
