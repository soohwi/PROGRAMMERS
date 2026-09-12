def solution(arr):
    arrLen = len(arr)
    itemLen = len(arr[0])
    diffLen = max(arrLen, itemLen) - min(arrLen, itemLen)
    
    if arrLen > itemLen:
        for i in range(arrLen):
            for _ in range(diffLen):
                arr[i].append(0)
                
    elif arrLen < itemLen:
        for i in range(diffLen):
            arr.append([0 for _ in range(itemLen)])
    
    return arr