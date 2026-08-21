def solution(q, r, code):
    result = ''
    for idx, val in enumerate(code):
        if idx % q == r:
            result += val
            
    return result