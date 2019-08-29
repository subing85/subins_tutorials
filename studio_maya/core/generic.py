'''
generic.py 0.0.1 
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
import glob
import ast

from xml.dom import minidom
from xml.etree import ElementTree

from studio_maya import resources


def get_mayapy(version, progress=None):
    root_path, tag, mayapy = resources.getRootPath()
    mayapy_path = None
    progress.setValue(0)
    index = 0    
    current_tag = '%s%s'%(tag, version)
    for dirname, folder, files in os.walk(root_path):
        progress.setValue(index)
        progress.setMaximum(100 + index)
        index += 1        
        dirname = dirname.replace('\\', '/')        
        if not dirname.endswith(current_tag):
            continue
        mayapy_path = os.path.join(dirname, 'bin', mayapy).replace('\\', '/')
        break
    if not mayapy_path:
        return None
    if not os.path.isfile(mayapy_path):
        return None
    return mayapy_path


def write_preset(data, path):
    '''
        :example        
            data = {'parent': {
                        'studio_maya':{
                            'version': '0.0.1',
                            'type': 'preset',
                            }
                        },
                    'child': {
                        'maya': {
                            'version': '2016',
                            'path': '/usr/autodesk/maya2016/bin/mayapy'
                            },
                        'settings': {
                            'edit': False,
                            'save': True
                            }
                        }
                    }            
            path = '/venture/subins_tutorials/studio_maya/result.xml'            
            element = xml_w(data, path)        
    '''
    element = ElementTree.Element('')
    for root, contents in data['parent'].items():
        element = ElementTree.Element(root)
        for k, v in contents.items():
            element.set(k, v)
    for child, contents in data['child'].items():
        sub_element = ElementTree.SubElement(element, child)
        for k, v in contents.items():
            sub_element.set(k, str(v))
    rough_string = ElementTree.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent='\t')
    xml_pretty = ElementTree.XML(pretty_xml)
    tree = ElementTree.ElementTree(xml_pretty)
    tree.write(path, xml_declaration=False)
    return element


def read_preset(path):
    if not os.path.isfile(path):
        return
    label, name, version = resources.getToolKit()
    data = {}
    element = ElementTree.parse(path)
    root = element.getroot()
    if root.tag != 'studio_maya':
        return data
    for each in ['version', 'type', 'label']:
        if each not in root.keys():
            return
    if root.get('version') != version:
        return
    if root.get('type') != 'preset':
        return
    if root.get('label') != 'Studio Maya Interpreter':
        return
    maya_versions = []
    current_version = None
    current_path = None
    query = True
    edit = False
    overwrite = True
    version = False
    for child in root.getchildren():
        if child.tag == 'maya':
            maya_versions = ast.literal_eval(child.get('maya_versions'))
            current_version = child.get('current_version')
            current_path = child.get('path')
        if child.tag == 'settings':
            edit = ast.literal_eval(child.get('edit'))
            version = ast.literal_eval(child.get('save'))
            if edit:
                query = False
            if version:
                overwrite = False
    data['maya_versions'] = maya_versions
    data['current_version'] = {
        'index': maya_versions.index(current_version),
        'name': current_version,
        'path': current_path
    }
    data['mode'] = {
        "query_only": query,
        "edit_quey": edit,
        "overwrite": overwrite,
        "next_version": version
    }
    return data


def write_data(data, path):
    element = ElementTree.Element('')
    for root, contents in data['parent'].items():
        element = ElementTree.Element(root)
        for k, v in contents.items():
            element.set(k, v)
    for child, contents in data['child'].items():
        sub_element = ElementTree.SubElement(element, child)
        sub_element.set('name', child)
        for index, path_contens in contents.items():
            path_element = ElementTree.SubElement(sub_element, 'content')
            path_element.set('index', str(index))
            path_element.set('label', path_contens['label'])
            path_element.set('path', path_contens['path'])
    rough_string = ElementTree.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent='\t')
    xml_pretty = ElementTree.XML(pretty_xml)
    tree = ElementTree.ElementTree(xml_pretty)
    tree.write(path, xml_declaration=False)
    return element


def read_data(path):
    label, name, version = resources.getToolKit()
    data = {}
    element = ElementTree.parse(path)
    root = element.getroot()
    if root.tag != 'studio_maya':
        return data
    for each in ['version', 'type', 'label']:
        if each not in root.keys():
            return
    if root.get('version') != version:
        return
    if root.get('type') != 'studio_maya_data':
        return
    if root.get('label') != 'Studio Maya Interpreter':
        return
    for child in root.getchildren():
        type = child.tag
        content_data = {}
        for sub_element in child.getchildren():
            if sub_element.tag != 'content':
                continue
            current_index = sub_element.get('index')
            label = sub_element.get('label')
            path = sub_element.get('path')
            contents = {
                'label': label.encode(),
                'path': path.encode()
            }
            content_data.setdefault(int(current_index), contents)
        data.setdefault(type, content_data)
    return data


def next_version(file_path):
    if not os.path.isfile(file_path):
        return None
    directory = os.path.dirname(file_path)
    files = os.listdir(directory)
    basename = os.path.basename(file_path)
    index = 1
    while files:
        name, extension = os.path.splitext(basename)
        split_name = name.split('_studio_maya')[0]
        name = '%s_studio_maya_%s%s' % (split_name, index, extension)
        if name not in files:
            return os.path.join(directory, name)
        index += 1
    return


def decode_message(messages, *args):
    status_message = 'Not able to read'
    
    operating_system = resources.getOperatingSystem()
    next = '\n'
    if operating_system == 'Windows':
        next = '\r\n'
    if '#&&#status&##&%s'%next in messages:
        status = messages.index('#&&#status&##&%s'%next)
        status_message = messages[status + 1].replace('\n', '')
    code_messages = 'Not able to read'
    if '#&&#code&##&%s'%next in messages and '#&&#code_end&##&%s'%next in messages:
        code_start = messages.index('#&&#code&##&%s'%next)
        code_end = messages.index('#&&#code_end&##&%s'%next)
        code_messages = messages[code_start + 1: code_end]
        code_messages = [
            each.replace('\n', '').replace('\r', '') for each in code_messages]
        
    save = {'5. Not able to save': None}
    if status_message == 'success' or status_message == 'failed':
        save = {'5. Successfully read': args[0]}
        if args[2]:
            save = {'5. Successfully read': args[2]}
    data = {
        '4. Status': status_message,
        '3. Code Messages': code_messages,
        '1. Maya File': args[0],
        '2. Source Code': args[1],
    }
    data.update(save)
    return data


def open_editer(file):
    editor = resources.getEditor()
    command = '%s %s' % (editor, file)
    os.system(command)


def get_codes(path):
    files = []
    for each in ['.py', '.mel']:
        pattern = '%s/*%s' % (path, each)
        current_files = glob.glob(pattern)
        files.extend(current_files)
    return files

