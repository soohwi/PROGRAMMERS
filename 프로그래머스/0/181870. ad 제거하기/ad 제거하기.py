def solution(strArr):
#     result = []
#     for i in strArr:
#         if i.find('ad') == -1:
#             result.append(i)
            
#     return result
    
    return [i for i in strArr if i.find('ad') == -1]