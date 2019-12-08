import os
import json
import warnings
import subprocess

from studio_usd_pipe import resources


def get_package_path():
    current_path = os.path.dirname(__file__)
    package_path = os.path.split(os.path.split(current_path)[0])[0]
    return package_path


def sub_process(mayapy, source_code, **args):
    package_path = get_package_path()
    commands = [
        'export PYTHONPATH=$PYTHONPATH:\"{}\"'.format(package_path),
        '&&',
        '\"{}\"'.format(mayapy),
        '-s',
        '\"{}\"'.format(source_code),
        str(args)
    ]
    process = None
    operating_system = resources.getOperatingSystem()
    if operating_system == 'Linux':
        command = ' '.join(commands)
        process = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    if operating_system == 'Windows':
        process = subprocess.Popen(
            [mayapy, '-c', '; '.join(commands)], shell=True, stdout=subprocess.PIPE)
    result = None
    if process:
        process.wait()
        result = process.stdout.readlines()
        communicate = process.communicate()  
    return result
    # result = subprocess.call(
    # bash_file, stdout=None, shell=True, stderr=None)   
