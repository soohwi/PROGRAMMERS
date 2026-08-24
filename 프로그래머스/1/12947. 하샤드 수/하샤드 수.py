def solution(x):
    # l = 0
    # for i in list(str(x)):
    #     l += int(i)
    
    # if x % l == 0:
    #     answer = True
    # else:
    #     answer = False
    
    l = sum([int(i) for i in list(str(x))])
    answer = x % l == 0
    
    return answer
