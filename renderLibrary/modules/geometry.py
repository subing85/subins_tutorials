
from renderLibrary.utils import mayaNode
reload(mayaNode)



def _export():
    sm = mayaNode.Connect(node='pasted__polySurface6')
    dagpath = sm.getRootNode()
    
    dagpaths = sm.getMeshHierarchy(dagpath)
    
    for x in range(dagpaths.length()):
        print dagpaths[x].fullPathName()



def _import():
    pass