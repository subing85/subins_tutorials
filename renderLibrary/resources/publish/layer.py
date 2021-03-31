NAME = 'Extract Layer'
ORDER = 4
ENABLE = False
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract render layer and passes data'
VERSION = '0.0.0'
MODIFIED = '2021:March:29:Monday-10:00:35:PM'
ACTION = 'renderLibrary.resources.publish.layer'


def execute(context, **kwargs):
    import os  
      
    from maya import OpenMaya
        
    from renderLibrary.core import export
    from renderLibrary.utils import studioMaya
  
    layer = context.get('layer')
    

    # get layer data    
    _geometries = studioMaya.getGeometries(layer, root_node)    
     
    
    