#!/usr/bin/python

NAME = 'Maya subprocess'
ORDER = 0
VALID = True
TYPE = 'subprocess'
KEY = 'maya_subprocess'
ICON = 'maya_subprocess.png'
OWNER = 'Subin Gopi'
COMMENTS = 'to execute scripts on maya file'
VERSION = '0.0.0'
MODIFIED = 'April 28, 2020'

import os
import ast
import subprocess
import tempfile

from studio_usd_pipe import resource



def execute(mayapath, maya, script, **kwargs):
    '''
        maya = '/usr/autodesk/maya2018/bin/mayapy'
        maya = '/venture/shows/batman/batman_0.0.3.mb'
        script = resource.getScriptPath() + '/find_assetids.py'
        data = read(mayapy, maya, script)
    '''
    mayapy = os.path.join(mayapath, 'bin/mayapy')
    popen = subprocess.Popen(
        [mayapy, '-s', script, maya, str(kwargs)], shell=False, stdout=subprocess.PIPE)
    popen_result = popen.stdout.readlines()        
    communicate = popen.communicate()
    if not popen_result:
        return False, 'failed'
    spack_return = None
    identity_key = resource.getIdentityKey()
    for each in popen_result:            
        if identity_key in each:
            spack_return = each.split(identity_key)[-1]
            continue
        print each.replace('\n', '')
    if not spack_return:
        return False, 'failed' 
    result = ast.literal_eval(spack_return.strip())
    return result, 'success'
