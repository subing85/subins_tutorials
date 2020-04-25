import sys
import ast

from studio_usd_pipe import resource
from studio_usd_pipe.core import asset

from studio_usd_pipe.api import studioMaya
reload(studioMaya)


def pre_release(**kwargs):
    from maya import standalone
    standalone.initialize(name="python")
    from maya import OpenMaya    
    maya_file = sys.argv[1]
    inputs = ast.literal_eval(sys.argv[2])    
    smaya = studioMaya.Maya()
    smaya.load_plugins(plugins=["pxrUsd", "pxrUsdPreviewSurface", "pxrUsdTranslators"])     
    
    smaya.open_maya(maya_file, None)    
    pipe = inputs['pipe']
    subfield = inputs['subfield']     
    from studio_usd_pipe.api import studioPublish
    reload(studioPublish)     
    pub = studioPublish.Publish(pipe=pipe, subfield=subfield)
    valid, message = pub.validate(repair=True, **inputs)    
    if not valid:
        returncode([valid, message])
        standalone.uninitialize(name='python')
        return    
    valid, message = pub.extract(repair=False, **inputs)
    if not valid:
        returncode([valid, message])
        return    
    extracted_data = pub.get_extracted_data()
    if not valid:
        returncode([valid, message])
        return    
    valid, message = pub.release()
    returncode([valid, message])
    standalone.uninitialize(name='python')


def returncode(values):
    if isinstance(values, str):
        values = [values]
    print resource.getIdentityKey(), values
    return values


if __name__ == '__main__':
    pre_release()
