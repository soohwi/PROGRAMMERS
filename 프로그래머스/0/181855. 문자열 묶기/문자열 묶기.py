from collections import Counter

def solution(strArr):
#     result = []
#     for i in strArr:
#         result.append(len(i))
    
#     count = Counter(result)

    count = Counter([len(i) for i in strArr])
    
    return max(list(count.values()))
