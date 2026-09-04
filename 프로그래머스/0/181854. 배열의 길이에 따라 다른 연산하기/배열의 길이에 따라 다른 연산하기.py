def solution(arr, n):
    lenArr = len(arr)
    
    for idx in range(lenArr):
        if lenArr % 2 != 0:
            if idx % 2 == 0:
                arr[idx] += n
        else:
            if idx % 2 != 0:
                arr[idx] += n
    return arr