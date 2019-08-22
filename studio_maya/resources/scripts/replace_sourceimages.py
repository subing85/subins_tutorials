import os
from pymel import core


def do_replace(source, target):
    files = core.ls(type='file')
    for each_file in files:
        attribute = each_file.attr('fileTextureName')
        exists_path = attribute.get()
        if search_for not in exists_path:
            print 'Warning! not found keys \"%s\" in %s' % (search_for, exists_path)
            continue
        new_path = exists_path.replace(search_for, replace_with)
        attribute.set(new_path)
        print 'exists path', exists_path
        print 'new_path', new_path, '\n'

search_for = '.tga'
replace_with = '.png'
do_replace(search_for, replace_with)
