'''
#Lattice weights transfer to skincluster
Data            : April 11, 2017
last modified   : April 15, 2017
Author          : Subin Gopi
subing85@gmail.com
Description     : select lattice and run the script
Input           : mesh > lattice > skincluster
Maya version    : Maya 2016
''' 

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds

#cmds.select ('ffd1Lattice', r=1)
selectList = cmds.ls (sl=1)
latticeShape = cmds.listRelatives (selectList[0], type='lattice')[0]
ffd = cmds.listConnections (latticeShape, type='ffd')[0]
skincluster = cmds.listConnections (latticeShape, type='skinCluster')[0]
geometry = cmds.lattice (latticeShape, q=1, g=1)[0]
jointList = cmds.skinCluster (skincluster, q=1, inf=1)

#Geometry to Dag Path
meshMSelection = om.MSelectionList ()
meshMSelection.add (geometry)
meshDagPath = meshMSelection.getDagPath (0)

#Get the mesh orgin position
mFnMesh = om.MFnMesh (meshDagPath)
geoPosition = mFnMesh.getPoints (om.MSpace.kObject)

#Get the weight from each joint
weightList = []
for index in range (len(jointList)) :    
    jntParent = cmds.listRelatives (jointList[index], p=1)
    jntChild = cmds.listRelatives (jointList[index], c=1)
    
    if jntParent :
        cmds.parent (jointList[index], w=1)
    if jntChild :
        cmds.parent (jntChild[0], w=1)
            
    jointMSelection = om.MSelectionList ()
    jointMSelection.add (jointList[index])
    jointDagPath = jointMSelection.getDagPath (0)
    
    #Set and reset the deformation value to joint
    mFnTransform = om.MFnTransform (jointDagPath)
    world = mFnTransform.translation (om.MSpace.kWorld)
    moveWorld = om.MVector (world.x+1, world.y, world.z)
    mFnTransform.setTranslation (moveWorld, om.MSpace.kWorld)
    
    movePosition = mFnMesh.getPoints (om.MSpace.kObject)    
    jointWeights = []       
    for vertexIndex in range (len(movePosition)) :
        length = movePosition[vertexIndex]-geoPosition[vertexIndex]
        weight = length.length ()
        jointWeights.append (weight)        
    weightList.append (jointWeights)    
    mFnTransform.setTranslation (world, om.MSpace.kWorld)
    
    if jntParent :
        cmds.parent (jointList[index], jntParent[0])
    if jntChild :
        cmds.parent (jntChild[0], jointList[index])      

#Set join weight to geometry
geoSkinCluster = cmds.skinCluster (jointList, geometry)[0]
skinMSelection = om.MSelectionList ()    
skinMSelection.add (geoSkinCluster)
skinMObject = skinMSelection.getDependNode (0)

mfnSkinCluster = oma.MFnSkinCluster (skinMObject)   

#Vertex components
vertexIndexList = range (len(geoPosition))
mfnIndexComp = om.MFnSingleIndexedComponent ()
vertexComp = mfnIndexComp.create (om.MFn.kMeshVertComponent)
mfnIndexComp.addElements (vertexIndexList)

#influences
influenceObjects = mfnSkinCluster.influenceObjects ()
influenceList = om.MIntArray ()
for eachInfluenceObject in influenceObjects :
    currentIndex = mfnSkinCluster.indexForInfluenceObject (eachInfluenceObject)
    influenceList.append (currentIndex)    

#weights
mWeightList = om.MDoubleArray ()
for wIndex in range (len(weightList[0])) :
    for jntIndex in range (len(weightList)) :  
        mWeightList.append (weightList[jntIndex][wIndex]) 

mfnSkinCluster.setWeights (meshDagPath, vertexComp, influenceList, mWeightList)
cmds.setAttr ('%s.envelope'% skincluster, 0)
cmds.setAttr ('%s.envelope'% ffd, 0)

print '\nLattice weights successfully transfer to skincluster'
