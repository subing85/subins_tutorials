container = {
    "shader_source_images": [
        [
            [
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/belt.png", 
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/belt_lores.png", 
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/suits.png", 
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/suits_lores.png", 
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/body.png", 
                "/usr/tmp/test_show/assets/batman/shader/3.0.0/source_images/body_lores.png"
            ]
        ], 
        "success!..."
    ], 
    "shader_thumbnail": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman.png"
        ], 
        "success!..."
    ], 
    "shader_preview_usd": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman_preview.usd"
        ], 
        "success!..."
    ], 
    "shader_assetids": [
        [
            [
                "sdependency", 
                "None"
            ], 
            [
                "ssubfield", 
                "shader"
            ], 
            [
                "sversion", 
                "3.0.0"
            ], 
            [
                "scaption", 
                "batman"
            ], 
            [
                "slocation", 
                "/venture/shows/batman/assets/batman/shader/3.0.0"
            ], 
            [
                "stag", 
                "character"
            ], 
            [
                "spipe", 
                "assets"
            ], 
            [
                "sdescription", 
                "aaaaaaaaaaaaaaaaaaaaa"
            ], 
            [
                "suser", 
                "shreya"
            ], 
            [
                "smodified", 
                "2020:05:May-12:06:38:AM"
            ], 
            [
                "stype", 
                "interactive"
            ]
        ], 
        "success!..."
    ], 
    "shader_scene": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman.ma"
        ], 
        "success!..."
    ], 
    "shader_usd": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman.usd"
        ], 
        "success!..."
    ], 
    "manifest": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman.manifest"
        ], 
        "success"
    ], 
    "studio_shader": [
        [
            "/usr/tmp/test_show/assets/batman/shader/3.0.0/batman.shader"
        ], 
        "success!..."
    ]
}

import os
import copy
extracted_data = {}

du_container = copy.deepcopy(container)


for name in du_container:
    stack = du_container[name][0]    
    while stack:
        input = stack.pop()                         
        if isinstance(input, str) or isinstance(input, unicode):
            if not os.path.exists(input):
                continue
            extracted_data.setdefault(name, []).append(input)
        if isinstance(input, list):
            stack.extend(input)
import json
print json.dumps(container, indent=4)

data = {}        
for contents in extracted_data:
    values = extracted_data[contents]
    if not values:
        continue
    for value in values:
        if not os.path.isfile(value):
            continue
        data.setdefault(contents, []).append(value)  
packing_data = sum(data.values(), [])
# print json.dumps(packing_data, indent=4)










