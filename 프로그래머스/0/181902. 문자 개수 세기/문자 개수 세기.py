import string

def solution(my_string):
    letters = string.ascii_uppercase + string.ascii_lowercase
#     answer = []
    
#     for i in letters:
#         answer.append(my_string.count(i))
    # return answer
        
    return [my_string.count(i) for i in letters]
        
