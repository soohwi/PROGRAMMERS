def solution(arr, flag):
    answer = []
    
    for idx, val in enumerate(flag):
        if val:
            answer += ([arr[idx]] * (arr[idx] * 2))
        else:
            end = len(answer) - arr[idx]
            answer = answer[:end]
            
    return answer