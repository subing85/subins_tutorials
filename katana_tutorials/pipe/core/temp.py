import os

path = '/venture/shows/katana_tutorials/asset'

for dirname, folder, files in os.walk(path):
    
    for file in files:        
        if not file.endswith('.josn'):
            continue
        # old = os.path.join(dirname, file)        
        # new = os.path.join(dirname, '%s.manifest'% dirname.split('/')[-3])
        print file
        
        # print old
        # print new, '\n'
        # os.rename(old, new)
