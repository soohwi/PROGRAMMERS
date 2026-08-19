def solution(number):
    
    sumVal = sum(int(i) for i in str(number))
    
    return sumVal % 9