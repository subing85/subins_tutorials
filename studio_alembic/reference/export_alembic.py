

import maya.cmds as cmds
import maya.mel as mel
import random
import os
from os import listdir
from os.path import isfile, join

def add_attr_id(derivative, output_path):

    selectedObj = cmds.ls(sl=1,dag=1,s=1)


    ###########################

    #Project directory to be created

    projectPath = output_path + "alembic_cache/"

    ###########################


    sceneName = cmds.file ( q=True, sn=True, shn=True).split('.mb')
    path = projectPath + str(sceneName[0]) + "//shaders//"
    pathFile = projectPath + str(sceneName[0]) + "//" + str(sceneName[0]) + derivative + ".abc"


    for i in selectedObj:
        aRandom=random.randint(0, 5000)
        bRandom=random.randint(0, 5000)
        cRandom=random.randint(0, 5000)
        id = aRandom*bRandom*cRandom
        time = cmds.date(f="YYYYYYMMDDhhmmss")
        id = "id" + str(id) + time
        attributes = cmds.listAttr(i)
        if "Alembic_id" in attributes:
            cmds.setAttr(i + ".Alembic_id", id, type="string")
        else:
            cmds.addAttr(i, longName='Alembic_id', dt="string")
            cmds.setAttr(i + ".Alembic_id", id, type="string")

        id=cmds.getAttr(i+".Alembic_id")
        interO = cmds.getAttr(i + '.intermediateObject')
        if interO != True:
            shaders_export(id, i, path)

    attrName = "Alembic_id"
    attrName_2 = "Face_id"
    frameRange = [str(cmds.playbackOptions(min=True, q=True)), str(cmds.playbackOptions(max=True, q=True))]

    alembic_export(selectedObj, frameRange[0], frameRange[1], pathFile, attrName, attrName_2)

def shaders_export(id, shape, path):

    attributes = cmds.listAttr(shape)
    shadingGrp = cmds.listConnections(shape,type='shadingEngine')
    if shadingGrp != None:
        lenShadingGrp=''
        lenShadingGrp = len(shadingGrp)
        ShapeListSG =[]

        if lenShadingGrp > 1:
            if "Face_id" in attributes:
                print "ok"
            else:
                cmds.addAttr(shape, longName='Face_id', dt="string")

            shadingGrp = list(set(shadingGrp))

            for j in shadingGrp:
                cmds.hyperShade(o = j)
                assignSelected = cmds.ls(sl=1)
                SuperAttr = j + id + "#"

                for t in assignSelected:
                    if ".f" in t:
                        t_tmp = t.split(".f")
                        t = t_tmp[0].rpartition(':')[2]
                        t = t + ".f" + t_tmp[1]
                        vertexes = cmds.polyEvaluate( shape, v=True )
                        t = t + "$vertexes" + str(vertexes) + "$"
                        #t = "{}.f" + t_tmp[1]
                        SuperAttr = SuperAttr + t + ","
                ShapeAttr = cmds.getAttr(shape + '.Face_id')



                if ShapeAttr == None:
                    ShapeAttr = ''
                cmds.setAttr(shape + '.Face_id', ShapeAttr + "@" + SuperAttr, type="string")

            shader = cmds.ls(cmds.listConnections(shadingGrp),materials=1)
            shaderSG = shadingGrp + shader
            cmds.select(shaderSG, r=True, ne=True)

            cmds.file (path + id + ".mb", es=True, type='mayaBinary')

        if lenShadingGrp == 1:
            shader = cmds.ls(cmds.listConnections(shadingGrp),materials=1)
            shaderSG = shadingGrp + shader
            cmds.select(shaderSG, r=True, ne=True)
            cmds.file (path + id + ".mb", es=True, type='mayaBinary')


def alembic_export(selectedObj, frameRange_1, frameRange_2, pathFile, attrName, attrName_2):

    for r in selectedObj:
        interO = cmds.getAttr(r + '.intermediateObject')
        if interO == True:
            selectedObj.remove(r)
    cmds.select (selectedObj)
    groupName = "Alembic_data_group"

    mel.eval('AbcExport -j "-frameRange ' + frameRange_1 + ' ' + frameRange_2 + ' -uvWrite -sl -ro -file ' + pathFile + ' -attr ' + attrName + ' -attr ' + attrName_2 + '";')
    for r in selectedObj:
        try:
            cmds.deleteAttr(r + '.Alembic_id')
        except:
            pass
        try:
            cmds.deleteAttr(r + '.Face_id')
        except:
            pass


