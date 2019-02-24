'''
assets.py 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import warnings

from multiprocessing.pool import ThreadPool


class SearchAssets(object):

    def __init__(self, root):
        if not os.path.isdir(root):
            raise Exception('can not found path')
        self.root = root
        self.formats = ['.ma', '.mb', '.MA', '.MB', '.obj', '.OBJ']
        self.quick_search()

    def quick_search(self):
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(self.search, (''))
        self.get_assets = async_result.get()
        return self.get_assets

    def search(self):
        my_files = []
        for path, dirs, files in os.walk(self.root):
            for each_file in files:
                my_asset = None
                for each_format in self.formats:
                    if not each_file.endswith(each_format):
                        continue
                    my_asset = each_file
                if not my_asset:
                    continue
                my_files.append(os.path.join(path, each_file))
        return my_files
