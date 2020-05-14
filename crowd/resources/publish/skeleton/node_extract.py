LONG_NAME = 'export joint'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'extract'
VALID = True
LAST_MODIFIED = 'June 24, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To collect skeleton data!...'
VERSION = '0.0.1'

from crowd.core import skeleton


class JointData(object):

    def __init__(self, input=None):
        print '\n\t#<%s> <%s> <%s>' % (
            BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.input = input
        self.result = self.get_nodes()

    def get_nodes(self):
        from pymel import core        
        joints = core.ls(type='joint')
        if not joints:
            return 'failed', None, 'not fount any joints' 
        data = skeleton.get_skeleton_inputs(joints)
        return 'success', data, 'skeleton'


def execute():
    input_joint = JointData()
    result, data, message = input_joint.result
    print '\t\tresult', result, data, message
    return result, data, message
