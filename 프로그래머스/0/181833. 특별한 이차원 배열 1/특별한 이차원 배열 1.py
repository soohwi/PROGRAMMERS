def solution(n):
    a = []
    for i in range(n):
        a.append([0] * n)
    
    for idx, val in enumerate(a):
        val[idx] = 1
        
    return a
