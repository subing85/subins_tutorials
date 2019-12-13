import os
import shutil

def time_stamping(self, path, time):
    if not os.path.exists(path):
        return
    os.utime(path, (time, time))
        
        
def copy_to(source, to, time):
    if not os.path.isfile(source):
        raise IOError('not find <{}>'.format(source))        
    if not os.path.isdir(os.path.dirname(to)):
        os.makedirs(os.path.dirname(to)) 
        time_stamping(os.path.dirname(to), time)       
    shutil.copy2(source, to)
    time_stamping(to, time)       
    
    