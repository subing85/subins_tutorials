import sys
from __builtin__ import int
sys.path.append('/venture/subins_tutorials')

import os
import json
import warnings

from pprint import pprint

from studioPipe import resources
from studioPipe.core import studioConfig
from studioPipe.api import studioConnect

reload(studioConnect)
reload(studioConfig)


class Connect(object):

    def __init__(self, **kwargs):
        '''
        Description -API operate on read and write description informations.
            : __init__() <None>.       
        '''
        self.studio_config = studioConfig.Connect()
        self.config_data = self.studio_config.get_exists_output() 
        studio_pipe_directory = self.config_data['pipe_shows_directory']        
        
        self.dirname = studio_pipe_directory
        self.localhost = 'root'
        self.name = 'tier'
        self.type = 'input_db'
        self.tag = 'tier'
        
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
            self.name = '%s_%s'%(self.name, kwargs['show'])
            
        self.format = '.json'
        self.full_path = os.path.join(
            self.dirname, self.localhost, '%s%s' % (self.name, self.format))
        self.icon_format = '.png'
        
        self.description_type = {
            1: 'assets',
            2: 'shots'
        }

    #########################
    def has(self, description_name):
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
        descriptions = stdio_input.sortData()
        if description_name in descriptions:
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
        input_file = os.path.join(resources.getInputPath(), 'description.json')
        studio_input = studioConnect.Connect(file_path=input_file)
        data, sort_data, key_data = studio_input.getInputData()
        return data, sort_data, key_data

    def create(self, current_show, description, input_data):
        input_data['enabled'] = True

        input_data['name'] = self.description_type[description]
        current_input_data = {
                input_data['name']: input_data
                }
        description_data = self.tierData(
            current_show, current_input_data)
        current_description_data = {
            current_show: description_data
            }
        studio_input = studioConnect.Connect()
        studio_input.createDb(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag,
            data=current_description_data            
        )     
        
    def tierData(self, show, current_data):
        studio_connect = studioConnect.Connect(file_path=self.full_path)
        data, rollback_data, sort_data = studio_connect.getAllData()
        exists_data = {}
        if data:
            for index, content in data.items():
                for k, v in content.items():  
                    if show!=k:
                        continue
                    exists_data = v
                    break
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

    def getDescriptionData(self, show):
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
        show_description_content = {}        
        for k, v in data[0].items():
            if show not in v:
                continue
            show_description_content = v
            break        
        return show_description_content  
    
    def getDescriptions(self, show):
        show_description_content = self.getDescriptionData(show)        
        if show not in show_description_content:
            return None, None
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        descriptions = stdio_input.sortData(data=show_description_content[show])
        description_content = {}
        for k, v in show_description_content[show].items():
            description_content.update(v)            
        return descriptions, description_content
    
    def getTiers(self, show, description=None):
        descriptions, description_content = self.getDescriptions(show)
        if not description_content:
            return None
        current_tier_data = {}
        if description:
            if description not in description_content:
                return None
            current_tier_data = {
                description: description_content[description]
                }
        else:
            current_tier_data = description_content        
        chunks = ['current_show', 'description', 'enabled', 'name']
        tiers = {}
        for des, contents in current_tier_data.items():
            result, index = [], 0
            while index < len(contents) + 1:
                x = 0
                for k, v, in contents.items():
                    
                    if k in chunks:
                        continue
                    if x > len(contents):
                        break
                    order = int(k)
                    if order != index:
                        continue
                    result.append(v.encode())
                    x += 1
                index += 1
            tiers.setdefault(des.encode(), result)
        return tiers      
    
    def getShows(self):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.sortData()
        return data    
          
    def getTierAllData(self):
        stdio_input = studioConnect.Connect(file_path=self.full_path)
        data = stdio_input.getAllData()
        return data

    def getSpecificTypes(self, show, description):
        if isinstance(description, int):
            description = self.description_type[description]
        specific_data = self.getTiers(show, description=description)
        return specific_data
    
    def getShowIndex(self, show):
        shows = self.getShows()  
        if show not in shows:
            return None   
        return shows.index(show)
        



