def solution(myString, pat):
    new_str = myString.lower()
    new_pat = pat.lower()
    
    if new_str.find(new_pat) != -1:
        return 1
    else:
        return 0