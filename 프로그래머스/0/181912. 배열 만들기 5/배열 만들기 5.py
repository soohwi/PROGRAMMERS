def solution(intStrs, k, s, l):
    result = []
    
    for i in intStrs:
        newNum = int(i[s:s+l])
        if newNum > k:
            result.append(newNum)
        
    return result