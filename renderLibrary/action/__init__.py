import pkgutil

from pprint import pprint

from renderLibrary import resources
reload(resources)



class Connect(object):
    
    def __init__(self, typed, path, name, layer):
        self.context = {
            'path': path,
            'name': name,
            'typed': typed,
            'layer': name
            }
        self.action_path = resources.getActionPath(typed)

    
    def do(self):
        '''
        :example
            from renderLibrary import action
            reload(action)
            path  = '/venture/shows/batman/library/render'
            name = 'day_light'
            act = action.Connect('publish', path, name)
            act.do()       
        '''                
        _modules = self.get_modules()  
        print '\n', 'action', self.context['typed']
        for order, modules in _modules.items():
            print 'index:', order
            self.context['order'] = order
            for module in modules:
                print '\t', module.ACTION
                print '\t', module.__file__
                print '\t', module.NAME
                print '\t', module.COMMENTS
                self.context['action'] = module.ACTION     
                self.context['order'] = module.ORDER     
                valid, message = module.execute(self.context)
                print '\n'
                if not valid:
                    raise RuntimeError('%s, %s' %(module.TAG, message))
            self.context.pop('order')
            
        import json
        print json.dumps(self.context, indent=4)
        
    def get_modules(self):
        modules = {}
        for loader, name, ispkg in pkgutil.iter_modules([self.action_path]):
            loader = loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'ENABLE'):
                continue
            if not hasattr(module, 'ORDER'):
                continue
            if module.TYPE != self.context.get('typed'):
                continue
            modules.setdefault(module.ORDER, []).append(module)
        return modules     

#===============================================================================
# path  = '/venture/shows/batman/render/'    
# act = Connect('publish', path)
# act.do()
#===============================================================================

