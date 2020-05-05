import os
import copy

from studio_usd_pipe.api import studioShow

 
class Environ(object):
    
    def __init__(self, current_show, application=None):
        self.shows = studioShow.Show()
        self.current_show = current_show
        self.current_application = application      
          
        
    def get_environ_value(self, environ):
        if environ in os.environ:
            return os.environ[environ], True
        environ_data = self.get_environ_keys()
        if environ in environ_data:  # value is taken from show preset
            return environ_data[environ], False
        return None, None
    
    def get_specific_environ_value(self, application_type, application, key):
        '''
            :param application_type <str> 'show_applications'
            :param application <str> 'maya'
            :param key <str> 'path'
        '''       
        input_data = self.shows.get_show_preset_data(self.current_show)
        if application_type not in input_data: 
            return None        
        if application not in input_data[application_type]:
            return None
        if key not in input_data[application_type][application]:
            return None        
        specific_key = input_data[application_type][application][key]
        value, valid = self.get_environ_value(specific_key[0])
        return value, valid 

    def get_environ_keys(self):        
        environ_preset_data = self.get_environ_preset_data()
        environ_data = {}
        for each in environ_preset_data:
            for name in environ_preset_data[each]:
                environ_data.update(environ_preset_data[each][name])
        return environ_data

    def get_environ_preset_data(self):      
        headers = ['common_applications', 'show_applications', 'current_show']
        environ_data = {}
        for header in headers:
            environ_typed_data = self.get_environ_typed_preset_data(header)
            environ_data.setdefault(header, environ_typed_data)
        return environ_data
                
    def get_environ_typed_preset_data(self, env_type, input_data=None):  
        if not input_data:
            input_data = self.shows.get_show_preset_data(self.current_show)
        tmp_environ_typed_data = {}  
        if not input_data:
            print '#warnings not input data contain empty'
            return tmp_environ_typed_data
        if env_type not in input_data:
            print '#warnings not found %s in the data' % env_type
            return tmp_environ_typed_data
        
        if not input_data[env_type]:
            print '#warnings empty data found in %s' % env_type
            return tmp_environ_typed_data
        for each in input_data[env_type]:
            tmp_environ_typed_data.setdefault(each, {})
            for key in input_data[env_type][each]:
                contents = input_data[env_type][each][key]
                if not isinstance(contents, list):
                    continue
                tmp_environ_typed_data[each].setdefault(
                    input_data[env_type][each][key][0],
                    input_data[env_type][each][key][1]
                )
        if not self.current_application:
            return tmp_environ_typed_data
        environ_typed_data = copy.deepcopy(tmp_environ_typed_data) 
        for each in tmp_environ_typed_data:
            if env_type == 'current_show':
                continue 
            if self.current_application == each:
                continue
            environ_typed_data.pop(each)
        return environ_typed_data
    

    

        
#a = Environ('btm')
#b = a.get_specific_environ_value
#print json.dumps(b, indent=4)        
