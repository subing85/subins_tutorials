import os
import json
import warnings

import sys
sys.path.append('/venture/subins_tutorials')

from pprint import pprint

from PySide import QtGui

from studioPipe import resources
from studioPipe.core import studioImage
from studioPipe.api import studioConnect


class Connect(object):

    def __init__(self, **kwargs):
        '''
            Description -API operate on read and write preferences informations.
                : __init__() <None>.       
        '''
        self.dirname = os.path.join(resources.getWorkspacePath())
        self.localhost = 'preferences'         
        self.name = 'preferences'            
        self.type = 'output_db'  
        self.tag = 'preferences'         
        
        if 'dirname' in kwargs:
            self.dirname = kwargs['dirname']
        if 'localhost' in kwargs:
            self.localhost = kwargs['localhost']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'tag' in kwargs:
            self.tag = kwargs['tag']
            
        self.format = '.json'
        self.full_path = os.path.join(
            self.dirname, self.localhost, '%s%s'%(self.name, self.format))               

    def getInputData(self):
        '''
        Description -function set for get the show input data.
            :paran <None>
            :return (<dict>, <list>, <dict>)
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.getInputData()
        '''
        input_file = os.path.join(resources.getInputPath(), 'preferences.json')
        studio_input = studioConnect.Connect(file_path=input_file)
        data, sort_input_data, key_data = studio_input.getInputData()
        return data, sort_input_data, key_data

    def getOutputData(self):
        '''
        Description -function set for get exists item or items data.
            :paran item_name <str> exmple 'my_super_hero'
            :return <dict>
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.getOutputData()
        '''
        studio_output = studioConnect.Connect(file_path=self.full_path)        
        data = studio_output.getOutputData()        
        return data['0']['studio_pipe']
    
    def create(self, input_data):
        '''
        Description - Creates and edit the exists show this function set to operate        
            :param input_data <{}> exmple 
                input_data = {
                    'pipe_maya_directory': '/usr/autodesk/maya2016', 
                    'pipe_nuke_version': '2.7',
                    'pipe_site_packages_directory': '/usr/lib64/python2.7/site-packages',
                    'pipe_nuke_directory': '/mnt/bkp/Icons gallery/icons_04',
                    'pipe_python_directory': '/usr/bin/python',
                    'pipe_maya_version': '2016',
                    'pipe_studio_pipe_directory': '/venture/subins_tutorials/studioPipe',
                    'pipe_name': 'studio_pipe',
                    'pipe_shows_directory': '/home/shreya/Documents/studio_pipe/showsdfsfdsfdf'
                    }
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.create(input_data)
        '''
        input_data['enable'] = True
        studio_input = studioConnect.Connect()
        dirname = os.path.join(resources.getWorkspacePath())
        studio_input.createDb(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag,
            data={input_data['pipe_name']: input_data}
        )

    def hasPreferences(self):
        '''
        Description -function set for validate the preferences.
            :paran show_name <str> example 'my_super_hero'
            :return <bool>
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.hasPreferencess()
        '''
        if not os.path.isfile(self.full_path):
            return False
        data = self.getOutputData()
        
        if 'enable' not in data:
            return False
        if not data['enable' ]:
            return False        
        return True
    
    def getKeys(self): 
        '''   
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.getKeys()
        '''         
        data = self.getInputData()
        return data[1]
    
    def getValues(self, keys):
        '''   
        
            :example
                from studioPipe.api import studioPreferences
                studio_preferences = studioPreferences.Connect()
                studio_preferences.getValues('pipe_studio_pipe_directory')
        ''' 
        data = self.getOutputData()
        if keys not in data:
            return None
        return data[keys]




