'''
Skincluster To Cluster
Data            : February 11, 2017
last modified   : February 11, 2017
Author          : Subin Gopi
subing85@gmail.com

Version         : Autodesk Maya 2016
Select the joint(bind joint) and run the below script.

More videos please visit my vimeo profile link mention below
Subin's Tutorials
https://vimeo.com/user55256190
'''

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds

jointList = cmds.ls(sl=1)

for currentJoint in jointList :
    # currentJoint = 'joint2'    
    currentSkincluster = cmds.listConnections(currentJoint, type='skinCluster')
    
    if currentSkincluster :    
        # Get skincluster MObject
        skinclusterSelection = om.MSelectionList()
        skinclusterSelection.add(currentSkincluster[0])
        skinclusterMObject = skinclusterSelection.getDependNode(0)
        
        # Get joint MDagPath
        jointSelection = om.MSelectionList()
        jointSelection.add(currentJoint)
        jointMDagPath = jointSelection.getDagPath(0)
        
        # Read skincluster weights and influence
        mfnSkincluster = oma.MFnSkinCluster(skinclusterMObject)
        weightDataList = mfnSkincluster.getPointsAffectedByInfluence(jointMDagPath)
        
        vertexSelction = weightDataList[0]
        vertexWightArray = weightDataList[1]
        component = vertexSelction.getComponent(0)
        
        mfnSingleIndexComp = om.MFnSingleIndexedComponent(component[1])
        vertexIndexList = mfnSingleIndexComp.getElements()
        vertexList = vertexSelction.getSelectionStrings()
        
        # Create new cluster
        myCluster = cmds.cluster(vertexList, n='My_Cluster')
        
        # Set the weights
        for index in range(len(vertexIndexList)) :    
            currentVertex = vertexIndexList[index]
            currentWeight = vertexWightArray[index]
            cmds.setAttr('%s.weightList[0].w[%s]' %(myCluster[0], currentVertex), currentWeight)    
            
        # Change the cluster position
        xyz = cmds.xform(currentJoint, q=1, ws=1, t=1)
        clusterShape = cmds.listRelatives(myCluster[1], s=1)
        cmds.setAttr('%s.rotatePivotX' % myCluster[1], xyz[0])    
        cmds.setAttr('%s.rotatePivotY' % myCluster[1], xyz[1])    
        cmds.setAttr('%s.rotatePivotZ' % myCluster[1], xyz[2])
        cmds.setAttr('%s.scalePivotX' % myCluster[1], xyz[0])    
        cmds.setAttr('%s.scalePivotY' % myCluster[1], xyz[1])    
        cmds.setAttr('%s.scalePivotZ' % myCluster[1], xyz[2])  
        cmds.setAttr('%s.originX' % clusterShape[0], xyz[0])    
        cmds.setAttr('%s.originY' % clusterShape[0], xyz[1])    
        cmds.setAttr('%s.originZ' % clusterShape[0], xyz[2])
        
        print '#Successfully done selected joint to cluster'
    
    else :
        print 'Skincluster does not exists'   
