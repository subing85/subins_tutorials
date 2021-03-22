import os
import json
import time
import getpass

from datetime import datetime

currentTime = time.time()


def studio_json(data, path, **kwargs):
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
