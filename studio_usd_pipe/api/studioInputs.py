import json
from studio_usd_pipe.core import bundles
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPipe


class Inputs(object):
    
    def __init__(self, pipe, application=None):
        self.pipe = pipe
        self.application = application
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe)        
        self.tags = [        
            'order',
            'key',
            'name',
            'location'
            ]
        
    
    def get_push_type(self):
        return 'extractor'
    
    def get_pull_type(self):
        return 'creator'    
        
    def find_subfileds(self):
        subfield = self.spipe.pipe_inputs['subfield']['values']        
        return subfield
    
    def get_usd_extractor_keys(self):
        extractor_keys = {
            'model': 'model_usd',
            'uv': 'uv_usd',            
            'shader': 'shader_usd'
            }
        return extractor_keys
    
    def get_puppet_extractor_keys(self):
        extractor_keys = {
            'puppet': 'puppet_scene'
            }
        return extractor_keys
    
    def get_composition_extractor_keys(self):
        extractor_keys = {
            'composition': 'composition'
            }
        return extractor_keys
    
            
    
        
    
    def find_extractor_order(self, verbose=True):
        types = self.get_push_type()                
        extractor_order = self.find_specific_bundle(types, self.tags[0], verbose=False)
        if verbose:
            print json.dumps(extractor_order, indent=4)
        return extractor_order       
    
    def find_extractor_key(self, verbose=True):
        types = self.get_push_type()                
        extractor_key = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(extractor_key, indent=4)
        return extractor_key 
     
    def find_extractor_name(self, verbose=True):
        types = self.get_push_type()    
        extractor_name = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(extractor_name, indent=4)
        return extractor_name
    
    def find_extractor_location(self, verbose=True):
        types = self.get_push_type()         
        extractor_location = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(extractor_location, indent=4)
        return extractor_location
    
    def find_creator_order(self, verbose=True): 
        types = self.get_pull_type()        
        creator_order = self.find_specific_bundle(types, self.tags[0], verbose=False)
        if verbose:
            print json.dumps(creator_order, indent=4)
        return creator_order       
    
    def find_creator_key(self, verbose=True):  
        types = self.get_pull_type()        
        creator_key = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(creator_key, indent=4)
        return creator_key 
     
    def find_creator_name(self, verbose=True): 
        types = self.get_pull_type()         
        creator_name = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(creator_name, indent=4)
        return creator_name
    
    def find_creator_location(self, verbose=True):
        types = self.get_pull_type()          
        creator_location = self.find_specific_bundle(types, self.tags[1], verbose=False)
        if verbose:
            print json.dumps(creator_location, indent=4)
        return creator_location    
    
    def find_specific_bundle(self, types, value, verbose=True):
        subfields_contents = None
        if types == 'extractor':
            subfields_contents = self.find_subfields_extractors(verbose=False)
        if types == 'creator':
            subfields_contents = self.find_subfields_creators(verbose=False)
        specific_bundle = {}
        if not subfields_contents:
            return specific_bundle
        for subfield, contents in subfields_contents.items():            
            for each in contents:
                specific_bundle.setdefault(
                    subfield, []).append(contents[each][value])
        if verbose:
            print json.dumps(specific_bundle, indent=4)
        return specific_bundle
    
    def find_subfield_extractors(self, subfiled, verbose=True):
        '''
            input = Inputs('assets', 'maya')
            input.find_subfield_extractors('model')
        '''             
        types = self.get_push_type() 
        subfield_extractors = self.get_bundles_info('push', types, subfiled, verbose=False)
        if verbose:
            print json.dumps(subfield_extractors, indent=4)               
        return subfield_extractors    
    
    def find_subfields_extractors(self, verbose=True):
        '''
            input = Inputs('assets', 'maya')
            input.find_subfields_extractors()
        '''          
        subfileds = self.find_subfileds()
        subfields_extractors = {}
        for subfiled in subfileds:
            subfield_extractors = self.find_subfield_extractors(subfiled, verbose=False)
            subfields_extractors.setdefault(subfiled, subfield_extractors)
        if verbose:
            print json.dumps(subfields_extractors, indent=4)            
        return subfields_extractors
    
    def find_subfield_creators(self, subfiled, verbose=True):
        '''
            input = Inputs('assets', 'maya')
            input.find_subfield_creators('model')
        '''          
        types = self.get_pull_type() 
        subfield_extractors = self.get_bundles_info('pull', types, subfiled, verbose=False)
        if verbose:
            print json.dumps(subfield_extractors, indent=4)               
        return subfield_extractors  
    
    def find_subfields_creators(self, verbose=True):
        '''
            input = Inputs('assets', 'maya')
            input.find_subfields_creators()        
        '''
        subfileds = self.find_subfileds()
        subfields_extractors = {}
        for subfiled in subfileds:
            subfield_extractors = self.find_subfield_creators(subfiled, verbose=False)
            subfields_extractors.setdefault(subfiled, subfield_extractors)
        if verbose:
            print json.dumps(subfields_extractors, indent=4)            
        return subfields_extractors    
    
    def get_bundles_info(self, header, type, subfiled, verbose=True):  # get push KEY values
        '''
            :param header <str> 'push' or 'pull'
            :param type <str> 'extractor' or 'creator'
        '''        
        bundles_info = {}
        bundle = bundles.Bundles(self.application, header, subfiled)
        bundle_data = bundle.get_bundles(types=[type])
        if not bundle_data:
            return bundles_info            
        if type not in bundle_data:
            return bundles_info
        for index in bundle_data[type]:
            module = bundle_data[type][index]
            contents = {
                self.tags[0]: module.ORDER,
                self.tags[1]: module.KEY,
                self.tags[2]: module.NAME,
                self.tags[3]: module.__file__
                }        
            bundles_info.setdefault(
                module.__name__, contents
                )
        if verbose:
            print json.dumps(bundles_info, indent=4)               
        return bundles_info

