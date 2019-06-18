LONG_NAME = 'Extract Test 2'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'extract'
VALID = True
LAST_MODIFIED = 'June 09, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To Check is its Joints?'
VERSION = 1.0
CLASS = 'InputJoint'

from pymel import core

from crowd.api import crowdPublish


class InputJoint(object):

    def __init__(self, input=None):
        print '\n%s WIP. %s' % (MODULE_TYPE, COMMENTS)
        self.input = input
        crowd_publish = crowdPublish.Connect()
        self.result = self.check()

    def check(self):
        out, nodes, message = self.get_nodes()
        return out, nodes, message

    def get_nodes(self):
        '''
        crowd_publish = crowdPublish.Connect(type=self.publish_type)
        bundle_keys = crowd_publish.getBundleKeys()
        '''
        default_nodes = ['persp', 'top', 'front', 'side']
        maya_nodes = core.ls(assemblies=True)
        nodes = [each.name().encode()
                 for each in maya_nodes if each.name() not in default_nodes]
        if len(nodes) > 1:
            return 'failed', nodes, 'more than one hierarchy found!..'
        if len(nodes) == 0:
            return 'error', 'None', 'not found any hierarchy!..'
        return 'success', nodes, 'shader'


def testRun():
    input_joint = InputJoint()
    result, data, message = input_joint.result
    print '\ntest run', result, data, message
    return result, data, message
