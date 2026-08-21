def solution(my_string, s, e):
#     origin = str(my_string[s:e+1])
    reverse = str(my_string[s:e+1][::-1])
    
#     result = my_string.replace(origin, reverse)
    
    return my_string[0:s] + reverse + my_string[e+1:]