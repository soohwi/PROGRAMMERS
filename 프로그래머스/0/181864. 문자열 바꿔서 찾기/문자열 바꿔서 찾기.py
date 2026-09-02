def solution(myString, pat):
    newArr = []
    for i in myString:
        if i == "A":
            newArr.append("B")
        else: 
            newArr.append("A")
            
    newString = ''.join(newArr)
    
    result = 0
    for i in range(len(newString)):
        if newString[i:].startswith(pat):
            result = 1
    
    return result