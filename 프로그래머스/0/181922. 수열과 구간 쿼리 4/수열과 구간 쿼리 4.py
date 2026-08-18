def solution(arr, queries):
    for s, e, k in queries:
        # l = [i for i in range(s, e+1) if i % k == 0]
        # print(arr[l])
        
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr