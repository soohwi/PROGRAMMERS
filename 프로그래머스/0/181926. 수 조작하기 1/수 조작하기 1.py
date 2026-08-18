def solution(n, control):
    answer = n
    calc = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    
    for i in control:
        answer += calc[i]
    return answer
    
    # for i in list(control):
    #     if i == 'w':
    #         n += 1
    #     elif i == 's':
    #         n -= 1
    #     elif i == 'd':
    #         n += 10
    #     elif i == 'a':
    #         n -= 10
    # return n