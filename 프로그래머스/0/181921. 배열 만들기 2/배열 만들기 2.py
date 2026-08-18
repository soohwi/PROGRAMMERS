def solution(l, r):
    answer = []
    
    
    for i in range(l, r+1):
        if i % 5 == 0:
            is_valid = True
            
            for j in str(i):
                if j != '5' and j != '0':
                    is_valid = False
            
            if is_valid:
                answer.append(i)
    
    if not answer:
        answer = [-1]
        
    return answer            
