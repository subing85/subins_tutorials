import os
import json
import tempfile
import warnings
import getpass

from datetime import datetime

from crowd import resource
from crowd.core import cdata
reload(cdata)


class Connect(object):

    def __init__(self, **kwargs):
        super(Connect, self).__init__()
        self.comment = 'subin gopi tool kits Subin Crowds'
        self.created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        self.description = 'This data contain information about subin gopi tool kits crowd'
        self.type = 'test_type'
        self.valid = True
        self.tag = 'tmp_publish'
        self.path = tempfile.gettempdir()
        self.format = 'json'
        self.name = 'test'
        self.author = 'Subin Gopi'
        long_names = {
            'co': ['comment', self.comment],
            'cd': ['created_date', self.created_date],
            'de': ['description', self.description],
            'ty': ['type', self.type],
            'va': ['valid', self.valid],
            'tg': ['tag', self.tag],
            'pa': ['path', self.path],
            'fm': ['format', self.format],
            'na': ['name', self.name],
            'au': ['author', self.author],
            'wa': ['warning', '# WARNING! All changes made in this file will be lost!'],
            'ur': ['user', getpass.getuser()],
            'su': ['source', None],
            'og': ['origin', None],
            'cp': ['components', None],
            'lo': ['location', None]
        }
        self.kwargs_data = self.get_input_data(long_names, kwargs)
        self.file_path = os.path.join(
            self.kwargs_data['path'], self.kwargs_data['tag'], '%s.%s' % (self.kwargs_data['name'], self.kwargs_data['format']))

    def collect(self, input, type):
        result = {}
        orders = {}
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
            orders.setdefault(data['order'], []).append(data['tag'])
        if not result or not orders:
            return None, None
        return result, orders

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
                warnings.warn(
                    'already exists the file called %s' % self.file_path, Warning)
                return
        if force:
            self.force()

        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))

        self.kwargs_data['data'] = data
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(self.kwargs_data, indent=4))
        print 'write success!...', '<%s>' % self.file_path

    def commit(self, force=False):
        keys = [
            'description',
            'author',
            'warning',
            'user',
            'type',
            'tag',
            'components',
            'location',
            'source',
            'origin',
            'comment',
            'valid'
        ]
        pyton_data = []
        dict_data = {}
        for each_key in keys:
            if each_key not in self.kwargs_data:
                continue
            pyton_data.append('%s = %s' %
                              (each_key, self.kwargs_data[each_key]))
            dict_data.setdefault(each_key, self.kwargs_data[each_key])

        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))

        with open(self.file_path, 'w') as file:
            # file.write('\n'.join(pyton_data))
            file.write(json.dumps(dict_data, indent=4))
        print 'write success!...', '<%s>' % self.file_path
        return self.file_path

    def force(self):
        if os.path.isfile(self.file_path):
            try:
                os.chmod(self.file_path, 0777)
                os.remove(self.file_path)
            except Exception as result:
                print(result)
        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))
            return self.file_path
        return None

    @classmethod
    def sorted_data(cls, data):
        return cdata.sorted_order_data(data)


# rw.write(data, force=True)
