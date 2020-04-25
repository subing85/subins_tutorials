import os
import json
import shutil
import tempfile
import warnings

from datetime import datetime

    
def sorted_order(input_dict):
    data = {}
    stack = input_dict.items()    
    while stack:
        k, v = stack.pop()
        if not isinstance(v, dict): 
            continue
        if 'order' not in v:
            continue
        data.setdefault(int(v['order']), []).append(k)
    result = sum(data.values(), [])    
    return result


def sorted_show_order(input_dict):
    data = {}
    stack = input_dict.items()    
    while stack:
        k, v = stack.pop()
        if not isinstance(v, dict): 
            continue
        if 'show' not in v:
            continue
        if 'show_order' not in v['show']:
            continue
        data.setdefault(v['show']['show_order'], []).append(k)
    result = sum(data.values(), [])    
    return result    
    

def sort_dictionary(dictionary):  # to remove
    sorted_data = {}
    for contents in dictionary:
        sorted_data.setdefault(
            dictionary[contents]['order'], []).append(contents)
    order = sum(sorted_data.values(), [])
    return order


def get_template_header():
    headers = {
        'created_by': 'subin gopi',
        'author': 'Subin. Gopi (subing85@gmail.com)',
        '#copyright': '(c) 2019, Subin Gopi All rights reserved.',
        'modified': '*******',
        'description': '********',
        'warning': '# WARNING! All changes made in this file will be lost!',
        'enable': True,
        'type': '****'
        }
    return headers


def get_modified_date():
    modified = datetime.now().strftime("%Y %d %B %A, %H:%M:%S %p")
    return modified


def get_time_date(time):
    dt_object = datetime.fromtimestamp(time)
    modified = dt_object.strftime("%Y %d %B %A, %H:%M:%S %p")
    return modified


def read_json(path):
    data = None
    with open(path, 'r') as file:
        data = json.load(file)
    return data











def make_argeuments(**kwargs):
    argeuments = ''
    for k, v in kwargs.items():
        if not v:
            argeuments += '%s=%s,' % (k, v)
            continue        
        argeuments += '%s=\'%s\',' % (k, v)
    return argeuments

    
def make_maya_batch(module, mayapy, commands, source_path=None):  # to remove
    batch_path = os.path.join(tempfile.gettempdir(), '%s.py' % module)
    if os.path.isfile(batch_path):
        try:
            os.chmod(batch_path, 0777)
        except Exception as error:
            warnings.warn(str(error), Warning)
        try:
            os.remove(batch_path)
        except Exception as error:
            warnings.warn(str(error), Warning)
    prefxi = [
        '#!%s' % mayapy,
        'from maya import standalone',
        'standalone.initialize(name=\'python\')',
        'from maya import OpenMaya',
        ]
    m_open = []    
    if source_path:    
        m_open = [
            'mfile = OpenMaya.MFileIO()',
            'mfile.open(\'%s\', None, True, mfile.kLoadDefault, True)' % source_path
            ]
    suffix = [
        'standalone.uninitialize(name=\'python\')'
        ]
    commands = prefxi + m_open + commands + suffix
    with open(batch_path, 'w') as batch:
        batch.write('\n'.join(commands))
        try:
            os.chmod(batch_path, 0o777)
        except:
            pass
        return batch_path

    
def data_exists(path, force): 
    if os.path.exists(path):      
        if not force:
            return True          
        os.chmod(path, 0777)
        try:
            os.remove(path)
            return True
        except Exception as error:
            return False
    else:
        return True

    
def remove_directory(path):
    if not os.path.isdir(path):
        return True
    try:
        os.chmod(path, 0777)
    except Exception as error:
        print '# warnings', error
    try:
        shutil.rmtree(path)   
    except Exception as error:
        print '# warnings', error

