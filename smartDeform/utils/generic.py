

def sortDictionary(dictionary):
    
    sort_result = {}
    for each, dict_data in dictionary.items():
        if 'order' not in dict_data:
           continue        
        sort_result.setdefault(dict_data['order'], []).append(each.encode())
    return sort_result   
    
        

