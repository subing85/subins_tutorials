'''
input.py 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import sys

from assetLibrary_maya2017.modules import readWrite
from assetLibrary_maya2017 import resources


def get_input_data():
    category_path = resources.getInputPath(module='categories')
    rw = readWrite.ReadWrite(tag='categories')
    rw.file_path = category_path
    input_data = rw.get_data()
    order_data = rw.set_order(input_data)
    return input_data, order_data
