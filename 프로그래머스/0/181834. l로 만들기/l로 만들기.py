def solution(myString):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

    return ''.join(['l' if i in alp else i for i in list(myString)])