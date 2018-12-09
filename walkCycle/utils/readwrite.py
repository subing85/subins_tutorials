import os
import json
import warnings


class Read():

    def __init__(self, **kwargs):
        self.file = None
        self.data = None

        if 'file' in kwargs:
            self.file = kwargs['file']
        if 'data' in kwargs:
            self.data = kwargs['data']

    def getData(self):
        if not os.path.isfile(self.file):
            warnings.warn('not found {}'.format(self.file), Warning)
            return
        try:
            readdd_my_data = open(self.file, 'r')
            python_dict = json.load(readdd_my_data)
        except Exception as result:
            warnings.warn(str(result), Warning)
            python_dict = None
        return python_dict


class Wirte():

    def __init__(self, **kwargs):
        self.file = None
        self.data = None

        if 'file' in kwargs:
            self.file = kwargs['file']
        if 'data' in kwargs:
            self.data = kwargs['data']
            
    def toWrite(self):
        pass
