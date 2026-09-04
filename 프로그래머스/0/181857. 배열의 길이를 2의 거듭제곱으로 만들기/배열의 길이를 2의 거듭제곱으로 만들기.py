def solution(arr):
    
    target = 1
    
    while target < len(arr):
        target *= 2
        
    if target != len(arr):
        arr += [0 for i in range(target - len(arr))]
    
    return arr