def solution(a, d, included):
    # a + (i * b)
    result = 0
    for idx, val in enumerate(included):
        if val:
            result += a + (idx * d)
        else:
            result += 0
    return result