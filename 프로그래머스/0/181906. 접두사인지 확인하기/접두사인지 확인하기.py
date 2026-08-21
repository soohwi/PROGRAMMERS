def solution(my_string, is_prefix):
    l = [my_string[0:i+1] for i in range(len(my_string))]
    
    result = l.count(is_prefix)
    
    return result
