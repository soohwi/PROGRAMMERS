def solution(order):
    result = 0
    for i in order:
        if 'latte' in i:
            result += 500
        
        result += 4500
        
    return result