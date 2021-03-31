import os
import json
import time
import getpass

from datetime import datetime

from renderLibrary.utils import studioMaya 


def studio_json(path, data, **kwargs):
    time_stamp = kwargs.get('time_stamp') or time.time()
    
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
        
    dt_object = datetime.fromtimestamp(time_stamp)
    
    input_data = {
        'comments': kwargs.get('comments'),
        '#copyright': '(c) 2021, Subin Gopi All rights reserved.',
        'modified date': dt_object.strftime("%Y:%B:%d:%A-%I:%M:%S:%p"),
        'author': 'Subin Gopi',
        'warning': '# WARNING! All changes made in this file will be lost!',
        'type': kwargs.get('type'),
        'tag': kwargs.get('tag'),
        'valid': kwargs.get('valid'),
        'user': getpass.getuser(),
        'action': kwargs.get('action'),
        'order': kwargs.get('order'),
        'data': data
        }
        
    with (open(path, 'w')) as file:
        file.write(json.dumps(input_data, indent=4))
    
    os.utime(path, (time_stamp, time_stamp))
    
    return True


def studio_geometry(dirname, data, **kwargs):    
    output_path = os.path.join(dirname, 'geometry.json')
    studio_json(output_path, data, **kwargs)
    return output_path


def studio_shader(dirname, data, **kwargs):
    output_path = os.path.join(dirname, 'shader')
    time_stamp = kwargs.get('time_stamp') or time.time()
    
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    
    output_paths = [] 
    # export shader maya file
    for node, contents in data['shader'].items():
        studioMaya.addStudioAttribute(node, contents)
        shader_path = os.path.join(output_path, '%s.ma' % node)
        studioMaya.exportSelection([node], shader_path, format='mayaAscii')
        os.utime(shader_path, (time_stamp, time_stamp))   
        data['shader'][node]['relative_path'] = 'shader/%s' % '%s.ma' % node
        data['shader'][node]['path'] = shader_path
        output_paths.append(shader_path)
        
    output_path = os.path.join(dirname, 'shader.json')
    studio_json(output_path, data, **kwargs)
    
    return output_path, output_paths
    
    
def studio_light(dirname, data, **kwargs):    
    output_path = os.path.join(dirname, 'light.json')
    studio_json(output_path, data, **kwargs)
    return output_path   
    
        

