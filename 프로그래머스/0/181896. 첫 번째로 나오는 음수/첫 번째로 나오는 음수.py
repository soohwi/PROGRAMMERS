def solution(num_list):
    result = 0
    
    for idx, val in enumerate(num_list):
        if val < 0:
            return idx
        else:
            result = -1
            
    return result