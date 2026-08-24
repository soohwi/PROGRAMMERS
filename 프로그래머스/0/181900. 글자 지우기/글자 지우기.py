def solution(my_string, indices):
    l = list(my_string)
    newIndices = sorted(indices)[::-1]

    for i in newIndices:
        l.pop(i)
        
    return ''.join(l)
