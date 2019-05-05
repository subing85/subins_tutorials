import warnings


from crowd import resource
from crowd.core import readWrite
from crowd.core import skeleton

class Skeleton(object):
    
    def __init__(self):
        pass
    
    
    def create(self, tag):
        '''
        :param tag <str> example 'biped'
        from crowd.api import skeleton
        ske = skeleton.Skeleton()
        ske.create('biped')
        '''        
        data = self.findSkeletons()
        if tag not in data:
            warnings.warn('not fount tag called %s'%tag, Warning)
            return
        result = skeleton.create_skeleton(data[tag])
        return result

    def findSkeletons(self):        
        rw = readWrite.ReadWrite()        
        data = rw.collect('skeletons', 'skeleton')
        return data
    
    
# Skeleton().findSkeletons()
