import os
import json

from studio_pipe import resources
reload(resources)


class Dccs(object):
    
    def __init__(self, name):
        pass
    
    
    
class Shows(object):
    
    def __init__(self, name):
        pass
    
    
    
class Read(object):
    
    def __init__(self, name):
        pass
    
    
    def 
    
    

class Generic(object):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.format = '.json'
        self.config_path = os.path.join(
            resources.getInputPath(), '{}.{}'.format(self.name, self.format))

    def create(self, input_data, **kwargs):
        type = kwargs['type']
        tag = kwargs['tag']
        valid = kwargs['valid']
        description = kwargs['description']
        data = resources.getRowData(
            type, tag, valid, description, input_data)
        with(open(self.config_path, 'w')) as open_data:
            open_data.write(json.dumps(data, indent=4))
            return True

    def get(self):
        with(open(self.config_path, 'r')) as open_data:
            data = json.load(open_data)
            return data
