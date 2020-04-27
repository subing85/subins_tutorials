import os
import json

env = {'PATHS': ['/venture/source_code/', '/venture/source_code/abc']}

# print os.environ['PATHS']

for k, v in env.items():
    
    value = v
    
    if isinstance(v, list):
        value = ':'.join(v)    
    
    if os.getenv(k):
        value = os.environ[k] + ':' + value
    # print merged  
    os.environ[k] = value
    
# print os.environ['PATHS']

print json.dumps(os.environ['PYTHONPATH'].split(':'), indent=4)

# print os.getenv('FOO')
