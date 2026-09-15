def solution(t, p):
    
    lenP = len(p)
    result = 0
    
    for i in range(len(t)):
        newNum = t[i:i+lenP]
        
        if len(newNum) == lenP and newNum <= p:
            result += 1
            
    return result