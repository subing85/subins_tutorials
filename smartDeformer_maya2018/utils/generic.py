'''
generic.py 0.0.1 
Date: January 01, 2019
Last modified: January 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    generic the functions
'''


def sortDictionary(dictionary):
    sort_result = {}
    for each, dict_data in dictionary.items():
        if 'order' not in dict_data:
            continue
        sort_result.setdefault(dict_data['order'], []).append(each.encode())
    return sort_result
