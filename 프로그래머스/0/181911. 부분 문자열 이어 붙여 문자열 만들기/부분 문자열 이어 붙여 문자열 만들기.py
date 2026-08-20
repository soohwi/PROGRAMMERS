def solution(my_strings, parts):
    result = ''
    
    for idx, val in enumerate(my_strings):
        start = parts[idx][0]
        end = parts[idx][1] + 1
        
        result += val[start:end]
        
    return result