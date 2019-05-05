def sorted_order_data(data):
    result = []
    index = 0
    while index < len(data) + 1:
        x = 0
        for k, v, in data.items():
            if x > len(data):
                break
            order = int(v['order'])
            if order != index:
                continue
            result.append(k.encode())
            x += 1
        index += 1        
    return result    