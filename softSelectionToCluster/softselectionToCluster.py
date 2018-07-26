'''
soft selection To Cluster
Data            : January 20, 2017
last modified   : January 21, 2017
Author          : Subin Gopi
subing85@gmail.com
Version         : Autodesk Maya 2016
Select the vertex with soft selection and run the below script.
'''

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds 

softSelection     = om.MGlobal.getRichSelection ()
richSelection     = om.MRichSelection (softSelection)
selectionList     = richSelection.getSelection ()
component         = selectionList.getComponent (0)
componentIndex    = om.MFnSingleIndexedComponent (component[1])
#componentIndex   = om.MFnComponent (component[1])
vertexList        = componentIndex.getElements()
weightList        = {}
deformVertexList  = []
for loop in range (len(vertexList)) :    
    weight        = componentIndex.weight (loop)
    influance     = weight.influence   
    weightList.setdefault (vertexList[loop], influance) 
    #print vertexList[loop], influance    
    deformVertexList.append ('pSphere1.vtx[%i]'% vertexList[loop])        
    
print '\n...................'    
print selectionList
print component[1] 
print weightList
print '\n...................'

myCluster         =  cmds.cluster (deformVertexList, n='MyCluster')
for eachWeight in weightList :    
    currentVertex     = eachWeight
    currentWeight     = weightList[eachWeight]    
    cmds.setAttr (myCluster[0] + '.weightList[0].w[%s]'%currentVertex, currentWeight)
