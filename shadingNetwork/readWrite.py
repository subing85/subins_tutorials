'''
Read, load and write Shading Network to custom data format in maya using PyMel
Date : January 10, 2018
Last modified: January 12, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    Read and write Shading Network to custom data format in maya using PyMel
    input - update the "shadingEngineList" variable (line number 26, 27, 29).  
'''

#Read and write(export) the shader networks to custom data format
import pymel.core as pm
import json
import pprint
import os

defaultShadingEngines = ['initialParticleSE',  'initialShadingGroup'] #default shading engines

#write (export) multiple shader networks
#shadingEngineList = ['Body_VRayMtlSG', ''Teeth_VRayMtol_ShaderSG']
shadingEngineList = ['Body_VRayMtlSG']
#write (export) all shader networks
#shadingEngineList = pm.ls(type='shadingEngine')

shaderNetworkData = {}

for eachShadingEngine in shadingEngineList:    
    pyNode = pm.PyNode(eachShadingEngine)    
    historyList = pyNode.listHistory(pdo=True)    
    if pyNode.name() in defaultShadingEngines:
        continue
    
    nodes = {}
    attributes = {}
    connections = {}
    geometries = []
    
    for eachNode in historyList:
                
        #get node a nd node type
        nodes.setdefault(eachNode.name(), eachNode.type())
        
        #get node attribute and attribute value        
        attributeList = eachNode.listAttr(r=True, w=True, u=True, m=True, hd=True)
        attributeValue = {}      
        
        if not attributeList:
            continue
                  
        for eachAttribute in attributeList:
            if eachAttribute.type()=='attributeAlias':
                continue
            
            currentValue = eachAttribute.get()  
                       
            if currentValue==None:
                currentValue = 'None'
                
            if type(currentValue)==bool:
                currentValue = int(currentValue)
                                           
            attributeValue.setdefault(eachAttribute.name(), currentValue)                                    
        attributes.setdefault(eachNode.name(), attributeValue)
        
        #get node connections 
        connectionList = eachNode.listConnections(s=False, d=True, p=True)
        sourceConnections = {}         
        if not connectionList:
            continue        
        for eachConnection in connectionList:
            sourceAttribute = eachConnection.listConnections(s=True, d=False, p=True)  
            if not sourceAttribute:
                continue 
            sourceConnections.setdefault(sourceAttribute[0].name(), []).append(eachConnection.name())      
        connections.setdefault(eachNode.name(), sourceConnections)
        
    #get shader assign geometries
    geometryList = pyNode.attr('dagSetMembers').listConnections(s=True, d=False)    
    if geometryList:
        for eachGeometry in geometryList:
            geometries.append(eachGeometry.name())        

    #Final data
    networks = {}        
    networks['nodes'] = nodes
    networks['attributes'] = attributes
    networks['connections'] = connections
    networks['geometries'] = geometries
    #pprint.pprint (networks)
    
    shaderNetworkData.setdefault(pyNode.name(), networks)

#write data
filePath = os.path.join(os.environ['temp'], 'myTestShader.shader')
shaderData = open(filePath, 'w')
jsonData = json.dumps(shaderNetworkData, indent=4)       
shaderData.write(jsonData)   
shaderData.close()

print '#Successfully write(export) my shader network data'
#End###########################################################################################