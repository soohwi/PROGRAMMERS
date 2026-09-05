def solution(a, b):
    
    result = [valA*valB for valA, valB in zip(a, b)]
    
    return sum(result)