


class Connect(object):
    
    def __init__(self, name, **kwargs):
        
        self.bundle = None
        if 'bundle' in kwargs:
            self.bundle  = kwargs['bundle']
        
    def isValid(self):
        pass 
           
    def currentVersion(self):
        pass

    def nextVersion(self):
        pass
    
    def get(self):
        pass    
        
    def pack(self):
        pass    
    
    def set(self):
        pass
    
    def release(self):
        pass  

