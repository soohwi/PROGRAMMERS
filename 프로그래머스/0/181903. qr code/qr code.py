def solution(q, r, code):
    # result = ''
    # for idx, val in enumerate(code):
    #     if idx % q == r:
    #         result += val

    result = ''.join(val for idx, val in enumerate(code) if idx % q == r)
    
    return result