from maya import OpenMaya as om
from maya import OpenMayaAnim as oma
from maya import OpenMaya
from maya import OpenMayaAnim
from smartDeform.modules import studioMaya
reload(studioMaya)

object = 'pSphereShape1'

my_maya = studioMaya.Maya(node=object)
depend_node = my_maya.getDependNode(object)

mesh_dependency_node = om.MFnDependencyNode(depend_node)
mesh_plug = mesh_dependency_node.findPlug('inMesh')

mesh_plug_array = om.MPlugArray()
mesh_plug.connectedTo(mesh_plug_array, True, False)
conncted_node = mesh_plug_array[0].node()

mode = om.MFn.kSkinClusterFilter
stack = []
node_list = [conncted_node]
result = {}

index = 0

while node_list:
    current = node_list.pop() 
    
    if index==200:
        break
    
    dependency_node = om.MFnDependencyNode(current)
    attribute_count = dependency_node.attributeCount()
    
    for x in range(attribute_count):
        attribute = dependency_node.attribute(x) 
        mfn_attribute = om.MFnAttribute(attribute)  
        plug = dependency_node.findPlug(attribute)
        
        plug_array = om.MPlugArray()    
        plug.connectedTo(plug_array, True, False)  
        
        current_arry   = plug_array[0]    
       
        if not current_arry:
            continue

        abc = current_arry.node()        
        if abc.hasFn(mode):
            print current_arry.name()            
            my_node = om.MFnDependencyNode(current_arry.node())
            abc_node = my_maya.getDependNode(my_node.name().encode())
            result.setdefault(my_node, my_node.name().encode())
            print abc_node
            
           
        if current_arry.node() in stack:
            continue
        stack.append(current_arry.node())   
        node_list.append(current_arry.node()) 

            
################################################
from maya import OpenMaya as om
from maya import OpenMayaAnim as oma
from maya import OpenMaya
from maya import OpenMayaAnim
from smartDeform.modules import studioMaya
reload(studioMaya)

object = 'pSphereShape1'

my_maya = studioMaya.Maya(node=object)
current_node = my_maya.getDependNode(object)

stack = set()
nodes = []
index = 0

while current_node:
    if index==100:
        break
    
    mfn_dependency_node = om.MFnDependencyNode(current_node)
    attribute_count = mfn_dependency_node.attributeCount()
    
    for x in range(attribute_count):
        attribute = mfn_dependency_node.attribute(x) 
        plug = mfn_dependency_node.findPlug(attribute)
        plug_array = om.MPlugArray()    
        plug.connectedTo(plug_array, True, False)  
        current_arry   = plug_array[0]    
       
        if not current_arry:
            continue
        print current_arry.name() 
              
    
    index+=1
    
##############################
from maya import OpenMaya as om
from maya import OpenMayaAnim as oma
from maya import OpenMaya
from maya import OpenMayaAnim
from smartDeform.modules import studioMaya
reload(studioMaya)

object = 'pSphereShape1'

my_maya = studioMaya.Maya(node=object)
node_node = my_maya.getDependNode()


mode = om.MFn.kClusterFilter
stack = []
nodes = [current_node]
result = {}

result = om.MObjectArray()


while nodes:
    node = nodes.pop()    
    mfn_dependency_node = om.MFnDependencyNode(node)
    attribute_count = mfn_dependency_node.attributeCount()
    
    for x in range(attribute_count):
        attribute = mfn_dependency_node.attribute(x) 
        plug = mfn_dependency_node.findPlug(attribute)
        
        plug_array = om.MPlugArray()    
        plug.connectedTo(plug_array, True, False)          
        current_arry   = plug_array[0]    
       
        if not current_arry:
            continue            

        mobject = current_arry.node()        
        if mobject.hasFn(mode):
            my_node = om.MFnDependencyNode(mobject)
            result.append(my_node.object())
           
        if current_arry.node() in stack:
            continue
        stack.append(current_arry.node())   
        nodes.append(current_arry.node()) 

print result            
                
        
            
                
                       
        