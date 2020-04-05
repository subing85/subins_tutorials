import os

PATH = '/venture/source_code/subins_tutorials/dumps'

for file in os.listdir(PATH):    
    if not file.endswith('.ui'):
        continue
    source = os.path.join(PATH, file)
    target = '{}.py'.format(os.path.splitext(source)[0])
    # command = 'pyuic4 {} -o {}'.format(source, target)
    command = 'pyside-uic {} -o {}'.format(source, target)
    #command = 'pyside2-uic {} -o {}'.format(source, target)
    
    
    os.system(command)
    print target