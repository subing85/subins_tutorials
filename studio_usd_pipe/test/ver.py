input_data = {
    "exe": [
        "KONSOLE_EXE", 
        "/venture/source_code/subins_tutorials/studio_usd_pipe/bin/build-in/konsole/main.sh"
    ], 
    "name": [
        "APPLICATION_NAME", 
        "konsole2.10.5"
    ], 
    "version": [
        "KONSOLE_VERSION", 
        "konsole2.10.5"
    ], 
    "path": [
        "KONSOLE_PATH", 
        "/venture/source_code/subins_tutorials/studio_usd_pipe/bin/build-in/konsole"
    ], 
    "order": 0, 
    "bash": "/venture/source_code/subins_tutorials/studio_usd_pipe/bin/build-in/konsole/main.sh", 
    "icon": [
        "KONSOLE_ICON", 
        "/venture/source_code/subins_tutorials/studio_usd_pipe/resource/icons/konsole.png"
    ]
}

import os
import json

os.environ['KONSOLE_EXE'] = "/venture/source_code/subins_tutorials/studio_usd_pipe/bin/build-in/konsole/main.sh:subin"

for each in input_data:
    if not isinstance(input_data[each], list):
        continue
    env_name = input_data[each][0]
    env_value = input_data[each][1]
    if isinstance(env_value, list):
        env_value = ':'.join(env_value)
    else:
        env_value = str(env_value)
        
    if os.getenv(env_name):
        envrons = os.getenv(env_name).split(':')
        envrons.append(env_value)
        envrons = list(set(envrons))
        env_value = os.environ[':'.join(envrons))
    else:
        env_value = str(env_value)