def solution(s):
    
    newS = s.lower()
    p = newS.count('p')
    y = newS.count('y')
    
    if p == y:
        return True
    return False