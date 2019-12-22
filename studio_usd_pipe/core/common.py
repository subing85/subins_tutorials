
def sorted_order(input_dict):
    data = {}
    stack = input_dict.items()    
    while stack:
        k, v = stack.pop()        
        if not isinstance(v, dict): 
            continue                
        data.setdefault(v['order'], []).append(k)
    result =  sum(data.values(), [])    
    return result

