def solution(n):
    odd = 0
    even = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even += i ** 2
        else:
            odd += i
            
    if n % 2 == 0:
        return even
    else:
        return odd