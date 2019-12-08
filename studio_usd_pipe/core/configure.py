import json
from studio_usd_pipe import resource


class Configure(object):
    
    def __init__(self):
        self.context = self.get_data()       
        
    def maya(self):
        self.lib = self.context['maya']        
        self.name = self.lib['name']
        self.pretty = self.lib['pretty']
        self.version = self.lib['version']

    def tool(self):
        self.lib = self.context['tool']        
        self.name = self.lib['name']
        self.pretty = self.lib['pretty']
        self.version = self.lib['version']
        
    def os(self):
        self.lib = self.context['os']        
        self.name = self.lib['name']
        self.pretty = self.lib['pretty']
        self.version = self.lib['version']
            
    def get_data(self):        
        data = resource.getConfigureData()
        return data
