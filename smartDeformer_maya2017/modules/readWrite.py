'''
readWrite.py 0.0.1 
Date: January 01, 2019
Last modified: January 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    readWrite is the function set for custom data structure. 
    The purpose of the readWrite to create, getting and setting the weights data.  
'''


import os
import json
import time
import getpass
import warnings

from datetime import datetime

from smartDeformer_maya2017 import resources


class ReadWrite(object):

    def __init__(self, **kwargs):
        comment = 'subin gopi tool kits'
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about subin gopi tool kits'
        type = 'generic'
        valid = True
        data = None
        tag = 'generic'

        if 'c' in kwargs:
            comment = kwargs['c']
        if 'cd' in kwargs:
            created_date = kwargs['cd']
        if 'd' in kwargs:
            description = kwargs['d']
        if 't' in kwargs:
            type = kwargs['t']
        if 'v' in kwargs:
            valid = kwargs['v']
        if 'data' in kwargs:
            data = kwargs['data']
        if 'tag' in kwargs:
            tag = kwargs['tag']

        self.datas = {'comment': comment,
                      'created_date': created_date,
                      'author': 'Subin Gopi',
                      '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
                      'warning': '# WARNING! All changes made in this file will be lost!',
                      'description': description,
                      'type': type,
                      'tag': tag,
                      'valid': valid,
                      'user': getpass.getuser(),
                      'data': data
                      }

        resource_types = resources.getResourceTypes()
        self.path = resource_types[type]
        self.extention = 'json'

    def create(self, name):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        self.file_path = os.path.join(
            self.path, '%s.%s' % (name, self.extention))
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        try:
            write(self.file_path, self.datas)
            return True
        except Exception as result:
            warnings.warn(str(result), Warning)
            return False

    def get(self):
        if not os.path.isfile(self.file_path):
            warnings.warn('Not fount  file %s' % self.file_path, Warning)
            return
        try:
            read(self.file_path)
        except Exception as error:
            warnings.warn(error, Warning)

    def getBundles(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        files = os.listdir(self.path)
        bundles = {}
        for each_file in files:
            if not each_file.endswith(self.extention):
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

    result = 'successfully created Database {}'.format(path)
    genericData = data.copy()
    currentTime = time.time()
    try:
        data = json.dumps(genericData, indent=4)
        jsonData = open(path, 'w')
        jsonData.write(data)
        jsonData.close()
        os.utime(path, (currentTime, currentTime))
    except Exception as exceptResult:
        result = str(exceptResult)
    print('\n#write result\t- ', result)


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
