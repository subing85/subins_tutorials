import os
import json
import tempfile
import warnings

from datetime import datetime

from crowd import resource
from crowd.core import cdata
reload(data)


class ReadWrite(object):

    def __init__(self, **kwargs):
        super(ReadWrite, self).__init__(**kwargs)        
        self.comment = 'subin gopi tool kits Subin Crowds'
        self.created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        self.description = 'This data contain information about subin gopi tool kits crowd'
        self.type = None
        self.valid = True
        self.tag = None
        self.path = tempfile.gettempdir()
        self.format = 'json'
        self.name = None
        long_names = {
            'co': ['comment', self.comment],
            'cd': ['created_date', self.created_date],
            'de': ['description', self.description],
            'ty': ['type', self.type],
            'va': ['valid', self.valid],
            'tg': ['tag', self.tag],
            'pa': ['path', self.path],
            'fm': ['format', self.format],
            'na': ['name', self.name]
        }
        self.kwargs_data = self.get_input_data(long_names, kwargs)
        self.file_path = os.path.join(
            self.kwargs_data['path'], '%s.%s' % (self.kwargs_data['name'], self.kwargs_data['format']))

    def collect(self, input, type):
        result = {}
        input_path = resource.getInputPath(input)
        if not os.path.isdir(input_path):
            warnings.warn('not fount input called %s' % input, Warning)
            return
        for each_input in os.listdir(input_path):
            if os.path.isdir(each_input):
                continue
            if not each_input.endswith(self.format):
                continue
            self.file_path = os.path.join(input_path, each_input)
            data = self.read(all=True)
            if data['type'] != type:
                continue
            result.setdefault(data['tag'], data['data'])
        if not result:
            return None
        return result

    def get_input_data(self, long_names, input):
        kwargs_data = {}
        for k, v in long_names.items():
            if k in input:
                kwargs_data.setdefault(v[0], input[k])
            else:
                kwargs_data.setdefault(v[0], v[1])
        return kwargs_data

    def read(self, all=False):
        '''
        :param all <boolen>
        :example
            from crowd.core import readWrite
            rw = readWrite.ReadWrite(    
                fm='json',
                pa='/venture/subins_tutorials/crowd/resource/skeletons',
                na='biped')
            rw.read()
        '''
        data = None
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        if not all:
            return data['data']
        return data

    def write(self, data, force=False):
        '''
        :param data <dict>
        :param force <boolen>
        :example
            from crowd.core import readWrite
            rw = readWrite.ReadWrite(    
                fm='json',
                pa='/venture/subins_tutorials/crowd/resource/skeletons',
                na='biped',
                ty='skeleton',
                tg='biped')
            rw.write(data, force=True)
        '''
        if not force:
            if os.path.isfile(self.file_path):
                warnings.warn('already exists the file called %s' %
                              self.file_path, Warning)
                return
        if os.path.isfile(self.file_path):
            try:
                os.chmod(self.file_path, 0777)
                os.remove(self.file_path)
            except Exception as result:
                print(result)
        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))
        self.kwargs_data['data'] = data
        json_data = json.dumps(self.kwargs_data, indent=4)
        with open(self.file_path, 'w') as file:
            file.write(json_data)
        print 'write success!.', self.file_path
        
    @classmethod
    def sorted_data(cls, data):
        return cdata.sorted_order_data(data)

    
