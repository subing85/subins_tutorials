'''
read.py 0.0.1 
Date: January 01, 2019
Last modified: January 15, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    read is the function set to read the inputs of the smart deformer package.
'''


import os
import json
import warnings


class Data():

    def __init__(self, **kwargs):
        self.file = None
        if 'file' in kwargs:
            self.file = kwargs['file']
        if not self.file:
            warnings.warn('<file> argument none')

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
