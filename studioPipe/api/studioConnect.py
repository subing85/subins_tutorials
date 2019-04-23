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

import sys
sys.path.append('/venture/subins_tutorials')

from datetime import datetime
from pprint import pprint

from studioPipe import resources
from studioPipe.core import studioDataBase


class Connect(object):

    def __init__(self, file_path=None, value=None):

        self.input_path = file_path
        self.value = value
        self.cursor = studioDataBase.Connect(full_path=self.input_path)

    def has(self, tag_name):
        '''
        Description -function set for validate the item.
            :paran item_name <str> example 'my_super_hero'
            :return <bool>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.hasShow('my_super_hero')
        '''
        result = self.getInputData()
        if tag_name == result[2]['tag']:
            return True
        return False

    def createDb(self, dirname=None, localhost=None, name=None, type=None, tag=None, data=None):
        '''
        Description - Creates and edit the exists item this function set to operate        
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
        self.create_cursor = studioDataBase.Connect(
            db_dirname=dirname, localhost=localhost, name=name, type=type, tag=tag)
        self.create_cursor.execute('update', data)

    def getInputData(self):
        '''
        Description -function set for get the item input data.
            :paran <None>
            :return (<dict>, <list>)
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getInputData('my_super_hero')
        '''
        if not self.input_path:
            warnings.warn('None db!.....')
            return

        if not os.path.isfile(self.input_path):
            warnings.warn('Not found db %s' % self.input_path)
            return

        read_db = studioDataBase.Connect(full_path=self.input_path)
        all_data = read_db.get_all_data()
        sort_input_data = read_db.sort_input_data(all_data['data'])
        key_datas = read_db.get_keys_data(all_data)
        return all_data['data'], sort_input_data, key_datas

    def getOutputData(self, tag_name=None):
        '''
        Description -function set for get exists item or items data.
            :paran item_name <str> exmple 'my_super_hero'
            :return <dict>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.get('my_super_hero')
        '''
        data = self.cursor.get_contents()
        if not tag_name:
            return data['data']
        self.cursor.rollback()
        if tag_name in self.cursor.rollback_data:
            item_index = self.cursor.rollback_data[tag_name]
            current = data['data'][item_index]
            return current

    def getAllData(self):
        data = self.cursor.get_contents()
        if not data:
            return None, None, None        
        if 'data' not in data:
            return None, None, None            
        rollback_data = self.cursor.rollback()
        sort_data = self.cursor.sort_db_data(data['data'])
        return data['data'], rollback_data, sort_data
    
    def getData(self):
        data = self.cursor.get_contents()
        return data['data']
    
    def sortData(self, data=None):
        if not data:
            content = self.cursor.get_contents()
            data = content['data']
        sort_data = self.cursor.sort_db_data(data)
        return sort_data
    
    def rollbackData(self):
        rollback_data = self.cursor.rollback()
        return rollback_data    
    
    def getSpecificType(self, value):
        data = self.cursor.get_contents()
        specific_data = self.cursor.sort_type_data(data['data'], value)
        return specific_data
    
    def getSpecificValue(self, key, value):
        data = self.cursor.get_contents()
        specific_value = self.cursor.find_specific_value(data['data'], key, value)
        return specific_value
        

#=========================================================================
# input_file = os.path.join(resources.getInputPath(), 'shows.json')
# a = Connect(input_file)
# print a.has('shows')
#=========================================================================
