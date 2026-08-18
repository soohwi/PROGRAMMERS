def solution(code):
    mode = 0
    ret = ''
    for i in range(0, len(code)):
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    ret += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2 != 0:
                    ret += code[i]
            else:
                mode = 0
    return 'EMPTY' if ret == '' else ret