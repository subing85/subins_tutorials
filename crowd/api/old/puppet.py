import warnings
import logging

from crowd.core import readWrite
from crowd.core import puppet

from crowd.api import crowdMaya

reload(puppet)
reload(crowdMaya)

from pprint import pprint


class Connect(object):

    def __init__(self):
        
        self.crowd_maya = crowdMaya.Connect()
        pass

    def create(self, root, tag=None):
        '''
        :param tag <str> example 'biped'
        from crowd.api import skeleton
        ske = skeleton.Skeleton()
        ske.create('biped')
        '''
        data = self.findInputs()
        if not tag:      
            tag = self.crowd_maya.skeleton_type(root)
        if tag not in data:
            logging.warning('Not found crowd type in the data')
            return        
        result = puppet.create_puppet(tag, root, data[tag])
        return result
    
    def findInputs(self):
        rw = readWrite.ReadWrite()
        data = rw.collect('puppets', 'puppet')
        return data
    
    def findSkeletons(self):
        rw = readWrite.ReadWrite()
        data = rw.collect('puppets', 'puppet')
        return data

    
