def solution(my_string):
    new_list = my_string.split(' ')
    return list(filter(None, new_list))