'''
#irror and Filp the Symmetrical Polygon Geometry
Data            : Jaunuary 26, 2017
last modified   : March 19, 2017
Author          : Subin Gopi
subing85@gmail.com
Description     : select lattice and run the script
Input           : mesh > lattice > skincluster
Maya version    : Maya 2016
''' 

import maya.api.OpenMaya as om
import maya.cmds as cmds

#Input object to M-Dag path
baseMSelectionList = om.MSelectionList()
baseMSelectionList.add('pSphereShape1')
baseGeoDagPath = baseMSelectionList.getDagPath(0)

shapeMSelectionList = om.MSelectionList()
shapeMSelectionList.add('pSphereShape2')
shapeGeoDagPath = shapeMSelectionList.getDagPath(0)

#Get Vertex Positions
baseMfnMesh = om.MFnMesh(baseGeoDagPath)
baseVertexList = baseMfnMesh.getPoints(om.MSpace.kObject)

shapeMfnMesh = om.MFnMesh(shapeGeoDagPath)
shapeVertexList = shapeMfnMesh.getPoints(om.MSpace.kObject)

#Collect Moved vertexs
movedVertexs = []
movedBaseVertexList = []
movedShapeVertexList = []
movedVertexList = []

for index in range(len(baseVertexList)) :
    baseVertexPosition = baseVertexList[index]
    sahpeVertexPosition = shapeVertexList[index]
    
    if baseVertexPosition!=sahpeVertexPosition :        
        movedVertexs.append('pSphereShape2.vtx[%i]'% index)
        
        movedBaseVertexList.append(baseVertexPosition) 
        movedShapeVertexList.append(sahpeVertexPosition) 
        movedVertexList.append(index)        
#cmds.select(movedVertexs, r=1)

#Set to Mirror Filp and Revert Shapes
mitMeshPolygon = om.MItMeshPolygon(baseGeoDagPath)
axis = [-1,1,1]
oppVertexList = [] 

for index in range(len(movedBaseVertexList)) :
    xyz = movedBaseVertexList[index]
    opp_xyz = om.MPoint(xyz.x*axis[0], xyz.y*axis[1], xyz.z*axis[2])    
    closetPoint, faceID = baseMfnMesh.getClosestPoint(opp_xyz, om.MSpace.kObject)
    
    mitMeshPolygon.setIndex(faceID)
    faceVertexList = mitMeshPolygon.getVertices()
    
    mVectorLengthList = []
    
    for eachVertex in faceVertexList :
        oppVertexPosition = baseMfnMesh.getPoint(eachVertex, om.MSpace.kObject)
        
        oppMVector = om.MVector(oppVertexPosition)
        mirrorMVector = om.MVector(opp_xyz)
        
        mVectorLength = oppMVector-mirrorMVector
        length = mVectorLength.length()
        mVectorLengthList.append(length)        
    
    closestVertex = min(mVectorLengthList)
    vertexIndex = mVectorLengthList.index(closestVertex)
    currentVertexID = faceVertexList[vertexIndex]        
    oppVertexList.append('pSphereShape2.vtx[%i]'% currentVertexID)
    
    movedVertex = movedShapeVertexList[index]
    
    oppMovedPosition = om.MPoint(movedVertex.x*axis[0], movedVertex.y*axis[1], movedVertex.z*axis[2])
    
    #Add Conditions - for Mirror, Filp and Revert    
    #Set Mirror    
    shapeMfnMesh.setPoint(currentVertexID, oppMovedPosition, om.MSpace.kObject)
    
    #Set Filp / Revert
    shapeMfnMesh.setPoint(movedVertexList[index], xyz, om.MSpace.kObject)
    
shapeMfnMesh.updateSurface()    
# cmds.select(oppVertexList, r=1)
print '#Successfully done My Symmetrical Polygon Geometry Shape'