def dirBrowse():

    subPath = output_path( q=True, rd=True )

    DirPath = cmds.fileDialog2(fileMode=3, caption="Choose Folder", dir=subPath)
    #DirPath = DirPath and os.path.normpath(DirPath[0])
    DirPath = DirPath and DirPath[0].replace('\\', '/')
    print DirPath
    print "_____________________"
    import_alembic(DirPath)

def import_alembic(DirPath):

    pathFile=''
    path = DirPath + "//shaders//"
    onlyfiles = [ f for f in listdir(DirPath) if isfile(join(DirPath,f)) ]
    print onlyfiles

    for files in onlyfiles:
        if ".abc" in files:
            pathFile = DirPath + "//" + files


    cmds.group( em=True, name='Alembic_data_group' )
    groupName = '|Alembic_data_group'
    print pathFile
    mel.eval('AbcImport -mode import -reparent "{0}" "{1}";'.format(groupName, pathFile))
    print pathFile

    myGroup = "Alembic_data_group"
    children = cmds.listRelatives(myGroup, allDescendents=True, noIntermediate=True, fullPath=True)
    InGroup = cmds.ls(children, type="mesh")
    listFiles = cmds.getFileList( folder=path )

    for i in InGroup:
        id = cmds.getAttr(i + ".Alembic_id")
        for s in listFiles:
            if id in s:
                cmds.file(path + s, i=True, ns="id_" + id)

    AllShaders = cmds.ls(mat=True)

    for s in InGroup:
        #set_attrs(s)
        allAttrs = cmds.listAttr(s)
        id = cmds.getAttr(s + ".Alembic_id")

        if "Face_id" not in allAttrs:
            for shader in AllShaders:
                shadingGrp = cmds.listConnections(shader,type='shadingEngine')
                if shadingGrp != None:
                    if id in shadingGrp[0]:
                        cmds.sets(s, e=1, forceElement=shadingGrp[0])

        if "Face_id" in allAttrs:
            finalSG =[]
            faceID = cmds.getAttr(s + ".Face_id")
            faceID_SG = faceID.split("@")
            for n in faceID_SG:
                faceID_SG = n.split("#")
                for g in faceID_SG:
                    faces_tmp = g.split(",")
                    for u in faces_tmp:
                        faces = u.split("$")
                        for e in faces:
                            if e != "":
                                if id in e:
                                    finalSG = e.split(id)
                                if ".f[" in e:
                                    FinalFaces = e
                                    if len(finalSG)>1:
                                        if finalSG[0] != "initialShadingGroup":
                                            for shader in AllShaders:
                                                shadingGrp = cmds.listConnections(shader,type='shadingEngine')
                                                if shadingGrp != None:
                                                    if finalSG[0] in shadingGrp[0]:
                                                        FinalFacesLongName = cmds.ls (s, long = True)
                                                        vertexes = cmds.polyEvaluate(FinalFacesLongName[0], v=True )
                                                        splitVertexes = faces[1].split("vertexes")
                                                        FinalFacesSplit = FinalFaces.split(".f")
                                                        FinalFacesObj = str(FinalFacesLongName[0]) + ".f" + str(FinalFacesSplit[1])
                                                        if str(vertexes) == str(splitVertexes[1]):
                                                            try:
                                                                cmds.sets(FinalFacesObj, e=1, forceElement=shadingGrp[0])
                                                            except:
                                                                pass
    renameShaders()

def renameShaders():
    myGroup = "Alembic_data_group"
    children = cmds.listRelatives(myGroup, allDescendents=True, noIntermediate=True, fullPath=True)
    InGroup = cmds.ls(children, type="mesh")
    for i in InGroup:
        transform = cmds.listRelatives(i,type='transform',p=True)
        shadingGrp = cmds.listConnections(i,type='shadingEngine')
        shader = cmds.ls(cmds.listConnections(shadingGrp), materials=1)
        try:
            cmds.rename(shader[0], transform[0] + "_mat")
            cmds.rename(shadingGrp[0], transform[0] + "_matSG")
        except:
            pass
