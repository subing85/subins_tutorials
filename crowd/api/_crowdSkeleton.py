import warnings
from pprint import pprint
from crowd.core import readWrite
from crowd.core import skeleton
from crowd.core import generic
from crowd.api import crowdPublish

reload(readWrite)
reload(skeleton)
reload(crowdPublish)


class Connect(object):

    def __init__(self, parent=None):
        self.parent = parent
        self.proxy_node = []

    def getTags(self):
        publish = crowdPublish.Connect(type='skeleton')
        return publish.getTags()

    def create(self, tag, position=None):
        '''
            :param tag <str> example 'biped'
            from crowd.api import skeleton
            ske = skeleton.Connect()
            ske.create('biped')
        '''
        data, orders = self.findInputs()
        if tag not in data:
            warnings.warn('not fount tag called %s' % tag, Warning)
            return
        root_dag_path, result = skeleton.create_skeleton(
            tag, data[tag], position=position)
        return root_dag_path, result

    def findInputs(self):
        rw = readWrite.Connect()
        data, orders = rw.collect('skeletons', 'skeleton')
        return data, orders

    def findSkeletons(self):
        skeletons = generic.get_root_children()
        return skeletons

    def make_skeleton(self, **kwargs):
        pass


# Skeleton().findSkeletons()
