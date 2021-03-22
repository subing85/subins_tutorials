import sys
import ast

from studio_usd_pipe import resource
from studio_usd_pipe.core import asset

from studio_usd_pipe.api import studioMaya
reload(studioMaya)


def release(**kwargs):
    from maya import standalone
    standalone.initialize(name="python")
    from maya import OpenMaya    
    maya_file = sys.argv[1]
    inputs = ast.literal_eval(sys.argv[2])    
    smaya = studioMaya.Maya()
    smaya.load_plugins(plugins=["pxrUsd", "pxrUsdPreviewSurface", "pxrUsdTranslators"])     
    
    smaya.open_maya(maya_file, None)    

    current_show = inputs['show']
    current_pipe = inputs['pipe']
    current_application = inputs['application']
    reapir = inputs['reapir']
        
    from studio_usd_pipe.api import studioPush
    publish = studioPush.Push(current_show, current_pipe)
    valid, message = publish.validate(repair=reapir, **inputs)    
    if not valid:
        returncode([valid, message])
        standalone.uninitialize(name='python')
        return    
    valid, message = publish.extract(repair=reapir, **inputs)
    if not valid:
        returncode([valid, message])
        return    
    extracted_data = publish.get_extracted_data()
    if not valid:
        returncode([valid, message])
        return    
    valid, message = publish.release()
    returncode([valid, message])
    standalone.uninitialize(name='python')


def returncode(values):
    if isinstance(values, str):
        values = [values]
    print resource.getIdentityKey(), values
    return values


if __name__ == '__main__':
    release()
