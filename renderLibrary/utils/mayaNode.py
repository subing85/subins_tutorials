

from maya import OpenMaya


class Connect(object):

    def __init__(self, **kwargs):        
        self.node = kwargs.get('node') or None

            
    def getDagPath(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mdag_path = OpenMaya.MDagPath()
        mselection.getDagPath(0, mdag_path)
        return mdag_path

    def getMObject(self):
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mobject = OpenMaya.MObject()
        mselection.getDependNode(0, mobject)
        return mobject
    
    def getRootNode(self):
        dagpath = self.getDagPath()
        self.node = dagpath.fullPathName().split('|')[1]
        mdag_path = self.getDagPath()
        return mdag_path
    
    def getMPlug(self):
        mplug = OpenMaya.MPlug()
        mselection = OpenMaya.MSelectionList()
        mselection.add(self.node)
        mselection.getPlug(0, mplug)    
        return mplug
    
    def findDagPaths(self, dagpath, typed):
        '''
        :dagpath <MDagPath>
        :typed <MFn object type> OpenMaya.MFn.kMesh
        '''
        dag_array = OpenMaya.MDagPathArray()
        stack = [dagpath]
        while stack:
            current = stack.pop()    
            mobject = current.node()
            if mobject.hasFn(typed):
                dag_array.append(current)      
            for x in range (current.childCount()):
                child_dagpath =  OpenMaya.MDagPath()
                child_dagpath.getAPathTo(current.child(x), child_dagpath)
                stack.append(child_dagpath)
        return dag_array
    
    
    def getMeshHierarchy(self, dagpath): 
        dag_array = OpenMaya.MDagPathArray()
        dagpaths = self.findDagPaths(dagpath, OpenMaya.MFn.kMesh)
        for x in range(dagpaths.length()):
            mfndag_node = OpenMaya.MFnDagNode(dagpaths[x])
            _parent = mfndag_node.parent(0)
            child_dagpath =  OpenMaya.MDagPath()
            child_dagpath.getAPathTo(_parent, child_dagpath)
            dag_array.append(child_dagpath)
        return dag_array
    
    def getSelectedDagPaths(self):
        mselection = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(mselection)
        dagpaths = OpenMaya.MDagPathArray()
        for x in range(mselection.length()):
            dag_path = OpenMaya.MDagPath()
            mselection.getDagPath(x, dag_path)
            dagpaths.append(dag_path)
        return dagpaths

    def getSelectionStrings(self):
        selected = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(selected)
        list = []
        selected.getSelectionStrings(list)
        return list
    
    

    
            
            
          
    
