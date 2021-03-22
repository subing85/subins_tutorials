 
import os

PATH = '/venture/source_code/tmp/SuperTools/'
print PATH
for root, dirs, files in os.walk(PATH):
    for each in files:
        c_file = os.path.join(root, each)
        if not c_file.endswith('.pyc'):
            continue
        dirname = os.path.dirname(c_file)
        command = 'uncompyle6 -o %s %s'%(dirname, c_file)
        print 'decompyled', c_file
        os.system(command)
        os.remove(c_file)
        
        
print 'done'
