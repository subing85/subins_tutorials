LONG_NAME = 'test 4'
ICON = 'object_type'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'validate'
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
        print '%s WIP. %s'%(MODULE_TYPE, COMMENTS)        
        self.input = input        
        crowd_publish = crowdPublish.Publish()        
        self.bundle_result = crowd_publish.bundle_result
        self.bundle_return = crowd_publish.bundle_return
        self.result = self.check()       
    
    def check(self):
        out, nodes, message = self.get_nodes()        
        return self.bundle_result[out], nodes, message       
            
    def get_nodes(self): 
        default_nodes = ['persp', 'top', 'front', 'side']               
        maya_nodes = core.ls(assemblies=True)        
        nodes = [each for each in maya_nodes if each.name() not in default_nodes]        
        if len(nodes)>0:            
            return 'faild', nodes, 'more than one hierarchy found!..'
        return 'success', nodes, 'good hierarchy!..'

def testRun():
    input_joint = InputJoint()
    print input_joint.result[2], input_joint.result[1]
    return input_joint.bundle_return[input_joint.result[0]]



