import os
import sys

from maya import OpenMaya



 
     

def relase(path, **kwargs):
    
    source_file = kwargs['source_file']    

    format = os.path.splitext(source_file)[-1]
    target_path = os.path.join(dirname, '{}{}'.format(caption, format))
    shutil.copy2(maya_file, target_path)
    self.time_stamp(target_path)
    return target_path


