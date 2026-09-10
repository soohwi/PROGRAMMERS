def solution(n):
    a = [[0] * n for i in range(n)]
    
    for i in range(n):
        a[i][i] = 1
        
    return a