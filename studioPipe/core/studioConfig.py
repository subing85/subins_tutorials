
import os
import sys
sys.path.append('/venture/subins_tutorials')


from studioPipe import resources
from studioPipe.api import studioPreferences
reload(studioPreferences)

class Connect(object):
    
    def __init__(self):
        self.studio_preferences = studioPreferences.Connect()
        
    def has_valid(self):
        return self.studio_preferences.hasPreferences()
        
    def get_default(self): 
        default_data = resources.getDefaultPreferences()
        return default_data                

    def get_exists_output(self):
        data = self.studio_preferences.getOutputData()
        input_data = data
        return input_data
    
    def find_exists(self):
        input_data = self.get_exists_output()        
        for k, v in input_data.items():
            if k=='enable':
                continue            
            if k.upper() not in os.environ:
                print k.upper(), 'not found'
            else:            
                print k.upper(), ': ', os.environ[k.upper()]
        return input_data    

    def set(self):
        input_data = self.get_exists_output()        
        for k, v in input_data.items():
            if k=='enable':
                continue
            os.environ[k.upper()] = str(v)

            
#===============================================================================
# a = Connect()
# b = a.set()
# print b
#===============================================================================