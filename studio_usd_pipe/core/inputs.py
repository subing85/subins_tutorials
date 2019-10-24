import os
import json

from studio_usd_pipe import resources


class Connect(object):

    def __init__(self, input):
        self.input_file = os.path.join(
            resources.getInputPath(), '{}.json'.format(input))
        self.all_data = self.read()
        self.data = None
        self.keys = None
        if self.all_data['enable']:
            self.data = self.all_data['data']
            self.keys = self.sort_input_data()
        
    def get(self, parent):
        for k, v in self.data.items():
            if v['parent']==parent:
                continue
            self.data.pop(k)
            self.keys.remove(k)
        
    def read(self):
        with (open(self.input_file, 'r')) as open_data:
            data = json.load(open_data)
            for k, v in data['data'].items():
                if v['enable']:
                    continue
                data['data'].pop(k)
            return data
        return None

    def sort_input_data(self):
        result = []
        index = 0
        while index < len(self.data) + 1:
            x = 0
            for k, v, in self.data.items():
                if x > len(self.data):
                    break
                if not v['enable']:
                    continue
                order = v['order']
                if order != index:
                    continue
                result.append(k)
                x += 1
            index += 1
        return result    


#input = Connect('tag')
#print input.keys
#print json.dumps(input.data, indent=4)
# input.get('scene')

