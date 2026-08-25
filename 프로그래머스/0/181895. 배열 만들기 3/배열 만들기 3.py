import itertools

def solution(arr, intervals):
    result = []
    for i in intervals:
        result.append(arr[i[0]:i[1]+1])
        
    return list(itertools.chain(*result))