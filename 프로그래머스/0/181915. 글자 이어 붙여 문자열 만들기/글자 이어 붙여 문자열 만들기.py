def solution(my_string, index_list):
    # 풀이1
#     result = ''
    
#     for i in index_list:
#         result += my_string[i]
        
#     return result
    
    # 풀이2
    return ''.join([my_string[i] for i in index_list])

    
    