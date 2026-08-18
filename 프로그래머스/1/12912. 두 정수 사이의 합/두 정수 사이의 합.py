def solution(a, b):
    # if a == b:
    #     return a
    # else:
    #     result = 0
    #     for i in range(min(a,b), max(a,b) + 1):
    #         result += i
    #     return result
        
    return a if a == b else sum(range(min(a,b), max(a,b)+1))