LONG_NAME = 'Object Type'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'validate'
VALID = True
LAST_MODIFIED = 'June 24, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To check is it joints in the scene?'
VERSION = '0.0.1'


from crowd.core import skeleton


class InputJoints(object):

    def __init__(self, input=None):
        print '\n\t#<%s> <%s> <%s>' % (
            BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.input = input
        self.result = self.get_nodes()

    def get_nodes(self):
        node, message = skeleton.get_root_skeletons()
        if not node:
            return 'failed', node, message
        return 'success', node, message


def execute():
    input_joint = InputJoints()
    result, data, message = input_joint.result
    print '\t\tresult', result, data, message
    return result, data, message
