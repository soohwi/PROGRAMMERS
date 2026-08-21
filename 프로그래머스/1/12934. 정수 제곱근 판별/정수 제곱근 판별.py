def solution(n):
    x = int(n ** 0.5)
        
    # if x ** 2 == n:
    #     answer = (x+1) ** 2
    # else:
    #     answer = -1
    
    answer = ((x+1)**2 if x**2 == n else -1)
    
    return answer