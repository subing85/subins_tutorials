
from maya import OpenMaya

from studio_alembic.core import studioMaya

reload(studioMaya)



def execute(*args):
    # type, select, directory, objects
    
    if args[0]=='export':
        studio_alembic_export(args[1], args[2], args[3])
        
    if args[0]=='import':
        studio_alembic_import(args[2])
        
        
    
    

def studio_alembic_export(select, directory, objects):
    '''
    :example
        abspath = '/venture/test_show/scenes/test'
        from studio_alembic.core import studioMaya
        reload(studioMaya)  
        studio_maya = studioMaya.Connect(abspath)
        shading_engines = studio_maya.saExport()
        
        remove unwanted geometry from metadata        
    '''
    
    if select:
        objects = None
    
    smaya = studioMaya.Connect(directory)
    
    if not select and objects:  
        mdag_paths = smaya.getSelectedNodes()
    else:    
        mdag_paths = smaya.getDagPaths(objects) 
    
    if mdag_paths.length()<1:
        OpenMaya.MGlobal.displayError(
            'This function requires at least 1 argument to be specified or selected, found 0.//')
        return
    
    smaya.almbicPack(mdag_paths)
    
    abspath = '/venture/test_show/scenes/test'
    from studio_alembic.core import studioMaya
    reload(studioMaya)  
    studio_maya = studioMaya.Connect(abspath)
    
    mdag_paths = studio_maya.getSelectedNodes()
    # mdag_paths = studio_maya.getDagPaths(objects)
    
    engines = studio_maya.exportShaderNetwork(mdag_paths)
    metadata = studio_maya.exportMetaData(mdag_paths)
    alembic = studio_maya.exportAlembic(mdag_paths)
    manifest = studio_maya.exportManifest(mdag_paths)
    
    
    
    return
    
    
    if not mdag_array:
        mdag_array = self.getShapeNodes()        

    
    objects = [mdag_array[x].fullPathName() for x in range (mdag_array.length())]
    shading_engines = self.getShadingEngines(mdag_array) 
    shader_path = self.exportShaderNetwork(shading_engines, self.stuio_path)
    meta_path = self.exportMetaData(shading_engines, self.stuio_path)
    alembic_path = self.exportAlembic(self.stuio_path)        
    maya_path = '{}_maya.ma'.format(self.stuio_path)
    
    data = {
        'name': self.name,
        'objects': objects,
        'shader': shader_path,
        'alembic': alembic_path,
        'metadata': meta_path,
        'maya': maya_path
    }
    self.createManifest(self.stuio_path, data)
    print '\n#', os.path.dirname(self.stuio_path)
    
def studio_alembic_import(mdag_array=None):
    pass    