import json
from studio_usd_pipe.core import bundles

from studio_usd_pipe.api import studioPipe


class Pull(object):
    
    def __init__(self, application=None, subfield=None):
        self.current_application = application
        self.current_subfield = subfield
        self.mode = 'creator'
    
    def get_creators(self):
        bundle = bundles.Bundles(self.current_application, 'pull', self.current_subfield)
        modules = bundle.get_bundles(types=[self.mode])
        if not modules:
            return {}
        if 'creator' not in modules:
            return {}        
        return  modules['creator']  
    
    def do_pull(self, module, **kwargs):
        valid, values, message = module.execute(**kwargs)
        print '# header:', self.mode
        print 'module key: '.rjust(15), module.KEY
        for value in values:
            print ': '.rjust(15), value
        print 'message: '.rjust(15), message
        return valid, message
       
        
  
    
