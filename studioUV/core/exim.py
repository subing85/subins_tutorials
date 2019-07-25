from pymel import core

from studioUV.core import studioMaya


def execute(*args):
    # (u'export', u'selected', u'/venture/subins_tutorials/uv_export/test.uv')
    
    if args[1]=='selected':
        nodes = core.ls(sl=True)
        all_polygons = core.listTransforms(type='mesh')
        polygons = []
        for node in nodes:
            if node not in all_polygons:
                continue
            polygons.append(node)
    elif args[1]=='all':
        polygons = core.listTransforms(type='mesh')
        
    
    studio_maya = studioMaya.Connect()
    
    if args[0]=='export':    
        uv_data_bundle = {}
        for index, polygon in enumerate(polygons):
            studio_maya.node = polygon
            mdag_path = studio_maya.getDagPath()
            data = studio_maya.getData(mdag_path)
            uv_data_bundle.setdefault(index, data)        
        studio_maya.write(args[2], uv_data_bundle)
        print args[2], 'export success!...'
        
    if args[0]=='import':
        pass
    
    
    # studio_maya = studioMaya.Connect()
    


    