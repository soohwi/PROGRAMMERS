def solution(arr, queries):
    result  = []
    
# 풀이1
#     for i in queries:
#         newVal = 1000001
        
#         for j in range(i[0], i[1]+1):
#             if arr[j] > i[-1] and arr[j] < newVal:
#                 newVal = arr[j]
                
#         if newVal == 1000001:
#             newVal = -1
        
#         result.append(newVal)

# 풀이2
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        result.append(-1 if len(l) == 0 else min(l))
        
    return result