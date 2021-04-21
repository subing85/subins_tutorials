import os
import copy
import json
import warnings

from renderLibrary.utils import setMaya


def studio_json(path, **kwargs):
    if not os.path.isfile(path):
        warnings.warn('not found <%s>' % path)
        return None
    with (open(path, mode='r')) as _file:
        input_data = json.load(_file)
        return input_data.get('data'), input_data.get('tag')
    return None, None


def update_aov_nodes(data, new_nodes): 
    _data = copy.deepcopy(data)
    for each in data:
        for key in ['inputs', 'outputs']:
            contents = data[each].get(key)
            for content in contents:
                node = contents[content].split('.')[0]
                if node not in new_nodes:
                    continue
                new = '%s%s' % (
                    new_nodes[node],
                    contents[content].rsplit(node, 1)[-1]
                    )
                _data[each][key][content] = new
    return _data
            
                
            
            
            
        
        
    #===========================================================================
    #     if each not in new_nodes:
    #         _data[each] = data[each]
    #         continue     
    #     new_node = new_nodes[each]
    #     _data[new_node] = data[each]
    # return _data
    #===========================================================================


def update_nodes(data, new_nodes): 
    _data = {}   
    for each in data:
        if each not in new_nodes:
            _data[each] = data[each]
            continue        
        new_node = new_nodes[each]
        _data[new_node] = data[each]
    return _data
 
