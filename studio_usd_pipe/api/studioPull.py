import json
from studio_usd_pipe.core import bundles


class Pull(object):
    
    def __init__(self, current_application, current_subfiled):
        self.current_subfiled = current_subfiled
        self.current_application = current_application
        self.mode = 'creator'
    
    def get_creators(self):
        bundle = bundles.Bundles(self.current_application, 'pull', self.current_subfiled)
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
        
