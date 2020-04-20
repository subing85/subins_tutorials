import os
import shutil
import tempfile
import warnings


def sorted_order(input_dict):
    data = {}
    stack = input_dict.items()    
    while stack:
        k, v = stack.pop()        
        if not isinstance(v, dict): 
            continue                
        data.setdefault(v['order'], []).append(k)
    result = sum(data.values(), [])    
    return result


def sort_dictionary(dictionary): # to remove
    sorted_data = {}
    for contents in dictionary:
        sorted_data.setdefault(
            dictionary[contents]['order'], []).append(contents)
    order = sum(sorted_data.values(), [])
    return order   


def make_argeuments(**kwargs):
    argeuments = ''
    for k, v in kwargs.items():
        if not v:
            argeuments += '%s=%s,' % (k, v)
            continue        
        argeuments += '%s=\'%s\',' % (k, v)
    return argeuments

    
def make_maya_batch(module, mayapy, commands, source_path=None):
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
        '#!%s'%mayapy,       
        'from maya import standalone',
        'standalone.initialize(name="python")',
        'from maya import OpenMaya',
        ]
    m_open = []    
    if source_path:    
        m_open = [
            'mfile = OpenMaya.MFileIO()',
            'mfile.open(\'%s\', None, True, mfile.kLoadDefault, True)'%source_path
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

