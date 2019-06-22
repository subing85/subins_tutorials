LONG_NAME = 'Object Type'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'validate'
VALID = True
LAST_MODIFIED = 'June 09, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To check is it joints scene?'
VERSION = 1.0
CLASS = 'InputJoint'

from pymel import core

from crowd.api import crowdPublish
from crowd.core import skeleton


class InputJoint(object):

    def __init__(self, input=None):
        print '\n#<%s> <%s> <%s>' % (BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.input = input
        crowd_publish = crowdPublish.Connect()
        self.result = self.check()

    def check(self):
        out, nodes, message = self.get_nodes()
        return out, nodes, message

    def get_nodes(self):
        nodes, message = skeleton.get_root_skeletons()
        if not nodes:
            return 'failed', nodes, message
        return 'success', nodes, message


def testRun():
    input_joint = InputJoint()
    result, data, message = input_joint.result
    print '\ntest run', result, data, message
    return result, data, message
