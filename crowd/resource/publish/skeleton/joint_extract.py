LONG_NAME = 'export joint'
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

from crowd.core import skeleton


class InputJoint(object):

    def __init__(self, input=None):
        print '\n%s WIP. %s' % (MODULE_TYPE, COMMENTS)
        self.input = input
        self.result = self.get()

    def get(self):
        out, nodes, message = self.get_nodes()
        return out, nodes, message

    def get_nodes(self):
        default_nodes = ['persp', 'top', 'front', 'side']
        maya_nodes = core.ls(assemblies=True)
        nodes = [each.name().encode()
                 for each in maya_nodes if each.name() not in default_nodes]
        if len(nodes) > 1:
            return 'failed', nodes, 'more than one hierarchy found!..'
        if len(nodes) == 0:
            return 'error', 'None', 'not found any hierarchy!..'
        
        joints = core.ls(type='joint')        
        data = skeleton.get_skeleton_inputs(joints)        
        return 'success', data, 'joints'


def testRun():
    input_joint = InputJoint()
    result, data, message = input_joint.result
    print '\ntest run', result, data, message
    return result, data, message
