LONG_NAME = 'export joint'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'puppet'
BUNDLE_TYPE = 'extract'
VALID = True
LAST_MODIFIED = 'June 09, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To collect puppet configure data!...'
VERSION = '0.0.1'


from crowd.core import puppet


class JointData(object):

    def __init__(self, input=None):
        print '\n#<%s> <%s> <%s>' % (BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.input = input
        self.result = self.get_configure_data()

    def get_configure_data(self):
        data, message = puppet.get_puupet_data()
        if not data:
            return 'failed', None, message
        return 'success', data, 'puppet'


def testRun():
    input_joint = JointData()
    result, data, message = input_joint.result
    print '\npublish run', result, data, message
    return result, data, message
