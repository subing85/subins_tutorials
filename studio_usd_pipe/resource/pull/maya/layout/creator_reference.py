NAME = 'reference maya'
ORDER = 0
VALID = True
TYPE = 'creator'
KEY = 'puppet_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To reference the maya puppet scene'
VERSION = '0.0.0'
MODIFIED = 'May 19, 2020'
ICON = 'reference_maya.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    puppet_data = kwargs['casting_data']['puppet']
    input_data = {}
    for location, path in puppet_data.items():
        namespace = location.split('|')[0]
        input_data.setdefault(namespace, path)        
    valids = maya_scene.references_maya_scene(input_data, new_scene=True)            
    if False in valids:    
        return False, valids[False], 'failed'    
    return True, valids[True], 'success'
            
    
