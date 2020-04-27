import sys
sys.path.append('/venture/subins_tutorials')

import os
import json
import warnings

from pprint import pprint

from studioPipe import resources
from studioPipe.core import studioConfig
from studioPipe.core import studioImage

from studioPipe.api import studioConnect

reload(studioConnect)
reload(studioConfig)


class Connect(object):

    def __init__(self, **kwargs):
        '''
        Description -API operate on read and write discipline informations.
            : __init__() <None>.       
        '''
        self.studio_config = studioConfig.Connect()
        self.config_data = self.studio_config.get_exists_output() 
        studio_pipe_directory = self.config_data['pipe_shows_directory']        
        
        self.dirname = studio_pipe_directory
        self.localhost = 'root'
        self.name = 'submit'
        self.type = 'output_db'
        self.tag = 'submit'
        
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
        if 'show' in kwargs:
            self.name = '%s_%s' % (self.name, kwargs['show'])
            
        self.format = '.json'
        self.full_path = os.path.join(
            self.dirname, self.localhost, '%s%s' % (self.name, self.format))
        self.icon_format = '.png'

    #########################
    def has(self, discipline_name):
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
        disciplines = stdio_input.sortData()
        if discipline_name in disciplines:
            return True
        return False

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

    def create(self, current_show, input_data):
        input_data['enabled'] = True    
        
        studio_image = studioImage.ImageCalibration(
            imgae_file=input_data['discipline_icon'])
        q_image, q_image_path = studio_image.set_studio_size(
            width=256, height=256) 
        icon_path = os.path.join(
            self.dirname, 'icons', '%s_%s%s' % (
                current_show, input_data['name'], self.icon_format))
        input_data['discipline_icon'] = icon_path
               
        current_input_data = {
                input_data['name']: input_data
            }        
        discipline_data = self.disciplineData(
            current_show, current_input_data)
        
        current_discipline_data = {
            current_show: discipline_data
            }

        studio_input = studioConnect.Connect()
        studio_input.createDb(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag,
            data=current_discipline_data            
        )
        
        if not os.path.isdir(os.path.dirname(icon_path)):
            os.makedirs(os.path.dirname(icon_path))
        q_image.save(icon_path)        
        
    def disciplineData(self, show, current_data):
        studio_connect = studioConnect.Connect(file_path=self.full_path)
        data, rollback_data, sort_data = studio_connect.getAllData()
        exists_data = {}
        if data:
            for index, content in data.items():
                for k, v in content.items():  
                    if show != k:
                        continue
                    exists_data = v
                    break
        pprint(exists_data)
        rollback_data = self.rollback(exists_data)
        pprint (rollback_data)
        length = len(exists_data)
        for k, v in current_data.items():
            if k in rollback_data:
                length = rollback_data[k]
            exists_data[length] = {k: v}
        return exists_data
                
    def rollback(self, data):
        rollback_data = {}
        for index, content in data.items():
            for k, v in content.items():
                rollback_data.setdefault(k, index)
        return rollback_data             

    def getOutputData(self):
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
        output_data = stdio_input.getOutputData()
        return output_data

    def getDisciplineData(self, show):
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
        data = stdio_input.getAllData()        
        show_discipline_content = {}        
        for k, v in data[0].items():
            if show not in v:
                continue
            show_discipline_content = v
            break        
        return show_discipline_content  
    
    def getDisciplines(self, show):
        show_discipline_content = self.getDisciplineData(show)
        if show not in show_discipline_content:
            return None, None
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        disciplines = stdio_input.sortData(data=show_discipline_content[show])
        discipline_content = {}
        for k, v in show_discipline_content[show].items():
            discipline_content.update(v)            
        return disciplines, discipline_content
    
    def getShows(self):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.sortData()
        return data    
          
    def getDisciplineAllData(self):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.getAllData()
        return data

    def getSpecificTypes(self, show):
        data = self.getDisciplines(show)        
        specific_data = {}      
        for k, v in data[1].items():
            specific_data.setdefault(v['type'], []).append(k.encode())
        return specific_data
    
    def getShowIndex(self, show):
        shows = self.getShows()  
        if show not in shows:
            return None   
        return shows.index(show)

#===============================================================================
# a = Connect()
# b = a.getSpecificTypes() 
# pprint(b)
#===============================================================================

