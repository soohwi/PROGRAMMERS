def solution(arr, queries):
    result = arr
    
    for q in queries:
        for j in range(q[0], q[1]+1):
            result[j] += 1
    return result
            