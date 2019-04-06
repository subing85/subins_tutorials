import sys
sys.path.append('/venture/subins_tutorials')

import os
import json
import copy
import warnings

from pprint import pprint

from PySide import QtGui

from studioPipe import resources
from studioPipe.core import studioImage
from studioPipe.core import studioConfig

from studioPipe.api import studioConnect
from studioPipe.api import studioDiscipline

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
        self.prefix = 'header'
        self.name = 'header'
        self.type = 'output_db'
        self.tag = 'header'

        if 'dirname' in kwargs:
            self.dirname = kwargs['dirname']
        if 'localhost' in kwargs:
            self.localhost = kwargs['localhost']
        if 'name' in kwargs:
            self.name = '{}_{}'.format(self.prefix, kwargs['name'])
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'tag' in kwargs:
            self.tag = kwargs['tag']
            
        self.description_type = {
            1: 'assets',
            2: 'shots'
        }

        self.format = '.json'
        self.icon_format = '.png'
        self.full_path = os.path.join(
            self.dirname, self.localhost, '%s%s' % (self.name, self.format))

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
        if not output_data:
            warnings.warn('not fount data')
            return           
        if show_name not in output_data:
            warnings.warn('not fount %s data' %show_name)
            return
        return output_data[show_name]    

    def create(self, show, description, discipline, input_data):
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
        
        studio_discipline = studioDiscipline.Connect()
        discipline_data = studio_discipline.getSpecificTypes(show)
        disciplines = discipline_data[description]
                
        exists_data = self.headerData(
            show, discipline, disciplines, input_data)
        

         
        #=======================================================================
        # all_data = {}
        # for k, v in input_data.items():
        #     each_data = {}
        #     for each in disciplines[description]:
        #         each_data.setdefault(each, v)
        #     all_data.setdefault(k, each_data)
        #=======================================================================
 
        current_data = {show: exists_data}
 
        studio_input = studioConnect.Connect()
        studio_input.createDb(
            dirname=self.dirname,
            localhost=self.localhost,
            name=self.name,
            type=self.type,
            tag=self.tag,
            data=current_data
        )
        
        
        
        
        
        
        
        
        
        
        
        

        # collect disciplines from description
        #=======================================================================
        # studio_discipline = studioDiscipline.Connect()
        # disciplines = studio_discipline.getSpecificTypes(show)
        # if description not in disciplines:
        #     print 'not found any disciplines!...'
        #     return
        #=======================================================================
       
        #=======================================================================
        # input_data = {'1': {'end': {'value': ''},
        #             'man_days': {'value': ''},
        #             'name': {'value': 'None'},
        #             'number': {'value': '1'},
        #             'start': {'value': ''},
        #             'status': {'value': 'None'},
        #             'super_user': {'value': ''},
        #             'tier': {'value': 'props'},
        #             'user': {'value': ''}}}
        #=======================================================================
        


    def findHeaderInDiscipline(self, data, ):
        pass


    def headerData(self, show, discipline, disciplines, current_data):
        # show, discipline, input_data
        studio_connect = studioConnect.Connect(file_path=self.full_path)
        data, rollback_data, sort_data = studio_connect.getAllData()
        show_data, show_index = self.getShowData(show, data=data)
                
        new_header = list(set(current_data.keys())-set(show_data.keys()))

        for index, discipline_content in show_data.items():
            if index in new_header:
                continue
            for each_discipline, content in discipline_content.items():
                # update all discipline header name
                content['name']['value'] = current_data[index]['name']
                if discipline not in each_discipline:
                    continue
                # update specific discipline header values
                for k, v in current_data[index].items():
                    content[k]['value'] = current_data[index][k]
        
        # create new header disciplines        
        new_data = {}        
        for index in new_header:
            new_discipline_data = {}
            for each_discipline in disciplines:
                new_header_data = {}
                for each_header, values in current_data[index].items():
                    values = {'value': values}
                    new_header_data.setdefault(each_header, values)
                new_discipline_data.setdefault(each_discipline, new_header_data)
            new_data.setdefault(index, new_discipline_data)
        
        show_data.update(new_data)
        # replace the specific show data
        #=======================================================================
        # data[show_index].pop(show)
        # data[show_index] = {show: show_data}
        #=======================================================================
        return show_data

    def getShowData(self, show, data=None):
        if not data:
            studio_connect = studioConnect.Connect(file_path=self.full_path)
            data, rollback_data, sort_data = studio_connect.getAllData() 
        show_index = 0           
        show_data = {}
        for index, content in data.items():
            if show not in content:
                continue
            show_data = content[show]
            show_index = index
            break
        return show_data, show_index
    
    def getHeader(self, exists_data, current_data):         
        current_index = None         
        for index, content in current_data.items():
            if index not in exists_data:
                continue
            
            
        
         
    
    def rollback(self, data):
        rollback_data = {}
        for index, content in data.items():
            for k, v in content.items():
                rollback_data.setdefault(k, index)
        return rollback_data  
    
        
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










