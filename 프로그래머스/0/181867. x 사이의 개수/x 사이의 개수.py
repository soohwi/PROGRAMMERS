def solution(myString):
    new_arr = myString.split('x')

    return [len(i) for i in new_arr]