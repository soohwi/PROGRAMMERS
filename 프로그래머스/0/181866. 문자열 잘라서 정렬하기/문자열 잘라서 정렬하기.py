def solution(myString):
    # return sorted([i for i in myString.split('x') if len(i) > 0])

    return sorted(i for i in myString.split('x') if i)