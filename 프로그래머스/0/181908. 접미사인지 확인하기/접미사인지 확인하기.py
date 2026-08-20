def solution(my_string, is_suffix):
    l = [my_string[i:] for i in range(len(my_string))]
    
    result = 0
    
    for j in l:
        if j == is_suffix:
            result += 1
        
    return result