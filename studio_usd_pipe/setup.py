#!/usr/bin/python
import os
import sys
import json

from datetime import datetime

# from studio_usd_pipe import resource
# from studio_usd_pipe.core import common


def main():    
    # studio_template_path = resource.getStudioTemplatePath()
    
    current_path = os.path.dirname(__file__)
    package_path = os.path.dirname(current_path)    
    package_name = os.path.basename(current_path)      

    write_bash(package_path, package_name)

    
def write_bash(package_path, package_name):
    template_path = os.path.join(
        package_path, package_name, 'template/studiopipe_template.txt')        
    contents = get_data(template_path)
    modified = datetime.now().strftime("%Y %d %B %A, %I:%M:%S %p")    
    contents = contents.replace(
        '#  modified: 2020 27 00 00, 00:00:00 PM',
        '#  modified: %s' % modified
        )
    contents = contents.replace(
        '\t\tPACKAGE_PATH=\"tmp\"\n',
        '\t\tPACKAGE_PATH=\"%s\"\n' % package_path
        )    
    contents = contents.replace(
        '\t\tPACKAGE_NAME=\"tmp\"\n',
        '\t\tPACKAGE_NAME=\"%s\"\n' % package_name
        )
    studiopipe_path = os.path.join(
        package_path, package_name, 'bin/pipe/studiopipe')  
    
    if not os.path.isdir(os.path.dirname(studiopipe_path)):
        os.makedirs(os.path.dirname(studiopipe_path))    
    with open(studiopipe_path, 'w') as file:
        data = file.write(contents)        
    os.chmod(studiopipe_path, 0o777)
    symlink_path = '/usr/bin/studiopipe'
    if os.path.isfile(symlink_path):
        try:
            os.chmod(symlink_path, 0777)
        except Exception:
            pass
        try:            
            os.remove(symlink_path)
        except Exception:
            pass
    try:        
        os.symlink(studiopipe_path, symlink_path)
        valid = True
    except Exception as error:
        sys.stderr.write('%s %s' % (str(error), symlink_path))
        valid = False
    if not valid:
        return  
    sys.stdout.write('#Successfully registered studio pipe usd')

        
def get_data(path):     
    with open(path, 'r') as file:
        contents = file.read()
        return contents     


if __name__ == '__main__':
    main() 
