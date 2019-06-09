import random

from pymel import core
from maya import OpenMaya

from crowd.api import crowdSkeleton
from crowd.api import crowdMaya
from crowd.api import crowdAttributes
reload(crowdAttributes)
reload(crowdSkeleton)

class Connect(object):
    
    def __init__(self, parent=None, **kwargs):
        self.parent = parent
        self.type  = kwargs['type']
        self.count = kwargs['count']
        self.distance = kwargs['distance']
        self.row = kwargs['row']
        self.column = kwargs['column']
        self.row_offset = kwargs['rowOffset']
        self.column_offset = kwargs['columnOffset']
        
        self.random = kwargs['random']        
        self.parent_name = 'proxy_crowd'

    
    def create(self):      
        print '\n\ntype', self.type
        print 'count', self.count
        print 'count', self.count        
        print 'row', self.row
        print 'column', self.column
        print 'row_offset', self.row_offset
        print 'column_offset', self.column_offset        
        print 'random', self.random
        
        self.createCrowdNode()
        crowd_skeleton = crowdSkeleton.Connect()
        root_joints = []

        s_row = 0
        s_column = 0
        
        a = 0
        b = 0
        
        print self.count
        
             
        for x in range(self.count):          
            if x % self.row:
                s_column+=(self.distance*-1)
                a+=1
            else:
                s_row+=(self.distance*1)
                s_column=0                
                b+=1
                a=0
                
            if not x % 2:         
                s_column = s_column+(self.row_offset*-1)
                
            if (a%2)!=0:
                s_row = s_row+(self.column_offset*-1)                
                
            if self.random:            
                s_row = random.randrange(s_row-self.random, s_row+self.random)
                s_column = random.randrange(s_column-self.random, s_column+self.random)
                
            
            #===================================================================
            # row = 0
            # column = 0
            # 
            # for x in range(0, 53):
            #     
            #     if x%5:
            #         column+=1
            #     else:
            #         row+=1
            #         column=0
            #         print '\n'
            #     if (column%2)!=0:
            #         print '\t', x
            #===================================================================

                
            #slide ===================================================================
            # if x % 2:        
            #     s_row = s_row+(self.column_offset*-1)
            #===================================================================
                                  
            position = [s_row, 0, s_column]  
                                       
            root_dag_path, result = crowd_skeleton.create(self.type, position=position)
            root_joints.append(root_dag_path)
         
        self.addTocontainer(root_joints)
        



                 
                 
                 
                 
                 
                 
                 
                 
            
    def createCrowdNode(self):
        dg_modifier = OpenMaya.MDGModifier()
        self.parent = dg_modifier.createNode('container')
        dg_modifier.renameNode(self.parent, self.parent_name)
        crowd_attribute = crowdAttributes.Connect(self.parent)        
        crowd_attribute.createParentAttributes(mobject=dg_modifier)
        dg_modifier.doIt()
        
    def addTocontainer(self, children):
        parent = core.PyNode(self.parent).name()
        children = [core.PyNode(each).name() for each in children]
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand(
            'container -e -an {\"%s\"} \"%s\"'%('\", \"'.join(
                children), parent), mcommand_result, True, True)
        return True
        

    def addChildren(self):
        pass

               
