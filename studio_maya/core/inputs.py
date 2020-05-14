'''
inputs.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import json
import warnings

from studio_maya import resources


class Connect(object):

    def __init__(self):
        self.path = os.path.join(
            resources.getInputPath(), 'maya.json')

    def get_data(self):
        input_data = self.read()
        if 'data' not in input_data:
            return None
        return input_data['data']

    def read(self):
        data = {}
        openData = open(self.path, 'r')
        try:
            data = json.load(openData)
        except Exception as result:
            warnings.warn(str(result))
        openData.close()
        return data
