'''
replace_sourceimages.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to replace the source image from the scenes.
'''


import os

from pymel import core


def do_replace(source, target):
    files = core.ls(type='file')
    print "\nhttp://www.subins-toolkits.com", '\n', '-'*41
    for each_file in files:
        attribute = each_file.attr('fileTextureName')
        exists_path = attribute.get()
        if source not in exists_path:
            print 'Warning! not found keys \"%s\" in %s' % (source, exists_path)
            continue
        new_path = exists_path.replace(source, target)
        attribute.set(new_path)
        print 'exists path', exists_path
        print 'new_path', new_path, '\n'


SEARCH_FOR = '.tga'
REPLACE_WITH = '.png'
do_replace(SEARCH_FOR, REPLACE_WITH)
