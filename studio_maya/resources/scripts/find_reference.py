'''
find_reference.py 0.0.1 
Date: August 05, 2019
Last modified: August 05, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    to find the reference details from the scenes.
'''


import os
import json
import tempfile
import webbrowser

from maya import cmds


def find(output_path=None, write=False):
    if not output_path:
        output_path = os.path.join(
            tempfile.gettempdir(), 'studio_maya_reference_data.txt')
    if os.path.isfile(output_path):
        try:
            os.chmod(output_path, 0777)
        except:
            pass
        try:
            os.remove(output_path)
        except Exception as error:
            print str(error)
    references = cmds.file(q=True, r=True)
    data = {}
    print "\nhttp://www.subins-toolkits.com", '\n', '-'*41         
    print '\nReference informations'    
    for index, reference in enumerate(references):
        namespace = cmds.file(reference, q=True, ns=True).encode()
        source_path = cmds.referenceQuery(reference, filename=True, wcn=True)
        source_path = source_path.replace('\\', '/').encode()
        world_node = cmds.referenceQuery(reference, n=1)[0]
        current_data = {
            'source_path': source_path,
            'namespace': namespace,
            'top_dag_node': world_node
        }
        data.setdefault(index + 1, current_data)
        print index
        print '\tsource_path :', source_path
        print '\tnamespace :', namespace
        print '\tTop level dag object :', world_node, '\n'
    if write:
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(data, indent=4))
    return data, output_path


data, path = find(write=True)
try:
    webbrowser.open(path)
except Exception as error:
    print str(error)
