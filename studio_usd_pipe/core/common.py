import os
import json
import shutil
import pkgutil
import tempfile
import warnings

from datetime import datetime

    
def sort_dictionary(input_dict): #**
    data = {}
    stack = input_dict.items()    
    while stack:
        k, v = stack.pop()
        if not isinstance(v, dict): 
            continue
        if 'order' not in v:
            continue
        data.setdefault(int(v['order']), []).append(k.encode())
    result = sum(data.values(), [])    
    return result


def sorted_show_order(input_dict): #**
    data = {}
    stack = input_dict.items()
    
    sorted_data = {}
    for show in input_dict:
        show_order = input_dict[show]['current_show']['show']['order']
        sorted_data.setdefault(
            int(show_order), []).append(show)  
    order = sum(sorted_data.values(), [])
    return order  


def get_template_header(): #**
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


def get_modules(dirname, module_types=None): #**
    module_data = {}
    for module_loader, name, ispkg in pkgutil.iter_modules([dirname]):
        loader = module_loader.find_module(name)
        module = loader.load_module(name)
        if not hasattr(module, 'TYPE'):
            continue            
        if not module.VALID:
            continue
        if not hasattr(module, 'VALID'):
            continue
        if not hasattr(module, 'ORDER'):
            continue
        if module_types:        
            if module.TYPE not in module_types:
                continue
        if module.TYPE not in module_data:
            module_data.setdefault(module.TYPE, {})
        module_data[module.TYPE].setdefault(module.ORDER, module)
    return module_data


def get_modified_date():
    modified = datetime.now().strftime("%Y %d %B %A, %I:%M:%S %p")
    return modified


def get_time_date(time):
    dt_object = datetime.fromtimestamp(time)
    modified = dt_object.strftime("%Y %d %B %A, %I:%M:%S %p")
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


