LONG_NAME = 'create puppet'
ICON = 'puppet'
ORDER = 0
MODULE_TYPE = 'puppet'
BUNDLE_TYPE = 'create'
VALID = True
LAST_MODIFIED = 'June 16, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To create skeleton'
VERSION = 1.0
CLASS = 'CreateNode'


from pymel import core

from crowd.core import puppet

reload(puppet)


class CreateNode(object):

    def __init__(self, **kwargs):
        print '\n#<%s> <%s> <%s>' % (BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.type = None
        self.tag = None
        self.input = None
        self.position = [0, 0, 0]
        self.parent = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'tag' in kwargs:
            self.tag = kwargs['tag']
        if 'input' in kwargs:
            self.input = kwargs['input']
        if 'position' in kwargs:
            self.position = kwargs['position']
        if 'parent' in kwargs:
            self.parent = kwargs['parent']
        self.result = self.make()

    def make(self):        
        print 'puppet\t', puppet
        reload(puppet)
        puppet.create_puppet(self.tag, self.input)
        
        print '\nDone.....................'
        #try:
        # root_dag_path, parent_data = puppet.create_puppet(self.tag, self.input)
        #    return 'success', root_dag_path, parent_data
        #except Exception as error:
        #    return 'failed', None, str(error)


def testRun(*args):
    input_joint = CreateNode(tag=args[0], input=args[1])
    result, data, message = input_joint.result
    print '\t\tresult', result, data, message    
    return result, data, message
