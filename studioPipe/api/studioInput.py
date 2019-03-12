'''
studioDiscipline.py 0.0.1 
Date: January 11, 2019
Last modified: February 11, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi

# WARNING! All changes made in this file will be lost!

Description
    None.
'''
import os
import time
import json
import getpass
import warnings

from datetime import datetime

from studioPipe import resources
from studioPipe.core import studioDataBase

class Connect(object):

    def __init__(self, type, value=None):
        self.value = value
        
        self.input_path = os.path.join(
            resources.getInputPath(), '{}.json'.format(type))

        self.db_type = 'pipe_db'
        self.studio_db = os.path.join(
            '/home/shreya/Documents/studio_pipe', self.db_type)
        self.module = type
        self.tag = 'pipe_%s'%type
        
        self.cursor = studioDataBase.Connect(
            db_dirname=self.studio_db, tag=self.tag, localhost=type, name='%s_inputs'%type)

    def hasShow(self, tag_name):
        '''
        Description -function set for validate the show.
            :paran show_name <str> example 'my_super_hero'
            :return <bool>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.hasShow('my_super_hero')
        '''
        self.cursor.rollback()
        if tag_name in self.cursor.rollback_data:
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
        read_db = studioDataBase.Connect(full_path=self.input_path)
        input_data = read_db.getData()
        if self.value:
            input_data = input_data[self.value]  
        sort_input_data = read_db.sort_input_data(input_data)
        return input_data, sort_input_data


    def get(self, tag_name=None):
        '''
        Description -function set for get exists show or shows data.
            :paran show_name <str> exmple 'my_super_hero'
            :return <dict>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.get('my_super_hero')
        '''
        data = self.cursor.getContents()
        if not tag_name:
            return data['data']
        self.cursor.rollback()
        if tag_name in self.cursor.rollback_data:
            show_index = self.cursor.rollback_data[tag_name]
            current_show = data['data'][show_index]
            print json.dumps(current_show, indent=4)
            return current_show

    def get(self):
        '''
        Description -function set for get show list.
            :paran <None> 
            :return <list>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getShows()
        '''
        data = self.cursor.getContents()
        sort_data = self.cursor.sort_db_data(data['data'])
        return sort_data
    
    def getAllData(self):
        data = self.cursor.getContents()        
        rollback_data = self.cursor.rollback()
        sort_data = self.cursor.sort_db_data(data['data'])        
        return data['data'], rollback_data, sort_data
       
    
    def create(self, **kwargs):
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
                    en = True,
                    sn = 'MSH',
                    tp = 'My Super Hero',
                    ic = '/tmp/hero.png'
                    )
        '''
        input_datas = {
            'enable': kwargs['en'],
            'name': kwargs['na'],
            'display_name': kwargs['dn'],
            'tooltip': kwargs['tp'],
            'type': kwargs['ty'],
            }
        self.cursor.execute('update', {kwargs['na']: input_datas})
