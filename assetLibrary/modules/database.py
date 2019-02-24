import shelve

import os
import copy
import warnings

class DataBase(object):
    
    def __init__(self, path):        
        self.path = path    
    
    def create(self, data=None, force=False):
        if os.path.isfile(self.path):            
            if not force:
                warnings.warn('\nalready exists the data base!..')                
                return False
            try:
                os.chmod(self.path, 0777)
                os.remove(self.path)
            except Exception as result:
                print result
                
        self.db = shelve.open(self.path)
        
        if data:        
            for k, v in data.items():
                try:
                    self.db[k] = v
                except:
                    pass            
        self.db.close ()
        
    def get(self, key):
        if not os.path.isfile(self.path):
            warnings.warn('\nnot found data base!...')
            return        
        self.db = shelve.open(self.path, flag='r')
        value = None
        if key in self.db:
            value = self.db[key]
        self.db.close()
        return value
    
    def get_all(self):
        if not os.path.isfile(self.path):
            warnings.warn('\nnot found data base!...')
            return        
        self.db = shelve.open(self.path, flag='r')
        self.data = {}
        for k, v in self.db.items():
            self.data.setdefault(k, v)
        self.db.close()        
        return self.data   
    
    def update(self, key, value):
        if not os.path.isfile(self.path):
            warnings.warn('\nnot found data base!...')
            return          
        self.db = shelve.open(self.path, writeback=True)
        self.db[key] = value
        self.db.close()
    
    def remove(self, key):
        if not os.path.isfile(self.path):
            warnings.warn('\nnot found data base!...')
            return
        self.db = shelve.open(self.path, writeback=True)
        if key in self.db:
            self.db.pop(key, None)
        self.db.close()
    
    def delete(self):
        if not os.path.isfile(self.path):
            warnings.warn('\nnot found data base!...')
            return False   
        try:
            os.chmod(self.path, 0777)
            os.remove(self.path)
        except Exception as result:
            print result        
        return True
            
             
        
#===============================================================================
# from pprint import pprint
# path = '/venture/temp/abd.txt'
# my_db = DataBase(path)
# my_db.create(data={'subin': 'base', 'abin': 'technicolor', 'albrt': 'bluesssky'}, force=True)    
# # r = my_db.update('sachin_85', 'pixar')
# #my_db.delete()
# #rm = my_db.remove('subin')
# all = my_db.get_all()
# pprint(all)
#===============================================================================



    