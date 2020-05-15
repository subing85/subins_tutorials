LONG_NAME = 'collect skeleton label inputs'
ICON = 'lable_inputs'
ORDER = 0
MODULE_TYPE = 'puppet'
BUNDLE_TYPE = 'extract'
VALID = True
LAST_MODIFIED = 'June 25, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To collect puppet configure data!...'
VERSION = '0.0.1'

from crowd.core import puppet
reload(puppet)


class JointData(object):

    def __init__(self, input=None):
        print '\n\t#<%s> <%s> <%s>' % (
            BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.input = input
        self.result = self.get_configure_data()

    def get_configure_data(self):
        data, message = puppet.get_puppet_data()
        if not data:
            return 'failed', None, message
        return 'success', data, 'input'


def execute():
    input_joint = JointData()
    result, data, message = input_joint.result
    print '\t\tresult', result, data, message
    return result, data, message
