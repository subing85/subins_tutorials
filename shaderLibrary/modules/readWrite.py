'''
readWrite.py 0.0.1 
Date: January 01, 2019
Last modified: February 10, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    readWrite is the function set for custom data structure. 
    The purpose of the readWrite to create, getting and setting the model data.  
'''


import os
import json
import time
import getpass
import warnings
import tempfile

from datetime import datetime


class ReadWrite(object):

    def __init__(self, **kwargs):
        comment = 'subin gopi tool kits'
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about subin gopi tool kits'
        self.type = 'generic'
        valid = True
        data = None
        self.tag = None
        self.path = tempfile.gettempdir()
        self.format = 'json'
        self.name = None
        if 'path' in kwargs:
            self.path = kwargs['path']
        if 'format' in kwargs:
            self.format = kwargs['format']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'c' in kwargs:
            comment = kwargs['c']
        if 'cd' in kwargs:
            created_date = kwargs['cd']
        if 'd' in kwargs:
            description = kwargs['d']
        if 't' in kwargs:
            self.type = kwargs['t']
        if 'v' in kwargs:
            valid = kwargs['v']
        if 'data' in kwargs:
            data = kwargs['data']
        if 'tag' in kwargs:
            self.tag = kwargs['tag']
        self.datas = {'comment': comment,
                      'created_date': created_date,
                      'author': 'Subin Gopi',
                      '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
                      'warning': '# WARNING! All changes made in this file will be lost!',
                      'description': description,
                      'type': self.type,
                      'tag': self.tag,
                      'valid': valid,
                      'user': getpass.getuser(),
                      'data': data
                      }

        self.file_path = os.path.join(
            self.path, '%s.%s' % (self.name, self.format))

    def has_file(self):
        if os.path.isfile(self.file_path):
            return True
        return False

    def has_valid(self):
        data = self.get_all()
        if not data:
            return False
        for each_key in self.datas:
            if each_key not in data:
                return False
        if not data['valid']:
            return False
        if data['type'] != self.type:
            return False
        return True

    def create(self):
        if not self.file_path:
            return
        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))
        result = write(self.file_path, self.datas)
        return result, self.file_path

    def get_data(self):
        data = self.get_all()
        if not data:
            return None
        if not self.tag:
            return data['data']
        if data['tag'] != self.tag:
            return None
        return data['data']

    def get_info(self):
        data = self.get_all()
        info_data = {}
        for k, v in data.items():
            if k == 'data':
                continue
            info_data.setdefault(k, v)
        return info_data

    def get_all(self):
        if not os.path.isfile(self.file_path):
            warnings.warn('Not fount  file %s' % self.file_path, Warning)
            return
        try:
            data = read(self.file_path)
        except Exception as error:
            warnings.warn(error, Warning)
            data = None
        if 'data' not in data:
            return None
        return data

    def get_library_paths(self):
        path_data = self.get_data()
        if not path_data:
            return None
        paths = []
        x = 0
        while x < len(path_data) + 1:
            for index,  path, in path_data.items():
                if int(index) != x:
                    continue
                paths.append(path.encode())
            x += 1
        print '\npaths', paths
        return paths

    def getBundles(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        files = os.listdir(self.path)
        bundles = {}
        for each_file in files:
            if not each_file.endswith(self.format):
                continue
            if os.path.isdir(os.path.join(self.path, each_file)):
                continue
            file_data = read(os.path.join(self.path, each_file))
            if not file_data:
                continue
            if 'valid' not in file_data:
                continue
            if not file_data['valid']:
                continue
            if 'type' not in file_data:
                continue
            if 'tag' not in file_data:
                continue
            bundle = os.path.splitext(os.path.basename(each_file))[0]
            data = {}
            data['tag'] = file_data['tag'].encode()
            data['path'] = os.path.join(self.path, each_file)
            data['data'] = file_data['data']
            bundles.setdefault(bundle, data)
        return bundles


def write(path, data):
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


def read(path):
    data = {}
    openData = open(path, 'r')
    try:
        data = json.load(openData)
    except Exception as result:
        warnings.warn(str(result))
    openData.close()
    return data

# end ####################################################################
