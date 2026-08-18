def solution(numLog):
    result = ''
    
    for i in range(0, len(numLog) - 1):
        diff = numLog[i] - numLog[i+1]
        
        if diff == -1:
            result += 'w'
        elif diff == 1:
            result += 's'
        elif diff == -10:
            result += 'd'
        elif diff == 10:
            result += 'a'
    
    return result