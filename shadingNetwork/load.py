'''
Read, load and write Shading Network to custom data format in maya using PyMel
Date : January 10, 2018
Last modified: January 12, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    Load (import) Shading Network from custom data format in maya using PyMel
    input - update the "shadingEngineList" variable (line number 26, 27, 29)    
'''


#Load (import) the shader networks from custom file(data)
import pymel.core as pm
import json
import pprint
import os

#Read custom shader network data
#write data
filePath = os.path.join(os.environ['temp'], 'myTestShader.shader')
shaderData = open(filePath, 'r')
shaderNetworkData = json.load(shaderData)       
shaderData.close()

#pprint.pprint(shaderNetworkData)

shaderList = pm.listNodeTypes('shader')
textureList = pm.listNodeTypes('texture')
utilityList = pm.listNodeTypes('utility')

for eachShaderNetwork in shaderNetworkData:
    #print eachShaderNetwork      
    nodes = shaderNetworkData[eachShaderNetwork]['nodes']
    attributes = shaderNetworkData[eachShaderNetwork]['attributes']
    connections = shaderNetworkData[eachShaderNetwork]['connections']
    geometries = shaderNetworkData[eachShaderNetwork]['geometries']
    
    updateNode = {}
    
    for eachNode in nodes:
        nodeType = nodes[eachNode]        
        #=======================================================================
        # if pm.objExists(eachNode):
        #     pm.delete(eachNode)
        #     print 'node removed\t-', eachNode
        #=======================================================================
            
        if nodeType in shaderList:
            currentNode = pm.shadingNode(nodeType, asShader=True, n=eachNode)
        elif nodeType in textureList:
            currentNode = pm.shadingNode(nodeType, asTexture=True, n=eachNode)
        elif nodeType in utilityList:
            currentNode = pm.shadingNode(nodeType, asUtility=True, n=eachNode)
        else:            
            currentNode = pm.createNode(nodeType, n=eachNode)
            
        updateNode.setdefault(eachNode, currentNode.name())
        
    for eachNode in attributes:
        for eachAttribute in attributes[eachNode]:
            if not pm.objExists(eachAttribute):
                continue
            currentAttribute = eachAttribute.replace(eachNode, updateNode[eachNode])
            pyAttribute = pm.PyNode(currentAttribute)
            currentValue = attributes[eachNode][eachAttribute]
            try:                
                pyAttribute.set(currentValue)
            except Exception as result:
                print 'set attribute warning', eachAttribute, '\t-   ', result
                
    for eachNode in connections:
        for eachAttribute in connections[eachNode]:
            currentSourceAttribute = eachAttribute.replace(eachNode, updateNode[eachNode])
            pySourceAttribute = pm.PyNode(currentSourceAttribute)            
            for eachConnection in connections[eachNode][eachAttribute]:
                
                targetNode = eachConnection.split('.')[0]
                currentTargetAttribute = eachConnection.replace(targetNode, updateNode[targetNode])
                
                pyTargetAttribute = pm.PyNode(currentTargetAttribute)  
                try:                
                    pySourceAttribute.connect(pyTargetAttribute)                
                except Exception as result:
                    print 'connection warning', eachAttribute, '\t-   ', result                
        
print '#Successfully load(import) my shader network data'
#End###########################################################################################