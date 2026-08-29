def solution(myString):
    result = ""
    
    for i in myString.lower():
        if i == "a":
            result += i.upper()
        else:
            result += i
            
    return result

