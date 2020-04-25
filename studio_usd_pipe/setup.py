#!/usr/bin/python
import os
import sys
import json

from datetime import datetime


def main():    
    current_path = os.path.dirname(__file__)
    write_bash(current_path)

    
def write_bash(path):
    input_path = os.path.join(path, 'bin/studio.txt')
    basename = os.path.basename(path)
    package_path = os.path.dirname(path)
    contents = get_data(input_path)
    modified = datetime.now().strftime("%A %B %d, %Y %H:%M %p")
    contents = contents.replace(
        'Last modified: April 22, 2020',
        'Last modified: %s' % modified
        )

    contents = contents.replace(
        '\t\tPACKAGE_PATH=\"tmp\"\n',
        '\t\tPACKAGE_PATH=\"%s\"\n' % package_path
        )
    
    contents = contents.replace(
        '\t\tPACKAGE_NAME=\"tmp\"\n',
        '\t\tPACKAGE_NAME=\"%s\"\n' % basename
        )
   
    studio_path = os.path.join(path, 'bin/studio.sh')
    with open(studio_path, 'w') as file:
        data = file.write(contents)
    os.chmod(studio_path, 0o777)
    symlink = '/usr/bin/studio'    
    if os.path.isfile(symlink):
        try:
            os.chmod(symlink, 0777)
        except Exception:
            pass
        try:            
            os.remove(symlink)
        except Exception:
            pass
    try:        
        os.symlink(studio_path, symlink)
        valid = True
    except Exception as error:
        sys.stderr.write('%s %s' % (str(error), symlink))
        valid = False
    if not valid:
        return  
    sys.stdout.write('#Successfully registered studio pipe usd')

        
def get_data(path):     
    with open(path, 'r') as file:
        contents = file.read()
        return contents     


# --studio usd pipe library
if __name__ == '__main__':
    main() 
