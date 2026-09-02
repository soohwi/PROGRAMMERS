def solution(myStr):
    
    repList = myStr.replace('b','a').replace('c', 'a')
    newList = list(filter(None, repList.split('a')))
    
    return newList if len(newList) != 0 else ["EMPTY"]