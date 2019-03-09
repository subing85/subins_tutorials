'''
studioImage.py 0.0.1 
Date: January 16, 2019
Last modified: February 24, 2019
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


class Connect(object):

    def __init__(self, tag=None, localhost=None, name=None, db_dirname=None, full_path=None):
        self.db_dirname = db_dirname
        self.tag = tag
        self.localhost = localhost
        self.name = name
        self.format = '.json'
        self.database = full_path
        if not full_path:
            self.database = os.path.join(
                self.db_dirname, self.localhost, '%s%s' % (self.name, self.format))
        self.contents = None
        self.commit = None
        self.rollback_data = None
        self.example = {
            'comment': 'subin gopi tool kits',
            'created_date': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'last_modified': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
            'author': 'Subin Gopi',
            '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': '# WARNING! All changes made in this file will be lost!',
            'description': 'This data contain information about studio pipe data base',
            'type': 'pipe_db',
            'tag': self.tag,
            'valid': True,
            'user': getpass.getuser(),
            'data': {}
        }

    def hasValid(self, force=False):
        if force:
            self.contents = self.getContents()
        if not self.contents:
            self.contents = self.getContents()
        if not self.contents:
            return False
        for each_key in self.contents:
            if each_key not in self.example:
                return False
        if not self.contents['valid']:
            return False
        if self.contents['type'] != 'pipe_db':
            return False
        return True

    def getData(self):
        data_contents = self.getContents()
        return data_contents['data']

    def getContents(self):
        if not os.path.isfile(self.database):
            warnings.warn('Not fount  file %s' % self.database, Warning)
            return
        try:
            data = self.read(self.database)
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
            data_contents = self.getContents()
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
        if os.path.isfile(self.database):
            if self.hasValid():
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
        self.write(self.database, my_data)

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
