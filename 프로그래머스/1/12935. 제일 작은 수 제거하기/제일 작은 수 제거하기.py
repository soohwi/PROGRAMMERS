def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    sorted_arr = sorted(arr)
    for i in arr:
        if i == sorted_arr[0]:
            arr.remove(i)
            
    return arr