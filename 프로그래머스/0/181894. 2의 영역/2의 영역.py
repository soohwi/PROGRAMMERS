def solution(arr):
            
    l = [i for i, v in enumerate(arr) if v == 2]
    
    return [-1] if len(l) == 0 else arr[l[0]:l[-1]+1]
            
    # if len(l) == 0:
    #     return [-1]
    # else:
    #     return arr[l[0]: l[-1]+1]
