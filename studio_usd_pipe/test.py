import json

node_list = [
    ['null1'],
    ['null1', 'group4', 'group3', 'group1', 'pSphere1'],
    ['null1', 'group4', 'group3', 'group2', 'pCube1'],
    ['null1', 'group4', 'group3', 'group1'],
    ['null1', 'group4', 'group3', 'group2'],
    ['null1', 'group4', 'group3'],
    ['null1', 'group4']
    ]


import copy

def _add(data, bundles):
    
    
    result = []
    index = 0
    while index < len(data) + 1:
        x = 0
        for k, v, in data.items():
            if x > len(data):
                break
            order = int(k)
            if order != index:
                continue                
            current = None                
            for each in v:
                if v[each]['type']!=value:
                    continue                        
                current = v.keys()[0].encode()
                break
            if not current:
                continue                    
            result.append(current)
            x += 1
        index += 1
    return result

def add(data, bundles):
    
    for k, v in data.items():  
        
        if isinstance(v, dict):      
            if k in bundles:
                print '\t', bundles
            add(v, None)
        
        
                    
    

data = {}
for nodes in node_list:    
    bundles = bundle = {}    
    for node in nodes:
        bundle[node] = {}
        bundle = bundle[node]
        
    if not data:
        data = copy.deepcopy(bundles)
         
    # print json.dumps(bundles, indent=4)
    print data
    print bundles
    add(data, bundles)
    
    

