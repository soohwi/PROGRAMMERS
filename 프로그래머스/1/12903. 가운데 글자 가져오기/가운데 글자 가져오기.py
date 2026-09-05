def solution(s):
#     quot = len(s) // 2
    
#     return s[quot] if len(s) % 2 != 0 else s[quot-1:quot+1]
    
    
    return s[(len(s)-1)//2 : len(s)//2 + 1]