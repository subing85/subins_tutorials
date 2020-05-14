import warnings

from pprint import pprint

from crowd.core import readWrite
from crowd.api import crowdMaya


class Connect(object):

    def __init__(self, tag):
        self.tag = tag
        
    def store_animation(self, nodes, path):        
        crowd_maya = crowdMaya.Connect()
        anim_data = crowd_maya.read_ainmations(nodes)
        
        rw = readWrite.ReadWrite()
        rw.file_path = path
        rw.write(anim_data, force=True)        
    
    def write_puppet(self):       
        data = self.findSkeletons()
        if self.tag not in data:
            warnings.warn('not fount tag called %s' % self.tag, Warning)
            return
        
        # pprint(data[self.tag])
        
    def findSkeletons(self):
        rw = readWrite.ReadWrite()
        data = rw.collect('puppets', 'puppet')
        return data        

    
