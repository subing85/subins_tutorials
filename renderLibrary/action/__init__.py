import os
import glob
import json
import time
import pkgutil
import warnings

from renderLibrary import resources
from renderLibrary.core import _import


class Connect(object):
    
    def __init__(self, dirname, label, layer):
        self.context = {
            'dirname': dirname,
            'path': os.path.join(dirname, label),
            'label': label,
            'layer': layer
            }
        self.format = '.json'
    
    def _publish(self):
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
        _modules = self.get_modules('publish')  
        print '\n', 'action type: publish'
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
        
    def _build(self):
        _modules = self.get_modules('build')   
        
        for order, modules in _modules.items():
            print '\n# index:', order
            for module in modules:
                if not hasattr(module, 'TAG'):
                    continue
                print 'name: '.rjust(15) + module.NAME
                print 'action: '.rjust(15) + module.ACTION
                print 'comments: '.rjust(15) + module.COMMENTS
                print 'tag: '.rjust(15) + module.TAG
                
                self.context['tag'] = module.TAG
                self.context['souce_path'] = os.path.join(
                    self.context['path'], '%s%s' % (module.TAG, self.format))
                
                data, tag = _import.studio_json(self.context['souce_path'])
              
                if tag != module.TAG:
                    print '\nimport module tag:', module.TAG
                    print 'export json preset:', tag
                    warnings.warn('not match tag from import module to export json preset')
                    continue
                
                self.context['data'] = data         
                
                valid, message, result, results = module.execute(self.context)
                
                print '\n'
                if not valid:
                    raise RuntimeError('%s, %s' % (module.ACTION, message))                
        
    def get_modules(self, typed):
        _path = resources.getActionPath(typed)
        modules = {}
        for loader, name, ispkg in pkgutil.iter_modules([_path]):
            loader = loader.find_module(name)
            module = loader.load_module(name)
            if not hasattr(module, 'ENABLE'):
                continue
            if not module.ENABLE:
                continue
            if not hasattr(module, 'ORDER'):
                continue
            if not hasattr(module, 'TYPE'):
                continue            
            if module.TYPE != typed:
                continue
            modules.setdefault(module.ORDER, []).append(module)
        return modules

#===============================================================================
# path  = '/venture/shows/batman/render/'    
# act = Connect('publish', path)
# act.do()
#===============================================================================

