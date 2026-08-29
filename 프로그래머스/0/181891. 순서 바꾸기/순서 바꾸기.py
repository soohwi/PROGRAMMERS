def solution(num_list, n):
    result = num_list[n:]
    
    for i in num_list[:n]:
        result.append(i)
    
    return result