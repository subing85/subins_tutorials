'''
Wire deformation  to cluster.
Data            : April 11, 2017
last modified   : April 15, 2017
Author          : Subin Gopi
subing85@gmail.com

Description     : 
Input           : 
Maya version    : Maya 2016
# Copyright(c) 2018, Subin Gopi All rights reserved.

More videos please visit my vimeo profile link mention below
    https://vimeo.com/user55256190

    Subin's Tutorials - Wire Deformer Weights to Cluster Deformer in Maya 2016. 
    This video tutorial for Transfer the Wire Deformer Weights to Cluster using Maya Python API 2.0. 
    This code is faster than when you perform the same task using MEL and Python scripts.16.

    https://vimeo.com/210275112
'''


import maya.api.OpenMaya as om
import maya.cmds as cmds

#Replace the with geometry shape
meshObject = 'pCylinderShape1'

#Input object to Dag Path
meshSelectionList = om.MSelectionList()
meshSelectionList.add(meshObject)
meshDagPath = meshSelectionList.getDagPath(0)

deformObjects = cmds.ls(sl=1)

for eachObject in deformObjects :
    
    deformSelectionList = om.MSelectionList()
    deformSelectionList.add(eachObject)
    deformDagPath = deformSelectionList.getDagPath(0)
    
    #Get the vertex Orig Position
    mfnMesh = om.MFnMesh(meshDagPath)
    origPositionList = mfnMesh.getPoints(om.MSpace.kObject)
    
    #Set the transform value to deformer
    mfnTransform = om.MFnTransform(deformDagPath)
    xyzMVector = om.MVector(1,0,0)
    mfnTransform.setTranslation(xyzMVector, om.MSpace.kTransform)
    
    deformPositionList = mfnMesh.getPoints(om.MSpace.kObject)
    
    zeroMVector = om.MVector(0,0,0)
    mfnTransform.setTranslation(zeroMVector, om.MSpace.kTransform)
    
    weightList = []
    for index in range(len(origPositionList)) :
        origMVector = om.MVector(origPositionList[index])
        deformMVector = om.MVector(deformPositionList[index])
        
        length = origMVector-deformMVector
        weight = length.length()
        weightList.append(weight)
    
    #Create New Cluster
    myCluster = cmds.cluster(meshObject, n='My_Cluster')
    
    #Set weights to vertex
    for index in range(len(weightList)) :
        cmds.setAttr('%s.weightList[0].w[%s]'%(myCluster[0], index), weightList[index])
    
    #Change the cluster position
    cluster_xyz = cmds.xform(eachObject, q=1, ws=1, piv=1)
    clusterShape = cmds.listRelatives(myCluster[1], s=1)
    
    cmds.setAttr('%s.rotatePivotX'% myCluster[1], cluster_xyz[0]) 
    cmds.setAttr('%s.rotatePivotY'% myCluster[1], cluster_xyz[1]) 
    cmds.setAttr('%s.rotatePivotZ'% myCluster[1], cluster_xyz[2]) 
    cmds.setAttr('%s.scalePivotX'% myCluster[1], cluster_xyz[0]) 
    cmds.setAttr('%s.scalePivotY'% myCluster[1], cluster_xyz[1]) 
    cmds.setAttr('%s.scalePivotZ'% myCluster[1], cluster_xyz[2])
    
    cmds.setAttr('%s.originX'% clusterShape[0], cluster_xyz[0])
    cmds.setAttr('%s.originY'% clusterShape[0], cluster_xyz[1])
    cmds.setAttr('%s.originZ' % clusterShape[0], cluster_xyz[2])
    
print '\nSuccessfully convert the wire deformation to cluster'
#End#############################################################################
