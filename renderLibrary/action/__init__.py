import os
import time
import pkgutil

from renderLibrary import resources
reload(resources)


class Connect(object):
    
    def __init__(self, typed, dirname, label, layer):
        self.context = {
            'dirname': dirname,
            'path': os.path.join(dirname, label),
            'label': label,
            'typed': typed,
            'layer': layer
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
        time_stamp = time.time()
        _modules = self.get_modules()  
        print '\n', 'action', self.context['typed']
        for order, modules in _modules.items():
            print '\n# index:', order
            for module in modules:
                print 'name: '.rjust(15) + module.NAME
                print 'action: '.rjust(15) + module.ACTION
                print 'comments: '.rjust(15) + module.COMMENTS
                
                self.context['order'] = order
                self.context['name'] = module.NAME
                self.context['action'] = module.ACTION     
                self.context['type'] = module.TYPE
                self.context['comments'] = module.COMMENTS
                self.context['enable'] = module.ENABLE
                self.context['time_stamp'] = time_stamp
                
                valid, message, result, results = module.execute(self.context)
                
                print '\n'
                if not valid:
                    raise RuntimeError('%s, %s' % (module.ACTION, message))
                
                self.context[order] = {
                    'name': module.NAME,
                    'type': module.TYPE,
                    'action': module.ACTION,
                    'comments': module.COMMENTS,
                    'enabel': module.ENABLE,
                    'result': result
                    }
                
                if result:   
                    self.context[order]['result'] = result
                
                if results:  
                    self.context[order]['results'] = results    
                                
                self.context.pop('name')
                self.context.pop('action')
                self.context.pop('type')
                self.context.pop('comments')
                self.context.pop('enable')
                self.context.pop('order')
                
        import json
        print '# remove', json.dumps(self.context, indent=4)
        
    def get_modules(self):
        modules = {}
        for loader, name, ispkg in pkgutil.iter_modules([self.action_path]):
            loader = loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'ENABLE'):
                continue
            if not module.ENABLE:
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

