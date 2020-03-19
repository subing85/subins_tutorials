import os
import json
import shutil
import getpass
import warnings

from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import image
from studio_usd_pipe.core import configure


class Preferences(object):
    
    def __init__(self):
        self.toolkit = 'subins-toolkits'
        self.config = configure.Configure()
        self.config.tool()     
        self.preference_path = self.get_path()

    def has_valid(self, input, argments):
        source = sorted(input)
        target = sorted(argments)
        if source != target:
            return False, 'kwargs arguments are wrong'
        for key in argments:
            if os.path.exists(argments[key]):
                continue
            return False, 'not find <{}>'.format(argments[key])
        return True, None
    
    def get_path(self):
        path = os.path.join(
            resource.getWorkspacePath(),
            self.toolkit,
            self.config.name,
            resource.getPreferenceFormat()
            )
        return path        
    
    def create(self, **kwargs):
        '''
            pre = Preference()
            pre.create(
                show_directory = '/venture/shows/my_hero',
                show_icon = '/local/references/images/batman.png',
                database_directory = '/venture/shows/my_hero/db',
                mayapy_directory = '/usr/autodesk/maya2018/bin/mayapy'
                )        
        '''
        input_data = self.get_inputs()
        valid, reason = self.has_valid(input_data, kwargs)
        if not valid:
            raise ValueError(reason)        
        data = {}                        
        for key in input_data:
            data.setdefault(key, kwargs[key])
            
        resolution = input_data['show_icon']['resolution']
        show_icon = self.update_show_icon(
            kwargs['show_directory'], kwargs['show_icon'], resolution)        
        data['show_icon'] = show_icon
        
        bundle = {
            'comment': 'subin gopi tool kits',
            'last_modified': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'author': 'Subin Gopi',
            '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': '# WARNING! All changes made in this file will be lost!',
            'description': 'This data contain information about {} preferences'.format(
                self.config.pretty),
            'type': 'preferences_inputs',
            'enable': True,
            'user': getpass.getuser(),
            'data': data
        }
        
        dirname = os.path.dirname(self.preference_path)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
                      
        with (open(self.preference_path, 'w')) as open_data:
            open_data.write(json.dumps(bundle, indent=4))
            print json.dumps(data, indent=4)
            print self.preference_path
            print 'Preferences saved successfully!...'
        
        return True
    
    def get(self):
        '''
            pre = Preference()
            pre.get()
        '''        
        if not os.path.isfile(self.preference_path):
            return None
        data = resource.get_input_data(self.preference_path)
        return data
    
    def get_inputs(self):
        data = resource.getPreferenceData(path=None)        
        return data       
        
    def update_show_icon(self, show_path, source_image, resoultion): 
        show_icon = image.image_resize(
            source_image,
            os.path.join(show_path, 'icons', 'show.png'),
            resoultion[0],
            resoultion[1],
            )         
        return show_icon

