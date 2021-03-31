

def reload_modules():
    
    from renderLibrary import resources    
    from renderLibrary.core import export
    from renderLibrary.api import mayaNode       
    from renderLibrary.api import mayaRender
    from renderLibrary.utils import studioMaya

   
    modules = [resources, export, mayaNode, mayaRender, studioMaya]
    print '\n# reload modules'
    for module in modules:
        print module.__file__
        reload(module)            