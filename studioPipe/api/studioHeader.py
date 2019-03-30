import sys
sys.path.append('/venture/subins_tutorials')

import os
import json
import warnings

from pprint import pprint

from PySide import QtGui

from studioPipe import resources
from studioPipe.core import studioImage
from studioPipe.core import studioConfig

from studioPipe.api import studioConnect

reload(studioConnect)
reload(studioConfig)


class Connect(object):

    def __init__(self, **kwargs):
        '''
        Description -API operate on read and write shows informations.
            : __init__() <None>.       
        '''
        self.studio_config = studioConfig.Connect()
        self.config_data = self.studio_config.get_exists_output() 
        studio_pipe_directory = self.config_data['pipe_shows_directory']        
        
        self.dirname = studio_pipe_directory
        self.localhost = 'root'
        self.name = 'header'
        self.type = 'output_db'
        self.tag = 'header'

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
        self.icon_format = '.png'
        self.full_path = os.path.join(
            self.dirname, self.localhost, '%s%s' % (self.name, self.format))

        self.width = 256
        self.height = 144

    def getInputData(self):
        '''
        Description -function set for get the show input data.
            :paran <None>
            :return (<dict>, <list>)
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getInputData('my_super_hero')
        '''
        input_file = os.path.join(resources.getInputPath(), 'header.json')
        studio_input = studioConnect.Connect(file_path=input_file)
        data, sort_data, key_data = studio_input.getInputData()
        return data, sort_data, key_data
    

    def create(self, input_data):
        '''
        Description - Creates and edit the exists show this function set to operate        
            :param na <str> exmple 'my_super_hero'
            :param dn <str> exmple 'My Super Hero'
            :param sn <str> exmple 'MSH'
            :param tp <str> exmple 'My Super Hero'
            :param ic <str> exmple '/tmp/hero.png'            
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.create(na='my_super_hero',
                    dn = 'My Super Hero',
                    sn = 'MSH',
                    tp = 'My Super Hero',
                    ic = '/tmp/hero.png'
                    )
        '''
        if not self.studio_config.has_valid():
            warnings.warn('not found studio preferences data, update the preferences and try', Warning)
            return    
        if not os.path.isdir(self.dirname):
            warnings.warn('not found studio pipe directory', Warning)
            return    

        if not os.path.isfile(input_data['show_icon']):
            warnings.warn('not found file %s' %
                          input_data['show_icon'], Warning)
            return

        studio_image = studioImage.ImageCalibration(
            imgae_file=input_data['show_icon'])
        q_image, q_image_path = studio_image.set_studio_size(
            width=self.width, height=self.height)

        icon_path = os.path.join(
            self.dirname, 'icons', '%s%s' % (input_data['show_name'], self.icon_format))
        input_data['show_icon'] = icon_path

        studio_input = studioConnect.Connect()
        studio_input.createDb(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag,
            data={input_data['show_name']: input_data}
        )
        if not os.path.isdir(os.path.dirname(icon_path)):
            os.makedirs(os.path.dirname(icon_path))
        q_image.save(icon_path)
        

    def hasShow(self, show_name):
        '''
        Description -function set for validate the show.
            :paran show_name <str> example 'my_super_hero'
            :return <bool>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.hasShow('my_super_hero')
        '''
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        shows = stdio_input.sortData()
        if show_name in shows:
            return True
        return False

    def getOutputData(self, show_name=None):
        '''
        Description -function set for get exists show or shows data.
            :paran show_name <str> exmple 'my_super_hero'
            :return <dict>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.get('my_super_hero')
        '''
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        output_data = stdio_input.getOutputData(tag_name=show_name)
        return output_data

    def getShows(self):
        '''
        Description -function set for get show list.
            :paran <None> 
            :return <list>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getShows()
        '''
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.sortData()
        return data

    def getShowAllData(self):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.getAllData()
        return data
    
    def getSpecificValue(self, key, value):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.getSpecificValue(key, value)     
        
        return data   










