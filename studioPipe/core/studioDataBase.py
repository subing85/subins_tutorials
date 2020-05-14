'''
studioImage.py 0.0.1 
Date: March 09, 2019
Last modified: March 10, 2019
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
from pprint import pprint

import sys
sys.path.append('/venture/subins_tutorials')


class Connect(object):

    def __init__(self, db_dirname=None, localhost=None, name=None, type=None, tag=None, full_path=None):
        '''
            :param tag <str> example input_data or output_data
            :param tag <str> example shows or preferences, etc
            :param localhost <str> example folder name
            :param name <str> example file name
            :param db_dirname <str> example directory name
            :param full_path <str> example full path of data base
        '''
        self.format = '.json'
        self.rollback_data = {}     
        self.db_dirname = db_dirname
        self.localhost = localhost
        self.name = name
        self.type = 'input_data'
        if type:
            self.type = type
        self.tag = tag        
        self.db_full_path = full_path
        if not full_path:
            self.db_full_path = '{}/{}/{}{}'.format(
                self.db_dirname, self.localhost, self.name, self.format)       
        self.contents = None
        self.commit = None
        self.example = {
            'comment': 'subin gopi tool kits',
            'created_date': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'last_modified': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'author': 'Subin Gopi',
            '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': '# WARNING! All changes made in this file will be lost!',
            'description': 'This data contain information about studio pipe data base',
            'type': self.type,
            'tag': self.tag,
            'valid': True,
            'user': getpass.getuser(),
            'data': {}}       

    def has_valid(self, force=False):
        if force:
            self.contents = self.get_contents()
        if not self.contents:
            self.contents = self.get_contents()
        if not self.contents:
            return False
        for each_key in self.contents:
            if each_key not in self.example:
                return False
        if not self.contents['valid']:
            return False
        if self.contents['type'] != self.type:
            return False
        return True

    def get_data(self):
        data_contents = self.get_contents()
        return data_contents['data']
    
    def get_all_data(self):
        data_contents = self.get_contents()
        return data_contents
    
    def get_keys_data(self, data):
        valid_data = {
            'type': data['type'],
            'tag': data['tag']
            }
        return valid_data
        
    def get_contents(self):
        if not os.path.isfile(self.db_full_path):
            warnings.warn('Not fount  file %s' % self.db_full_path, Warning)
            return
        try:
            data = self.read(self.db_full_path)
        except Exception as error:
            warnings.warn(error, Warning)
            data = None
        if 'data' not in data:
            return None
        return data    
    
    def rollback(self):
        data_contents = self.contents
        self.rollback_data = {}
        if not self.contents:
            data_contents = self.get_contents()
        if not data_contents:
            return self.rollback_data
        if 'data' not in data_contents:
            return self.rollback_data
        for index, data in data_contents['data'].items():
            for k, v in data.items():
                self.rollback_data.setdefault(k, index)
        return self.rollback_data       

    def execute(self, commit, data, force=False):
        '''
            :param commit <str> example 'create', 'insert', 'update', 'read'
            :param data <dict>
        '''
        if commit != 'create' and commit != 'insert' and commit != 'update':
            raise Exception(
                '# commit not contain any of - \"create\" or \"insert\" or \"update\"!...')
        if not isinstance(data, dict):
            raise Exception('# data not contain dictionary!...')
        my_data = self.example
        if os.path.isfile(self.db_full_path):
            if self.has_valid():
                my_data = self.contents
        my_data['last_modified'] = datetime.now(
            ).strftime('%Y/%d/%B - %I:%M:%S:%p')
        my_data['tag'] = self.tag
        
        if not self.rollback_data:
            self.rollback()
            
        if commit == 'create':
            my_data['data'] = {}
            length = 0
            for k, v in data.items():
                my_data['data'][length] = {k: v}
                length += 1
        if commit == 'insert' or commit == 'update':
            length = len(my_data['data'])
            for k, v in data.items():
                if commit == 'insert':
                    if k in self.rollback_data:
                        warnings.warn(
                            'Already found same value in the studio data base \"%s\"' % k, Warning)
                        continue
                    my_data['data'][length] = {k: v}
                if commit == 'update':
                    if k in self.rollback_data:
                        length = self.rollback_data[k]
                    my_data['data'][length] = {k: v}
        self.write(self.db_full_path, my_data)

    def write(self, path, data):
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        if os.path.isfile(path):
            try:
                os.chmod(file, 0777)
                os.remove(file)
            except Exception as result:
                print(result)
        result = {True: 'successfully created Database {}'.format(path)}
        genericData = data.copy()
        currentTime = time.time()
        try:
            data = json.dumps(genericData, indent=4)
            jsonData = open(path, 'w')
            jsonData.write(data)
            jsonData.close()
            os.utime(path, (currentTime, currentTime))
        except Exception as except_result:
            result = {False: str(except_result)}
        print('\n#write result\t- ', result)
        return result

    def read(self, path):
        data = {}
        openData = open(path, 'r')
        try:
            data = json.load(openData)
        except Exception as result:
            warnings.warn(str(result))
        openData.close()
        return data

    def sort_db_data(self, data):
        result = []
        index = 0
        while index < len(data) + 1:
            x = 0
            for k, v, in data.items():
                if x > len(data):
                    break
                order = int(k)
                if order != index:
                    continue
                result.append(v.keys()[0].encode())
                x += 1
            index += 1
        return result

    def sort_input_data(self, data):
        '''
        sort_data = {}
        for each, dict_data in data.items():
            if 'order' not in dict_data:
                continue
            sort_data.setdefault(dict_data['order'], []).append(each.encode())

        result = sum(sort_data.values(), [])
        return result
        '''
        result = []
        index = 0
        while index < len(data) + 1:
            x = 0
            for k, v, in data.items():
                if x > len(data):
                    break
                order = v['order']
                if order != index:
                    continue
                result.append(k)
                x += 1
            index += 1
        return result
    
    def sort_type_data(self, data, value):
        result = []
        index = 0
        while index < len(data) + 1:
            x = 0
            for k, v, in data.items():
                if x > len(data):
                    break
                order = int(k)
                if order != index:
                    continue                
                current = None                
                for each in v:
                    if v[each]['type'] != value:
                        continue                        
                    current = v.keys()[0].encode()
                    break
                if not current:
                    continue                    
                result.append(current)
                x += 1
            index += 1
        return result
    
    def find_specific_value(self, data, key, value):
        
        result = None
        for index, data_content in data.items():
            for each_data, v in data_content.items():
                if key != each_data:
                    continue  
                if value not in v:
                    continue
                result = v[value]
                break
        return result

#===============================================================================
# from studioPipe import resources
# full_path = os.path.join(resources.getInputPath(), 'shows.json')   
# a = Connect(full_path=full_path)
#===============================================================================

