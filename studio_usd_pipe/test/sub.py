from maya import standalone
import subprocess
standalone.initialize(name='python')

commands = ['import os', 'print help(os)']
command = ' '.join(commands)
process = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)

process.wait()
#result = process.stdout.readlines()
communicate = process.communicate() 

standalone.uninitialize(name='python')