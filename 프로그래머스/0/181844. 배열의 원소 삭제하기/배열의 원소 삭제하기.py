def solution(arr, delete_list):
    a = []
    for i in arr:
        for j in delete_list:
            if i == j:
                a.append(i)
    
    for i in a:
        arr.remove(i)
    
    return arr