import os
import json
import shutil
import warnings

from studio_usd_pipe import resource
from studio_usd_pipe.core import configure
from studio_usd_pipe.api import studioImage
 

class Preference(object):
    
    def __init__(self):
        self.toolkit = 'subins-toolkits'
        self.file_name = '.pref'
        self.config = configure.Configure()
        self.pref_path = self.get_path()

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
        workspace = resource.getWorkspacePath()        
        self.config.tool()        
        path = os.path.join(
            workspace, self.toolkit, self.config.name, self.file_name)
        return path        
    
    def create(self, **kwargs):
        '''
            pre = Preference()
            pre.create(
                shows_directory = '/venture/shows/my_hero',
                show_icon = '/local/references/images/batman.png',
                database_directory = '/venture/shows/my_hero/db',
                mayapy_directory = '/usr/autodesk/maya2018/bin/mayapy'
                )        
        '''
        input_data = self.get_inputs()
        valid, reason = self.has_valid(input_data, kwargs)
        if not valid:
            raise ValueError(reason)        
        bundle = {}                        
        for key in input_data:
            bundle.setdefault(key, kwargs[key])
        data = {
            'data': bundle,
            'enable': True
            }
        dirname = os.path.dirname(self.pref_path)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        resolution = input_data['show_icon']['resolution']
        show_icon = self.update_show_icon(
            kwargs['show_directory'], kwargs['show_icon'], resolution)        
        bundle['show_icon'] = show_icon        
        with (open(self.pref_path, 'w')) as open_data:
            open_data.write(json.dumps(data, indent=4))
            print json.dumps(data, indent=4)
            print self.pref_path
            print 'Preferences saved successfully!...'
    
    def get(self):
        '''
            pre = Preference()
            pre.get()
        '''        
        with (open(self.pref_path, 'r')) as open_data:
            data = json.load(open_data)
            if not data['enable']:
                return None
            return data['data']
    
    def get_inputs(self):
        data = resource.getPreferenceData(type='input')        
        return data       
        
    def update_show_icon(self, show_path, source_image, resoultion): 
        image = studioImage.ImageCalibration()
        show_icon = os.path.join(show_path, 'icons', 'show.png')
        width, height = resoultion[0], resoultion[1]
        studio_image = studioImage.ImageCalibration(imgae_file=source_image)
        image, image_path = studio_image.set_studio_size(
            output_path=show_icon,
            width=width,
            height=height
            )
        return show_icon

